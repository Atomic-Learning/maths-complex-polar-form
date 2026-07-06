#!/usr/bin/env python3
"""
Generate a diagram showing conversions between rectangular and polar forms in all quadrants.
Outputs to polar-form-conversions.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 12), dpi=150)
fig.suptitle('Converting Between Rectangular and Polar Forms', fontsize=14, fontweight='bold', y=0.995)

# Define example complex numbers
examples = [
    (3, 2, '3 + 2i', 0),          # Q1
    (-2.5, 2, '-2.5 + 2i', 1),    # Q2
    (-2, -2.5, '-2 - 2.5i', 2),   # Q3
    (2.5, -1.5, '2.5 - 1.5i', 3), # Q4
]

for real, imag, label, ax_idx in examples:
    ax = axes[ax_idx // 2, ax_idx % 2]
    ax.set_aspect('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.axhline(y=0, color='k', linewidth=1.5)
    ax.axvline(x=0, color='k', linewidth=1.5)
    
    # Axis labels
    ax.set_xlabel('Re', fontsize=10, fontweight='bold')
    ax.set_ylabel('Im', fontsize=10, fontweight='bold')
    ax.tick_params(labelsize=9)
    
    # Compute polar form
    r = np.sqrt(real**2 + imag**2)
    phi = np.arctan2(imag, real)
    phi_deg = np.degrees(phi)
    
    # Draw radius line
    ax.plot([0, real], [0, imag], 'r-', linewidth=2.5)
    ax.plot(real, imag, 'ro', markersize=8)
    
    # Draw angle arc
    arc_angles = np.linspace(0, phi, 50)
    arc_r = 0.7
    ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 'b--', linewidth=2)
    ax.text(0.85, 0.15, r'$\varphi$', fontsize=11, color='blue', fontweight='bold')
    
    # Draw rectangular components
    ax.plot([real, real], [0, imag], 'g--', linewidth=1.5, alpha=0.6)
    ax.plot([0, real], [0, 0], 'orange', linestyle='--', linewidth=1.5, alpha=0.6)
    
    # Rectangular form box
    rect_text = f'Rectangular:\n$z = {real} + {imag:.1f}i$'
    ax.text(0.02, 0.98, rect_text, transform=ax.transAxes, fontsize=10, fontweight='bold',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
            family='monospace')
    
    # Polar form box
    polar_text = f'Polar:\n$r = {r:.2f}$\n$\\varphi = {phi_deg:.1f}°$'
    ax.text(0.02, 0.65, polar_text, transform=ax.transAxes, fontsize=10, fontweight='bold',
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
            family='monospace')
    
    # Full polar form
    polar_full = f'$z = {r:.2f}(\\cos {phi_deg:.1f}° + i \\sin {phi_deg:.1f}°)$'
    ax.text(0.5, -0.08, polar_full, transform=ax.transAxes, fontsize=9, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # Set ticks
    ax.set_xticks([-4, -2, 0, 2, 4])
    ax.set_yticks([-4, -2, 0, 2, 4])

plt.tight_layout()
plt.savefig('polar-form-conversions.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: polar-form-conversions.png")
plt.close()
