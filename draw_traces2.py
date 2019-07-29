import matplotlib.pyplot as plt
import pandas as pd



# load csv as data frame
df_geco = pd.read_csv('./jRGECO.csv')
df_gcamp = pd.read_csv('./GCamP7.csv')
#df_gcamp

# extract time (t) and fluorescence data for each ROI
t = df_geco.ix[:,'y0000']
VIP = df_geco.ix[:,'x0000']
camk = df_gcamp.ix[:,'x0000']

#time in cropped video
t_crop = t.ix[316:715]
VIP_crop = VIP.ix[316:715]
camk_crop = camk.ix[316:715]



# Plot all cells for TP1

fig = plt.figure(figsize=(15,5))
ax_vip = fig.add_subplot(211)
ax_camk = fig.add_subplot(212)

ax_vip.plot(t_crop, VIP_crop, linewidth = 1, color = 'magenta')
ax_camk.plot(t_crop, camk_crop, linewidth = 1, color = 'limegreen')


#Adjust spacing between subplots
plt.ylabel('ΔF/F')
plt.xlabel('# of frames')

#plt.show()
fig.savefig('2059_GCamP_GECO_example_traces.svg', format = 'svg')


plt.show()
