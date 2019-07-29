import os
import matplotlib.pyplot as plt
import numpy as np

command = 'python ../scripts/draw_traces.py'

os.system(command)

with open('../example_data/draw_traces/reference_TP1.svg', 'rb') as reference_file:
    ref_file_content = reference_file.read()

with open('../example_data/draw_traces/TP1.svg', 'rb') as exec_file:
    exec_file_content = exec_file.read()


print('\n')
print(exec_file_content)
print('\n')
print(ref_file_content)
print(type(exec_file_content))

print("File not empty:", bool(exec_file_content))
print("File has xml data:", exec_file_content[:5] == b'<?xml')
print("File lengths are equal:", len(exec_file_content) == len(ref_file_content))

ref_im = plt.imread("../example_data/draw_traces/reference_TP1.png")
exec_im = plt.imread("../example_data/draw_traces/TP1.png")


print('png files are equal:', np.all(ref_im == exec_im))