import os
import matplotlib.pyplot as plt
import numpy as np




def test_if_plots_are_the_same_as_reference():
    command = 'python ./scripts/draw_traces.py'
    os.system(command)
    ref_im = plt.imread("./example_data/draw_traces/reference_TP1.png")
    exec_im = plt.imread("./example_data/draw_traces/TP1.png")

    assert np.all(ref_im == exec_im)