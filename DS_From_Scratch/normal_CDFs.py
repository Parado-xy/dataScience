from Stats import normal_cdf
import matplotlib.pyplot as plt

#generate an array of values from -5.0 - 4.9
xs = [(x/10) for x in range(-50,50)]

plt.plot(xs, [normal_cdf(x) for x in xs], '-', label='mu = 0,sigma = 1')

plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu = 0, sigma = 2')

plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu = 0 , sigma = 0.5')

plt.plot(xs, [normal_cdf(x,mu=-1) for x in xs], '-.', label='mu = -1 , sigma = 0')

plt.legend(loc = 4)#bottom right

plt.title('Various normal CDFs')

plt.show()