# Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime

**Authors:** Keith Brodie, with AI assistance (Claude/Anthropic, Grok/xAI)

**Draft v4 — 2026-02-19**

---

## Abstract

Jacobson (1995) demonstrated that the Einstein field equations emerge as an equation of state from the first law of thermodynamics applied to local Rindler horizons, assuming the Bekenstein-Hawking entropy-area relation S = A/4 and the Unruh temperature T = ℏa/2πck_B. His derivation assumes local thermodynamic equilibrium: every vacuum mode's entanglement is fully available to the local Rindler horizon. We show that this assumption fails at very low accelerations, where the Rindler horizon distance c²/a approaches the Hubble radius R_H = c/H₀. Both horizons are entangled with the same vacuum modes, and entanglement monogamy forces the finite budget to be partitioned between them. The effective entropy available to the local Rindler horizon is reduced below S = A/4. Propagating this modified entropy through Jacobson's thermodynamic machinery yields, in the non-relativistic weak-field limit, a sharing function f(a) = a/(a + cH₀/6) that modifies the inertial response. The geometric factor 1/6 arises from the angular overlap between planar Rindler and spherical Hubble entanglement structures: only the backward hemisphere competes, and the cos²θ projection averages to 1/3, giving (1/2)(1/3) = 1/6. The critical acceleration scale is a₀ = cH₀/6 = 1.09 × 10⁻¹⁰ m/s² — within 9% of Milgrom's empirical MOND value (1.2 × 10⁻¹⁰ m/s²), derived with zero free parameters. Standard inertia is recovered at high accelerations. A companion paper [36] tests this prediction against the full SPARC radial acceleration relation (2693 data points, 153 galaxies), obtaining σ = 0.133 dex — identical to fitted MOND. We thus demonstrate that Quantized Inertia is not an independent hypothesis but a boundary correction to Jacobson's established framework — the natural consequence of applying horizon thermodynamics in a universe where entanglement is finite.

---

## I. Introduction

Newton's second law F = ma is the most used and least explained equation in physics. It defines inertial mass as the ratio of applied force to resulting acceleration, but says nothing about why matter resists acceleration, why the resistance is proportional to the force, or why the proportionality constant is what it is. In both Newtonian and Einsteinian mechanics, inertial mass is axiomatic — a given, not a derivation.

Two developments suggest this need not be so.

The first is Jacobson's remarkable result [1]. In 1995, Jacobson showed that the Einstein field equations — the foundation of general relativity — are not fundamental geometric postulates but can be *derived* from thermodynamic principles applied to local Rindler horizons. The derivation requires only three inputs: the Bekenstein-Hawking entropy-area relation S = A/4 [2,3], the Clausius relation δQ = TdS, and the Unruh temperature T = ℏa/2πck_B [4]. The Einstein equations emerge as the condition for local thermodynamic equilibrium of the vacuum at every spacetime point. This result, now cited over 3,500 times with no published rebuttals, reframes gravity as an equation of state — the macroscopic thermodynamic behavior of microscopic vacuum degrees of freedom at horizons.

The second is McCulloch's Quantized Inertia (QI) [5–9]. McCulloch identified a key principle: the Hubble horizon modifies inertia. An accelerating body creates a Rindler horizon behind it at distance c²/a; when the acceleration is very low (a → cH₀), this Rindler horizon approaches the Hubble radius, and the cosmic horizon alters the local vacuum state. In this regime, inertia is reduced, and McCulloch derives flat galaxy rotation curves without dark matter, using only visible baryonic mass and the Hubble diameter, with no adjustable parameters [8,9].

Despite sharing the same physical ingredients — Rindler horizons, Unruh radiation, the Bekenstein-Hawking entropy — these two results have developed independently. Jacobson's work is mainstream (3,500+ citations). McCulloch's is emerging (~200 citations). No paper has connected them. This independence persists despite shared reliance on Rindler horizons and Unruh radiation, highlighting an opportunity to unify thermodynamic spacetime with low-acceleration dynamics.

Several authors have derived MOND-like phenomenology from the entropic gravity programme descended from Jacobson, notably Verlinde [10,11], Klinkhamer [12,13], Sheykhi [14–16], and Rostami et al. [17]. However, these works uniformly modify the *gravitational force law* — they change what gravity does. McCulloch's programme modifies *inertia* — it changes how matter responds. This is not a semantic distinction: modified gravity and modified inertia make different predictions for galaxy rotation curve shapes [18], and the two are in principle distinguishable observationally.

