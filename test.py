"""
import ephem


mars = ephem.Mars(datetime.today())
const = ephem.constellation(mars)
print (type(const))
print(const)

"""
from datetime import datetime
print ('{:*>11}'.format('hello') )