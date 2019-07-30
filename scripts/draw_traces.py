import matplotlib.pyplot as plt
import pandas as pd



dfs = pd.read_csv('./data/draw_traces/top5_correlated.csv',
                 index_col=0,
                 usecols=lambda s: s.startswith('x'),
                 chunksize=6080)


# Suggestion: insert pd.melt() here.

for idx, df in enumerate(dfs):
    df.plot(subplots=True, legend=False)
    for fmt in ['png', 'svg']:
        plt.savefig('./data/draw_traces/TP{}.{}'.format(idx, fmt))

