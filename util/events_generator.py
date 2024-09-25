import numpy as np
import yfinance as yf
# Descargar datos históricos de Tesla
datos = yf.download('TSLA', start='2024-01-01', end='2024-09-05', interval="1d")

# Obtener los precios de cierre ajustados
precios = datos['Adj Close']
variation = np.diff(np.log(precios))
# retornos = np.log(precios / precios.shift(1))
# print(variation)
mean = np.mean(variation)

standard_deviation = np.std(variation)

print(mean, standard_deviation)