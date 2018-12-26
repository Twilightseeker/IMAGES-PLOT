#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([1, 2, 3, 4, 5, 6])
Model_1 = np.array([2.9749694, 3.9357018, 4.7440844, 6.482254, 8.720203, 13.687582])
Model_2 = np.array([2.1044724, 2.9757383, 3.7754183, 5.686206, 8.367847, 14.144531])
Model_3 = np.array([2.0205495, 2.6509762, 3.1876223, 4.380781, 6.004548, 9.9298])


#label displayed in legend. If it is an equation, better add '$' before the string.
#line style: - -- -. : ,
#marker style: . , o, v < * ^ + 1

plt.figure(figsize=(15, 8))
plt.grid(linestyle='--') # set a grid background, or screen it if don't want it.
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.plot(x, Model_1, marker='o', color='black',
         label="Model1-Style result", linewidth=3)
plt.plot(x, Model_2, marker='o', color='green',
         label="Model2-Style result", linewidth=3)
plt.plot(x, Model_3, marker='o', color='red',
         label="Model3-Style result", linewidth=3)

group_labels = ['Top 0-5%', 'Top 5-10%', 'Top 10-20%', 'Top 20-50%', 'Top 50-70%', 'Top 70-100%']
plt.xticks(x, group_labels, fontsize=17, fontweight='bold')
plt.yticks(fontsize=17, fontweight='bold')
plt.title("an   example   to   display", fontsize=27, fontweight='bold')
plt.xlabel("Performance Percentage", fontsize=17, fontweight='bold')
plt.ylabel("4pt-Homography RMSE", fontsize=17, fontweight='bold')
plt.xlim(.9, 6.1) #x axis displaying range
plt.ylim(1.5, 16)#y axis displaying range

plt.legend(loc=0, numpoints=1)
#plt.legend() could use parameters to control its place.
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=15, fontweight='bold')

plt.savefig('./an-example.svg', format='svg')
#recommend to save svg format, then use inkscape to change to arrow image .emf then insert into word
plt.show()
