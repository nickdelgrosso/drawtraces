import matplotlib.pyplot as plt
import pandas as pd



# load csv as data frame
df = pd.read_csv('./data/draw_traces/top5_correlated.csv')

# extract time (t) and fluorescence data for each ROI (cell 1-5)

t = df.ix[:,'y0000']
cell_names = ['x0000', 'x0001', 'x0002', 'x0003', 'x0004']
cells = []
for cell_name in cell_names:
    cell = df.ix[:,cell_name]
    cells.append(cell)

#extract time (t) for 4 timepoints (TP)
t_TPs = []
for tp in [0, 6080, 12160, 18240]:
    t_TP = t.ix[tp:tp+6079]
    t_TPs.append(t_TP)

# extract data for each time point from ROI 0000 (cells[0])
cells_TPs = []
cell1_TPs = []
for tp in [0, 6080, 12160, 18240]:
    cells_TP = []
    for cell in cells:
        cell_TP = cell.ix[tp:tp+6079]
        cells_TP.append(cell_TP)
    cells_TPs.append(cells_TP)


# Plot all cells for TP1

fig, axes = plt.subplots(nrows=5)
for ax, cell_TP in zip(axes, cells_TPs[0]):
    ax.plot(t_TPs[0], cell_TP, linewidth = 0.25)

#Adjust spacing between subplots
plt.ylabel('ΔF/F')
plt.xlabel('# of frames')
fig.savefig('./data/draw_traces/TP1.png', format = 'png')


