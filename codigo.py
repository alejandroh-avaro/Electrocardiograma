#ELECTROCARDIOGRAMA 
#Alejandro Quenan Hurtado 

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd

# Paso 1: Definir los datos
# Leer los datos desde el archivo CSV
df = pd.read_csv('csv.csv')

# Convertir los datos a un array NumPy
spectrum = df.to_numpy().flatten()
print(spectrum)

# Reemplaza esto con tu espectro real
fs = 150  # Frecuencia de muestreo

# Paso 2: Calcular las frecuencias correspondientes
n = len(spectrum)
print("Tamaño del vector:", n)
frequencies = np.fft.fftfreq(n, d=1/fs)

print(frequencies)
K =np.argmax(frequencies)
print("El arguemento  maximo  en la lista es:", K)

#nota: un vez tenemos el valor maximo  que puede tomaR SE PROCEDE HACER LA SIGUIENETE RELCAICON CON EL FIN DE
#SABER LA FRECUENCIA FUNDMANETAL
F=(K/n)*fs
print("FRECUENCIA CARDIACA  DEL PACIENTE ",F)

# Paso 3: Identificar los armónicos
# Encontramos los picos en el espectro
peaks, _ = find_peaks(np.abs(spectrum)[:n//2], height=0.1)  # Ajusta el umbral de altura según sea necesario

# Paso 4: Graficar la magnitud del espectro y resaltar los armónicos
plt.figure(figsize=(10, 5))

plt.plot(frequencies[:n//2], np.abs(spectrum)[:n//2], label='Espectro de la señal')
plt.scatter(frequencies[peaks], np.abs(spectrum)[peaks], color='red', label='Armónicos')
plt.title('Espectro de Frecuencia de la Señal con Armónicos')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid()
plt.xlim(0, fs/2)  # Graficar solo un periodo de la señal transformada
plt.show()


# Paso 5: Filtrar las frecuencias entre 60 y 70 Hz
mask = (frequencies >= 74) & (frequencies <= 75)
filtered_frequencies = frequencies[mask]
filtered_spectrum = np.abs(spectrum)[mask]

# Paso 6: Graficar la magnitud del espectro en el rango deseado
plt.figure(figsize=(101, 10))

plt.plot(filtered_frequencies, filtered_spectrum, label='Espectro de la señal (60-70 Hz)')
plt.scatter(filtered_frequencies, filtered_spectrum, color='red', label='Armónicos')
plt.title('Espectro de Frecuencia de la Señal (60-70 Hz)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(linestyle='--', linewidth=0.5)  # Cambiar el estilo y grosor de la cuadrícula
plt.show()
