from scipy.optimize import curve_fit
import pandas as pd
import numpy as np

#DUMMY REPRESENTATION OF ELECTRICITY PRICE(y) AND THERMAL GAP 

x=thermal=[146.0,155.9,308.6,332.1,278.1,176.0,55.1,44.2,55.2,135.9,310.7]
y=price=[39.34,39.17,49.26,50.67,44.98,39.72,26.89,29.25,24.72,41.43,48.35]


def f(x, b, m):
    return b * m ** x

popt, pcov = curve_fit(f, x, y)

b=popt[0]
m=popt[1]

new_y=[286.91,189.56,16.23,-18.25,-95.56,48.47,96.86,187.79,201.73,199.60,-21.35]

new_x=b*m**new_y
new_x=pd.DataFrame(new_x)
display(b)
display(m)
display(new_x)
