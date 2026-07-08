For a complex number $z = x + iy$, the polar form is:

$$
z = r(\cos \phi + i \sin \phi)
$$

where:

- $r = |z| = \sqrt{x^2 + y^2}$ is the modulus (the distance from the origin to $z$)
- $\phi = \arg(z)$ is the argument (the angle from the positive real axis)

It can be shown that this can also be expressed using Euler's formula:

$$
z = re^{i\phi}
$$

The above is a common and compact way to represent complex numbers in polar form.

# Relationship to Rectangular Form

The connection between rectangular and polar forms comes from considering a right-angled triangle formed by the real and imaginary parts of the complex number on the complex plane. The sides of the triangle are $x$ (the real part) and $y$ (the imaginary part), and the hypotenuse is $r$ (the modulus). The angle $\phi$ is the argument of the complex number. 

![Diagram showing a complex number with both rectangular and polar representations](resources/polar-form-diagram.png)

$$
\cos \phi = \frac{x}{r}\label{eq:cos_phi}\\
\sin \phi = \frac{y}{r}\label{eq:sin_phi}
$$

Rearranging:

$$
x = r \cos \phi\label{eq:x}\\
y = r \sin \phi\label{eq:y}
$$

This means:

$$
z = x + iy = r \cos \phi + ir \sin \phi = r(\cos \phi + i \sin \phi) \label{eq:z}
$$

The visualisation of this relationship as a right-angled triangle only works cleanly in the first quadrant (positive $x$ and $y$). For other quadrants, the angle $\phi$ must be adjusted accordingly in Equations \ref{eq:cos_phi} and \ref{eq:sin_phi}. However, the relationships in Equations \ref{eq:x}, \ref{eq:y} and \ref{eq:z} hold for all quadrants with no adjustments, and the polar form is valid for all complex numbers.

# Why Use Polar Form?

The polar form is particularly useful for:

- **Multiplication and division**: Polar forms multiply and divide more easily than rectangular forms.
- **Powers and roots**: Raising a complex number to a power or finding roots is much simpler using De Moivre's theorem, which applies to polar form.
- **Geometric interpretation**: The polar form immediately shows the size ($r$) and direction ($\phi$) of a complex number, making geometric operations intuitive.
- **Exponential notation**: The form $z = r e^{i\phi}$ connects complex numbers to exponentials, which is fundamental in many areas of mathematics and engineering.

Both rectangular and polar forms represent the same complex number; choosing which to use depends on the task at hand.
