import matplotlib.pyplot as plt
import pandas as pd



# load csv as data frame
df = pd.read_csv('./example_data/draw_traces/top5_correlated.csv')

# extract time (t) and fluorescence data for each ROI (cell 1-5)
t = df.ix[:,'y0000']
cell1 = df.ix[:,'x0000']
cell2 = df.ix[:,'x0001']
cell3 = df.ix[:,'x0002']
cell4 = df.ix[:,'x0003']
cell5 = df.ix[:,'x0004']

#extract time (t) for 4 timepoints (TP)
t_TP1 = t.ix[0:6079]
t_TP2 = t.ix[6080:12159]
t_TP3 = t.ix[12160:18239]
t_TP4 = t.ix[18240:24319]

# extract data for each time point from ROI 0000 (cell1)
cell1_TP1 = cell1.ix[0:6079]
cell1_TP2 = cell1.ix[6080:12159]
cell1_TP3 = cell1.ix[12160:18239]
cell1_TP4 = cell1.ix[18240:24319]


# extract data for each time point from ROI 0001 (cell2)
cell2_TP1 = cell2.ix[0:6079]
cell2_TP2 = cell2.ix[6080:12159]
cell2_TP3 = cell2.ix[12160:18239]
cell2_TP4 = cell2.ix[18240:24319]

# extract data for each time point from ROI 0002 (cell3)
cell3_TP1 = cell3.ix[0:6079]
cell3_TP2 = cell3.ix[6080:12159]
cell3_TP3 = cell3.ix[12160:18239]
cell3_TP4 = cell3.ix[18240:24319]

# extract data for each time point from ROI 0003 (cell4)
cell4_TP1 = cell4.ix[0:6079]
cell4_TP2 = cell4.ix[6080:12159]
cell4_TP3 = cell4.ix[12160:18239]
cell4_TP4 = cell4.ix[18240:24319]

# extract data for each time point from ROI 0004 (cell5)
cell5_TP1 = cell5.ix[0:6079]
cell5_TP2 = cell5.ix[6080:12159]
cell5_TP3 = cell5.ix[12160:18239]
cell5_TP4 = cell5.ix[18240:24319]


# Plot all cells for TP1

fig_TP1 = plt.figure()
axTP1_cell1 = fig_TP1.add_subplot(511)
axTP1_cell2 = fig_TP1.add_subplot(512)
axTP1_cell3 = fig_TP1.add_subplot(513)
axTP1_cell4 = fig_TP1.add_subplot(514)
axTP1_cell5 = fig_TP1.add_subplot(515)


axTP1_cell1.plot(t_TP1, cell1_TP1, linewidth = 0.25, color = 'firebrick')
axTP1_cell1.set_ylim(3.8,4.8)
axTP1_cell1.axis('off')
axTP1_cell2.plot(t_TP1,cell2_TP1, linewidth = 0.25, color = 'sandybrown')
axTP1_cell2.set_ylim(3.3,4.3)
axTP1_cell2.axis('off')
axTP1_cell3.plot(t_TP1,cell3_TP1, linewidth = 0.25, color = 'darkkhaki')
axTP1_cell3.set_ylim(2,3)
axTP1_cell3.axis('off')
axTP1_cell4.plot(t_TP1,cell4_TP1, linewidth = 0.25, color = 'seagreen')
axTP1_cell4.set_ylim(0.8,1.8)
axTP1_cell4.axis('off')
axTP1_cell5.plot(t_TP1,cell5_TP1, linewidth = 0.25, color = 'royalblue')
axTP1_cell5.set_ylim(-0.2,0.8)
#axTP1_cell5.axis('off')


axTP1_cell5.spines['right'].set_visible(False)
axTP1_cell5.spines['top'].set_visible(False)
axTP1_cell5.spines['bottom'].set_position(('outward',10))
axTP1_cell5.set_yticks([])

#Adjust spacing between subplots
plt.ylabel('ΔF/F')
plt.xlabel('# of frames')

plt.show()
fig_TP1.savefig('./example_data/draw_traces/TP1.svg', format = 'svg')




# Plot all cells for TP2

fig_TP2 = plt.figure()
axTP2_cell1 = fig_TP2.add_subplot(511)
axTP2_cell2 = fig_TP2.add_subplot(512)
axTP2_cell3 = fig_TP2.add_subplot(513)
axTP2_cell4 = fig_TP2.add_subplot(514)
axTP2_cell5 = fig_TP2.add_subplot(515)

