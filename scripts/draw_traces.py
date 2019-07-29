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

    fig_TP1 = plt.figure()
    axTP1_cell1 = fig_TP1.add_subplot(511)
    axTP1_cell2 = fig_TP1.add_subplot(512)
    axTP1_cell3 = fig_TP1.add_subplot(513)
    axTP1_cell4 = fig_TP1.add_subplot(514)
    axTP1_cell5 = fig_TP1.add_subplot(515)


    axTP1_cell1.plot(t_TPs[0], cell1_TPs[0], linewidth = 0.25, color = 'firebrick')
    axTP1_cell1.set_ylim(3.8,4.8)
    axTP1_cell1.axis('off')
    axTP1_cell2.plot(t_TPs[0],cell2_TPs[0], linewidth = 0.25, color = 'sandybrown')
    axTP1_cell2.set_ylim(3.3,4.3)
    axTP1_cell2.axis('off')
    axTP1_cell3.plot(t_TPs[0],cell3_TPs[0], linewidth = 0.25, color = 'darkkhaki')
    axTP1_cell3.set_ylim(2,3)
    axTP1_cell3.axis('off')
    axTP1_cell4.plot(t_TPs[0],cell4_TPs[0], linewidth = 0.25, color = 'seagreen')
    axTP1_cell4.set_ylim(0.8,1.8)
    axTP1_cell4.axis('off')
    axTP1_cell5.plot(t_TPs[0],cell5_TPs[0], linewidth = 0.25, color = 'royalblue')
    axTP1_cell5.set_ylim(-0.2,0.8)
    #axTP1_cell5.axis('off')


    axTP1_cell5.spines['right'].set_visible(False)
    axTP1_cell5.spines['top'].set_visible(False)
    axTP1_cell5.spines['bottom'].set_position(('outward',10))
    axTP1_cell5.set_yticks([])

    #Adjust spacing between subplots
    plt.ylabel('ΔF/F')
    plt.xlabel('# of frames')

    #plt.show()
    fig_TP1.savefig('./example_data/draw_traces/TP1.svg', format = 'svg')
    fig_TP1.savefig('./example_data/draw_traces/TP1.png', format = 'png')




    # Plot all cells for TP2

    fig_TP2 = plt.figure()
    axTP2_cell1 = fig_TP2.add_subplot(511)
    axTP2_cell2 = fig_TP2.add_subplot(512)
    axTP2_cell3 = fig_TP2.add_subplot(513)
    axTP2_cell4 = fig_TP2.add_subplot(514)
    axTP2_cell5 = fig_TP2.add_subplot(515)

    axTP2_cell1.plot(t_TPs[1],cell1_TPs[1], linewidth = 0.25, color = 'firebrick')
    axTP2_cell1.set_ylim(4,5)
    axTP2_cell1.axis('off')
    axTP2_cell2.plot(t_TPs[1],cell2_TPs[1], linewidth = 0.25, color = 'sandybrown')
    axTP2_cell2.set_ylim(2.8,3.8)
    axTP2_cell2.axis('off')
    axTP2_cell3.plot(t_TPs[1],cell3_TPs[1], linewidth = 0.25, color = 'darkkhaki')
    axTP2_cell3.set_ylim(2, 3)
    axTP2_cell3.axis('off')
    axTP2_cell4.plot(t_TPs[1],cell4_TPs[1], linewidth = 0.25, color = 'seagreen')
    axTP2_cell4.set_ylim(0.8,1.8)
    axTP2_cell4.axis('off')
    axTP2_cell5.plot(t_TPs[1],cell5_TPs[1], linewidth = 0.25, color = 'royalblue')
    axTP2_cell5.set_ylim(0.2,1.2)
    axTP2_cell5.axis('off')

    #plt.show()
    fig_TP2.savefig('./example_data/draw_traces/TP2.svg', format = 'svg')

    # Plot all cells for TP3

    fig_TP3 = plt.figure()
    axTP3_cell1 = fig_TP3.add_subplot(511)
    axTP3_cell2 = fig_TP3.add_subplot(512)
    axTP3_cell3 = fig_TP3.add_subplot(513)
    axTP3_cell4 = fig_TP3.add_subplot(514)
    axTP3_cell5 = fig_TP3.add_subplot(515)

    axTP3_cell1.plot(t_TPs[2],cell1_TPs[2], linewidth = 0.25, color = 'firebrick')
    axTP3_cell1.set_ylim(4,5)
    axTP3_cell1.axis('off')
    axTP3_cell2.plot(t_TPs[2],cell2_TPs[2], linewidth = 0.25, color = 'sandybrown')
    axTP3_cell2.set_ylim(2.8,3.8)
    axTP3_cell2.axis('off')
    axTP3_cell3.plot(t_TPs[2],cell3_TPs[2], linewidth = 0.25, color = 'darkkhaki')
    axTP3_cell3.set_ylim(2, 3)
    axTP3_cell3.axis('off')
    axTP3_cell4.plot(t_TPs[2],cell4_TPs[2], linewidth = 0.25, color = 'seagreen')
    axTP3_cell4.set_ylim(0.8,1.8)
    axTP3_cell4.axis('off')
    axTP3_cell5.plot(t_TPs[2],cell5_TPs[2], linewidth = 0.25, color = 'royalblue')
    axTP3_cell5.set_ylim(0.2,1.2)
    axTP3_cell5.axis('off')

    #plt.show()
    fig_TP3.savefig('./example_data/draw_traces/TP3.svg', format = 'svg')

    # Plot all cells for TP4

    fig_TP4 = plt.figure()
    axTP4_cell1 = fig_TP4.add_subplot(511)
    axTP4_cell2 = fig_TP4.add_subplot(512)
    axTP4_cell3 = fig_TP4.add_subplot(513)
    axTP4_cell4 = fig_TP4.add_subplot(514)
    axTP4_cell5 = fig_TP4.add_subplot(515)

    axTP4_cell1.plot(t_TPs[3],cell1_TPs[3], linewidth = 0.25, color = 'firebrick')
    axTP4_cell1.set_ylim(4,5)
    axTP4_cell1.axis('off')
    axTP4_cell2.plot(t_TPs[3],cell2_TPs[3], linewidth = 0.25, color = 'sandybrown')
    axTP4_cell2.set_ylim(3.1,4.1)
    axTP4_cell2.axis('off')
    axTP4_cell3.plot(t_TPs[3],cell3_TPs[3], linewidth = 0.25, color = 'darkkhaki')
    axTP4_cell3.set_ylim(2, 3)
    axTP4_cell3.axis('off')
    axTP4_cell4.plot(t_TPs[3],cell4_TPs[3], linewidth = 0.25, color = 'seagreen')
    axTP4_cell4.set_ylim(1,2)
    axTP4_cell4.axis('off')
    axTP4_cell5.plot(t_TPs[3],cell5_TPs[3], linewidth = 0.25, color = 'royalblue')
    axTP4_cell5.set_ylim(0.2,1.2)
    axTP4_cell5.axis('off')

    #plt.show()
    fig_TP4.savefig('./example_data/draw_traces/TP4.svg', format = 'svg')


if __name__ == '__main__':
    main()