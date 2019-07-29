import matplotlib.pyplot as plt
import pandas as pd


def main():
    # load csv as data frame
    df = pd.read_csv('./example_data/draw_traces/top5_correlated.csv')

    # calculate number of time points
    frames_recorded = 6080
    ntimepoints = int(len(df) // frames_recorded)

    # extract time (t) and fluorescence data for each ROI (cell 1-5)
    t = df['y0000']

    # extract data for each time point from all ROIs
    cell_names = ['x0000', 'x0001', 'x0002', 'x0003', 'x0004']
    for timepoint in range(ntimepoints):
        cells_TP = []
        for cell_name in cell_names:
            cell = df[cell_name]
            cell_TP = cell.iloc[timepoint*frames_recorded : (timepoint+1)*frames_recorded -1]
            cells_TP.append(cell_TP)

        fig, axes = plt.subplots(nrows=len(cell_names))
        colors = ['firebrick', 'sandybrown', 'darkkhaki', 'seagreen', 'royalblue']
        y_lims = [(3.8, 4.8), (3.3, 4.3), (2, 3), (0.8, 1.8), (-0.2, 0.8)]
        visibilities = ['off', 'off', 'off', 'off', 'on']

        t_TP = t.iloc[timepoint * frames_recorded: (timepoint + 1) * frames_recorded - 1]
        for cell_TP, color, y_lim, ax, visibility in zip(cells_TP, colors, y_lims, axes, visibilities):
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