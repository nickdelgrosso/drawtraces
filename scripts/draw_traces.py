import matplotlib.pyplot as plt
import pandas as pd



# load csv as data frame
df = pd.read_csv('./data/draw_traces/top5_correlated.csv')

# extract time (t) and fluorescence data for each ROI (cell 1-5)

t = df.ix[:,'y0000']
cell_names = ['x0000', 'x0001', 'x0002', 'x0003', 'x0004']

#extract time (t) for 4 timepoints (TP)
for idx, tp in enumerate([0, 6080, 12160, 18240]):
    t_TP = t.ix[tp:tp+6079]

    fig, axes = plt.subplots(nrows=5)

    for ax, cell_name in zip(axes, cell_names):
        cell_TP = df.ix[tp:tp + 6079, cell_name]
        ax.plot(t_TP, cell_TP, linewidth = 0.25)

    #Adjust spacing between subplots
    plt.ylabel('ΔF/F')
    plt.xlabel('# of frames')
    fig.savefig('./data/draw_traces/TP{}.png'.format(idx+1), format = 'png')


