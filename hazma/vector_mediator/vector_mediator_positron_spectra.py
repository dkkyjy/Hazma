import numpy as np

from ..positron_spectra import muon as pspec_muon
from ..positron_spectra import charged_pion as pspec_charged_pion
from .vector_mediator_cross_sections import branching_fractions


def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx


def pspec_electron(eng_ps, eng_e):
    spec = np.zeros(len(eng_ps), dtype=float)
    idx = find_nearest(eng_ps, eng_e)
    spec[idx] = 1.
    return spec


def positron_spectra(eng_ps, cme, params):
    """
    """

    # Compute branching fractions
    bfs = branching_fractions(cme, params)

    # Only compute the spectrum if the channel's branching fraction is nonzero
    def spec_helper(bf, specfn):
        if bf != 0:
            return bf * specfn(eng_ps, cme / 2.)
        else:
            return np.zeros(eng_ps.shape)

    cpions = spec_helper(bfs['pi pi'], pspec_charged_pion)
    muons = spec_helper(bfs['mu mu'], pspec_muon)
    electrons = spec_helper(bfs['e e'], pspec_electron)

    total = cpions + muons + electrons

    return {"total": total, "e e": electrons, "mu mu": muons, "pi pi": cpions}