In this paper, we bridge the gap. We show that McCulloch's Quantized Inertia emerges directly from Jacobson's thermodynamic spacetime when a single physically motivated correction is applied: the recognition that the Hubble horizon competes for vacuum entanglement with the local Rindler horizon. Jacobson's original derivation implicitly assumes that each mode's entanglement is fully available to the local horizon — that no competing horizon claims a share. In a universe with a finite cosmological horizon, this assumption fails. Both the Rindler and Hubble horizons are entangled with the same vacuum modes, and entanglement monogamy [37] forces a partition. The resulting correction to the entropy-area relation is negligible at ordinary accelerations but becomes dominant at the cosmological scale, precisely where galaxy dynamics deviate from Newtonian predictions. A companion paper [36] derives the quantitative prediction and tests it against the full SPARC radial acceleration relation.

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

where ℓₚ = √(ℏG/c³) is the Planck length. This relation, originally derived for black holes, extends to all causal horizons [19].

### B. The First Law at the Horizon

Jacobson applies the Clausius relation

```math
\delta Q = T \, dS \qquad \text{(4)}
```

to infinitesimal patches of the local Rindler horizon. The heat flow δQ is identified with the boost energy flux across the horizon:

```math
\delta Q = T_{ab} \, k^a \, d\Sigma^b \qquad \text{(5)}
```

where T_ab is the stress-energy tensor, kᵃ is the approximate Killing vector generating boosts (the local time-translation symmetry for the accelerated observer), and dΣᵇ is the horizon area element.

### C. Entropy and the Raychaudhuri Equation

The change in horizon area is governed by the Raychaudhuri equation for null geodesic congruences. For a pencil of horizon generators with cross-sectional area A:

```math
\frac{dA}{d\lambda} = -R_{ab} \, k^a k^b \, A \qquad \text{(6)}
```

where λ is the affine parameter along the generators and R_ab is the Ricci tensor. The entropy change is therefore:

```math
dS = \frac{k_B}{4\ell_P^2} \, dA = -\frac{k_B}{4\ell_P^2} \, R_{ab} \, k^a k^b \, A \, d\lambda \qquad \text{(7)}
```

### D. The Einstein Equations Emerge

Substituting Eqs. (2), (5), and (7) into the Clausius relation (4):

```math
T_{ab} \, k^a \, d\Sigma^b = \frac{\hbar a}{2\pi c k_B} \cdot \left( -\frac{k_B}{4\ell_P^2} \right) R_{ab} \, k^a k^b \, A \, d\lambda \qquad \text{(8)}
```

The acceleration a, the Killing vector kᵃ, and the geometric factors combine such that, after requiring this relation to hold for all horizon patches and all boost directions at every spacetime point, one obtains:

```math
R_{ab} - \frac{1}{2} R \, g_{ab} + \Lambda \, g_{ab} = \frac{8\pi G}{c^4} \, T_{ab} \qquad \text{(9)}
```

These are the Einstein field equations. The cosmological constant Λ appears as an integration constant — the thermodynamic ground-state energy of the vacuum.

**The Einstein equations are an equation of state.** They express the condition for thermodynamic equilibrium of the vacuum at every local Rindler horizon. Spacetime geometry is not fundamental — it is the macroscopic manifestation of microscopic horizon thermodynamics.

### E. The Equilibrium Assumption

Jacobson's derivation rests on a critical assumption: **local thermodynamic equilibrium**. The entropy-area relation S = A/4 is taken to hold exactly at every horizon patch. This means:

1. All vacuum field modes contribute to the entropy
2. Each mode's entanglement is fully available to the local Rindler horizon — no competing horizon claims a share
3. The entanglement budget of every mode is exhausted by the single local horizon

In an infinite or asymptotically flat universe, this is unproblematic — only the local Rindler horizon exists. In a finite, expanding cosmos, however, a second horizon competes for entanglement with the same vacuum modes — precisely the correction we introduce in Section III.

---

## III. The Finite Boundary Correction

### A. Two Competing Horizons

An accelerating observer lives between two horizons:

- **Inner boundary** (Rindler): at distance d_R = c²/a, with associated temperature T_R = ℏa/(2πck_B)
- **Outer boundary** (Hubble): at distance R_H = c/H₀ ≈ 1.3 × 10²⁶ m, with associated temperature T_H = ℏcH₀/(2πk_B)

