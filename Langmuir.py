import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker

I = np.linspace(0.01, 0.16, 15)
Ierr = np.array([0.002]*8 + [0.005]*7)
T = np.array([380, 393, 397, 400, 403, 404, 406, 408, 409, 410, 411, 412, 413, 414, 415])
y = I*np.sqrt(T)
y_err = Ierr*np.sqrt(T)
x1 = 1/T
################################################################

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%.3e' % x))
fmt = mticker.FuncFormatter(g)
################################################################

def exp(x, a, b):
    return a*np.e**(-b * x)

popt, pcov = curve_fit(exp, x1, y, maxfev=1000)
################################################################################
residuals = y - exp(x1, *popt)
ss_res = np.sum(residuals ** 2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
################################################################################

plt.plot(1000*np.linspace(min(x1), max(x1), 100), exp(np.linspace(min(x1), max(x1), 100), *popt), linestyle='-',
         color='black', linewidth=0.5, label=f"$I(T)\sqrt{{T}} =$ {fmt(popt[0])} exp{{-{fmt(popt[1])} / T}}\n($R^2 = ${r_squared:.3f})")
plt.errorbar(1000*x1, y, marker='.', yerr=y_err, ls='none')
plt.xlabel("Inverse de la température du four 1/T $[10^3 \cdot K^{-1}]$", fontsize=13)
plt.ylabel('$I(T)\sqrt{T}$  $[nA \cdot K^{1/2}]$', fontsize=13)
plt.legend(fontsize=12)
plt.tick_params(labelsize=13)
plt.savefig('figures/langmuir', dpi=200)

###############################################################################
k_B = 86.174E-6
phi = k_B*popt[1]
print(f"La constante C est égale à {popt[0]:.3e}")
print(f"La constante Lambda est égale à {popt[1]:.2f} K")
print(f"La constante phi est égale à {phi:.2f} eV")
