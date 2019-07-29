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
        fig = plt.figure()
        colors = ['firebrick', 'sandybrown', 'darkkhaki', 'seagreen', 'royalblue']
        y_lims = [(3.8, 4.8), (3.3, 4.3), (2, 3), (0.8, 1.8), (-0.2, 0.8)]
        cells = [cell1_TPs, cell2_TPs, cell3_TPs, cell4_TPs, cell5_TPs]
        subplots = [511, 512, 513, 514, 515]
        visibilities = ['off', 'off', 'off', 'off', 'on']

        for color, y_lim, cell, subplot, visibility in zip(colors, y_lims, cells, subplots, visibilities):
            ax = fig.add_subplot(subplot)
            ax.plot(t_TPs[timepoint], cell[timepoint], linewidth=0.25, color=color)
            ax.set_ylim(y_lim[0], y_lim[1])
            ax.axis(visibility)


        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_position(('outward',10))
        ax.set_yticks([])

        #Adjust spacing between subplots
        ax.set_ylabel('ΔF/F')
        ax.set_xlabel('# of frames')

        #plt.show()
        fig.savefig('./example_data/draw_traces/TP{}.svg'.format(timepoint+1), format = 'svg')
        fig.savefig('./example_data/draw_traces/TP{}.png'.format(timepoint+1), format = 'png')


if __name__ == '__main__':
    main()