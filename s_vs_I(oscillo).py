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


document = xlrd.open_workbook("Jets non-défléchi&défléchi.xlsx")
feuille_1 = document.sheet_by_index(0)

s_m = np.array([])
s_p = np.array([])
err_s = np.array([])
I_EA = np.array([])

for r in range(15, 22):
    s_m = np.append(s_m, feuille_1.cell_value(rowx=r, colx=9))
    s_p = np.append(s_p, feuille_1.cell_value(rowx=r, colx=10))
    err_s = np.append(err_s, feuille_1.cell_value(rowx=r, colx=11))
    I_EA = np.append(I_EA, feuille_1.cell_value(rowx=r, colx=3))

errI_EA = np.array([0.1] * len(I_EA))

s_moy = (s_m + s_p)/2
err_s_moy = 2*err_s

def lin(x, a, b):
    return a*x + b

popt, pcov = curve_fit(lin, I_EA, s_moy)
x = np.linspace(min(I_EA), max(I_EA), 1000)

residuals = s_moy - lin(I_EA, *popt)
ss_res = np.sum(residuals ** 2)
ss_tot = np.sum((s_moy-np.mean(s_moy))**2)
r_squared = 1 - (ss_res / ss_tot)

plt.errorbar(I_EA, s_m, xerr=errI_EA, yerr=err_s, marker='v', ls='None', label='$s_-$')
plt.errorbar(I_EA, s_p, xerr=errI_EA, yerr=err_s, marker='^', ls='None', label='$s_+$')
plt.plot(x, lin(x, *popt), linestyle='-', color='black', label="Fit linéaire de la moyenne de $s_+$ et $s_-$ :"
                                                               f"\n$s_{{moy}} = ${fmt(popt[0])}$I + ${fmt(popt[1])} $(R^2 = {r_squared:.3f})$")
plt.legend()
plt.xlabel("Intensité de l'électro-aimant $[A]$")
plt.ylabel("Déflexion induite par l'électro-aimant $[mm]$")
plt.savefig('figures/s_vs_I(oscillo).png', dpi=200)
plt.show()

