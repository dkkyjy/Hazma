cimport decay_muon
cimport decay_charged_pion
cimport decay_neutral_pion
from ..phases_space_generator cimport rambo
import numpy as np
cimport numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp2d
from libc.math cimport exp, log, M_PI, log10, sqrt, fmax
import cython
include "parameters.pxd"

"""
Module for computing the photon spectrum from radiative long kaon decay.

Description:
    The charged kaon has many decay modes:

    kl    -> pi  + e   + nu
    kl    -> pi  + mu  + nu
    kl    -> pi0 + pi0  + pi0
    kl    -> pi  + pi  + pi0

    For the three-body final state, the energies of the final state
    particles are computed using RAMBO. The spectra for each final state
    particle is computed are each point in phases space in the charged kaon's rest frame and then spectra are summed over. The spectra is then boosted into the lab frame.
"""

__spec = np.loadtxt("long_kaon_interp.dat", delimiter=',')

cdef double __interp_spec(double eng_gam):
    np.interp(eng_gam, __spec[:, 0], __spec[:, 1])

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef double __integrand(double cl, double eng_gam, double eng_k):
    """
    Integrand for K -> X, where X is a three body final state. The X's
    used are
        pi + pi + pi
        pi0 + mu + nu.
    When the ChargedKaon object is instatiated, the energies of the FSP are
    computed using RAMBO and energy distributions are formed. All the
    energies from the energy distributions are summed over against their
    weights.

    Keyword arguments::
        cl: Angle of photon w.r.t. charged kaon in lab frame.
        eng_gam: Energy of photon in laboratory frame.
        eng_k: Energy of kaon in laboratory frame.
    """
    cdef double gamma_k = eng_k / MASS_K
    cdef double beta_k = sqrt(1.0 - (MASS_K / eng_k)**2)
    cdef double eng_gam_k_rf = eng_gam * gamma_k * (1.0 - beta_k * cl)

    cdef double ret_val
    cdef double pre_factor \
        = 1.0 / (2.0 * gamma_k * (1.0 - beta_k * cl))

    # ret_val += BR_KL_TO_PIENU * __interp_PIENU(eng_gam_k_rf)
    # ret_val += BR_KL_TO_PIMUNU * __interp_PIMUNU(eng_gam_k_rf)
    # ret_val += BR_KL_TO_3PI0 * __interp_3PI0(eng_gam_k_rf)
    # ret_val += BR_KL_TO_2PIPI0 * __interp_2PIPI0(eng_gam_k_rf)

    ret_val = __interp_spec(eng_gam_k_rf)
    return pre_factor * ret_val


def SpectrumPoint(double eng_gam, double eng_k):
    """
    Returns the radiative spectrum value from charged kaon at
    a single gamma ray energy.

    Keyword arguments::
        eng_gam: Energy of photon is laboratory frame.
        eng_k: Energy of charged kaon in laboratory frame.
    """
    cdef double result = 0.0

    return quad(__integrand, -1.0, 1.0, points=[-1.0, 1.0], \
                  args=(eng_gam, eng_k), epsabs=10**-10., \
                  epsrel=10**-4.)[0]


@cython.boundscheck(False)
@cython.wraparound(False)
def Spectrum(np.ndarray[np.float64_t, ndim=1] eng_gams, double eng_k):
    """
    Returns the radiative spectrum dNde from charged kaon for a
    list of gamma ray energies.

    Keyword arguments::
        eng_gams: List of energies of photon in laboratory frame.
        eng_k: Energy of charged kaon in laboratory frame.
    """
    cdef double result = 0.0

    cdef int numpts = len(eng_gams)

    cdef np.ndarray spec = np.zeros(numpts, dtype=np.float64)

    cdef int i = 0

    for i in range(numpts):
        spec[i] = quad(__integrand, -1.0, 1.0, points=[-1.0, 1.0], \
                       args=(eng_gams[i], eng_k), epsabs=0.0, \
                       epsrel=10**-4.)[0]

    return spec