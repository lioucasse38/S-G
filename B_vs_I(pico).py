import xlrd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker

################################################################

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%.3e' % x))
fmt = mticker.FuncFormatter(g)
################################################################


document = xlrd.open_workbook("Distribution spatiale de l'intensité du jet atomique non-défléchi.xlsx")
feuille_1 = document.sheet_by_index(0)

I_EA = np.array([])
B_moy = np.array([])
errB_moy = np.array([])

for r in range(12, 18):
    I_EA = np.append(I_EA, feuille_1.cell_value(rowx=r, colx=2))
    B_moy = np.append(B_moy, feuille_1.cell_value(rowx=r, colx=9))
    errB_moy = np.append(errB_moy, feuille_1.cell_value(rowx=r, colx=12))

errI_EA = np.array([0.1]*len(I_EA))


def lin(x, a, b):
    return a*x + b

popt, pcov = curve_fit(lin, I_EA, B_moy)
x = np.linspace(min(I_EA), max(I_EA), 1000)

residuals = B_moy - lin(I_EA, *popt)
ss_res = np.sum(residuals ** 2)
ss_tot = np.sum((B_moy-np.mean(B_moy))**2)
r_squared = 1 - (ss_res / ss_tot)
print(r_squared)

plt.errorbar(I_EA, B_moy, xerr=errI_EA, yerr=errB_moy, ls='None', marker='v', color='#20B2AA')
plt.plot(x, lin(x, *popt), label=f"$B = ${fmt(popt[0])}$I + ${fmt(popt[1])}\n($R^2 = {r_squared:.3f}$)", color='#FFD700')
plt.xlabel("Intensité de l'électro-aimant $[A]$", fontsize=15)
plt.ylabel('Champ magnétique moyen $[T]$', fontsize=15)
plt.tick_params(labelsize=13)
plt.legend()
plt.show()
plt.savefig('figures/B_vs_I(pico).png', dpi=200)