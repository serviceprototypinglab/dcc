import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('ggplot')

entry = pd.read_csv('entry.csv')
nprop = pd.read_csv('nprop.csv')
proptype = pd.read_csv('proptype.csv')
pop = pd.read_csv('pop.csv')


fig, axs = plt.subplots(2,2)

color = 'black'
color2 = 'darkgrey'

#axs[0,2].set_xlabel('Date')
axs[0,0].set_title('Local vs network execution time by # of entries', color=color)
axs[0,0].set_xlabel("# of entries")
axs[0,0].set_ylabel("Time (s)")
axs[0,0].bar(entry['Entries'], entry['Local'], color='darkgrey', width=75,label="Local")
print(entry['Local'])
#ax2 = axs[0,0].twinx().twiny()  # instantiate a second axes that shares the same x-axis
#ax2.set_ylim(800,1300)
r2 = [x + 75 for x in entry['Entries']]
axs[0,0].bar(r2, entry['Network'], color='dimgrey', width=75, label='Network')
axs[0,0].legend()
#ax2.yaxis.set_ticks([])
#ax2.xaxis.set_ticks([])

#axs[0,0].set_xlabel('Date')
axs[0,1].set_title('Execution time by number of properties', color=color)
axs[0,1].set_xlabel("# of properties")
axs[0,1].set_ylabel("Time (s)")
axs[0,1].bar(nprop['Nprop'], nprop['Local'], color=color2)

#axs[0,1].set_xlabel('Date')
axs[1,0].set_title('Execution time by number of numeric properties', color=color)
axs[1,0].set_xlabel("# of numeric properties")
axs[1,0].set_ylabel("Time (s)")
#axs[1,0].set_ylim(2,4)
axs[1,0].bar(proptype['Proptype'], proptype['Local'], color=color2)


#axs[1,0].set_xlabel('Date')
axs[1,1].set_title('Local vs network execution time by cluster population', color=color)
axs[1,1].set_xlabel("# of nodes in cluster")
axs[1,1].set_ylabel("Time (s)")
#axs[1,1].set_ylim(800,1300)
axs[1,1].bar(pop['Pop'], pop['Local'], color=color2, label="Local")
#ax3 = axs[1,1].twinx().twiny()  # instantiate a second axes that shares the same x-axis
#ax2.set_ylim(800,1300)
r3 = [x + 1 for x in pop['Pop']]
axs[1,1].bar(r3, pop['Network'], color='dimgrey', label="Network")
#ax3.yaxis.set_ticks([])
#ax3.xaxis.set_ticks([])
axs[1,1].legend()

#plt.show()
fig.set_size_inches(14, 10)
fig.savefig("plot.pdf")
