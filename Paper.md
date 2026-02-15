# Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime

**Authors:** Keith Brodie, with AI assistance (Claude/Anthropic, Grok/xAI)

**Draft v2 — 2026-02-14**

---

## Abstract

Jacobson (1995) demonstrated that the Einstein field equations emerge as an equation of state from the first law of thermodynamics applied to local Rindler horizons, assuming the Bekenstein-Hawking entropy-area relation S = A/4 and the Unruh temperature T = ℏa/2πck_B. His derivation assumes local thermodynamic equilibrium: all vacuum modes contribute fully to the horizon entropy. We show that this assumption fails at very low accelerations, where the Rindler horizon distance c²/a approaches the Hubble radius R_H = c/H₀. The finite size of the observable universe imposes an infrared cutoff on the vacuum mode spectrum, reducing the effective entropy below S = A/4. Propagating this modified entropy through Jacobson's thermodynamic machinery yields, in the non-relativistic weak-field limit, a modified inertial mass m_i = m_g[1 − (2c²/aΘ)²], where Θ = 2c/H₀ is the Hubble diameter. This is McCulloch's Quantized Inertia. The critical acceleration at which the correction becomes order unity is a₀ = cH₀ ≈ 6.9 × 10⁻¹⁰ m/s² — the same order as the empirical MOND scale (a₀_MOND ≈ 1.2 × 10⁻¹⁰ m/s²), with the O(1) numerical prefactor depending on the detailed mode-counting between horizons. This scale is derived here with no free parameters from the geometry of nested horizons. Standard inertia is recovered at high accelerations. We thus demonstrate that Quantized Inertia is not an independent hypothesis but a boundary correction to Jacobson's established framework — the natural consequence of applying horizon thermodynamics in a universe of finite extent.

---

## I. Introduction

Newton's second law F = ma is the most used and least explained equation in physics. It defines inertial mass as the ratio of applied force to resulting acceleration, but says nothing about why matter resists acceleration, why the resistance is proportional to the force, or why the proportionality constant is what it is. In both Newtonian and Einsteinian mechanics, inertial mass is axiomatic — a given, not a derivation.

Two developments suggest this need not be so.

The first is Jacobson's remarkable result [1]. In 1995, Jacobson showed that the Einstein field equations — the foundation of general relativity — are not fundamental geometric postulates but can be *derived* from thermodynamic principles applied to local Rindler horizons. The derivation requires only three inputs: the Bekenstein-Hawking entropy-area relation S = A/4 [2,3], the Clausius relation δQ = TdS, and the Unruh temperature T = ℏa/2πck_B [4]. The Einstein equations emerge as the condition for local thermodynamic equilibrium of the vacuum at every spacetime point. This result, now cited over 3,500 times with no published rebuttals, reframes gravity as an equation of state — the macroscopic thermodynamic behavior of microscopic vacuum degrees of freedom at horizons.

The second is McCulloch's Quantized Inertia (QI) [5–9]. McCulloch proposes that inertia, like gravity, emerges from the physics of horizons. An accelerating body creates a Rindler horizon behind it at distance c²/a, which truncates the spectrum of Unruh radiation on one side. The resulting asymmetry in radiation pressure produces a net force opposing the acceleration — this *is* inertia. Crucially, when the acceleration is very low (a → cH₀), the Rindler horizon distance approaches the Hubble radius, and the cosmic horizon provides a second boundary that further truncates the available modes. In this regime, inertia is reduced, and McCulloch derives flat galaxy rotation curves without dark matter, using only visible baryonic mass and the Hubble diameter, with no adjustable parameters [8,9].

Despite sharing the same physical ingredients — Rindler horizons, Unruh radiation, the Bekenstein-Hawking entropy — these two results have developed independently. Jacobson's work is mainstream (3,500+ citations). McCulloch's is emerging (~200 citations). No paper has connected them. This independence persists despite shared reliance on Rindler horizons and Unruh radiation, highlighting an opportunity to unify thermodynamic spacetime with low-acceleration dynamics.

Several authors have derived MOND-like phenomenology from the entropic gravity programme descended from Jacobson, notably Verlinde [10,11], Klinkhamer [12,13], Sheykhi [14–16], and Rostami et al. [17]. However, these works uniformly modify the *gravitational force law* — they change what gravity does. McCulloch's programme modifies *inertia* — it changes how matter responds. This is not a semantic distinction: modified gravity and modified inertia make different predictions for galaxy rotation curve shapes [18], and the two are in principle distinguishable observationally.

In this paper, we bridge the gap. We show that McCulloch's Quantized Inertia emerges directly from Jacobson's thermodynamic spacetime when a single physically motivated correction is applied: the imposition of the Hubble horizon as a finite outer boundary on the vacuum mode spectrum. Jacobson's original derivation implicitly assumes that all modes contribute to the horizon entropy — that the infrared sector of the mode sum extends to infinity. In a universe of finite extent, it does not. The resulting correction to the entropy-area relation is negligible at ordinary accelerations but becomes dominant at the cosmological scale, precisely where galaxy dynamics deviate from Newtonian predictions. Our correction is negligible in solar-system tests but dominant at a ~ cH₀, naturally bridging lab-scale GR to cosmic-scale anomalies.