At ordinary accelerations, the Rindler horizon is close — for a = 1 m/s², d_R ≈ 10¹⁶ m, fourteen orders of magnitude inside the Hubble radius. The Hubble horizon is irrelevant: all vacuum modes that straddle the Rindler horizon have their entanglement partners well within the observable universe. The full Bekenstein-Hawking entropy is available, and Jacobson's derivation proceeds without correction. Inertia is Newtonian.

As acceleration decreases, the Rindler horizon recedes. At a ~ cH₀ ≈ 7 × 10⁻¹⁰ m/s², the Rindler distance c²/a reaches the Hubble radius. Now vacuum modes straddling the Rindler horizon also have entanglement partners behind the Hubble horizon. Entanglement monogamy [37] — the fundamental constraint that a quantum system's entanglement with one partner limits its entanglement with any other — forces the finite entanglement budget to be partitioned between the two horizons.

Crucially, no mode is eliminated. The mode spectrum remains intact. What changes is the *share* of each mode's entanglement that is available to the local Rindler horizon. Entanglement is shared, not destroyed.

### B. Temperature-Weighted Sharing

In thermal equilibrium, entanglement distributes in proportion to temperature. The horizon with the higher temperature — corresponding to the shorter-wavelength, more energetic vacuum fluctuations — claims a larger share. For two horizons at temperatures T_R and T_H, the fraction of entanglement available to the Rindler horizon is:

```math
f_{\text{naive}} = \frac{T_R}{T_R + T_H} = \frac{a}{a + cH_0} \qquad \text{(10)}
```

This gives the correct structure — f → 1 at high acceleration, f → 0 as a → 0 — but treats both horizons as geometrically equivalent. They are not.

### C. The Geometric Factor

The Rindler horizon is *planar*: it is a null surface perpendicular to the acceleration axis ẑ, and its entanglement structure is defined by modes propagating along ẑ. The Hubble horizon is *spherical*: it is a cosmological sphere surrounding the observer, with radial modes propagating in all directions r̂.

The competition for entanglement between the two horizons depends on their geometric overlap — specifically, how strongly a given Hubble-horizon radial mode competes with the Rindler-horizon modes. A Hubble mode propagating radially at angle θ from the acceleration axis projects onto the Rindler direction as k̂ᵣ · ẑ = cosθ. The competition strength — the fraction of entanglement contested — scales as cos²θ.

Furthermore, only the **backward hemisphere** competes. Hubble modes in the forward hemisphere (θ < π/2 relative to the acceleration direction) propagate on the same side of the Rindler horizon as the observer — their entanglement partners are not behind the Rindler horizon, so there is no competition. Only modes in the backward hemisphere (θ > π/2), whose partners straddle both horizons, contest the entanglement budget.

The effective geometric overlap is therefore:

```math
g = \frac{1}{4\pi} \int_{\text{backward}} \cos^2\theta \, d\Omega = \frac{1}{4\pi} \int_0^{2\pi} d\phi \int_{\pi/2}^{\pi} \cos^2\theta \, \sin\theta \, d\theta \qquad \text{(11)}
```

```math
= \frac{1}{2} \int_{\pi/2}^{\pi} \cos^2\theta \, \sin\theta \, d\theta = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6} \qquad \text{(12)}
```

The factor 1/2 comes from restricting to the backward hemisphere. The factor 1/3 comes from the cos²θ average over that hemisphere.

**A note on directionality.** The entanglement sharing described here is intrinsically directional in the instantaneous proper rest frame of the observer, where the Unruh temperature gradient and the Rindler horizon normal are defined along the proper acceleration vector â. The cos²θ kernel in Eq. (12) encodes this: the Hubble horizon competes most strongly along â and not at all perpendicular to it. In the present paper we average over all angles to obtain the scalar sharing function f(a), which suffices for isolated systems with isotropic dynamics (e.g., circular orbits in axisymmetric potentials). However, the underlying modification is anisotropic — the entanglement deficit is concentrated along the acceleration axis. This directional structure may have observable consequences in systems where the acceleration direction is not aligned with the restoring force, such as galaxies embedded in external gravitational fields. We defer the development of the full directional formalism to future work.

### D. The Sharing Function

The effective Hubble temperature seen by the Rindler entanglement budget is reduced by the geometric factor:

```math
T_{H,\text{eff}} = \frac{T_H}{6} \qquad \text{(13)}
```

The sharing function — the fraction of vacuum entanglement available to the local Rindler horizon — is:

```math
\boxed{f(a) = \frac{T_R}{T_R + T_{H,\text{eff}}} = \frac{T_R}{T_R + T_H/6} = \frac{a}{a + cH_0/6}} \qquad \text{(14)}
```

