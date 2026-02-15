"""
Figure 1: Modified inertial mass ratio m_i/m_g as a function of acceleration.

Shows the transition from standard inertia (m_i = m_g) at high accelerations
to vanishing inertia at the critical acceleration a_0 = cH_0.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3.0e8          # m/s
H0 = 2.27e-18      # 1/s  (70 km/s/Mpc)
a0 = c * H0        # ~6.9e-10 m/s^2
a0_MOND = 1.2e-10  # Milgrom's empirical value

# Acceleration range
a = np.logspace(-11, 1, 2000)

# Modified inertial mass ratio: m_i/m_g = 1 - (a0/a)^2
# Clamp to zero below a0 (negative is unphysical — self-regulation regime)
ratio = 1.0 - (a0 / a)**2
ratio_clipped = np.clip(ratio, 0, None)

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 5.5))

# Main curve
ax.plot(a, ratio_clipped, color='#1a1a2e', linewidth=2.5, zorder=5)

# Shade regions
ax.fill_between(a, 0, ratio_clipped, where=(a < a0),
                color='#e8d5b7', alpha=0.4, zorder=2)
ax.fill_between(a, 0, ratio_clipped, where=(a >= a0),
                color='#c5d5e8', alpha=0.25, zorder=2)

# Horizontal reference
ax.axhline(y=1.0, color='grey', linewidth=0.5, linestyle='--', zorder=1)

# --- Vertical markers with staggered labels ---

# a0 = cH0 (our prediction)
ax.axvline(x=a0, color='#c0392b', linewidth=1.4, linestyle=':', alpha=0.8, zorder=3)
ax.annotate('$a_0 = cH_0$\n$6.9 \\times 10^{-10}$',
            xy=(a0, 1.06), fontsize=8.5, color='#c0392b', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#c0392b', alpha=0.9))

# a0_MOND (Milgrom's empirical)
ax.axvline(x=a0_MOND, color='#e67e22', linewidth=1.2, linestyle=':', alpha=0.8, zorder=3)
ax.annotate('$a_0^{\\mathrm{MOND}}$\n$1.2 \\times 10^{-10}$',
            xy=(a0_MOND, 0.42), fontsize=8, color='#e67e22', ha='right',
            xytext=(a0_MOND * 0.4, 0.42),
            arrowprops=dict(arrowstyle='->', color='#e67e22', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#e67e22', alpha=0.9))

# Galaxy edges
ax.axvline(x=1e-10, color='#2980b9', linewidth=1.0, linestyle=':', alpha=0.7, zorder=3)
ax.annotate('Galaxy edges',
            xy=(1e-10, 0.72), fontsize=8, color='#2980b9', ha='left',
            xytext=(3e-10, 0.82),
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
ax.text(3e-1, 0.12, 'Standard inertia\n$m_i \\approx m_g$',
        fontsize=10, color='#2c3e50', ha='center', style='italic')
ax.text(5e-9, 0.50, 'Transition\nregion',
        fontsize=9, color='#555555', ha='center', style='italic')
ax.text(2e-11, 0.12, 'Self-\nregulation',
        fontsize=9, color='#8b7355', ha='center', style='italic', alpha=0.8)

# Brace / annotation for the ~5.8x gap
ax.annotate('', xy=(a0_MOND, 0.03), xytext=(a0, 0.03),
            arrowprops=dict(arrowstyle='<->', color='#888888', lw=1.0))
ax.text(np.sqrt(a0 * a0_MOND), 0.08, '$\\times 5.8$',
        fontsize=8, color='#888888', ha='center',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='#cccccc', alpha=0.9))

# Axes
ax.set_xscale('log')
ax.set_xlim(5e-12, 3e1)
ax.set_ylim(-0.05, 1.18)
ax.set_xlabel('Acceleration  $a$  (m/s$^2$)', fontsize=12)
ax.set_ylabel('$m_i \\, / \\, m_g$', fontsize=14)
ax.set_title('Figure 1.  Modified inertial mass from horizon thermodynamics\n'
             '$m_i/m_g = 1 - (a_0/a)^2$,  $a_0 = cH_0$',
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
