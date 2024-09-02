from matplotlib import pyplot as plt

movies = ['Annie Hall','Ben-Hur','Casablanca','Gandhi','West side story']
num_oscars = [5,11,3,8,10]

#plot bars with left x-coordinates [0,1,2,3,4], heights[num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title('My favorite Movies')#add a title

plt.ylabel('# of academy awards')

#label x-axis with movie names at bar centers
plt.xticks(range(len(movies)),movies)


#show the graph
plt.show()