The critical acceleration scale is:

```math
a_0 = \frac{cH_0}{6} \qquad \text{(15)}
```

Using H₀ = 67.4 km/s/Mpc (Planck 2018):

```math
a_0 = \frac{6.548 \times 10^{-10}}{6} = 1.09 \times 10^{-10} \text{ m/s}^2 \qquad \text{(16)}
```

This is within **9%** of Milgrom's empirical MOND constant a₀(MOND) = 1.2 × 10⁻¹⁰ m/s² [22], derived with zero free parameters. Using H₀ = 73 km/s/Mpc (SH0ES), one obtains a₀ = 1.16 × 10⁻¹⁰ m/s², within 3% of Milgrom.

Key properties of f(a):
- f > 0 always: entanglement is suppressed, never eliminated
- f → 1 as a → ∞: standard inertia recovered
- f → a/a₀ as a → 0: linear suppression at low acceleration
- f(a₀) = 1/2: the midpoint of the transition

### E. Propagation Through the First Law

We now repeat Jacobson's derivation with the modified entropy. The Clausius relation becomes:

```math
\delta Q = T_U \cdot f(a) \cdot dS \qquad \text{(17)}
```

Expanding:

```math
\delta Q = \frac{\hbar a}{2\pi c k_B} \cdot f(a) \cdot \frac{k_B}{4\ell_P^2} \cdot dA \qquad \text{(18)}
```

The sharing function f(a) is a smooth scalar function of the local acceleration magnitude. In Jacobson's original derivation, Eq. (8) must hold for all boost directions at every spacetime point; requiring this for the modified relation introduces f(a) as a multiplicative correction.

**A note on covariance.** Jacobson's derivation is fully covariant: it yields the tensor equation (9) by demanding consistency across all boost directions. Our correction factor f(a) depends on the magnitude of the acceleration, which is observer-dependent in full GR. In the non-relativistic limit that we treat here, acceleration is unambiguous (it is the coordinate acceleration in the rest frame of the gravitating system). For the present paper, we restrict attention to the weak-field, non-relativistic regime where the correction is observationally relevant (galaxy dynamics, wide binaries) and where the four-acceleration reduces to the familiar 3-vector **a**. The anisotropic character of the modification (Sec. III.C) means that the covariant extension is a tensor structure built from the unit four-acceleration, not a scalar function of its magnitude.

### F. The Non-Relativistic Limit: Modified Inertia

In the weak-field, non-relativistic limit, the Einstein equations reduce to the Poisson equation for the Newtonian potential, and the geodesic equation reduces to Newton's second law. Consider a test mass m_g (gravitational mass) in a gravitational field producing acceleration a. The standard Newtonian limit gives F = m_g a.

With our modification, the relationship between the stress-energy source and the resulting geometry is altered by the factor f(a). In the Newtonian limit, this manifests as a modification to the inertial response: the effective force law becomes

```math
F = m_g \cdot a \cdot f(a) = m_g \cdot a \cdot \frac{a}{a + a_0} \qquad \text{(19)}
```

We can equivalently express this as a modified inertial mass:

```math
\boxed{m_i(a) = m_g \cdot \frac{a}{a + a_0}} \qquad \text{(20)}
```

where a₀ = cH₀/6.

This is the Jacobson-framework realization of McCulloch's Quantized Inertia [5–9]. Inertial mass is no longer identically equal to gravitational mass. At high accelerations (a ≫ a₀), the equivalence principle holds: m_i → m_g. At cosmological accelerations (a ~ a₀), inertia is reduced as entanglement is partitioned between the Rindler and Hubble horizons.

![Figure 1](Figure1.png)

**Figure 1.** Sharing function f(a) = a/(a + a₀) with a₀ = cH₀/6 = 1.09 × 10⁻¹⁰ m/s². At solar-system accelerations (right), f ≈ 1 and standard Newtonian inertia holds. At galaxy-edge accelerations (~10⁻¹⁰ m/s²), the transition begins. The function is smooth and strictly positive everywhere — entanglement is suppressed but never eliminated — in contrast to mode-truncation models where inertia vanishes at finite acceleration. The predicted a₀ lies within 9% of Milgrom's empirical value (orange), derived with zero free parameters.

---

## IV. Limiting Cases and Predictions

### A. High Acceleration (a ≫ a₀)

When a ≫ a₀ = cH₀/6:

