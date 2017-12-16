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
Module for computing the photon spectrum from radiative kaon decay.

Description:
    The charged kaon has many decay modes:

        k -> mu  + nu
        k -> pi  + pi0
        k -> pi  + pi  + pi
        k -> pi0 + e   + nu
        k -> pi0 + mu  + nu
        k -> pi  + pi0 + pi0

    For the the two-body final states, the sum of the decay spectra are
    computed given the known energies of the final state particles in the
    kaon's rest frame. The spectrum is then boosted into the lab frame.

    For the three-body final state, the energies of the final state
    particles are computed using RAMBO. The spectra for each final state
    particle is computed are each point in phases space in the charged kaon's rest frame and then spectra are summed over. The spectra is then boosted into the lab frame.
"""

""" Distributions for 3-body final states """
# Number of phase space points to use for RAMBO in creating energies
# distributions for three-body final states. Set to 1000 by default.
__num_ps_pts = 1000
# Number of bins to use for energies distributions of three-body final
# states (i.e. the number of energies to use.) Set to 10 by default.
__num_bins = 10
# Array of masses for the three charged pion final state.
__msPiPiPi = np.array([MASS_PI, MASS_PI, MASS_PI])
# Array of masses for the pi0 + mu + nu final
__msPi0MuNu = np.array([MASS_PI0, MASS_MU, 0.0])
# Array storing the energies and probabilities of the three charged pion
# final state.
__probsPiPiPi = np.zeros((3, 2, __num_bins), dtype=np.float64)
# Array storing the energies and probabilities of the pi0 + mu + nu final
# state.
__probsPi0MuNu = np.zeros((3, 2, __num_bins), dtype=np.float64)
# Rambo object used to create energy distributions.
__ram = rambo.Rambo()
# Call rambo to generate energ distributions for 3 charged pion final state.
__probsPiPiPi = __ram.generate_energy_histogram(__num_ps_pts, __msPiPiPi,
                                                MASS_K, __num_bins)
# Call rambo to generate energ distributions for pi0 + mu + nu  final state.
__probsPi0MuNu = __ram.generate_energy_histogram(__num_ps_pts, __msPi0MuNu,
                                                 MASS_K, __num_bins)

# Energy of muon in the k -> mu + nu final state.
__eng_mu_k_rf = (MASS_K**2 + MASS_MU**2) / (2.0 * MASS_K)
# Energy of charged pion in the k -> pi + pi0 final state.
__eng_pi_k_rf = (MASS_K**2 + MASS_PI**2 - MASS_PI0**2) / (2.0 * MASS_K)
# Energy of neutral pion in the k -> pi + pi0 final state.
__eng_pi0_k_rf = (MASS_K**2 - MASS_PI**2 + MASS_PI0**2) / (2.0 * MASS_K)

""" Interpolating spectrum functions """
# Gamma ray energies for interpolating functions. Need a very low lower bound
# in order to no pass outside interpolation bounds when called from kaon decay.
__eng_gams_interp = np.logspace(-5.5, 3.0, num=10000, dtype=np.float64)

__spec_PiPi0 = decay_charged_pion.CSpectrum(__eng_gams_interp, __eng_pi_k_rf)
__spec_PiPi0 += decay_neutral_pion.CSpectrum(__eng_gams_interp, __eng_pi0_k_rf)
__spec_MuNu = decay_muon.CSpectrum(__eng_gams_interp, __eng_mu_k_rf)

__spec_Pi0MuNu = np.zeros(10000, dtype=np.float64)
__spec_PiPiPi = np.zeros(10000, dtype=np.float64)

cdef int k
for k in range(__num_bins):
    __spec_Pi0MuNu += __probsPi0MuNu[0, 0, k] * \
        decay_muon.CSpectrum(__eng_gams_interp, __probsPi0MuNu[0, 1, k])
    __spec_Pi0MuNu += __probsPi0MuNu[1, 0, k] * \
        decay_muon.CSpectrum(__eng_gams_interp, __probsPi0MuNu[1, 1, k])

    __spec_PiPiPi += __probsPiPiPi[0, 0, k] * \
        decay_muon.CSpectrum(__eng_gams_interp, __probsPiPiPi[0, 1, k])
    __spec_PiPiPi += __probsPiPiPi[1, 0, k] * \
        decay_muon.CSpectrum(__eng_gams_interp, __probsPiPiPi[1, 1, k])
    __spec_PiPiPi += __probsPiPiPi[2, 0, k] * \
        decay_muon.CSpectrum(__eng_gams_interp, __probsPiPiPi[2, 1, k])


cdef double __interp_MuNu(double eng_gam):
    return np.interp(eng_gam, __eng_gams_interp, __spec_MuNu)

cdef double __interp_PiPi0(double eng_gam):
    return np.interp(eng_gam, __eng_gams_interp, __spec_PiPi0)

cdef double __interp_PiPiPi(double eng_gam):
    return np.interp(eng_gam, __eng_gams_interp, __spec_PiPiPi)

cdef double __interp_Pi0MuNu(double eng_gam):
    return np.interp(eng_gam, __eng_gams_interp, __spec_Pi0MuNu)

@cython.cdivision(True)
cdef double __integrand2(double cl, double eng_gam, double eng_k):
    """
    Integrand for K -> X, where X is a two body final state. The X's
    used are
        mu + nu
        pi  + pi0
    Keyword arguments::
        cl: Angle of photon w.r.t. charged kaon in lab frame.
        eng_gam: Energy of photon in laboratory frame.
        eng_k: Energy of kaon in laboratory frame.
    """

    cdef double gamma_k = eng_k / MASS_K
    cdef double beta_k = sqrt(1.0 - (MASS_K / eng_k)**2)
    cdef double eng_gam_k_rf = eng_gam * gamma_k * (1.0 - beta_k * cl)

    cdef int i, j
    cdef double ret_val = 0.0
    cdef double pre_factor \
        = 1.0 / (2.0 * gamma_k * (1.0 - beta_k * cl))

    ret_val += BR_K_TO_MUNU * __interp_MuNu(eng_gam_k_rf)
    ret_val += BR_K_TO_PIPI0 * __interp_PiPi0(eng_gam_k_rf)

    return pre_factor * ret_val

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef double __integrand3(double cl, double eng_gam, double eng_k):
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

    cdef int i, j
    cdef double ret_val = 0.0
    cdef double eng, weight
    cdef double pre_factor \
        = 1.0 / (2.0 * gamma_k * (1.0 - beta_k * cl))

    ret_val += BR_K_TO_PI0MUNU * __interp_Pi0MuNu(eng_gam_k_rf)
    ret_val += BR_K_TO_3PI * __interp_PiPiPi(eng_gam_k_rf)

    return pre_factor * ret_val


cdef double __integrand(double cl, double eng_gam, double eng_k):
    """
    Integrand for K -> X, where X is a any final state. The X's
    used are
        mu + nu
        pi  + pi0
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
    cdef double ret_val = 0.0

    ret_val += __integrand2(cl, eng_gam, eng_k)
    ret_val += __integrand3(cl, eng_gam, eng_k)

    return ret_val



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
                       epsrel=10**-2.)[0]

    return spec
