import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator


# Zestaw danych 1
Ud1 = np.array([-0.8, -0.5, 0, 0.2, 0.4, 0.5, 0.55, 0.6, 0.65, 0.69, 0.77, 0.79, 0.8, 0.815])
Id1 = np.array([0, 0, 0, 0, 0, 0.14, 0.53, 1.25, 3.4, 5.23, 11.57, 13.49, 15.56, 18.8])

# Zestaw danych 2
Ud2 = np.array([-7.07, -7.02, -7, -6.98, -6.93, -6.91, -5, -4, -1, 0, 0.2, 0.63, 0.659, 0.681, 0.706, 0.715, 0.732, 0.738, 0.748, 0.77, 0.78, 0.808, 0.816, 0.832])
Id2 = np.array([-8.49, -5.66, -3.45, -1.39, -0.09, -0.01, 0, 0, 0, 0, 0, 0.08, 0.2, 0.39, 0.81, 1.07, 1.72, 2, 2.59, 3.94, 5.12, 8.24, 9.32, 11.07])

# Zestaw danych 3
Ud3 = np.array([-10, -5, 0, 1.5, 1.83, 1.9, 1.924, 1.95, 1.97, 1.993, 2.041, 2.055, 2.074, 2.1, 2.13, 2.18, 2.2, 2.25])
Id3 = np.array([0, 0, 0, 0, 0.73, 2.47, 3.27, 4.24, 5.07, 6.28, 7.09, 8.61, 9.45, 10.8, 12.11, 14.35, 15.98, 17.678])

# Interpolacja danych za pomocą funkcji PchipInterpolator
f1 = PchipInterpolator(Ud1, Id1)
f2 = PchipInterpolator(Ud2, Id2)
f3 = PchipInterpolator(Ud3, Id3)

# Generowanie nowych punktów na podstawie funkcji interpolacji
Ud1_new = np.linspace(Ud1.min(), Ud1.max(), 1000)
Id1_new = f1(Ud1_new)

Ud2_new = np.linspace(Ud2.min(), Ud2.max(), 1000)
Id2_new = f2(Ud2_new)

Ud3_new = np.linspace(Ud3.min(), Ud3.max(), 1000)
Id3_new = f3(Ud3_new)

def add_axes(ax):
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

# Rysowanie wykresów
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 12))

# Wykres 1
ax1.plot(Ud1, Id1, 'o',color='cyan', label='Dane punktowe ')
ax1.plot(Ud1_new, Id1_new, '-',color='red', label='Funkcja prądu dla napięcia')
ax1.set_xlabel('Napięcie [V]')
ax1.set_ylabel('Prąd diody [mA]')
ax1.set_title('Wykres Prądu Diody Krzemowej')
add_axes(ax1)
ax1.legend()

# Wykres 2
ax2.plot(Ud2, Id2, 'o',color='cyan', label='Dane punktowe ')
ax2.plot(Ud2_new, Id2_new, '-',color='red', label='Funkcja prądu dla napięcia')
ax2.set_xlabel('Napięcie [V]')
ax2.set_ylabel('Prąd diody [mA]')
ax2.set_title('Wykres Prądu Diody Zenera')
add_axes(ax2)
ax2.legend()

# Wykres 3
ax3.plot(Ud3, Id3, 'o',color='cyan', label='Dane punktowe ')
ax3.plot(Ud3_new, Id3_new, '-',color='red', label='Funkcja prądu dla napięcia')
ax3.set_xlabel('Napięcie [V]')
ax3.set_ylabel('Prąd diody [mA]')
ax3.set_title('Wykres Prądu Diody LED')
add_axes(ax3)
ax3.legend()

# Dopasowanie układu i wyświetlenie wykresów
plt.tight_layout()
plt.show()





