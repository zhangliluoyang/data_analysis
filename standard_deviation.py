"""
This is module containing two unrelated functions.
The Standard Deviation is a measure of how spread out numbers are.
"""
import math

def get_mean(num_list):
    # get the mean
    mean = sum(num_list)/len(num_list)
    return mean

def standard_deviation(num_list):
    """
    The standard deviation (sigma) is "the square root of the Variance"
    The variance is "The average of the squared differences from the Mean"
    """
    # get the mean
    mean = sum(num_list)/len(num_list)
    # get variance
    diff_sq_sum = 0
    for num in num_list:
        diff = num - mean
        diff_sq_sum += diff**2
    variance = diff_sq_sum/len(num_list)  # if based on the population
    #or# variance = diff_sq_sum/(len(num_list) - 1) # if based on a sample
    # get square root of variance
    sigma = math.sqrt(variance)
    return round(sigma, 4), variance


#num_list = [9,2,5,4,12,7,8,11]
#num_list = [11367.16112, 12489.95006, 13462.48555, 16076.58803, 18970.57086, 22090.88306, 22898.79214, 26626.51503, 26342.88426, 28954.92589, 33328.96507, 36319.23501]
num_list = [1952.0, 1957.0, 1962.0, 1967.0, 1972.0, 1977.0, 1982.0, 1987.0, 1992.0, 1997.0, 2002.0, 2007.0]
print(standard_deviation(num_list))
