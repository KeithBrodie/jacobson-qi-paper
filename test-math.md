# Math Rendering Test

## Test 1: Code fence (current approach)

```math
d_R = \frac{c^2}{a} \qquad \text{(1)}
```

## Test 2: Dollar signs on separate lines

$$
d_R = \frac{c^2}{a}
$$

## Test 3: Dollar signs on same line

$$d_R = \frac{c^2}{a}$$

## Test 4: Longer equation - code fence

```math
T_{ab} \, k^a \, d\Sigma^b = \frac{\hbar a}{2\pi c k_B} \cdot \left( -\frac{k_B}{4\ell_P^2} \right) R_{ab} \, k^a k^b \, A \, d\lambda
```

## Test 5: Longer equation - dollar signs separate lines

$$
T_{ab} \, k^a \, d\Sigma^b = \frac{\hbar a}{2\pi c k_B} \cdot \left( -\frac{k_B}{4\ell_P^2} \right) R_{ab} \, k^a k^b \, A \, d\lambda
$$

## Test 6: No thin spaces

```math
T_{ab} k^a d\Sigma^b = \frac{\hbar a}{2\pi c k_B} \cdot \left( -\frac{k_B}{4\ell_P^2} \right) R_{ab} k^a k^b A d\lambda
```

## Test 7: Simple fraction only

```math
\frac{c^2}{a}
```

## Test 8: Aligned environment

```math
\begin{aligned}
d_R &= \frac{c^2}{a} \\
T_U &= \frac{\hbar a}{2\pi c k_B}
\end{aligned}
```
