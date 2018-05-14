from cmath import sqrt, pi

import numpy as np
from ..parameters import vh, b0, alpha_em
from ..parameters import charged_kaon_mass as mk
from ..parameters import neutral_kaon_mass as mk0
from ..parameters import charged_pion_mass as mpi
from ..parameters import neutral_pion_mass as mpi0
from ..parameters import up_quark_mass as muq
from ..parameters import down_quark_mass as mdq
from ..parameters import strange_quark_mass as msq
from ..parameters import electron_mass as me
from ..parameters import muon_mass as mmu


def width_s_to_gg(params):
    """
    Returns the partial decay width of the scalar decaying into photon.
    """

    return (alpha_em**2 * params.gsFF**2 * (params.ms**2)**1.5 *
            np.heaviside(params.ms, 0.0)) / (256. * np.pi**3 * vh**2)


def width_s_to_pi0pi0(params):
    """
    Returns the partial decay width of the scalar decaying into
    neutral pions.
    """

    return (sqrt(-4 * mpi0**2 + params.ms**2) *
            (2 * params.gsGG * (2 * mpi0**2 - params.ms**2) *
             (-9 * vh - 9 * params.gsff * params.vs +
                2 * params.gsGG * params.vs) *
             (9 * vh + 8 * params.gsGG * params.vs) +
             b0 * (mdq + muq) * (9 * vh + 4 * params.gsGG * params.vs) *
             (54 * params.gsGG * vh -
                32 * params.gsGG**2 * params.vs + 9 * params.gsff *
                (9 * vh + 16 * params.gsGG * params.vs)))**2 *
            np.heaviside(-2 * mpi0 + params.ms, 0.)) / \
        (32. * params.ms**2 * np.pi *
         (9 * vh + 9 * params.gsff * params.vs -
          2 * params.gsGG * params.vs)**2 *
         (9 * vh + 4 * params.gsGG * params.vs)**2 *
         (9 * vh + 8 * params.gsGG * params.vs)**2)


def width_s_to_pipi(params):
    """
    Returns the partial decay width of the scalar decaying into
    charged pion.
    """

    return (sqrt(-4 * mpi**2 + params.ms**2) *
            (2 * params.gsGG * (2 * mpi**2 - params.ms**2) *
             (-9 * vh - 9 * params.gsff * params.vs +
                2 * params.gsGG * params.vs) *
             (9 * vh + 8 * params.gsGG * params.vs) +
             b0 * (mdq + muq) * (9 * vh + 4 * params.gsGG * params.vs) *
             (54 * params.gsGG * vh -
                32 * params.gsGG**2 * params.vs + 9 * params.gsff *
                (9 * vh + 16 * params.gsGG * params.vs)))**2 *
            np.heaviside(-2 * mpi + params.ms, 0.)) / \
        (16. * params.ms**2 * pi *
         (9 * vh + 9 * params.gsff * params.vs -
          2 * params.gsGG * params.vs)**2 *
         (9 * vh + 4 * params.gsGG * params.vs)**2 *
         (9 * vh + 8 * params.gsGG * params.vs)**2)


def width_s_to_xx(params):
    """
    Returns the partial decay width of the scalar decaying into
    two fermions x.
    """

    return (params.gsxx**2 * (params.ms - 2 * params.mx) *
            (params.ms + 2 * params.mx) *
            sqrt(params.ms**2 - 4 * params.mx**2) *
            np.heaviside(params.ms - 2 * params.mx, 0.)) / \
        (8. * params.ms**2 * pi)


def width_s_to_ff(mf, params):
    """
    Returns the partial decay width of the scalar decaying into
    two fermions x.

    Parameters
    ----------
    mf : double
        Mass of the final state fermion.
    """

    return (params.gsff**2 * (params.ms - 2 * mf) * (params.ms + 2 * mf) *
            sqrt(params.ms**2 - 4 * mf**2) *
            np.heaviside(params.ms - 2 * mf, 0.)) / \
        (8. * params.ms**2 * pi)


def partial_widths(params):
    """
    Returns a dictionary for the partial decay widths of the scalar
    mediator.

    Returns
    -------
    width_dict : dictionary
        Dictionary of all of the individual decay widths of the scalar
        mediator as well as the total decay width. The possible decay
        modes of the scalar mediator are 'g g', 'k0 k0', 'k k', 'pi0 pi0',
        'pi pi', 'x x' and 'f f'. The total decay width has the key
        'total'.
    """
    w_gg = width_s_to_gg(params).real
    w_pi0pi0 = width_s_to_pi0pi0(params).real
    w_pipi = width_s_to_pipi(params).real
    w_xx = width_s_to_xx(params).real

    w_ee = width_s_to_ff(me, params).real
    w_mumu = width_s_to_ff(mmu, params).real

    total = w_gg + w_pi0pi0 + w_pipi + w_xx + w_ee + w_mumu

    width_dict = {'g g': w_gg,
                  'pi0 pi0': w_pi0pi0,
                  'pi pi': w_pipi,
                  'x x': w_xx,
                  'e e': w_ee,
                  'mu mu': w_mumu,
                  'total': total}

    return width_dict
