import matplotlib.pyplot as plt
import pandas as pd



# load csv as data frame
df = pd.read_csv('/Users/blumenstock/Documents/161results/top5_correlated.csv')

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

axTP1_cell1.plot(t_TP1, cell1_TP1, linewidth = 0.17, color = 'firebrick')
axTP1_cell1.set_ylim(4,4.8)
axTP1_cell2.plot(t_TP1,cell2_TP1, linewidth = 0.17, color = 'sandybrown')
axTP1_cell2.set_ylim(3.3,4.1)
axTP1_cell3.plot(t_TP1,cell3_TP1, linewidth = 0.17, color = 'darkkhaki')
axTP1_cell3.set_ylim(2.1,2.9)
axTP1_cell4.plot(t_TP1,cell4_TP1, linewidth = 0.17, color = 'seagreen')
axTP1_cell4.set_ylim(0.9,1.7)
axTP1_cell5.plot(t_TP1,cell5_TP1, linewidth = 0.17, color = 'royalblue')
axTP1_cell5.set_ylim(-0.1,0.7)

plt.ylabel('ΔF/F')
plt.xlabel('no. of frames')

plt.show()

# Plot all cells for TP2
#
# fig_TP2 = plt.figure()
# axTP2_cell1 = fig_TP2.add_subplot(511)
# axTP2_cell2 = fig_TP2.add_subplot(512)
# axTP2_cell3 = fig_TP2.add_subplot(513)
# axTP2_cell4 = fig_TP2.add_subplot(514)
# axTP2_cell5 = fig_TP2.add_subplot(515)
#
# axTP2_cell1.plot(t_TP2,cell1_TP2)
# axTP2_cell2.plot(t_TP2,cell2_TP2)
# axTP2_cell3.plot(t_TP2,cell3_TP2)
# axTP2_cell4.plot(t_TP2,cell4_TP2)
# axTP2_cell5.plot(t_TP2,cell5_TP2)
#
# plt.show()


#ax2_cell1.plot(y0_TP2,x0_TP2)



#ax3_cell1.plot(y0_TP3,x0_TP3)



#ax4_cell1.plot(y0_TP4,x0_TP4)