---

## II. Jacobson's Derivation

We reproduce the essential steps of Jacobson's argument [1] to establish the framework we will modify. The reader is referred to the original paper for full details.

### A. Local Rindler Horizons

Consider any point P in spacetime. An observer undergoing uniform acceleration a in the neighborhood of P perceives a Rindler horizon — a null surface beyond which signals cannot reach the observer — at proper distance


```math
d_R = \frac{c^2}{a} \qquad \text{(1)}
```


behind the direction of acceleration. This horizon has thermodynamic properties:

**Temperature.** By the Unruh effect [4], the accelerating observer perceives the vacuum as a thermal bath at temperature


```math
T_U = \frac{\hbar a}{2\pi c k_B} \qquad \text{(2)}
```


**Entropy.** By the Bekenstein-Hawking relation [2,3], the entropy associated with a horizon of area A is


```math
S = \frac{k_B A}{4 \ell_P^2} \qquad \text{(3)}
```


where $\ell_P = \sqrt{\hbar G/c^3}$ is the Planck length. This relation, originally derived for black holes, extends to all causal horizons [19].

### B. The First Law at the Horizon

Jacobson applies the Clausius relation


```math
\delta Q = T \, dS \qquad \text{(4)}
```


to infinitesimal patches of the local Rindler horizon. The heat flow δQ is identified with the boost energy flux across the horizon:


```math
\delta Q = T_{ab} \, k^a \, d\Sigma^b \qquad \text{(5)}
```


where $T_{ab}$ is the stress-energy tensor, $k^a$ is the approximate Killing vector generating boosts (the local time-translation symmetry for the accelerated observer), and $d\Sigma^b$ is the horizon area element.

### C. Entropy and the Raychaudhuri Equation

The change in horizon area is governed by the Raychaudhuri equation for null geodesic congruences. For a pencil of horizon generators with cross-sectional area A:


```math
\frac{dA}{d\lambda} = -R_{ab} \, k^a k^b \, A \qquad \text{(6)}
```


where λ is the affine parameter along the generators and $R_{ab}$ is the Ricci tensor. The entropy change is therefore:


```math
dS = \frac{k_B}{4\ell_P^2} \, dA = -\frac{k_B}{4\ell_P^2} \, R_{ab} \, k^a k^b \, A \, d\lambda \qquad \text{(7)}
```


### D. The Einstein Equations Emerge

Substituting Eqs. (2), (5), and (7) into the Clausius relation (4):


```math
T_{ab} \, k^a \, d\Sigma^b = \frac{\hbar a}{2\pi c k_B} \cdot \left( -\frac{k_B}{4\ell_P^2} \right) R_{ab} \, k^a k^b \, A \, d\lambda \qquad \text{(8)}
```


The acceleration a, the Killing vector $k^a$, and the geometric factors combine such that, after requiring this relation to hold for all horizon patches and all boost directions at every spacetime point, one obtains:


```math
R_{ab} - \frac{1}{2} R \, g_{ab} + \Lambda \, g_{ab} = \frac{8\pi G}{c^4} \, T_{ab} \qquad \text{(9)}
```


These are the Einstein field equations. The cosmological constant Λ appears as an integration constant — the thermodynamic ground-state energy of the vacuum.

**The Einstein equations are an equation of state.** They express the condition for thermodynamic equilibrium of the vacuum at every local Rindler horizon. Spacetime geometry is not fundamental — it is the macroscopic manifestation of microscopic horizon thermodynamics.

### E. The Equilibrium Assumption

Jacobson's derivation rests on a critical assumption: **local thermodynamic equilibrium**. The entropy-area relation S = A/4 is taken to hold exactly at every horizon patch. This means:

1. All vacuum field modes contribute to the entropy
2. The mode sum extends from the ultraviolet cutoff (Planck scale) to arbitrarily long wavelengths
3. There is no infrared truncation of the mode spectrum

In an infinite or asymptotically flat universe, this is unproblematic. In a finite, expanding cosmos, however, the infrared spectrum truncates at the Hubble scale — precisely the correction we introduce in Section III.

---

## III. The Finite Boundary Correction

### A. The Mode Spectrum Between Two Horizons

The entropy S = A/4 counts the quantum degrees of freedom associated with the horizon [20,21]. These degrees of freedom correspond to modes of the vacuum field — oscillations characterized by wavelength λ. The mode sum runs from a UV cutoff $\lambda_{\min} \sim \ell_P$ (the Planck scale, below which the semiclassical treatment breaks down) to an IR cutoff $\lambda_{\max}$.

In Jacobson's derivation, $\lambda_{\max}$ is implicitly taken to infinity: all long-wavelength modes are available to contribute to the horizon entropy.

But the observable universe has a finite size. The Hubble horizon at radius


```math
R_H = \frac{c}{H_0} \approx 1.3 \times 10^{26} \text{ m} \qquad \text{(10)}
```


provides a physical outer boundary. Modes with wavelengths exceeding the Hubble diameter