```math
f(a) = \frac{a}{a + a_0} \to 1 - \frac{a_0}{a} + \mathcal{O}(a_0^2/a^2) \qquad \text{(21)}
```

Standard Newtonian inertia is recovered. Jacobson's full Einstein equations hold without correction. This regime covers all laboratory physics and solar system dynamics. For Earth's orbital acceleration (a ≈ 6 × 10⁻³ m/s²):

```math
1 - f(a) = \frac{a_0}{a + a_0} \approx \frac{a_0}{a} \approx \frac{1.1 \times 10^{-10}}{6 \times 10^{-3}} \sim 2 \times 10^{-8} \qquad \text{(22)}
```

This is far below current precision tests of the equivalence principle (~10⁻¹⁵ for Eötvös-type experiments), ensuring no conflict with solar system ephemerides, lunar laser ranging, or the Cassini spacecraft constraint on post-Newtonian parameters.

### B. Low Acceleration (a ≪ a₀)

As a → 0:

```math
f(a) \to \frac{a}{a_0} \qquad \text{(23)}
```

Inertia is linearly suppressed but **never vanishes**. Even at arbitrarily low acceleration, f(a) > 0 — the Rindler horizon always claims a nonzero share of the entanglement budget, because T_R > 0 for any a > 0. There is no zero-crossing and no regime of negative inertial mass. This is a structural improvement over mode-truncation models [5–9], where m_i → 0 at a finite acceleration and m_i < 0 for a < a₀, requiring a self-regulation argument to avoid unphysical behavior. The entanglement-sharing function is well-behaved everywhere by construction.

### C. Galaxy Rotation Curves

Stars in the outer regions of spiral galaxies orbit with accelerations a ~ 10⁻¹⁰ m/s², comparable to a₀. In this regime, the rotation velocity of a star of gravitational mass m_g at radius r from a galaxy of mass M satisfies:

```math
\frac{m_i v^2}{r} = \frac{G M m_g}{r^2} \qquad \text{(24)}
```

Substituting m_i = m_g f(a) with a = v²/r and the force balance condition:

```math
f(a) \cdot a = \frac{GM}{r^2} = a_N \qquad \text{(25)}
```

where a_N is the Newtonian gravitational acceleration. In the deep low-acceleration regime (a ≪ a₀), f(a) → a/a₀, so:

```math
\frac{a^2}{a_0} = a_N \implies a = \sqrt{a_N \, a_0} \qquad \text{(26)}
```

This is the MOND deep-regime relation. Since a = v²/r and a_N = GM/r²:

```math
\frac{v^4}{r^2} = \frac{GM}{r^2} \cdot a_0 \implies v^4 = G M a_0 = \frac{G M c H_0}{6} \qquad \text{(27)}
```

This is the baryonic Tully-Fisher relation [24]: the asymptotic rotation velocity depends only on the baryonic mass of the galaxy and cosmological constants, with no free parameters. The companion paper [36] tests the full sharing function f(a) = a/(a + a₀) against the SPARC radial acceleration relation [25] — 2693 data points across 153 galaxies — obtaining a scatter of σ = 0.133 dex, identical to fitted MOND.

The Tully-Fisher relation has been one of the strongest empirical arguments for MOND over dark matter: ΛCDM has no natural explanation for why v⁴ ∝ M should hold with the observed tightness and zero scatter. In our framework, it is a geometric consequence of entanglement sharing between the Rindler and Hubble horizons.

### D. Wide Binary Stars

Wide binary stars with separations exceeding ~5,000 AU have internal orbital accelerations below a₀. In isolation, the scalar sharing function Eq. (14) would predict non-Newtonian behavior at these separations. However, wide binaries in the Milky Way are not isolated: each star accelerates at a_Gal ≈ 1.8 × 10⁻¹⁰ m/s² toward the Galactic center, comparable to a₀. This external field dominates the Rindler horizon, and the directional structure noted in Section III.C becomes critical.

Because the Galactic acceleration is a fixed direction that does not co-rotate with the binary orbit, the anisotropic entanglement modification averages over the orbital cycle. The predicted internal dynamics are therefore approximately Newtonian — the external field effectively restores standard inertia for the binary's internal motion. This is the analogue of the external field effect (EFE) in MOND [39], arising here from the directional entanglement sharing rather than from a modified Poisson equation.

Current Gaia DR3 analyses are contested — Chae [26] reports a significant anomaly consistent with MOND, while Banik et al. [27] find consistency with Newton. If the anomaly is confirmed, it would challenge the directional sharing mechanism described above and require revision of the angular structure of entanglement competition. If wide binaries prove Newtonian, our framework is consistent. Gaia DR4 should resolve the observational question.

