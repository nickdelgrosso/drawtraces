import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

def main():
    # load csv as data frame
    df = pd.read_csv('./example_data/draw_traces/top5_correlated.csv')

    frames_recorded = 6080

    # calculate number of time points
    ntimepoints = int(len(df) // frames_recorded)

    # extract time (t) and fluorescence data for each ROI (cell 1-5)
    t = df.ix[:,'y0000']
    cell1 = df.ix[:,'x0000']
    cell2 = df.ix[:,'x0001']
    cell3 = df.ix[:,'x0002']
    cell4 = df.ix[:,'x0003']
    cell5 = df.ix[:,'x0004']

    #extract time (t) for 4 timepoints (TP)
    t_TPs = []
    for timepoint in range(ntimepoints):
        t_TP = t.ix[timepoint*frames_recorded : (timepoint+1)*frames_recorded - 1]
        t_TPs.append(t_TP)

    # extract data for each time point from ROI 0000 (cell1)
    cell1_TPs = []
    for timepoint in range(ntimepoints):
        cell1_TP = cell1.ix[timepoint*frames_recorded : (timepoint+1)*frames_recorded -1]
        cell1_TPs.append(cell1_TP)


    # extract data for each time point from ROI 0001 (cell2)
    cell2_TPs = []
    for timepoint in range(ntimepoints):
        cell2_TP = cell2.ix[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        cell2_TPs.append(cell2_TP)

    # extract data for each time point from ROI 0002 (cell3)
    cell3_TPs = []
    for timepoint in range(ntimepoints):
        cell3_TP = cell3.ix[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        cell3_TPs.append(cell3_TP)

    # extract data for each time point from ROI 0003 (cell4)
    cell4_TPs = []
    for timepoint in range(ntimepoints):
        cell4_TP = cell4.ix[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        cell4_TPs.append(cell4_TP)

    # extract data for each time point from ROI 0004 (cell5)
    cell5_TPs = []
    for timepoint in range(ntimepoints):
        cell5_TP = cell5.ix[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        cell5_TPs.append(cell5_TP)


    # Plot all cells for TP1


    for timepoint in range(ntimepoints):
        fig_TP1 = plt.figure()
        axTP1 = fig_TP1.add_subplot(511)
        axTP1.plot(t_TPs[timepoint], cell1_TPs[timepoint], linewidth = 0.25, color = 'firebrick')
        axTP1.set_ylim(3.8,4.8)
        axTP1.axis('off')

        axTP1 = fig_TP1.add_subplot(512)
        axTP1.plot(t_TPs[timepoint],cell2_TPs[timepoint], linewidth = 0.25, color = 'sandybrown')
        axTP1.set_ylim(3.3,4.3)
        axTP1.axis('off')

        axTP1 = fig_TP1.add_subplot(513)
        axTP1.plot(t_TPs[timepoint],cell3_TPs[timepoint], linewidth = 0.25, color = 'darkkhaki')
        axTP1.set_ylim(2,3)
        axTP1.axis('off')

        axTP1 = fig_TP1.add_subplot(514)
        axTP1.plot(t_TPs[timepoint],cell4_TPs[timepoint], linewidth = 0.25, color = 'seagreen')
        axTP1.set_ylim(0.8,1.8)
        axTP1.axis('off')

        axTP1 = fig_TP1.add_subplot(515)
        axTP1.plot(t_TPs[timepoint],cell5_TPs[timepoint], linewidth = 0.25, color = 'royalblue')
        axTP1.set_ylim(-0.2,0.8)
        #axTP1_cell5.axis('off')


        axTP1.spines['right'].set_visible(False)
        axTP1.spines['top'].set_visible(False)
        axTP1.spines['bottom'].set_position(('outward',10))
        axTP1.set_yticks([])

        #Adjust spacing between subplots
        plt.ylabel('ΔF/F')
        plt.xlabel('# of frames')

        #plt.show()
        fig_TP1.savefig('./example_data/draw_traces/TP{}.svg'.format(timepoint+1), format = 'svg')
        fig_TP1.savefig('./example_data/draw_traces/TP{}.png'.format(timepoint+1), format = 'png')


if __name__ == '__main__':
    main()