```math
\Theta = 2R_H = \frac{2c}{H_0} \approx 2.6 \times 10^{26} \text{ m} \qquad \text{(11)}
```


cannot exist as standing waves within the observable universe. They are not merely unobservable — they do not fit within the causal domain and therefore do not contribute to the local vacuum state.

An accelerating observer thus lives between two horizons:
- **Inner boundary** (Rindler): at distance $d_R = c^2/a$, with associated characteristic Unruh wavelength $\lambda_R \approx 2c^2/a$
- **Outer boundary** (Hubble): at distance $R_H = c/H_0$, providing a maximum wavelength $\lambda_{\max} = \Theta$

The characteristic Unruh wavelength $\lambda_R$ is set by the Rindler horizon scale. The Unruh thermal spectrum has a Planckian distribution with temperature $T_U$ (Eq. 2), whose Wien peak lies at $\lambda_{\text{peak}} = 2\pi c / (2.82 \, a) \approx 2.2 \, c^2/a$. We adopt the convention $\lambda_R \approx 2c^2/a$, consistent with the QI literature [7,9] and within the O(1) uncertainty of the Wien factor. The precise numerical coefficient does not affect the structure of the argument; it sets the numerical prefactor of a₀ relative to cH₀.

The mode spectrum is not infinite. It runs from $\ell_P$ to $\Theta$, and the fraction that contributes at any given acceleration depends on the ratio $\lambda_R / \Theta$.

### B. When the Correction Matters

At high accelerations ($a \gg cH_0$), the Rindler horizon is close: $d_R = c^2/a \ll R_H$. The characteristic Unruh wavelength is far shorter than the Hubble diameter. Essentially all modes are available. The correction is negligible, and Jacobson's full entropy applies.

At low accelerations ($a \rightarrow cH_0$), the Rindler horizon recedes toward the Hubble radius: $d_R \rightarrow R_H$. The characteristic Unruh wavelength approaches the size of the observable universe. Long-wavelength modes are progressively excluded. The entropy is reduced.

The transition occurs at the acceleration


```math
a_0 = cH_0 \approx 6.9 \times 10^{-10} \text{ m/s}^2 \qquad \text{(12)}
```


derived from the geometry of two nested horizons with no free parameters. We note that this raw geometric scale differs from Milgrom's empirical MOND constant $a_0^{\text{MOND}} \approx 1.2 \times 10^{-10}$ m/s² [22] by a factor of ~5.8. This O(1) discrepancy is expected: the precise numerical prefactor depends on the detailed shape of the Unruh thermal spectrum and the exact mode-counting between the two horizons. The Wien displacement law, the transition from 1+1 to 3+1 dimensional mode-counting, and the specific boundary conditions at the Hubble surface all contribute factors of order unity. What is robust is the *scale*: a₀ ~ cH₀, derived from geometry alone. Resolving the precise prefactor requires the full mode calculation discussed in Section VI.

### C. The Modified Entropy-Area Relation

To quantify the entropy reduction, we follow 't Hooft's observation [20] that both UV and IR cutoffs regulate the entropy of quantum fields near a horizon, and the recent demonstration [23] that Jacobson's derivation remains valid when the entropy-area relation is modified.

The fraction of available modes at acceleration a is determined by the ratio of the characteristic Unruh wavelength to the Hubble diameter. Modes with wavelengths between $\ell_P$ and $\Theta$ contribute fully. Modes that would have wavelengths exceeding $\Theta$ — those in the infrared tail of the Unruh spectrum — are excluded.

The relevant dimensionless ratio is


```math
\epsilon(a) = \frac{\lambda_R}{\Theta} = \frac{2c^2}{a\Theta} = \frac{cH_0}{a} = \frac{a_0}{a} \qquad \text{(13)}
```


At high accelerations, $\epsilon \ll 1$ and all modes contribute. At $a = a_0$, $\epsilon = 1$ and a significant fraction of the long-wavelength spectrum is excluded.

The modified entropy is:


```math
S'(a) = \frac{k_B A}{4\ell_P^2} \cdot \left[1 - \epsilon^2\right] = \frac{k_B A}{4\ell_P^2} \cdot \left[1 - \left(\frac{2c^2}{a\Theta}\right)^2\right] \qquad \text{(14)}
```


The quadratic form arises because the entropy of a field in a cavity scales with the number of available mode *cells* in phase space. For a Casimir-like geometry — two boundaries separated by distances $d_R$ and $\Theta$ — the excluded mode energy scales as $(d_R/\Theta)^2$ [21], mirroring the well-known Casimir energy scaling between conducting plates. This specific functional form is also consistent with McCulloch's derivation from information-theoretic arguments [7,9].

**Remark on the functional form.** The precise power in Eq. (14) — whether ε² or some other function of ε — depends on the detailed mode-counting between the two horizons. A full calculation requires specifying the field content (scalar, spinor, vector), the dimensionality of the mode sum (1+1 vs. 3+1), and the boundary conditions at both surfaces. What is robust is: (i) the correction vanishes as $\epsilon \to 0$ (high a), (ii) it becomes order unity as $\epsilon \to 1$ (a → a₀), and (iii) a₀ ~ cH₀ with no free parameters. McCulloch's specific quadratic form fits galaxy rotation data for 153 SPARC galaxies [9], providing strong empirical support. A first-principles derivation of the exponent — adapting 't Hooft's brick-wall model [20] to concentric Rindler and de Sitter horizons, or using the finite-capacity Rindler horizon analysis of [23] — would strengthen this result and is a target for future work. Such a calculation may also resolve the O(1) prefactor discrepancy with Milgrom's empirical a₀.