### E. Cosmological Predictions

Because a₀ = cH₀/6 and H₀ evolves with cosmic time, our framework predicts that the critical acceleration scale is not constant but tracks the expansion history:

```math
a_0(z) = \frac{c \, H(z)}{6} \qquad \text{(28)}
```

At higher redshift, H(z) is larger, so a₀ is larger, and galaxy rotation anomalies should appear at higher accelerations and smaller radii than in the local universe. McCulloch [9] has noted that this prediction is consistent with observations of galaxy dynamics out to z ~ 2.2, where enhanced rotation anomalies are observed.

This is a testable cosmological prediction that distinguishes horizon-based inertia modification from fixed-a₀ MOND, where a₀ is a fundamental constant with no redshift dependence.

---

## V. Addressing Objections

### A. The Circularity Question

Chirco et al. [28] criticized Jacobson's derivation as circular: the entropy-area relation S = A/4 is derived from the Bekenstein-Hawking result, which itself assumes the Einstein equations. If GR is assumed to justify S = A/4, then deriving GR from S = A/4 is circular.

This objection, far from undermining our result, supports it. If S = A/4 is not a fundamental axiom but an emergent relation (as Chirco argues), then it can be *modified* at boundaries without violating any deeper principle. Our modification — accounting for entanglement sharing with the Hubble horizon — is not ad hoc but reflects the physical fact that entanglement monogamy constrains the entropy available to any single horizon when multiple horizons coexist. The Bousso covariant entropy bound [29], which Chirco recommends as a replacement for S = A/4, naturally incorporates causal boundaries. Our work is compatible with this programme.

### B. The Equivalence Principle

Equation (20) implies m_i ≠ m_g at low accelerations, apparently violating the equivalence principle. However:

1. The equivalence principle is a *local* statement. It requires m_i = m_g in a sufficiently small neighborhood. Our correction involves the ratio of the local Rindler horizon to the cosmological horizon — an intrinsically non-local quantity. The equivalence principle is not violated locally; it is *supplemented* by a cosmological boundary condition.

2. The Weak Equivalence Principle (universality of free fall) is preserved: all bodies experience the same inertia reduction at the same acceleration, regardless of composition. What is modified is the *value* of inertial mass, not its universality.

3. The strong equivalence principle *is* broken by the Hubble boundary condition: the cosmological horizon defines a preferred vacuum state, so a uniform external gravitational field is not locally invisible. This breaking is the physical origin of the external field effect. However, the violation is cosmological in character and undetectable at solar-system accelerations.

### C. Non-Equilibrium Considerations

Jacobson's derivation assumes thermodynamic equilibrium at the horizon. Our modification introduces a departure from equilibrium: entanglement sharing with the Hubble horizon reduces the entropy available to the Rindler horizon. This is precisely the regime addressed by Eling, Guedens, and Jacobson [30], who extended the thermodynamic spacetime programme to non-equilibrium situations by including entropy production terms.

In their framework, departures from S = A/4 generate additional terms in the field equations proportional to the gradient of the entropy modification. Our sharing function f(a) = a/(a + a₀) is smooth everywhere — it has no discontinuities, no zero crossings, and its spatial gradient is negligible except where a ~ a₀. Non-equilibrium entropy production terms are therefore subdominant, consistent with the fact that galaxy dynamics, while anomalous, are quasi-static.

### D. Relation to Prior Work on Entropic MOND

Several authors have derived MOND-like phenomenology from entropic gravity:

- **Verlinde [10,11]:** Uses competition between area-law and volume-law entropy in de Sitter space. Works with holographic screens rather than Rindler horizons.
- **Klinkhamer [12,13]:** Introduces a minimum temperature for holographic-screen degrees of freedom. Derives the full Bekenstein-Milgrom equation including the external field effect.
- **Sheykhi [14–16]:** Modifies the entropy-area relation using Tsallis statistics (S ∝ A^β) to derive modified Friedmann equations and galaxy rotation.
- **Sheykhi & Liravi [16]:** Reverse-engineers the horizon entropy that produces MOND.
- **Rostami et al. [17]:** Derives relativistic MOND from temperature-dependent corrections to the equipartition law.

All of these modify the *gravitational force law*. None derives a modification to *inertia*. Our work differs in three respects:

