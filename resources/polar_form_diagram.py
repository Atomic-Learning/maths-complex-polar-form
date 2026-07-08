#!/usr/bin/env python3
"""
Generate a diagram showing rectangular and polar forms of a complex number.
Outputs to polar-form-diagram.png in the same directory.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(10, 9), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Add axis labels
ax.set_xlabel('Real Part (Re)', fontsize=18, fontweight='bold')
ax.set_ylabel('Imaginary Part (Im)', fontsize=18, fontweight='bold')
ax.set_title('Polar Form of a Complex Number', fontsize=21, fontweight='bold', pad=20)

# Example: z = 3 + 2i
real, imag = 3, 2
r = np.sqrt(real**2 + imag**2)
phi = np.arctan2(imag, real)

# Draw radius line
ax.plot([0, real], [0, imag], 'r-', linewidth=3)
ax.plot(real, imag, 'ro', markersize=10)

# Draw angle arc
arc_angles = np.linspace(0, phi, 50)
arc_r = 1.0
ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 'b-', linewidth=2.5)
ax.text(1.3, 0.3, r'$\phi$', fontsize=19.5, color='blue', fontweight='bold')

# Draw rectangular components
ax.plot([real, real], [0, imag], 'g--', linewidth=2, alpha=0.7)
ax.plot([0, real], [0, 0], 'orange', linestyle='--', linewidth=2, alpha=0.7)

# Labels for rectangular parts
ax.text(real + 0.3, imag / 2, f'Im = {imag}', fontsize=16.5, fontweight='bold', color='green')
ax.text(real / 2, -0.5, f'Re = {real}', fontsize=16.5, fontweight='bold', color='darkorange')

# Label the point with both forms
box_text = (
    f'Rectangular:\n'
    f'$z = {real} + {imag}i$\n\n'
    f'Polar:\n'
    rf'$z = {r:.2f}(\cos({phi:.3f}) + i \sin({phi:.3f}))$' + '\n\n' +
    rf'Or: $z = {r:.2f} e^{{i \cdot {phi:.3f}}}$'
)
ax.text(0.02, 0.98, box_text, transform=ax.transAxes, fontsize=16.5, fontweight='bold',
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9),
        family='monospace')

# Add formulas
formula_text = (
    r'$r = |z| = \sqrt{\text{Re(z)}^2 + \text{Im(z)}^2}$' + '\n' +
    r'$\phi = \arg(z)$'
)
ax.text(0.02, 0.40, formula_text, transform=ax.transAxes, fontsize=16.5, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# Set ticks
ax.set_xticks([-4, -2, 0, 2, 4])
ax.set_yticks([-4, -2, 0, 2, 4])
ax.tick_params(labelsize=15)

# Label the radius
ax.text(0.2, 1.2, f'r = {r:.2f}', fontsize=16.5, fontweight='bold', color='red')

plt.tight_layout()
plt.savefig('polar-form-diagram.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: polar-form-diagram.png")
plt.close()
