
# matplotlib

#importing libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data = {'Names' : ['Adjoa', 'Jerry', 'Divine', 'Freedom', 'Gertrude', 'Mabel', 'Gabriel', 'Gifty', 'Nana', 'Qwame'], 
        'Hieghts' : [12,23,34,56,45,56,78,65,47,67], 'Wieghts' : [234,345,456,765,876,345,679,434,243,264]}

plt.plot('Names','Hieghts')
plt.scatter('Names','Wieghts')
plt.show()