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

fig_TP1 = plt.figure()
axTP1_cell1 = fig_TP1.add_subplot(511)
axTP1_cell2 = fig_TP1.add_subplot(512)
axTP1_cell3 = fig_TP1.add_subplot(513)
axTP1_cell4 = fig_TP1.add_subplot(514)
axTP1_cell5 = fig_TP1.add_subplot(515)


axTP1_cell1.plot(t_TPs[0], cells_TPs[0][0], linewidth = 0.25)
axTP1_cell2.plot(t_TPs[0], cells_TPs[0][1], linewidth = 0.25)
axTP1_cell3.plot(t_TPs[0], cells_TPs[0][2], linewidth = 0.25)
axTP1_cell4.plot(t_TPs[0], cells_TPs[0][3], linewidth = 0.25)
axTP1_cell5.plot(t_TPs[0], cells_TPs[0][4], linewidth = 0.25)


#Adjust spacing between subplots
plt.ylabel('ΔF/F')
plt.xlabel('# of frames')

fig_TP1.savefig('./data/draw_traces/TP1.png', format = 'png')