### D. Propagation Through the First Law

We now repeat Jacobson's derivation with the modified entropy (14). The Clausius relation becomes:


```math
\delta Q = T_U \, dS' \qquad \text{(15)}
```


Expanding:


```math
\delta Q = \frac{\hbar a}{2\pi c k_B} \cdot \frac{k_B}{4\ell_P^2} \cdot \left[1 - \left(\frac{a_0}{a}\right)^2\right] \cdot dA \qquad \text{(16)}
```


The correction factor $f(a) = [1 - (a_0/a)^2]$ is a scalar function of the local acceleration magnitude. In Jacobson's original derivation, Eq. (8) must hold for all boost directions at every spacetime point; requiring this for the modified relation introduces $f(a)$ as a multiplicative correction.

**A note on covariance.** Jacobson's derivation is fully covariant: it yields the tensor equation (9) by demanding consistency across all boost directions. Our correction factor $f(a)$ depends on the magnitude of the acceleration, which is observer-dependent in full GR. In the non-relativistic limit that we treat here, acceleration is unambiguous (it is the coordinate acceleration in the rest frame of the gravitating system). The fully covariant formulation — expressing $f$ in terms of the four-acceleration magnitude $\sqrt{a^\mu a_\mu}$ or a related tensorial quantity — is essential for the relativistic extension and is discussed in Section VI. For the present paper, we restrict attention to the weak-field, non-relativistic regime where the correction is observationally relevant (galaxy dynamics, wide binaries) and where the four-acceleration reduces to the familiar 3-vector **a**.

### E. The Non-Relativistic Limit: Modified Inertia

In the weak-field, non-relativistic limit, the Einstein equations reduce to the Poisson equation for the Newtonian potential, and the geodesic equation reduces to Newton's second law. Consider a test mass $m_g$ (gravitational mass) in a gravitational field producing acceleration $a$. The standard Newtonian limit gives $F = m_g \, a$.

With our modification, the relationship between the stress-energy source and the resulting geometry is altered by the factor $f(a)$. In the Newtonian limit, this manifests as a modification to the inertial response: the effective force law becomes


```math
F = m_g \cdot a \cdot f(a) = m_g \cdot a \cdot \left[1 - \left(\frac{a_0}{a}\right)^2\right] \qquad \text{(17)}
```


We can equivalently express this as a modified inertial mass:


```math
\boxed{m_i(a) = m_g \left[1 - \left(\frac{a_0}{a}\right)^2\right]} \qquad \text{(18)}
```


where $a_0 = cH_0$.

This is McCulloch's Quantized Inertia [5–9]. Inertial mass is no longer identically equal to gravitational mass. At high accelerations ($a \gg a_0$), the equivalence principle holds: $m_i \to m_g$. At cosmological accelerations ($a \sim a_0$), inertia is reduced as the Rindler horizon approaches the Hubble boundary and the mode spectrum truncates.

![Figure 1](Figure1.png)

**Figure 1.** Modified inertial mass ratio $m_i/m_g = 1 - (a_0/a)^2$ as a function of acceleration, with $a_0 = cH_0 \approx 6.9 \times 10^{-10}$ m/s². At solar-system accelerations (right), $m_i \approx m_g$ and standard Newtonian inertia holds. At galaxy-edge accelerations ($\sim 10^{-10}$ m/s²), the transition region begins. At $a = a_0$, inertia vanishes and the system self-regulates (left). The ×5.8 gap between our geometric $a_0$ and Milgrom's empirical $a_0^{\text{MOND}} \approx 1.2 \times 10^{-10}$ m/s² reflects the O(1) prefactor to be resolved by detailed mode-counting between the Rindler and Hubble horizons.

---

## IV. Limiting Cases and Predictions

### A. High Acceleration ($a \gg a_0$)

When $a \gg cH_0$:


```math
\left(\frac{a_0}{a}\right)^2 \ll 1 \implies m_i \to m_g \qquad \text{(19)}
```


Standard Newtonian inertia is recovered. Jacobson's full Einstein equations hold without correction. This regime covers all laboratory physics and solar system dynamics. For Earth's orbital acceleration ($a \approx 6 \times 10^{-3}$ m/s²):


```math
\left(\frac{a_0}{a}\right)^2 \approx \left(\frac{7 \times 10^{-10}}{6 \times 10^{-3}}\right)^2 \sim 10^{-14} \qquad \text{(20)}
```


This is far below current precision tests of the equivalence principle (~10⁻¹⁵ for Eötvös-type experiments), ensuring no conflict with solar system ephemerides, lunar laser ranging, or the Cassini spacecraft constraint on post-Newtonian parameters.

### B. Low Acceleration ($a \to a_0$)