1. **We modify inertia, not gravity.** The correction appears in m_i, not in G or the gravitational potential. This has distinct observational signatures: modified gravity and modified inertia predict subtly different rotation curve shapes, testable with current data [18].
2. **We start from Jacobson's local Rindler horizons**, not Verlinde's holographic screens or Padmanabhan's surface-volume thermodynamics [33]. This keeps us closest to the foundational result.
3. **The entropy modification has a physical origin** (entanglement sharing between competing horizons, governed by monogamy), not a statistical-mechanical one (Tsallis, Kaniadakis, Debye). No new statistical mechanics is required — only the established physics of entanglement and the observed existence of a cosmological horizon.

Verlinde's emergent gravity [11] also invokes entropy competition — between area-law and volume-law entanglement in de Sitter space. However, Verlinde modifies the gravitational potential (producing an additional gravitational force), whereas our framework modifies the inertial response. The physical mechanism is distinct: Verlinde works with holographic screens and emergent spacetime; we work with Jacobson's local Rindler horizons and entanglement monogamy between those horizons and the Hubble boundary.

---

## VI. Discussion

### What This Paper Demonstrates

We have shown that Quantized Inertia — McCulloch's proposal that the Hubble horizon modifies inertial mass at low accelerations — is not an independent hypothesis. It is the natural consequence of Jacobson's thermodynamic spacetime when one accounts for the fact that the Hubble horizon competes for vacuum entanglement with the local Rindler horizon. The derivation requires no new physics beyond:

1. Jacobson's result (Einstein equations from horizon thermodynamics) — 3,500+ citations, mainstream
2. The Unruh effect (thermal radiation for accelerated observers) — standard QFT
3. The Bekenstein-Hawking entropy (proportional to horizon area) — standard
4. The Gibbons-Hawking effect (thermal radiation from cosmological horizons) — standard
5. Entanglement monogamy (finite entanglement budgets must be shared) — fundamental quantum mechanics
6. The existence of a finite cosmological horizon — observed

The MOND acceleration scale a₀ = cH₀/6 emerges from the geometry of two competing horizons: the temperature-weighted sharing of entanglement, modulated by the angular overlap between planar Rindler and spherical Hubble entanglement structures. The factor 1/6 = (1/2)(1/3) is a geometric constant. This is not a fitted parameter — it is a derived consequence of horizon geometry.

### What Remains To Be Done

**Galaxy clusters.** MOND-like theories underpredict the mass deficit in galaxy clusters by a factor of ~2. If our modified inertia inherits this deficit, the transition region of f(a) — where accelerations are slightly above a₀ — becomes important. The smooth sharing function may behave differently from standard MOND interpolation functions in this regime, and a detailed cluster analysis is warranted.

**Backreaction and self-consistency.** If inertia depends on acceleration and acceleration depends on inertia, the system must be self-consistent. McCulloch [8] addresses this iteratively and finds convergence. A formal proof of convergence — or a demonstration that the modified field equation has a well-posed initial value problem — would strengthen the result.

**CMB consistency.** The framework predicts a₀(z) = cH(z)/6, which implies a different MOND scale in the early universe. This must be consistent with cosmic microwave background constraints on structure formation and the angular power spectrum. The CMB test is the most important open challenge for this programme: if the modified inertia at high redshift produces unacceptable deviations in the CMB power spectrum, the framework fails regardless of its success with galaxy rotation. Addressing this requires embedding the sharing function in a cosmological perturbation theory, which is a target for future work.

### Experimental Tests

The most decisive near-term tests involve systems where the internal acceleration is below a₀ but an external field is present. **Wide binary stars** are one such system: the Galactic field dominates the Rindler horizon, and the directional sharing predicts approximately Newtonian internal dynamics despite the low internal acceleration. This prediction — that the external field restores Newtonian behavior through the angular structure of entanglement competition — is falsifiable with Gaia data. Current analyses are contested [26,27]; Gaia DR4 should resolve the systematics. **Galaxy rotation curves** in external fields (the external field effect) provide a complementary test: the directional sharing predicts that the EFE strength depends on the angle between the disk plane and the external field direction, not merely on its magnitude.

**Laboratory tests** require accelerations approaching a₀ ~ 10⁻¹⁰ m/s², below current torsion balance and atom interferometer sensitivity. However, McCulloch has proposed that asymmetric electromagnetic cavities — which modify the local Rindler horizon geometry — could produce measurable thrust [6]. DARPA-funded tests of QI-inspired thrusters are ongoing.