axTP2_cell1.plot(t_TP2,cell1_TP2, linewidth = 0.25, color = 'firebrick')
axTP2_cell1.set_ylim(4,5)
axTP2_cell1.axis('off')
axTP2_cell2.plot(t_TP2,cell2_TP2, linewidth = 0.25, color = 'sandybrown')
axTP2_cell2.set_ylim(2.8,3.8)
axTP2_cell2.axis('off')
axTP2_cell3.plot(t_TP2,cell3_TP2, linewidth = 0.25, color = 'darkkhaki')
axTP2_cell3.set_ylim(2, 3)
axTP2_cell3.axis('off')
axTP2_cell4.plot(t_TP2,cell4_TP2, linewidth = 0.25, color = 'seagreen')
axTP2_cell4.set_ylim(0.8,1.8)
axTP2_cell4.axis('off')
axTP2_cell5.plot(t_TP2,cell5_TP2, linewidth = 0.25, color = 'royalblue')
axTP2_cell5.set_ylim(0.2,1.2)
axTP2_cell5.axis('off')

plt.show()
fig_TP2.savefig('./example_data/draw_traces/TP2.svg', format = 'svg')

# Plot all cells for TP3

fig_TP3 = plt.figure()
axTP3_cell1 = fig_TP3.add_subplot(511)
axTP3_cell2 = fig_TP3.add_subplot(512)
axTP3_cell3 = fig_TP3.add_subplot(513)
axTP3_cell4 = fig_TP3.add_subplot(514)
axTP3_cell5 = fig_TP3.add_subplot(515)

axTP3_cell1.plot(t_TP3,cell1_TP3, linewidth = 0.25, color = 'firebrick')
axTP3_cell1.set_ylim(4,5)
axTP3_cell1.axis('off')
axTP3_cell2.plot(t_TP3,cell2_TP3, linewidth = 0.25, color = 'sandybrown')
axTP3_cell2.set_ylim(2.8,3.8)
axTP3_cell2.axis('off')
axTP3_cell3.plot(t_TP3,cell3_TP3, linewidth = 0.25, color = 'darkkhaki')
axTP3_cell3.set_ylim(2, 3)
axTP3_cell3.axis('off')
axTP3_cell4.plot(t_TP3,cell4_TP3, linewidth = 0.25, color = 'seagreen')
axTP3_cell4.set_ylim(0.8,1.8)
axTP3_cell4.axis('off')
axTP3_cell5.plot(t_TP3,cell5_TP3, linewidth = 0.25, color = 'royalblue')
axTP3_cell5.set_ylim(0.2,1.2)
axTP3_cell5.axis('off')

plt.show()
fig_TP3.savefig('./example_data/draw_traces/TP3.svg', format = 'svg')

# Plot all cells for TP4

fig_TP4 = plt.figure()
axTP4_cell1 = fig_TP4.add_subplot(511)
axTP4_cell2 = fig_TP4.add_subplot(512)
axTP4_cell3 = fig_TP4.add_subplot(513)
axTP4_cell4 = fig_TP4.add_subplot(514)
axTP4_cell5 = fig_TP4.add_subplot(515)

axTP4_cell1.plot(t_TP4,cell1_TP4, linewidth = 0.25, color = 'firebrick')
axTP4_cell1.set_ylim(4,5)
axTP4_cell1.axis('off')
axTP4_cell2.plot(t_TP4,cell2_TP4, linewidth = 0.25, color = 'sandybrown')
axTP4_cell2.set_ylim(3.1,4.1)
axTP4_cell2.axis('off')
axTP4_cell3.plot(t_TP4,cell3_TP4, linewidth = 0.25, color = 'darkkhaki')
axTP4_cell3.set_ylim(2, 3)
axTP4_cell3.axis('off')
axTP4_cell4.plot(t_TP4,cell4_TP4, linewidth = 0.25, color = 'seagreen')
axTP4_cell4.set_ylim(1,2)
axTP4_cell4.axis('off')
axTP4_cell5.plot(t_TP4,cell5_TP4, linewidth = 0.25, color = 'royalblue')
axTP4_cell5.set_ylim(0.2,1.2)
axTP4_cell5.axis('off')

plt.show()
fig_TP4.savefig('./example_data/draw_traces/TP4.svg', format = 'svg')