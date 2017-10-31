import matplotlib.pyplot as plt


#dot
#plt.scatter(2, 4, s=200, color="black")

#square numbers
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


#edgecolor - remove outline(outline around points)
#colormap - c=y_values, cmap=plt.cm.Blues
plt.scatter(x_values, y_values, s=20, c=y_values, cmap=plt.cm.Blues, edgecolor='none')


#set chart title and label axes.
plt.title("square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set range for each axis
plt.axis([0, 1100, 0, 1100000])

#set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#save plot
plt.savefig('squares_plot.png')

plt.show()

