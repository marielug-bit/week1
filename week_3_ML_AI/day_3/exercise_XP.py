#Exercice2
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

data = [12, 15, 13, 12, 18, 20, 22, 21]

mean = stats.tmean(data)
med = np.median(data)

#Exercise 3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 50, 10  # mean and standard deviation
gaussian_dist = stats.norm(mu, sigma)
print("PDF at x=0.5:", gaussian_dist.pdf(0.5))

#Exercice 4
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)
t_stat, p_val = stats.ttest_ind(data1, data2)

#Exercice 5
house_sizes = [50, 70, 80, 100, 120]
house_prices = [150000, 200000, 210000, 250000, 280000]

#What is the slope and intercept of the regression line?
#Predict the price of a house that is 90 square meters.
#Interpret the meaning of the slope in the context of housing prices.

slope, intercept, r_value, p_value, std_err = stats.linregress(house_sizes, house_prices)
print("Slope:", slope)
print("Intercept:", intercept)
line = [slope*x + intercept for x in house_sizes]
print(f'price of a house of 90m2 will be {slope*90+intercept} dollars')
plt.scatter(house_sizes, house_prices)
plt.plot(house_sizes, line)
plt.show()

#Exercice 6
fertilizer_1= [5, 6, 7, 6, 5]
fertilizer_2= [7, 8, 7, 9, 8]
fertilizer_3= [4, 5, 4, 3, 4]

f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)
print("F-value:", f_value)
print("P-value:", p_value)