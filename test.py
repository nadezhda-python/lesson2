import ephem
from datetime import datetime

mars = ephem.Mars(datetime.today())
const = ephem.constellation(mars)
print (type(const))
print(const)

