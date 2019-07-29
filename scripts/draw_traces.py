import matplotlib.pyplot as plt
import pandas as pd


def main():
    # load csv as data frame
    df = pd.read_csv('./example_data/draw_traces/top5_correlated.csv')

    frames_recorded = 6080
    # calculate number of time points
    ntimepoints = int(len(df) // frames_recorded)

    # extract time (t) and fluorescence data for each ROI (cell 1-5)
    t = df.ix[:,'y0000']

    # extract data for each time point from all ROIs
    cell_names = ['x0000', 'x0001', 'x0002', 'x0003', 'x0004']
    for timepoint in range(ntimepoints):
        cells_TP = []
        for cell_name in cell_names:
            cell = df.ix[:, cell_name]
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
            ax.set(ylim=y_lim, yticks=[])
            ax.axis(visibility)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_position(('outward',10))
        ax.set(ylabel='ΔF/F', xlabel='# of frames')

        #plt.show()
        for fmt in ['svg', 'png']:
            fig.savefig('./example_data/draw_traces/TP{}.svg'.format(timepoint+1), format=fmt)


if __name__ == '__main__':
    main()