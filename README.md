# Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime

**Author:** Keith Brodie (2026), with AI assistance (Claude/Anthropic, Grok/xAI)

## Summary

Jacobson (1995) showed that the Einstein equations emerge from horizon thermodynamics, assuming all vacuum entanglement is available to the local Rindler horizon. We show this assumption fails when the Hubble horizon competes for the same entanglement. Entanglement monogamy forces a partition between the two horizons, reducing the effective entropy and modifying the inertial response:

```math
f(a) = \frac{a}{a + cH_0/6}
```

The geometric factor 1/6 = (1/2 backward hemisphere) × (1/3 cos²θ overlap) arises from the angular mismatch between planar Rindler and spherical Hubble entanglement structures. The critical acceleration scale:

```math
a_0 = \frac{cH_0}{6} = 1.09 \times 10^{-10} \text{ m/s}^2
```

is within **9%** of Milgrom's empirical MOND constant (1.2 × 10⁻¹⁰ m/s²), derived with **zero free parameters**.

This embeds McCulloch's Quantized Inertia into Jacobson's established framework, revealing the mechanism as entanglement sharing rather than mode truncation. A companion paper ([Paper 4](https://doi.org/10.5281/zenodo.18677307)) tests this prediction against the full SPARC radial acceleration relation — 2,693 data points, 153 galaxies, σ = 0.133 dex — identical to fitted MOND.

## Files

- `Draft-v3.md` — Full paper text (Markdown with LaTeX math)
- `figure1.py` — Figure generation script
- `Figure1.png` — Entanglement sharing function f(a) = a/(a + a₀)
- `LiteratureSearch.md` — Background literature survey
- `LICENSE` — CC BY 4.0

## Running the Code

```bash
pip install numpy matplotlib
python figure1.py
```

## Related Papers

1. **Paper 2:** K. Brodie, "Karlsson's Redshift Periodicity as an Efimov Spectrum" (2026). [DOI: 10.5281/zenodo.18664931](https://doi.org/10.5281/zenodo.18664931)

2. **Paper 3:** K. Brodie, "Accelerated Structure Formation from Horizon Thermodynamics" (2026). [DOI: 10.5281/zenodo.18665076](https://doi.org/10.5281/zenodo.18665076)

3. **Paper 4:** K. Brodie, "The Radial Acceleration Relation from Two-Horizon Entropy Sharing with Zero Free Parameters" (2026). [DOI: 10.5281/zenodo.18677307](https://doi.org/10.5281/zenodo.18677307)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