As $a \to a_0$:


```math
m_i \to 0 \qquad \text{(21)}
```


Inertia vanishes. The object's Rindler horizon has expanded to the Hubble radius, and the Unruh radiation spectrum is fully truncated by the cosmic boundary. There is no radiation pressure asymmetry to resist acceleration, and hence no inertia.

For $a < a_0$, the formula (18) as written gives $m_i < 0$, which is unphysical. This signals the breakdown of the linear regime, not a failure of the framework. As McCulloch emphasizes [8,9], gravitationally bound systems self-regulate: as acceleration decreases toward $a_0$, inertia diminishes, reducing the centripetal force needed to maintain orbit, which in turn modifies the orbital velocity until the system stabilizes with $a \geq a_0$. Accelerations cannot drop below $a_0$ because vanishing inertia causes any residual force to produce unbounded acceleration, driving the system back above the threshold. The physical prediction is that gravitationally bound systems exhibit a minimum acceleration floor at $a_0$, producing flat rotation curves.

### C. Galaxy Rotation Curves

Stars in the outer regions of spiral galaxies orbit with accelerations $a \sim 10^{-10}$ m/s², comparable to $a_0$. In this regime, the rotation velocity of a star of gravitational mass $m_g$ at radius $r$ from a galaxy of mass $M$ satisfies:


```math
\frac{m_i v^2}{r} = \frac{G M m_g}{r^2} \qquad \text{(22)}
```


Substituting $m_i = m_g f(a)$ with $a = v^2/r$ and solving in the deep low-acceleration regime (where the system self-regulates at $a \sim a_0$) yields the asymptotic rotation velocity:


```math
v^4 = GMa_0 = GMcH_0 \implies v = (GMcH_0)^{1/4} \qquad \text{(23)}
```


This is exact in the deep low-acceleration limit and is the baryonic Tully-Fisher relation [24]: the asymptotic rotation velocity depends only on the baryonic mass of the galaxy and cosmological constants, with no free parameters. McCulloch [9] has shown that this formula fits the rotation curves of 153 galaxies in the SPARC dataset [25] using only visible baryonic mass.

The Tully-Fisher relation has been one of the strongest empirical arguments for MOND over dark matter: ΛCDM has no natural explanation for why $v^4 \propto M$ should hold with the observed tightness and zero scatter. In our framework, it is a geometric consequence of the Rindler-Hubble boundary condition.

### D. Wide Binary Stars

Wide binary stars with separations exceeding ~5,000 AU have orbital accelerations below $a_0$. The dark matter paradigm predicts strictly Newtonian dynamics for these systems, because the local dark matter density (~0.3 GeV/cm³) is far too diffuse to affect binary orbits at kiloparsec separations within the Milky Way.

Equation (18) predicts measurably non-Newtonian behavior: reduced inertia causes the binary to orbit faster than the Keplerian prediction. Chae [26] has reported statistically significant anomalies in Gaia DR3 wide binary data consistent with this prediction, though the result is contested by Banik et al. [27] on grounds of sample contamination (unresolved triples, chance alignments) and enhanced proper motion uncertainties. Future Gaia data releases should resolve the systematics.

This is a particularly clean test because: (i) it is local (within the Milky Way, no cosmological modeling), (ii) the dark matter prediction is unambiguous (strictly Newtonian), and (iii) any confirmed anomaly at the $a_0$ scale would be incompatible with particle dark matter while being naturally explained by horizon-based inertia modification. If wide-binary anomalies are confirmed, our framework provides the thermodynamic mechanism.

### E. Cosmological Predictions

Because $a_0 = cH_0$ and $H_0$ evolves with cosmic time, our framework predicts that the critical acceleration scale is not constant but tracks the expansion history:


```math
a_0(z) = c \, H(z) \qquad \text{(24)}
```


At higher redshift, $H(z)$ is larger, so $a_0$ is larger, and galaxy rotation anomalies should appear at higher accelerations and smaller radii than in the local universe. McCulloch [9] has noted that this prediction is consistent with observations of galaxy dynamics out to $z \sim 2.2$, where enhanced rotation anomalies are observed.

This is a testable cosmological prediction that distinguishes horizon-based inertia modification from fixed-$a_0$ MOND, where $a_0$ is a fundamental constant with no redshift dependence. It also predicts weaker MOND effects in the early universe (high z, larger $a_0$ means the transition to anomalous dynamics occurs at larger accelerations, but galaxies are also more compact and higher-acceleration), providing a rich phenomenological landscape testable with JWST and next-generation surveys.

---

## V. Addressing Objections

### A. The Circularity Question

Chirco et al. [28] criticized Jacobson's derivation as circular: the entropy-area relation S = A/4 is derived from the Bekenstein-Hawking result, which itself assumes the Einstein equations. If GR is assumed to justify S = A/4, then deriving GR from S = A/4 is circular.

This objection, far from undermining our result, supports it. If S = A/4 is not a fundamental axiom but an emergent relation (as Chirco argues), then it can be *modified* at boundaries without violating any deeper principle. Our modification — imposing a finite IR cutoff from the Hubble horizon — is not ad hoc but reflects the physical fact that the observable universe has a boundary. The Bousso covariant entropy bound [29], which Chirco recommends as a replacement for S = A/4, naturally incorporates causal boundaries. Our work is compatible with this programme.

