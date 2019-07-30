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
cell1_TP1 = cells[0].ix[0:6079]
cell1_TP2 = cells[0].ix[6080:12159]
cell1_TP3 = cells[0].ix[12160:18239]
cell1_TP4 = cells[0].ix[18240:24319]


# extract data for each time point from ROI 0001 (cells[1])
cell2_TP1 = cells[1].ix[0:6079]
cell2_TP2 = cells[1].ix[6080:12159]
cell2_TP3 = cells[1].ix[12160:18239]
cell2_TP4 = cells[1].ix[18240:24319]

# extract data for each time point from ROI 0002 (cells[2])
cell3_TP1 = cells[2].ix[0:6079]
cell3_TP2 = cells[2].ix[6080:12159]
cell3_TP3 = cells[2].ix[12160:18239]
cell3_TP4 = cells[2].ix[18240:24319]

# extract data for each time point from ROI 0003 (cells[3])
cell4_TP1 = cells[3].ix[0:6079]
cell4_TP2 = cells[3].ix[6080:12159]
cell4_TP3 = cells[3].ix[12160:18239]
cell4_TP4 = cells[3].ix[18240:24319]

# extract data for each time point from ROI 0004 (cells[4])
cell5_TP1 = cells[4].ix[0:6079]
cell5_TP2 = cells[4].ix[6080:12159]
cell5_TP3 = cells[4].ix[12160:18239]
cell5_TP4 = cells[4].ix[18240:24319]


# Plot all cells for TP1

fig_TP1 = plt.figure()
axTP1_cell1 = fig_TP1.add_subplot(511)
axTP1_cell2 = fig_TP1.add_subplot(512)
axTP1_cell3 = fig_TP1.add_subplot(513)
axTP1_cell4 = fig_TP1.add_subplot(514)
axTP1_cell5 = fig_TP1.add_subplot(515)


axTP1_cell1.plot(t_TPs[0], cell1_TP1, linewidth = 0.25)
axTP1_cell2.plot(t_TPs[0],cell2_TP1, linewidth = 0.25)
axTP1_cell3.plot(t_TPs[0],cell3_TP1, linewidth = 0.25)
axTP1_cell4.plot(t_TPs[0],cell4_TP1, linewidth = 0.25)
axTP1_cell5.plot(t_TPs[0],cell5_TP1, linewidth = 0.25)


#Adjust spacing between subplots
plt.ylabel('ΔF/F')
plt.xlabel('# of frames')

fig_TP1.savefig('./data/draw_traces/TP1.png', format = 'png')


