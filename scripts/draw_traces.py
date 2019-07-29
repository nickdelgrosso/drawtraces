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


    # extract data for each time point from all ROIs
    cells = [cell1, cell2, cell3, cell4, cell5]
    for timepoint in range(ntimepoints):
        cells_TP = []
        for cell in cells:
            cell_TP = cell.ix[timepoint*frames_recorded : (timepoint+1)*frames_recorded -1]
            cells_TP.append(cell_TP)

        fig = plt.figure()
        colors = ['firebrick', 'sandybrown', 'darkkhaki', 'seagreen', 'royalblue']
        y_lims = [(3.8, 4.8), (3.3, 4.3), (2, 3), (0.8, 1.8), (-0.2, 0.8)]
        subplots = [511, 512, 513, 514, 515]
        visibilities = ['off', 'off', 'off', 'off', 'on']

        t_TP = t.ix[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        for cell_TP, color, y_lim, subplot, visibility in zip(cells_TP, colors, y_lims, subplots, visibilities):
            ax = fig.add_subplot(subplot)
            ax.plot(t_TP, cell_TP, linewidth=0.25, color=color)
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