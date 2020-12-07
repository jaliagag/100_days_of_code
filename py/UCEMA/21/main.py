import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#x = np.arange(-5, 5,0.1) # rango a cubrir
#y = np.cos(x) # función a graficar

#plt.plot(x, y, 'r.')
#plt.plot(x, y, 'r')
#plt.plot(x, y, 'r--')
#plt.plot(x, y, 'r-')

#plt.show()

archivo = pd.read_csv("AAPL.csv")
#print(archivo)
stock = archivo.to_dict("list")

plt.figure(figsize=(10, 10))

x = [stock["Date"][0]]
y = [stock["Close"][0]]

for i in range(1,len(stock["Date"])):
    x.append(stock["Date"][i])
    y.append(stock["Close"][i])

plt.plot(x,y)

plt.show()



