#import necessary modules
import matplotlib.pyplot as plt 
from Stats import normal_pdf 

#generate an array of values , divide each of those values by 10
# and put them in an array
xs =[(x/10) for x in range(-50,50)]

plt.plot(xs,[normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')

plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')

plt.plot(xs,[normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')

plt.plot(xs,[normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')

plt.legend()

plt.title('Various Normal PDFs')
#show curves
plt.show()