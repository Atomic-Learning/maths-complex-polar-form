# Introduction to Polar Form

Every complex number can be expressed in two equivalent ways:

1. **Rectangular form** (also called Cartesian form): $z = x + iy$, where $x$ and $y$ are the real and imaginary parts
2. **Polar form** (also called trigonometric form): $z = r(\cos \varphi + i \sin \varphi)$, where $r$ is the modulus and $\varphi$ is the argument

The polar form expresses a complex number using its distance from the origin ($r$) and its angle from the positive real axis ($\varphi$).

# The Polar Form Formula

For a complex number $z = x + iy$, the polar form is:

$$
z = r(\cos \varphi + i \sin \varphi)
$$

where:
- $r = |z| = \sqrt{x^2 + y^2}$ is the modulus (the distance from the origin to $z$)
- $\varphi = \arg(z)$ is the argument (the angle from the positive real axis)

An alternative notation using Euler's formula is:

$$
z = r e^{i\varphi}
$$

# Relationship to Rectangular Form

The connection between rectangular and polar forms comes from the definitions of sine and cosine:

$$
\cos \varphi = \frac{x}{r} \quad \text{and} \quad \sin \varphi = \frac{y}{r}
$$

Rearranging:

$$
x = r \cos \varphi \quad \text{and} \quad y = r \sin \varphi
$$

This means:

$$
z = x + iy = r \cos \varphi + ir \sin \varphi = r(\cos \varphi + i \sin \varphi)
$$

## Converting from Rectangular to Polar

Given $z = x + iy$, to find the polar form:

1. Compute the modulus: $r = \sqrt{x^2 + y^2}$
2. Compute the argument: $\varphi = \arctan(y/x)$ (with quadrant adjustments)
3. Write: $z = r(\cos \varphi + i \sin \varphi)$

![Diagram showing a complex number with both rectangular and polar representations](resources/polar-form-diagram.png)

## Converting from Polar to Rectangular

Given $z = r(\cos \varphi + i \sin \varphi)$, to find the rectangular form:

1. Compute $x = r \cos \varphi$
2. Compute $y = r \sin \varphi$
3. Write: $z = x + iy$

# Examples in All Quadrants

Here are examples of conversions in each quadrant:

![Conversions between rectangular and polar forms for complex numbers in all four quadrants](resources/polar-form-conversions.png)

# Why Use Polar Form?

The polar form is particularly useful for:

- **Multiplication and division**: Polar forms multiply and divide more easily than rectangular forms.
- **Powers and roots**: Raising a complex number to a power or finding roots is much simpler using De Moivre's theorem, which applies to polar form.
- **Geometric interpretation**: The polar form immediately shows the size ($r$) and direction ($\varphi$) of a complex number, making geometric operations intuitive.
- **Exponential notation**: The form $z = r e^{i\varphi}$ connects complex numbers to exponentials, which is fundamental in many areas of mathematics and engineering.

Both rectangular and polar forms represent the same complex number; choosing which to use depends on the task at hand.
