import numpy as np

from ..positron_spectra import muon as pspec_muon
from ..positron_spectra import positron_rambo
from .pseudo_scalar_mediator_cross_sections import branching_fractions

from hazma.pseudo_scalar_mediator.pseudo_scalar_mediator_mat_elem_sqrd_rambo \
    import msqrd_xx_to_p_to_pm0

from hazma.parameters import charged_pion_mass as mpi
from hazma.parameters import neutral_pion_mass as mpi0


def positron_spectra_pi0pipi(eng_ps, cme, params, num_ps_pts=1000):

    if cme <= 2. * mpi + mpi0:
        return np.zeros(len(eng_ps), dtype=float)

    def msqrd_tree(momenta):
        return msqrd_xx_to_p_to_pm0(momenta, params)

    return positron_rambo(["charged_pion", "charged_pion", "neutral_pion"],
                          cme, eng_ps, num_ps_pts=1000,
                          mat_elem_sqrd=msqrd_tree)

# TODO: figure this out!


def positron_spectra(eng_ps, cme, params):
    """Computes continuum part of positron spectrum from DM annihilation.

    Parameters
    ----------
    eng_ps : array-like
        Positron energies at which to compute the spectrum.
    cme : float
        Center of mass energy.

    Returns
    -------
    specs : dict
        Dictionary of positron spectra. The keys are the final states producing
        contributions to the continuum positron spectrum and 'total'.
    """
    # Compute branching fractions
    bfs = branching_fractions(cme, params)

    # Only compute the spectrum if the channel's branching fraction is nonzero
    def spec_helper(bf, specfn):
        if bf != 0:
            return bf * specfn(eng_ps, cme / 2.)
        else:
            return np.zeros(eng_ps.shape)

    mumu_spec = spec_helper(bfs['mu mu'], pspec_muon)

    pi0pipi_spec = positron_spectra_pi0pipi(eng_ps, cme, params)

    total = mumu_spec

    return {"total": total,
            "mu mu": mumu_spec,
            "pi0 pi pi": pi0pipi_spec}


def positron_lines(cme, params):
    bf = branching_fractions(cme, params)["e e"]

    return {"e e": {"energy": cme / 2., "bf": bf}}
