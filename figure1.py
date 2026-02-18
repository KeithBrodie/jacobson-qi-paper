"""
Figure 1: Sharing function f(a) = a/(a + a_0) as a function of acceleration.

Shows the entanglement sharing between Rindler and Hubble horizons,
with a_0 = cH_0/6 = 1.09e-10 m/s^2.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3.0e8          # m/s
H0 = 2.184e-18     # 1/s  (67.4 km/s/Mpc)
cH0 = c * H0       # 6.548e-10 m/s^2
a0 = cH0 / 6.0     # 1.09e-10 m/s^2
a0_MOND = 1.2e-10  # Milgrom's empirical value

# Acceleration range
a = np.logspace(-12, 1, 2000)

# Sharing function: f(a) = a / (a + a0)
f = a / (a + a0)

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 5.5))

# Main curve
ax.plot(a, f, color='#1a1a2e', linewidth=2.5, zorder=5)

# Shade regions
ax.fill_between(a, 0, f, where=(a < a0),
                color='#e8d5b7', alpha=0.4, zorder=2)
ax.fill_between(a, 0, f, where=(a >= a0),
                color='#c5d5e8', alpha=0.25, zorder=2)

# Horizontal references
ax.axhline(y=1.0, color='grey', linewidth=0.5, linestyle='--', zorder=1)
ax.axhline(y=0.5, color='grey', linewidth=0.4, linestyle=':', alpha=0.5, zorder=1)

# --- Vertical markers with staggered labels ---

# a0 = cH0/6 (our prediction)
ax.axvline(x=a0, color='#c0392b', linewidth=1.4, linestyle=':', alpha=0.8, zorder=3)
ax.annotate('$a_0 = cH_0/6$\n$1.09 \\times 10^{-10}$',
            xy=(a0, 1.06), fontsize=8.5, color='#c0392b', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#c0392b', alpha=0.9))

# a0_MOND (Milgrom's empirical)
ax.axvline(x=a0_MOND, color='#e67e22', linewidth=1.2, linestyle=':', alpha=0.8, zorder=3)
ax.annotate('$a_0^{\\mathrm{MOND}}$\n$1.2 \\times 10^{-10}$',
            xy=(a0_MOND, 0.62), fontsize=8, color='#e67e22', ha='left',
            xytext=(a0_MOND * 3, 0.72),
            arrowprops=dict(arrowstyle='->', color='#e67e22', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#e67e22', alpha=0.9))

# f(a0) = 0.5 annotation
ax.plot(a0, 0.5, 'o', color='#c0392b', markersize=5, zorder=6)
ax.annotate('$f(a_0) = \\frac{1}{2}$',
            xy=(a0, 0.5), fontsize=8.5, color='#c0392b', ha='right',
            xytext=(a0 * 0.15, 0.44),
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#c0392b', alpha=0.9))

# Galaxy edges
ax.axvline(x=1e-10, color='#2980b9', linewidth=1.0, linestyle=':', alpha=0.7, zorder=3)
ax.annotate('Galaxy edges',
            xy=(1e-10, 0.82), fontsize=8, color='#2980b9', ha='right',
            xytext=(2e-11, 0.88),
            arrowprops=dict(arrowstyle='->', color='#2980b9', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#2980b9', alpha=0.9))

# Earth orbit
ax.axvline(x=6e-3, color='#27ae60', linewidth=1.0, linestyle=':', alpha=0.7, zorder=3)
ax.annotate('Earth orbit\n$6 \\times 10^{-3}$',
            xy=(6e-3, 1.06), fontsize=8, color='#27ae60', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#27ae60', alpha=0.9))

# Region labels
ax.text(3e-1, 0.12, 'Standard inertia\n$f \\approx 1$',
        fontsize=10, color='#2c3e50', ha='center', style='italic')
ax.text(3e-10, 0.25, 'Transition\nregion',
        fontsize=9, color='#555555', ha='center', style='italic')
ax.text(1e-12, 0.06, 'Deep MOND\n$f \\approx a/a_0$',
        fontsize=9, color='#8b7355', ha='center', style='italic', alpha=0.8)

# 9% gap annotation
ax.annotate('', xy=(a0_MOND, 0.03), xytext=(a0, 0.03),
            arrowprops=dict(arrowstyle='<->', color='#888888', lw=1.0))
ax.text(np.sqrt(a0 * a0_MOND), 0.08, '9%',
        fontsize=8, color='#888888', ha='center',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='#cccccc', alpha=0.9))

# Axes
ax.set_xscale('log')
ax.set_xlim(3e-13, 3e1)
ax.set_ylim(-0.05, 1.18)
ax.set_xlabel('Acceleration  $a$  (m/s$^2$)', fontsize=12)
ax.set_ylabel('$f(a) = m_i \\, / \\, m_g$', fontsize=14)
ax.set_title('Figure 1.  Entanglement sharing function from horizon thermodynamics\n'
             '$f(a) = a/(a + a_0)$,  $a_0 = cH_0/6$',
             fontsize=11, pad=10)

# Clean up
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.savefig('/mnt/public/Vault/Resources/Physics/Projects/JacobsonQI-Paper/Figure1.png',
            dpi=200, bbox_inches='tight', facecolor='white')
plt.savefig('/mnt/public/Vault/Resources/Physics/Projects/JacobsonQI-Paper/Figure1.pdf',
            bbox_inches='tight', facecolor='white')
print("Saved Figure1.png and Figure1.pdf")
