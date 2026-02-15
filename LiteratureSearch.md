# Literature Search: Jacobson → QI Derivation

Conducted 2026-02-14. Searched for prior art bridging Jacobson's thermodynamic spacetime to McCulloch's Quantized Inertia, and for mathematical tools needed for the derivation.

---

## Executive Summary

**The good news:** No paper exists that explicitly derives McCulloch's Quantized Inertia from Jacobson's framework. The niche is open.

**The bad news (sort of):** Multiple papers derive MOND from entropic/thermodynamic gravity — the same phenomenological endpoint. But they all modify *gravity* (the force law), not *inertia* (the mass). This is a meaningful distinction that our paper must articulate clearly.

**The key prior art:** Sheykhi & Liravi (2025) come closest — they reverse-engineer the horizon entropy that produces MOND. But they work from the gravity side, not the inertia side.

**The mathematical tools we need exist:** 't Hooft (1985), Bazarov et al. (2023), and arXiv:2509.03470 (2025) all compute how finite boundaries modify horizon entropy. These give us the mathematical machinery.

---

## Tier 1: Direct Prior Art (MOND from Thermodynamic Gravity)

These papers derive MOND-like behavior from frameworks descended from Jacobson. They are the papers we must cite, distinguish from, and build on.

### Sheykhi & Liravi (2025) — CLOSEST PRIOR ART
- **Title:** "MOND Theory and Thermodynamics of Spacetime"
- **Journal:** Physics of the Dark Universe 49, 101967
- **arXiv:** [2510.14345](https://arxiv.org/abs/2510.14345)
- **What they do:** Construct the specific entropy expression that produces MOND, then derive modified Friedmann equations via three methods (first law, entropic force, Padmanabhan emergence)
- **How we differ:** They modify gravity (force law). We modify inertia (mass). They reverse-engineer entropy from MOND. We derive the entropy modification from first principles (finite Hubble boundary on mode spectrum)

### Sheykhi (2020) — Galaxy Rotation from Tsallis Entropy
- **Title:** "New Explanation for Accelerated Expansion and Flat Galactic Rotation Curves"
- **Journal:** European Physical Journal C 80, 25
- **arXiv:** [1912.08693](https://arxiv.org/abs/1912.08693)
- **What they do:** Use Tsallis entropy S ~ A^β at the apparent horizon → modified Newton's law → flat rotation curves without dark matter (β < 1/2)
- **How we differ:** Tsallis entropy is a phenomenological ansatz. Our modification has a physical origin (mode truncation at the Hubble boundary)

### Klinkhamer (2012) — Most Complete MOND from Entropic Gravity
- **Title:** "Entropic-gravity derivation of MOND"
- **Journal:** Modern Physics Letters A 27, 1250056
- **arXiv:** [1201.4160](https://arxiv.org/abs/1201.4160)
- **What they do:** Derive full non-relativistic MOND (including external field effect and Bekenstein-Milgrom equation) from entropic gravity + minimum temperature on holographic screen. a₀ identified with Unruh temperature of de Sitter space
- **How we differ:** Klinkhamer uses Verlinde's holographic screens. We use Jacobson's local Rindler horizons. Klinkhamer modifies gravity. We modify inertia

### Klinkhamer & Kopp (2011) — Minimum Temperature
- **Title:** "Entropic gravity, minimum temperature, and modified Newtonian dynamics"
- **Journal:** Modern Physics Letters A 26, 2783
- **arXiv:** [1104.2022](https://arxiv.org/abs/1104.2022)
- **What they do:** First paper positing minimum temperature for holographic-screen degrees of freedom → MOND

### Sheykhi & Sarab (2012) — Debye Model
- **Title:** "Einstein Equations and MOND Theory from Debye Entropic Gravity"
- **Journal:** JCAP 10 (2012) 012
- **arXiv:** [1206.1030](https://arxiv.org/abs/1206.1030)
- **What they do:** Modify equipartition using Debye model (low-temperature cutoff) → Einstein equations + MOND from single framework
- **How we differ:** Debye model is a condensed-matter analogy. Our cutoff has a geometric origin (Hubble boundary)

### Rostami, Rezazadeh & Rostampour (2025) — Relativistic MOND
- **Title:** "Relativistic MOND Theory from Modified Entropic Gravity"
- **arXiv:** [2511.05632](https://arxiv.org/abs/2511.05632)
- **What they do:** Temperature-dependent corrections to equipartition → modified Einstein equations → MOND in weak-field limit. Tested against NGC 3198 rotation curve data

### Zhang & Li (2012) — MOND Cosmology
- **Title:** "MOND Cosmology from Entropic Force"
- **Journal:** Physics Letters B 715, 15
- **arXiv:** [1106.2966](https://arxiv.org/abs/1106.2966)
- **What they do:** Derive a₀ at cosmological scales from entropic gravity, solving the "coincidence problem" (why a₀ ~ cH₀)

---

## Tier 2: Mathematical Tools (Finite Boundary → Modified Entropy)

These papers provide the mathematical machinery for computing how a finite outer boundary modifies the Bekenstein-Hawking entropy. This is the technical core of our derivation.

### Bazarov, Piroli & Solodukhin (2023) — ESSENTIAL
- **Title:** "Infrared Regularization and Finite Size Dynamics of Entanglement Entropy in Schwarzschild Black Hole"
- **Journal:** Physical Review D 108, 046005
- **arXiv:** [2209.00036](https://arxiv.org/abs/2209.00036)
- **What they do:** Explicitly compute how a finite outer boundary modifies entanglement entropy in Schwarzschild spacetime. Introduce IR regularization for semi-infinite entangling regions. Show finite lifetime of entanglement islands
- **Why we need it:** Direct calculation of S(A, R_outer) — entropy as a function of both horizon area and outer boundary distance

### 't Hooft (1985) — ESSENTIAL
- **Title:** "On the Quantum Structure of a Black Hole"
- **Journal:** Nuclear Physics B 256, 727
- **What they do:** The original "brick wall" model. Both UV cutoff (inner boundary) and IR cutoff (outer boundary) needed for finite entropy. S ∝ A_horizon
- **Why we need it:** Shows that the entropy-area law *requires* boundary regulation — our finite Hubble boundary is physically motivated IR regulation

### Modified Unruh Thermodynamics (2025) — ESSENTIAL
- **arXiv:** [2509.03470](https://arxiv.org/abs/2509.03470)
- **What they do:** Treat local Rindler horizons as finite heat-capacity systems → entropy shifts from Bekenstein-Hawking to Rényi form with nonextensivity parameter λ ~ 1/C. Show Jacobson's derivation survives the modification
- **Why we need it:** Demonstrates that modifying horizon entropy is compatible with Jacobson's framework — the machine still works with different entropy input

### Solodukhin (2011) — Review
- **Title:** "Entanglement Entropy of Black Holes"
- **Journal:** Living Reviews in Relativity 14, 8
- **What they do:** Comprehensive review of entanglement entropy, area law, logarithmic corrections. Discusses how UV and IR cutoffs regulate entropy
- **Why we need it:** Background and formalism for the entropy calculation

### Logarithmic Corrections (various, 2000s–2010s)
- **Review:** [MDPI Entropy 13, 1](https://www.mdpi.com/1099-4300/13/1/11)
- **What they do:** Beyond S = A/4, corrections go as −3/2 ln(A) plus subleading 1/A terms. From LQG (Kaul & Majumdar), quantum entropy function (Sen), entanglement (Solodukhin)
- **Why we need it:** These corrections are relevant when the system departs from the thermodynamic limit — exactly our regime

---

## Tier 3: Framework Papers

### Jacobson (1995) — The Foundation
- Phys. Rev. Lett. 75, 1260. [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)

### Verlinde (2010/2017) — Entropic Gravity
- JHEP 1104:029 (2011). [arXiv:1001.0785](https://arxiv.org/abs/1001.0785)
- SciPost Physics 2, 016 (2017). [arXiv:1611.02269](https://arxiv.org/abs/1611.02269)
- 2017 paper: competition between area-law and volume-law entropy in de Sitter → "dark gravitational force" at Hubble scale → MOND-like phenomenology

### Padmanabhan (2010) — Equipartition
- Modern Physics Letters A 25, 1129. [arXiv:0912.3165](https://arxiv.org/abs/0912.3165)
- Equipartition of horizon degrees of freedom → Newton's law

### Cai & Kim (2005) — Friedmann from Horizon Thermodynamics
- JHEP 0502:050. [arXiv:hep-th/0501055](https://arxiv.org/abs/hep-th/0501055)
- First law at FRW apparent horizon → Friedmann equations. Extended to Gauss-Bonnet and Lovelock gravity

### Jacobson (2003) — Horizon Entropy Review
- [arXiv:gr-qc/0302099](https://arxiv.org/abs/gr-qc/0302099)
- All causal horizons (Rindler, de Sitter, BH) obey thermodynamic laws

### Kothawala, Sarkar & Padmanabhan (2007)
- Physics Letters B 652, 338
- Einstein equations reduce to TdS = dE + PdV on wide class of horizons including Rindler

### Eling, Guedens & Jacobson (2006) — Non-equilibrium Extension
- Non-equilibrium thermodynamics of spacetime. Extends Jacobson beyond equilibrium assumption

### Jae-Weon Lee (2010/2012) — Inertia from Rindler Horizons
- Foundations of Physics 42, 1153. [arXiv:1003.4464](https://arxiv.org/abs/1003.4464)
- Inertia from "dragging Rindler horizons." Holographic screens = local Rindler horizons

### Smolin (2017) — MOND from Quantum Gravity
- Physical Review D 96, 083523. [arXiv:1704.00780](https://arxiv.org/abs/1704.00780)
- MOND as regime of quantum gravity below de Sitter temperature. Different route but related endpoint

---

## Tier 4: McCulloch's Program

### McCulloch (2007) — First QI Paper
- MNRAS 376, 338. Pioneer anomaly from modified inertia via Hubble-scale Casimir effect

### McCulloch (2013) — Clearest Mechanism
- EPL 101, 59001. [arXiv:1302.2775](https://arxiv.org/abs/1302.2775)
- Rindler horizon suppresses Unruh radiation on one side (Casimir-like). Hubble horizon provides uniform suppression. Net radiation pressure = inertia

### McCulloch (2017) — Galaxy Rotation
- Astrophysics and Space Science 362, 149. [arXiv:1709.04918](https://arxiv.org/abs/1709.04918)
- 153 SPARC galaxies, zero free parameters, comparable to MOND

### McCulloch (2020) — Information Theory Derivation
- Advances in Astrophysics 5(3)
- QI from Landauer's principle: information stored in horizon distances, mass-energy released when horizon area changes

### Gillot (2025) — Quantum Modified Inertia
- [arXiv:2507.11524](https://arxiv.org/abs/2507.11524)
- Modified inertia within special relativity with maximal and minimal acceleration bounds. Better than MOND at ~10⁻¹⁰ m/s²

### Costantino & Broadhurst (2020) — Modified Gravity vs Modified Inertia
- A&A 636, A15. [arXiv:2001.03348](https://arxiv.org/abs/2001.03348)
- Attempts to observationally distinguish modified gravity from modified inertia using rotation curves. Subtly different predictions

---

## Tier 5: Luciano & Sheykhi Collaboration (Detail)

### Their Method
Systematically modify the entropy-area relation on cosmological horizons (Tsallis, Kaniadakis, string T-duality, generalized mass-to-horizon), then apply first law at apparent horizon → modified Friedmann equations → modified gravity

### Key Papers
- Lambiase, Luciano & Sheykhi (2023): Kaniadakis inflation. EPJC 83, 936. [arXiv:2307.04027](https://arxiv.org/abs/2307.04027)
- Luciano & Sheykhi (2023): Black hole Tsallis thermodynamics. PDU 42, 101319. [arXiv:2304.11006](https://arxiv.org/abs/2304.11006)
- Luciano & Sheykhi (2024): String T-duality cosmology + zero-point length. EPJC 84, 682. [arXiv:2404.12707](https://arxiv.org/abs/2404.12707)
- Jusufi, Luciano, Sheykhi & Samart (2024/2025): Kaluza-Klein dark universe. JHEA 47, 100373. [arXiv:2411.14176](https://arxiv.org/abs/2411.14176)
- Luciano & Paliathanasis (2025): MHR entropy vs DESI DR2. PLB 139954. [arXiv:2508.13260](https://arxiv.org/abs/2508.13260)
- Luciano (2025): MHR structure growth + primordial GW. JHEA 50, 100487. [arXiv:2510.00673](https://arxiv.org/abs/2510.00673)

### Gap in Their Program
They modify *gravity*, not *inertia*. They do not frame results as modifications to F = ma or to inertial mass. This is the opening for our paper.

---

## Casimir at Cosmological Scale

### Casimir Effect and the Cosmological Constant (2025)
- [MDPI Symmetry 17, 634](https://www.mdpi.com/2073-8994/17/5/634)
- Global Casimir effect at Hubble horizon → EM Casimir energy ≈ 56% of observed cosmological constant
- Relevant: shows that treating the Hubble horizon as a physical boundary that selects vacuum modes has real consequences

---

## Strategic Assessment for Our Paper

### What's New (Our Niche)
1. **Nobody derives McCulloch's specific QI formula from Jacobson.** The Jacobson → MOND papers all go through Verlinde's holographic screens or Padmanabhan's emergence, and they all modify gravity. We start from Jacobson's local Rindler horizons (closer to the source) and modify inertia (closer to McCulloch)
2. **The modified-gravity vs modified-inertia distinction is observationally testable** (Costantino & Broadhurst 2020). Our paper is on the inertia side of that divide
3. **The physical origin of the entropy modification is different.** Sheykhi uses Tsallis/Kaniadakis (statistical mechanics ansätze). Klinkhamer uses minimum temperature. We use a geometric fact: the universe has a finite size, which truncates the mode spectrum. No new statistical mechanics needed

### What We Must Cite and Distinguish
1. Sheykhi & Liravi (2025) — closest prior art, MOND from horizon entropy
2. Klinkhamer (2012) — most complete MOND from entropic gravity
3. Sheykhi (2020) — galaxy rotation from Tsallis entropy
4. Verlinde (2017) — area vs volume entropy competition
5. Costantino & Broadhurst (2020) — modified gravity vs modified inertia distinction
6. Gillot (2025) — recent modified inertia work

### Mathematical Resources
1. 't Hooft (1985) — brick wall, finite boundary entropy
2. Bazarov et al. (2023) — finite outer boundary entropy calculation
3. arXiv:2509.03470 (2025) — modified Unruh thermodynamics, Rényi entropy, compatible with Jacobson
4. Solodukhin (2011) — entanglement entropy review

### The Key Sentence for the Introduction
"While several authors have derived MOND-like phenomenology from entropic gravity by modifying the gravitational force law (Verlinde 2017, Sheykhi 2020, Klinkhamer 2012), we show that McCulloch's Quantized Inertia — which modifies the *inertial response* of matter — emerges directly from Jacobson's thermodynamic spacetime when the Hubble horizon is imposed as a finite outer boundary on the vacuum mode spectrum."
