import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('ggplot')

byzantine = pd.read_csv('byzantine.csv')
byzantine4 = pd.read_csv('byzantine4.csv')
byzantine40 = pd.read_csv('byzantine40.csv')
byzantine100 = pd.read_csv('byzantine100.csv')
weighted = pd.read_csv('weighted.csv')
weighted4 = pd.read_csv('weighted4.csv')
weighted40 = pd.read_csv('weighted40.csv')
weighted100 = pd.read_csv('weighted100.csv')
outlier = pd.read_csv('outlier.csv')
outlier4 = pd.read_csv('outlier4.csv')
outlier40 = pd.read_csv('outlier40.csv')
outlier100 = pd.read_csv('outlier100.csv')

x = byzantine['frequency']
y1 = byzantine['correctness']
y2 = weighted['correctness']
y3 = outlier['correctness']

x2 = byzantine4['magnitude']
y4 = byzantine4['correctness']
y5 = weighted4['correctness']
y6 = outlier4['correctness']

y7 = byzantine40['correctness']
y8 = weighted40['correctness']
y9 = outlier40['correctness']

y10 = byzantine100['correctness']
y11 = weighted100['correctness']
y12 = outlier100['correctness']

t_byzantine = byzantine['elapsed'].mean()
t_outlier = outlier['elapsed'].mean()
t_weighted = weighted['elapsed'].mean()
names = ['byzantine', 'outlier', 'weighted']
#plt.barh(names, [t_byzantine, t_outlier, t_weighted])

fig, axs = plt.subplots(1, 4)

axs[0].set_title("Correctness by error rate \n e = 0.3")
axs[0].set_xlabel("Error rate")
axs[0].set_ylabel("% of correct results")
axs[0].plot(x, y1, label='Byzantine', color="black", linestyle="solid")
axs[0].plot(x, y2, label='W. Average', color="black", linestyle="dotted")
axs[0].plot(x, y3, label='Outliers + Avg', color="black", linestyle="dashed")
axs[0].legend()

axs[1].set_title("Correctness by error amplitude \n 4% error rate")
axs[1].set_xlabel("Error Amplitude")
axs[1].set_ylabel("% of correct results")
axs[1].plot(x2, y4, label='Byzantine', color="black", linestyle="solid")
axs[1].plot(x2, y5, label='W. Average', color="black", linestyle="dotted")
axs[1].plot(x2, y6, label='Outliers + Avg', color="black", linestyle="dashed")
axs[1].legend()

axs[2].set_title("Correctness by error amplitude \n 40% error rate")
axs[2].set_xlabel("Error Amplitude")
axs[2].set_ylabel("% of correct results")
axs[2].plot(x2, y7, label='Byzantine', color="black", linestyle="solid")
axs[2].plot(x2, y8, label='W. Average', color="black", linestyle="dotted")
axs[2].plot(x2, y9, label='Outliers + Avg', color="black", linestyle="dashed")
axs[2].legend()

axs[3].set_title("Correctness by error amplitude \n 100% error rate")
axs[3].set_xlabel("Error Amplitude")
axs[3].set_ylabel("% of correct results")
axs[3].plot(x2, y10, label='Byzantine', color="black", linestyle="solid")
axs[3].plot(x2, y11, label='W. Average', color="black", linestyle="dotted")
axs[3].plot(x2, y12, label='Outliers + Avg', color="black", linestyle="dashed")
axs[3].legend()

"""
axs[1,1].set_title("Completion time for 10000 voting rounds")
axs[1,1].set_xlabel("Algorithm")
axs[1,1].set_xticklabels(['Byzantine', 'W. Average', 'Outliers + Avg'])
axs[1,1].set_ylabel("Elapsed time (seconds)")
#axs[1,1].barh(names, [t_byzantine, t_outlier, t_weighted])
byzantine_t = pd.concat([byzantine['elapsed'], byzantine4['elapsed'], byzantine40['elapsed'], byzantine100['elapsed']])
weighted_t = pd.concat([weighted['elapsed'], weighted4['elapsed'], weighted40['elapsed'], weighted100['elapsed']])
outlier_t = pd.concat([outlier['elapsed'], outlier4['elapsed'], outlier40['elapsed'], outlier100['elapsed']])
axs[1,1].boxplot([byzantine_t, weighted_t, outlier_t])

fig.delaxes(axs[1][2])
#plt.plot(x2, y4, x2, y5, x2, y6)
#plt.plot(x2, y7, x2, y8, x2, y9)
#plt.plot(x2, y10, x2, y11, x2, y12)
"""
plt.show()
