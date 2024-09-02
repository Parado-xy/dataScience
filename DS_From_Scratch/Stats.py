from matplotlib import pyplot as plt
from typing import List , Tuple
from collections import Counter 
from vectors import sum_of_squares,dot
import math , random
#a bar chart. 

Vector = List[float]

#a mean function
def mean(a:Vector)-> float:
    '''Returns the mean of a supplied vector'''
    ans = round(sum(a) /len(a),0)
    return ans
    

def median(a:Vector)-> float:
    '''Returns the median of a Vector (a) supplied.'''
    if len(a) % 2 != 0:
        ans = len(a)//2
        return sorted(a)[ans]
    else:
        ans = len(a)//2 
        final = (sorted(a)[ans] +sorted(a)[ans-1])/2
        return final



def mode(a:Vector)->float:
    '''Takes s vector a and returns its most common data point 
    and its number off occurences as a tuple '''
    count = Counter(a).most_common(1)[0]
    return count

def quantile(a:Vector, p:float)->float:
    '''Returns the pth-percentile value in a'''
    p_index = int(p*len(a))
    return sorted(a)[p_index]

def stat_range(a:Vector)->float:
    '''Takes a vector (a) and returns its range i.e maximum - minimum '''
    return max(a) - min(a)

def de_mean(a:Vector)-> Vector:
    '''Translate a by subtracting its mean (so the result has mean 0)'''
    x_bar = mean(a)
    return[x -x_bar for x in a]

def variance(a:Vector)->float:
    '''Almost the average squared deviation from the mean'''
    assert len(a) >= 2, 'Variance requires at least 2 elements'
    n = len(a)
    deviation = de_mean(a)
    return sum_of_squares(deviation)/(n-1)

def standard_deviation(a:Vector)->float:
    '''Takes in a vector (a) and returns a number representing
    its standard deviation'''
    
    return math.sqrt(variance(a))



def interquartile_range(a:Vector)->float:
    '''Returns the difference between the 75%-ile and 25%-ile'''
    return quantile(a, 0.75) - quantile(a, 0.25)



def covariance(a:Vector, b:Vector)-> float:
    assert len(a) == len(b), 'a and b must be of the same length'
    return  dot(de_mean(a),de_mean(b))/ (len(a)-1)

def correlation(a:Vector , b:Vector)->float:
    '''
    Measures how much a and b vary in tandem about their means
    '''
    stdev_a = standard_deviation(a)
    stdev_b = standard_deviation(b)

    if stdev_a > 0 and stdev_b > 0:
        return (covariance(a,b)/stdev_a/stdev_b)
    else:
        return 0 #if no variation, correlation is zero
    

#Probability section
    ##uniform probability density function
def uniform_pdf(x:float)-> float:
    return 1 if 0 <= x < 1 else 0

##uniform cummulative probability distribution function
def uniform_cdf(x:float)-> float:
    '''
    Returns the probability that a uniform random variable is <= x
    '''
    if x < 0: return 0 #uniform random is never less than 0
    elif x < 1: return x #e.g P(X <= 0.4)= 0.4
    else:       return 1 #uniform random is always less than 1

#normal distribution probability function
#get the square root of 2pi
SQRT_TWO_PI = math.sqrt(2 * math.pi)  

def normal_pdf(x:float, mu:float = 0, sigma:float = 1)-> float:
    '''Returns the normal PDF'''
    return (math.exp(-(x-mu)** 2 / 2 / sigma**2) / (SQRT_TWO_PI * sigma))


#normal cummulative probability distribution function
def normal_cdf(x:float, mu:float=0, sigma:float=1)->float:
    '''Returns the normal CDF'''
    return(
        1 + math.erf((x-mu) / math.sqrt(2) / sigma)
    ) / 2
  

def inverse_normal_cdf(
        p:float,
        mu:float = 0,
        sigma:float = 1,
        tolerance:float = 0.00001
                                    )->float:
    '''Find approximate inverse using binary search'''
    #if not standard, compute standard and rescale
    if mu !=0 or sigma != 1:
        return (mu + sigma) * inverse_normal_cdf(p, tolerance=tolerance)

    '''binary search''' 
    low_z = -10.0   #normal_cdf(-10) is very close to 0
    high_z = 10.0   #normal_cdf(10) is very close to 1

    while high_z - low_z > tolerance:
        mid_z = (high_z + low_z) / 2 #consider the midpoint
        mid_p = normal_cdf(mid_z) # and the CDF's value
        if mid_p < p:
            low_z = mid_z         #mid point is too low, search above it
        else:
            high_z = mid_z        #midpoint is too high, search below it
    return mid_z  

def normal_approximation_to_binomial(n:int, p:float)-> Tuple[float, float]:
    '''Returns mu and sigma corresponding to a Binomial(n,p)'''
    mu = p*n
    sigma = math.sqrt(p *(1-p) * n)
    return mu, sigma

#Whenever a random variable follows a normal distribution, we can use 
#normal_cdf to figure out the probability that its realized value 
#lies within or outside a particular interval:

#The normal_cdf is the probability the variable is below a treshold
normal_probability_below = normal_cdf

#It's above the treshold if it's not below the treshold 
def normal_probability_above (
        lo:float,
        mu:float = 0,
        sigma:float = 1
                        )->float:
    '''The probability that an N(mu, sigma) is greater than lo'''
    return 1 - normal_cdf(lo,mu,sigma)

#It's between if it's less than hi, but not less than lo
def normal_probability_between(
        lo:float,
        hi:float,
        mu:float = 0,
        sigma: float = 1
                          )->float:
    '''The probability that an N(mu, sigma) is between lo and hi'''
    return normal_cdf(hi,mu,sigma) - normal_cdf(lo, mu, sigma)

#It's outside if it's not between
def normal_probability_outside(
        lo:float,
        hi:float,
        mu:float = 0,
        sigma:float = 1
                         )->float:
    '''The probability that an N(mu, sigma ) is not between lo and hi'''
    return 1 - normal_probability_between(lo,hi,mu,sigma) 

#We can also do the reverse—find either the nontail region or the
#(symmetric) interval around the mean that accounts for a certain level of
#likelihood. For example, if we want to find an interval centered at the mean
#and containing 60% probability, then we find the cutoffs where the upper
#and lower tails each contain 20% of the probability (leaving 60%):

def normal_upper_bound(
        probability:float,
        mu:float = 0,
        sigma:float = 1
                        )->float:
    '''Returns the Z for which P(Z <= z) = probabillity '''
    return inverse_normal_cdf(probability, mu ,sigma)

def normal_lower_bound(
        probability:float,
        mu:float = 0,
        sigma:float = 1 
                            )->float:
    '''Returns the Z for which P(Z <= z) = probabillity '''
    return inverse_normal_cdf(1 - probability, mu ,sigma)

def normal_two_sided_bounds(
                    probability: float,
                    mu: float = 0,
                    sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound 
     














    


    