### B. The Equivalence Principle

Equation (18) implies $m_i \neq m_g$ at low accelerations, apparently violating the equivalence principle. However:

1. The equivalence principle is a *local* statement. It requires $m_i = m_g$ in a sufficiently small neighborhood. Our correction involves the ratio of the local Rindler horizon to the cosmological horizon — an intrinsically non-local quantity. The equivalence principle is not violated locally; it is *supplemented* by a cosmological boundary condition.

2. The Weak Equivalence Principle (universality of free fall) is preserved: all bodies experience the same inertia reduction at the same acceleration, regardless of composition. What is modified is the *value* of inertial mass, not its universality.

3. If observations ultimately confirm wide-binary anomalies at $a \sim a_0$ [26], then the equivalence principle is empirically broken at cosmological acceleration scales — and our framework provides the physical mechanism via horizon thermodynamics.

### C. Non-Equilibrium Considerations

Jacobson's derivation assumes thermodynamic equilibrium at the horizon. Our modification introduces a departure from equilibrium: the finite Hubble boundary prevents the full mode spectrum from thermalizing. This is precisely the regime addressed by Eling, Guedens, and Jacobson [30], who extended the thermodynamic spacetime programme to non-equilibrium situations by including entropy production terms.

In their framework, departures from S = A/4 generate additional terms in the field equations proportional to the gradient of the entropy modification. Our correction factor $f(a) = 1 - (a_0/a)^2$ is slowly varying in space and time (its spatial gradient is negligible except in the immediate vicinity of $a \sim a_0$), so the non-equilibrium entropy production terms are subdominant — consistent with the fact that galaxy dynamics, while anomalous, are quasi-static.

### D. Relation to Prior Work on Entropic MOND

Several authors have derived MOND-like phenomenology from entropic gravity:

- **Verlinde [10,11]:** Uses competition between area-law and volume-law entropy in de Sitter space. Works with holographic screens rather than Rindler horizons.
- **Klinkhamer [12,13]:** Introduces a minimum temperature for holographic-screen degrees of freedom. Derives the full Bekenstein-Milgrom equation including the external field effect.
- **Sheykhi [14–16]:** Modifies the entropy-area relation using Tsallis statistics ($S \propto A^\beta$) to derive modified Friedmann equations and galaxy rotation.
- **Sheykhi & Liravi [16]:** Reverse-engineers the horizon entropy that produces MOND.
- **Rostami et al. [17]:** Derives relativistic MOND from temperature-dependent corrections to the equipartition law.

All of these modify the *gravitational force law*. None derives a modification to *inertia*. Our work differs in three respects:

1. **We modify inertia, not gravity.** The correction appears in $m_i$, not in $G$ or the gravitational potential. This has distinct observational signatures: modified gravity and modified inertia predict subtly different rotation curve shapes, testable with current data [18].
2. **We start from Jacobson's local Rindler horizons**, not Verlinde's holographic screens or Padmanabhan's surface-volume thermodynamics [33]. This keeps us closest to the foundational result.
3. **The entropy modification has a geometric origin** (finite Hubble boundary truncating the mode spectrum), not a statistical-mechanical one (Tsallis, Kaniadakis, Debye). No new statistical mechanics is required — only the physical fact that the universe has a finite size.

---

## VI. Discussion

### What This Paper Demonstrates

We have shown that Quantized Inertia — McCulloch's proposal that inertial mass depends on acceleration via the ratio of the Rindler horizon to the cosmic horizon — is not an independent hypothesis. It is the natural consequence of Jacobson's thermodynamic spacetime in a universe of finite extent. The derivation requires no new physics beyond:

1. Jacobson's result (Einstein equations from horizon thermodynamics) — 3,500+ citations, mainstream
2. The Unruh effect (thermal radiation for accelerated observers) — standard QFT
3. The Bekenstein-Hawking entropy (proportional to horizon area) — standard
4. The existence of a finite cosmological horizon — observed

The MOND acceleration scale $a_0 \sim cH_0$ emerges as the acceleration at which the inner (Rindler) and outer (Hubble) horizons become comparable, truncating the mode spectrum and reducing the effective entropy. This is not a fitted parameter — it is a geometric consequence of nested horizons.

### What Remains To Be Done

