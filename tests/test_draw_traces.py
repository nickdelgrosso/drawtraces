import os
import numpy as np
import matplotlib.pyplot as plt


def test_plots_are_unchanged():
    os.system("python scripts/draw_traces.py")

    ref_im = plt.imread('data/draw_traces/ref_TP1.png')
    new_im = plt.imread('data/draw_traces/TP1.png')

    assert np.all(ref_im == new_im)