import numpy as np

from ..parameters import vh, b0, alpha_em, fpi
from ..parameters import muon_mass as mmu
from ..parameters import electron_mass as me
from ..parameters import up_quark_mass as muq
from ..parameters import down_quark_mass as mdq
from ..parameters import neutral_pion_mass as mpi0
from ..parameters import charged_pion_mass as mpi

from scipy.integrate import quad


def width_p_to_gg(params):
    """Returns the partial decay width of the pseudoscalar decaying into
    photons.
    """
    ret = (alpha_em**2*(1. - params.beta**2)*params.gpFF**2*params.mp**3) / \
        (128.*np.pi**3*vh**2)

    assert ret.imag == 0
    assert ret.real >= 0

    return ret.real


def width_p_to_xx(params):
    mp = params.mp
    rx = params.mx / mp

    if 2.*rx < 1:
        ret = -((-1 + params.beta**2)*params.gpxx**2*mp*np.sqrt(1-4*rx**2)) / \
            (32.*np.pi)

        assert ret.imag == 0
        assert ret.real >= 0

        return ret.real
    else:
        return 0.


def width_p_to_ff(f, params):
    mp = params.mp

    if f == "e":
        rf = me / mp
        gpff = params.gpee
    elif f == "mu":
        rf = mmu / mp
        gpff = params.gpmumu

    if 2.*rf < 1:
        ret = -((-1 + params.beta**2)*gpff**2*mp*np.sqrt(1 - 4*rf**2)) / \
            (8.*np.pi)

        assert ret.imag == 0
        assert ret.real >= 0

        return ret.real
    else:
        return 0.


def dwidth_ds_p_to_pi0pi0pi0(s, params):
    mp = params.mp

    if mp >= 3.*mpi0:
        gpuu = params.gpuu
        gpdd = params.gpdd
        gpGG = params.gpGG
        beta = params.beta

        ret = -(b0**2*np.sqrt(s*(-4*mpi0**2 + s)) *
                np.sqrt(mp**4 + (mpi0**2 - s)**2 - 2*mp**2*(mpi0**2 + s)) *
                (-(beta**2*(mdq + muq)**2*vh**2) +
                 2*beta*fpi*(mdq + muq)*vh*(gpGG*(mdq - muq) +
                                            (gpdd - gpuu)*vh) +
                 (-1 + 10*beta**2)*fpi**2*(gpGG*(mdq - muq) +
                                           (gpdd - gpuu)*vh)**2)) / \
            (256.*fpi**4*mp**3*np.pi**3*s*vh**2)

        assert ret.imag == 0
        assert ret.real >= 0

        return ret
    else:
        return 0.


def width_p_to_pi0pi0pi0(params):
    """
    Returns the width for the pseudoscalar's decay into three neutral pions.

    Parameters
    ----------
    params : PseudoScalarMediator or PseudoScalarMediatorParameters object
        Object containing the parameters of the pseudo-scalar mediator
        model. Can be a PseudoScalarMediator or a
        PseudoScalarMediatorParameters object.

    Returns
    -------
    gamma : float
        The width for P -> pi0 pi0 pi0.
    """
    mp = params.mp
    smax = (mp - mpi0)**2
    smin = 4. * mpi0**2

    res = quad(dwidth_ds_p_to_pi0pi0pi0, smin, smax, args=(params))

    return res[0]


def dwidth_ds_p_to_pi0pipi(s, params):
    mp = params.mp

    if mp >= 2.*mpi + mpi0:
        gpuu = params.gpuu
        gpdd = params.gpdd
        gpGG = params.gpGG
        beta = params.beta

        ret = (np.sqrt(s*(-4*mpi**2 + s)) *
               np.sqrt(mp**4 + (mpi0**2 - s)**2 - 2*mp**2*(mpi0**2 + s)) *
               (beta**2*(2*mpi**2 + mpi0 - 3*s)**2*vh**2 +
                2*b0*beta*(2*mpi**2 + mpi0 - 3*s)*vh *
                (-(beta*(mdq + muq)*vh) + fpi*(gpGG*(mdq - muq) +
                                               (gpdd - gpuu)*vh)) +
                b0**2*(beta**2*(mdq + muq)**2*vh**2 -
                       2*beta*fpi*(mdq + muq)*vh*(gpGG*(mdq - muq) +
                                                  (gpdd - gpuu)*vh) -
                       (-1 + 4*beta**2)*fpi**2*(gpGG*(mdq - muq) +
                                                (gpdd - gpuu)*vh)**2))) / \
            (2304.*fpi**4*mp**3*np.pi**3*s*vh**2)

        assert ret.imag == 0
        assert ret.real >= 0

        return ret
    else:
        return 0.


def width_p_to_pi0pipi(params):
    """
    Returns the width for the pseudoscalar's decay into a neutral pion and
    two charged pions.

    Parameters
    ----------
    params : PseudoScalarMediator or PseudoScalarMediatorParameters object
        Object containing the parameters of the pseudo-scalar mediator
        model. Can be a PseudoScalarMediator or a
        PseudoScalarMediatorParameters object.

    Returns
    -------
    gamma : float
        The width for P -> pi0 pi+ pi-.
    """
    mp = params.mp
    smax = (mp - mpi0)**2
    smin = 4. * mpi**2

    res = quad(dwidth_ds_p_to_pi0pipi, smin, smax, args=(params))

    return res[0]


def partial_widths(params):
    """
    Returns a dictionary for the partial decay widths of the pseudoscalar
    mediator.

    Returns
    -------
    width_dict : dictionary
        Dictionary of all of the individual decay widths of the pseudoscalar
        mediator as well as the total decay width.
    """
    w_gg = width_p_to_gg(params)
    w_xx = width_p_to_xx(params)

    w_ee = width_p_to_ff('e', params)
    w_mumu = width_p_to_ff('mu', params)

    w_pi0pipi = width_p_to_pi0pipi(params)

    total = w_gg + w_xx + w_ee + w_mumu + w_pi0pipi

    width_dict = {'g g': w_gg,
                  'x x': w_xx,
                  'e e': w_ee,
                  'mu mu': w_mumu,
                  'pi0 pi pi': w_pi0pipi,
                  'total': total}

    return width_dict