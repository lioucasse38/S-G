import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as mticker



f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%.3e' % x))
fmt = mticker.FuncFormatter(g)

I = np.linspace(0.1, 1.6, 15)
Ierr = np.array([0.02]*8 + [0.05]*7)
T = np.array([107, 120, 124, 127, 130, 131, 133, 135, 136, 137, 138, 139, 140, 141, 142])
y = I*np.sqrt(T)
y_err = Ierr*np.sqrt(T)
x1 = 1/T

def exp(x, a, b):
    return a*np.e**(-b * x)


popt, pcov = curve_fit(exp, x1, y)
print(popt)
plt.plot(1000*np.linspace(0.007, 0.0095, 100), exp(np.linspace(0.007, 0.0095, 100), *popt), linestyle='-',
         color='black', linewidth=0.5, label=f"$I(T)\sqrt{{T}} =$ {fmt(popt[0])} exp{{{fmt(popt[1])} / T}}")
plt.errorbar(1000*x1, y, marker='.', yerr=y_err, ls='none')
plt.xlabel("Inverse de la température du four 1/T $[10^3 \cdot K^{-1}]$", fontsize=13)
plt.ylabel('$I(T)\sqrt{T}$  $[nA \cdot K^{1/2}]$', fontsize=13)
plt.legend(fontsize=13)
plt.tick_params(labelsize=13)
plt.savefig('figures/langmuir', dpi=200)
plt.show()