The **cosmological prediction** a₀(z) = cH(z)/6 is testable with high-redshift galaxy kinematics. Preliminary data supports a time-varying MOND scale out to z ~ 2.2 [9]. JWST observations of compact high-redshift galaxies provide further opportunities.

---

## VII. Conclusion

Jacobson showed that spacetime has an equation of state. The Einstein equations express the condition for thermodynamic equilibrium at local Rindler horizons. This paper has shown that when that equilibrium is modified by the finite extent of the observable universe — when the Hubble horizon competes for vacuum entanglement with the Rindler horizon of a slowly accelerating body — the result is a modified inertia that reproduces the phenomenology of McCulloch's Quantized Inertia.

The mechanism is entanglement sharing, not mode truncation. Both horizons are entangled with the same vacuum modes. Entanglement monogamy forces a partition, governed by the temperature ratio of the two horizons and their geometric overlap. The sharing function f(a) = a/(a + cH₀/6) is smooth, strictly positive, and recovers standard inertia at high acceleration. The critical scale a₀ = cH₀/6 = 1.09 × 10⁻¹⁰ m/s² lies within 9% of Milgrom's empirical MOND constant, with zero free parameters.

Below a₀, entanglement is partitioned, the entropy-area relation is modified, and inertial mass is reduced. This produces flat galaxy rotation curves, the baryonic Tully-Fisher relation, and a time-varying MOND scale that tracks cosmic expansion — all from Jacobson's framework plus the physical fact that entanglement is finite and horizons must share it.

The conceptual debt to McCulloch is total. He identified the key principle: the Hubble horizon modifies inertia. Embedding that principle in Jacobson's rigorous thermodynamic framework reveals the precise mechanism — entanglement sharing rather than mode truncation — and yields a specific functional form that matches observations. The interpolation function f(a) = a/(a + cH₀/6) differs from McCulloch's original 1 − (cH₀/a)², but the physical insight is the same: inertia has a boundary condition, and that boundary is the edge of the observable universe.

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

[17] A. Rostami, K. Rezazadeh, and M. Rostampour, "Relativistic MOND Theory from Modified Entropic Gravity," [arXiv:2511.05632](https://arxiv.org/abs/2511.05632) (2025).

[18] V. Costantino and T. Broadhurst, "A First Attempt to Differentiate between Modified Gravity and Modified Inertia with Galaxy Rotation Curves," Astron. Astrophys. **636**, A15 (2020). [arXiv:2001.03348](https://arxiv.org/abs/2001.03348)

[19] T. Jacobson, "Horizon Entropy," [arXiv:gr-qc/0302099](https://arxiv.org/abs/gr-qc/0302099) (2003).

[20] G. 't Hooft, "On the Quantum Structure of a Black Hole," Nucl. Phys. B **256**, 727 (1985).

[21] N. Bazarov, S. Piroli, and S. N. Solodukhin, "Infrared Regularization and Finite Size Dynamics of Entanglement Entropy in Schwarzschild Black Hole," Phys. Rev. D **108**, 046005 (2023). [arXiv:2209.00036](https://arxiv.org/abs/2209.00036)

[22] M. Milgrom, "A Modification of the Newtonian Dynamics as a Possible Alternative to the Hidden Mass Hypothesis," Astrophys. J. **270**, 365 (1983).

[23] "Modified Unruh Thermodynamics in Emergent Gravity: Finite Heat Capacity and Rényi Entropy," [arXiv:2509.03470](https://arxiv.org/abs/2509.03470) (2025).

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

[34] J. Gillot, "Quantum Modified Inertia: An Application to Galaxy Rotation Curves," [arXiv:2507.11524](https://arxiv.org/abs/2507.11524) (2025).

[35] S. N. Solodukhin, "Entanglement Entropy of Black Holes," Living Rev. Relativ. **14**, 8 (2011).

[36] K. Brodie, "The Radial Acceleration Relation from Two-Horizon Entropy Sharing with Zero Free Parameters," Zenodo (2026). [DOI: 10.5281/zenodo.18677307](https://doi.org/10.5281/zenodo.18677307).

[37] V. Coffman, J. Kundu, and W. K. Wootters, "Distributed Entanglement," Phys. Rev. A **61**, 052306 (2000).

[38] G. W. Gibbons and S. W. Hawking, "Cosmological Event Horizons, Thermodynamics, and Particle Creation," Phys. Rev. D **15**, 2738 (1977).

[39] J. D. Bekenstein and M. Milgrom, "Does the Missing Mass Problem Signal the Breakdown of Newtonian Gravity?" Astrophys. J. **286**, 7 (1984).
