from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']
#plot the scatter diagram
plt.scatter(friends,minutes)

#label each point
for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy=(friend_count,minute_count),#put the label with its points
                 xytext=(5,-5),#but slightly offset
                 textcoords='offset points')
    
plt.title('Daily minutes vs Number of friends')
plt.xlabel('# of friends')
plt.ylabel('Daily minutes on the site')
plt.show()


