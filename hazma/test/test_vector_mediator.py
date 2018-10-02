from hazma.vector_mediator import VectorMediator
import numpy as np


def test_list_final_states():
    mx, mv = [100., 200.]
    gvxx, gvuu, gvdd, gvss, gvee, gvmumu = 6 * [1.]

    VM = VectorMediator(mx, mv, gvxx, gvuu, gvdd, gvss, gvee, gvmumu)
    VM.list_annihilation_final_states()


def test_cross_sections():
    mx, mv = [100., 200.]
    cme = 1000.
    gvxx, gvuu, gvdd, gvss, gvee, gvmumu = 6 * [1.]

    VM = VectorMediator(mx, mv, gvxx, gvuu, gvdd, gvss, gvee, gvmumu)
    VM.annihilation_cross_sections(cme)


def test_branching_fractions():
    mx, mv = [100., 200.]
    cme = 1000.
    gvxx, gvuu, gvdd, gvss, gvee, gvmumu = 6 * [1.]

    VM = VectorMediator(mx, mv, gvxx, gvuu, gvdd, gvss, gvee, gvmumu)
    VM.annihilation_branching_fractions(cme)


def test_spectra():
    mx, mv = [100., 200.]
    cme = 1000.
    egams = np.logspace(0., np.log10(cme), num=50)
    gvxx, gvuu, gvdd, gvss, gvee, gvmumu = 6 * [1.]

    VM = VectorMediator(mx, mv, gvxx, gvuu, gvdd, gvss, gvee, gvmumu)
    VM.spectra(egams, cme)


def test_spectrum_functions():
    mx, mv = [100., 200.]
    gvxx, gvuu, gvdd, gvss, gvee, gvmumu = 6 * [1.]

    VM = VectorMediator(mx, mv, gvxx, gvuu, gvdd, gvss, gvee, gvmumu)
    VM.spectrum_functions()


def test_partial_widths():
    pass
