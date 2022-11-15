import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.available
plt.style.use("dark_background")
x=[1,2,3,4]
y=[3,5,3,7]
# plt.plot(x,y,color="red")

plt.plot(x,np.sin(x),color="blue")
plt.plot(x, np.cos(x),color="pink")

plt.title("Ten do thi ")

plt.show()
