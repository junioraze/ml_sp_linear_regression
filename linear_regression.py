from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

# create values
xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)


def best_fit_slop(xs, ys):
    ''' FUNCTION TO CALCULATE BEST FIT SLOP '''
    m = ((mean(xs)*mean(ys)) - mean(xs*ys))/(mean(xs)**2 - mean(xs**2))
    return m

def y_intercept(xs, ys, m):
    ''' FUNCTION TO CALCULATE THE Y INTERCEPT'''
    y_int = mean(ys) - m*mean(xs)
    return y_int



if __name__ = '__main__':
    #define the values of m and b    
    m = best_fit_slop(xs,ys)
    b = y_intercept(xs, ys, m)
    print(f'best fit slop value:\t {m}')
    print(f'y intercept:\t {b}')

    #create a regression line 
    regression_line = [(m*x) + b for x in xs]
    print(regression_line)

    #plot the data (scatter) and the regression line
    plt.scatter(xs, ys)
    plt.plot(regression_line, color='r')
    plt.show()