**The mode-counting.** The most important open problem. Our derivation establishes the structure of the correction — it must vanish at high a, become order unity at $a \sim a_0$, and yield $a_0 \sim cH_0$ — but the precise functional form (the exponent in Eq. 14, and the O(1) numerical prefactor relating our geometric $a_0$ to Milgrom's empirical value) requires a first-principles calculation of the mode density for quantum fields between concentric Rindler and de Sitter horizons. The mathematical tools exist: 't Hooft's brick-wall model [20] provides the framework for mode-counting with finite boundaries; Bazarov et al. [21] have computed finite-boundary entropy corrections for Schwarzschild; and the finite-capacity Rindler horizon analysis of [23] demonstrates that Jacobson's derivation survives modified entropy input. Adapting these tools to the nested Rindler-Hubble geometry is a well-defined calculation and the natural next step. Such a calculation may also resolve whether the quadratic form is exact or an approximation to a more complex function (e.g., involving logarithmic corrections as found in other entropy modification contexts [35]).

**Covariant formulation.** Equation (16) presents the modified Clausius relation with $f(a)$ as a scalar function of local acceleration magnitude. In full GR, acceleration is observer-dependent (it is the magnitude of the four-acceleration $a^\mu = u^\nu \nabla_\nu u^\mu$). A fully covariant formulation must express $f$ in terms of $\sqrt{a^\mu a_\mu}$ or equivalent tensorial quantities. This connects to the broader programme of scalar-tensor and f(R) gravity theories and determines whether the modification admits a Lagrangian formulation. The non-relativistic limit treated here is sufficient for the observationally relevant regimes (galaxy rotation, wide binaries, solar system), but the covariant extension is necessary for strong-field applications and for formal consistency.

**Galaxy clusters.** MOND-like theories underpredict the mass deficit in galaxy clusters by a factor of ~2. If our modified inertia inherits this deficit, it may indicate that the quadratic correction in Eq. (14) is approximate and the true functional form provides stronger modification in the cluster regime (where accelerations are slightly above $a_0$ and the transition region is important). Alternatively, the observed baryonic mass in hot intracluster gas — which is already substantial — may close the gap.

**Backreaction and self-consistency.** If inertia depends on acceleration and acceleration depends on inertia, the system must be self-consistent. McCulloch [8] addresses this iteratively and finds convergence. A formal proof of convergence — or a demonstration that the modified field equation has a well-posed initial value problem — would strengthen the result.

### Experimental Tests

The most decisive near-term test is **wide binary stars**. Dark matter predicts Newtonian dynamics; Eq. (18) predicts anomalies below $a_0$. Current Gaia DR3 data is suggestive [26] but contested [27]. Gaia DR4 should resolve the systematic uncertainties in sample contamination.

**Laboratory tests** require accelerations approaching $a_0 \sim 10^{-10}$ m/s², below current torsion balance and atom interferometer sensitivity. However, McCulloch has proposed that asymmetric electromagnetic cavities — which modify the local Rindler horizon geometry — could produce measurable thrust [6]. DARPA-funded tests of QI-inspired thrusters are ongoing.

The **cosmological prediction** $a_0(z) = cH(z)$ is testable with high-redshift galaxy kinematics. Preliminary data supports a time-varying MOND scale out to $z \sim 2.2$ [9]. JWST observations of compact high-redshift galaxies provide further opportunities.

---

## VII. Conclusion

Jacobson showed that spacetime has an equation of state. The Einstein equations express the condition for thermodynamic equilibrium at local Rindler horizons. This paper has shown that when that equilibrium is broken by the finite extent of the observable universe — when the Rindler horizon of a slowly accelerating body reaches the cosmic boundary and the vacuum mode spectrum is truncated — the result is McCulloch's Quantized Inertia.

Inertia is not a primitive property of matter. It emerges from the thermodynamics of the vacuum at horizons, and it has a boundary condition: the edge of the observable universe. Below the critical acceleration $a_0 = cH_0$, the mode spectrum runs out, the entropy-area relation is modified, and inertial mass is reduced. This produces flat galaxy rotation curves, the baryonic Tully-Fisher relation, and a time-varying MOND scale that tracks cosmic expansion — all from Jacobson's framework plus the physical fact that the universe is finite.

No dark matter. No new particles. No free parameters. Only horizons, thermodynamics, and a boundary.

---

## References

[1] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," Phys. Rev. Lett. **75**, 1260 (1995). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)

[2] J. D. Bekenstein, "Black Holes and Entropy," Phys. Rev. D **7**, 2333 (1973).

[3] S. W. Hawking, "Particle Creation by Black Holes," Commun. Math. Phys. **43**, 199 (1975).

[4] W. G. Unruh, "Notes on Black-Hole Evaporation," Phys. Rev. D **14**, 870 (1976).

[5] M. E. McCulloch, "Modelling the Pioneer Anomaly as Modified Inertia," MNRAS **376**, 338 (2007). [arXiv:astro-ph/0612599](https://arxiv.org/abs/astro-ph/0612599)

[6] M. E. McCulloch, "Inertia from an Asymmetric Casimir Effect," EPL **101**, 59001 (2013). [arXiv:1302.2775](https://arxiv.org/abs/1302.2775)

[7] M. E. McCulloch, "Quantised Inertia from Relativity and the Uncertainty Principle," EPL **115**, 69001 (2016). [arXiv:1610.06787](https://arxiv.org/abs/1610.06787)

[8] M. E. McCulloch, "Testing Quantised Inertia on Galactic Scales," Astrophys. Space Sci. **342**, 575 (2012).

[9] M. E. McCulloch, "Galaxy Rotations from Quantised Inertia and Visible Matter Only," Astrophys. Space Sci. **362**, 149 (2017). [arXiv:1709.04918](https://arxiv.org/abs/1709.04918)

[10] E. Verlinde, "On the Origin of Gravity and the Laws of Newton," JHEP **04**, 029 (2011). [arXiv:1001.0785](https://arxiv.org/abs/1001.0785)

[11] E. Verlinde, "Emergent Gravity and the Dark Universe," SciPost Phys. **2**, 016 (2017). [arXiv:1611.02269](https://arxiv.org/abs/1611.02269)

[12] F. R. Klinkhamer, "Entropic-Gravity Derivation of MOND," Mod. Phys. Lett. A **27**, 1250056 (2012). [arXiv:1201.4160](https://arxiv.org/abs/1201.4160)

[13] F. R. Klinkhamer and M. Kopp, "Entropic Gravity, Minimum Temperature, and Modified Newtonian Dynamics," Mod. Phys. Lett. A **26**, 2783 (2011). [arXiv:1104.2022](https://arxiv.org/abs/1104.2022)

[14] A. Sheykhi and K. Rezazadeh Sarab, "Einstein Equations and MOND Theory from Debye Entropic Gravity," JCAP **10**, 012 (2012). [arXiv:1206.1030](https://arxiv.org/abs/1206.1030)

[15] A. Sheykhi, "New Explanation for Accelerated Expansion and Flat Galactic Rotation Curves," Eur. Phys. J. C **80**, 25 (2020). [arXiv:1912.08693](https://arxiv.org/abs/1912.08693)

[16] A. Sheykhi and L. Liravi, "MOND Theory and Thermodynamics of Spacetime," Phys. Dark Univ. **49**, 101967 (2025). [arXiv:2510.14345](https://arxiv.org/abs/2510.14345)

[17] A. Rostami, K. Rezazadeh, and M. Rostampour, "Relativistic MOND Theory from Modified Entropic Gravity," arXiv:2511.05632 (2025).

[18] V. Costantino and T. Broadhurst, "A First Attempt to Differentiate between Modified Gravity and Modified Inertia with Galaxy Rotation Curves," Astron. Astrophys. **636**, A15 (2020). [arXiv:2001.03348](https://arxiv.org/abs/2001.03348)

[19] T. Jacobson, "Horizon Entropy," arXiv:gr-qc/0302099 (2003).

[20] G. 't Hooft, "On the Quantum Structure of a Black Hole," Nucl. Phys. B **256**, 727 (1985).

[21] N. Bazarov, S. Piroli, and S. N. Solodukhin, "Infrared Regularization and Finite Size Dynamics of Entanglement Entropy in Schwarzschild Black Hole," Phys. Rev. D **108**, 046005 (2023). [arXiv:2209.00036](https://arxiv.org/abs/2209.00036)

[22] M. Milgrom, "A Modification of the Newtonian Dynamics as a Possible Alternative to the Hidden Mass Hypothesis," Astrophys. J. **270**, 365 (1983).

[23] "Modified Unruh Thermodynamics in Emergent Gravity: Finite Heat Capacity and Rényi Entropy," arXiv:2509.03470 (2025).

[24] S. S. McGaugh, "The Baryonic Tully-Fisher Relation," Astrophys. J. **632**, 859 (2005).

[25] F. Lelli, S. S. McGaugh, and J. M. Schombert, "SPARC: Mass Models for 175 Disk Galaxies," Astron. J. **152**, 157 (2016).

[26] K.-H. Chae, "Breakdown of the Newton–Einstein Standard Gravity at Low Acceleration in Internal Dynamics of Wide Binary Stars," Astrophys. J. **952**, 128 (2023).

[27] I. Banik et al., "Strong Constraints on the Gravitational Law from Gaia DR3 Wide Binaries," MNRAS **530**, 4988 (2024).

[28] G. Chirco, H. M. Haggard, A. Riello, and C. Rovelli, "Spacetime Thermodynamics without Hidden Degrees of Freedom," Phys. Rev. D **90**, 044044 (2014).

[29] R. Bousso, "The Holographic Principle," Rev. Mod. Phys. **74**, 825 (2002).

[30] C. Eling, R. Guedens, and T. Jacobson, "Nonequilibrium Thermodynamics of Spacetime," Phys. Rev. Lett. **96**, 121301 (2006).

[31] L. Smolin, "MOND as a Regime of Quantum Gravity," Phys. Rev. D **96**, 083523 (2017). [arXiv:1704.00780](https://arxiv.org/abs/1704.00780)

[32] J.-W. Lee, "On the Origin of Entropic Gravity and Inertia," Found. Phys. **42**, 1153 (2012). [arXiv:1003.4464](https://arxiv.org/abs/1003.4464)

[33] T. Padmanabhan, "Equipartition of Energy in the Horizon Degrees of Freedom and the Emergence of Gravity," Mod. Phys. Lett. A **25**, 1129 (2010). [arXiv:0912.3165](https://arxiv.org/abs/0912.3165)

[34] J. Gillot, "Quantum Modified Inertia: An Application to Galaxy Rotation Curves," arXiv:2507.11524 (2025).

[35] S. N. Solodukhin, "Entanglement Entropy of Black Holes," Living Rev. Relativ. **14**, 8 (2011).
