# importing the required module
import matplotlib.pyplot as plt
import pandas
import numpy as np

df = pandas.read_csv('2023/vrsic-slemenova-spica.csv')
print(df)
 
# x axis values
x = df['datum']
x = x[0::48]

x.reindex(index=range(0,len(x)))

print(x)
# corresponding y axis values
# y = df['vhodi']
# np.add.reduceat(y, np.arange(0, len(y), 48))
 
# # plotting the points 
# plt.plot(x, y)
 
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
 
# # giving a title to my graph
# plt.title('My first graph!')
 
# # function to show the plot
# plt.show()