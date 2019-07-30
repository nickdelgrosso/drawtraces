import matplotlib.pyplot as plt
import pandas as pd
from PyFunctional import seq


seq(pd.read_csv('./data/draw_traces/top5_correlated.csv',
                 index_col='y0000',
                 usecols=['x0000', 'x0001', 'x0002', 'x0003', 'x0004'],
                 chunksize=6080)
     )
    .map(tp.plot(subplots=True, xlabel='dfa', ylabel='dfa'))
    .map(plt.savefig)
)

