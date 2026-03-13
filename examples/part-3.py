"""
Midterm Part 3 solution.

This script covers:
(a) Derive the flux integral over the closed hemispherical surface S
(b) Compute the numerical value of the flux
(c) Compute the equivalent surface density on S
(d) Compute the vertical gravity effect g_z(x, y) on the plane z = 0,
    plot it on a grid, estimate total mass using the excess-mass formula,
    and compare with the true total mass

NOTE: The derivations required for the assignment are written in the comments
so that the logical steps are clearly documented.

NOTE: Questions requiring written components are written at the bottom under final answers, headed explanation

ASSUMPTIONS
-----------
1. The surface S is CLOSED and consists of:
      - the curved hemispherical surface below z = 0
      - the flat circular disk in the plane z = 0
2. All three point masses lie inside this closed surface.
3. Gravity obeys Gauss's law:
      ∬_S g · n dS = -4πG M_enclosed
4. In part (d), the point-mass vertical gravity at observation point (x, y, 0)
   due to a source mass m at (x0, y0, z0) is obtained from Newton's law:
      g(r) = -Gm (r - r0) / |r - r0|^3
   so its z-component at z = 0 is:
      g_z(x, y) = Gm z0 / [(x-x0)^2 + (y-y0)^2 + z0^2]^(3/2)
   Since the masses are below the plane, z0 < 0, so g_z is negative.
5. For the excess-mass estimate over the plane:
      M_total = -(1 / (2πG)) ∬ g_z(x, y) dA
   The minus sign is needed because g_z is negative for buried positive masses.
6. The numerical area integral is approximated with the trapezoidal rule.
"""

import numpy as np
import matplotlib.pyplot as plt


def gz_point_mass(x, y, m, x0, y0, z0, G):
    """
    Vertical gravity effect at (x, y, 0) from a point mass m at (x0, y0, z0).

    DERIVATION
    ----------
    Observation point:
        r = (x, y, 0)

    Source point:
        r0 = (x0, y0, z0)

    Vector from source to observation:
        R = r - r0 = (x-x0, y-y0, -z0)

    Newtonian gravity vector:
        g = -Gm R / |R|^3

    Therefore the z-component is:
        g_z = -Gm(-z0) / |R|^3
            =  Gm z0 / |R|^3

    where
        |R|^2 = (x-x0)^2 + (y-y0)^2 + z0^2

    So:
        g_z(x, y) = Gm z0 / [(x-x0)^2 + (y-y0)^2 + z0^2]^(3/2)

    Since z0 < 0 for a buried mass, g_z is negative.
    """
    R2 = (x - x0) ** 2 + (y - y0) ** 2 + z0 ** 2
    return G * m * z0 / (R2 ** 1.5)


def main():
    # -----------------------------------------------------------------
    # GIVEN VALUES
    # -----------------------------------------------------------------
    G = 6.67430e-11  # m^3 kg^-1 s^-2

    m1 = 8.54e5
    m2 = 3.26e6
    m3 = 5.21e6

    x1 = np.array([76.0, -86.0, -26.0])   # m
    x2 = np.array([-34.0, -26.0, -7.0])   # m
    x3 = np.array([-94.0, 36.0, -10.0])   # m

    r = 270.0  # hemisphere radius, m

    # -----------------------------------------------------------------
    # PART (a): FLUX THROUGH THE CLOSED SURFACE S
    # -----------------------------------------------------------------
    #
    # Gauss's law for gravity:
    #
    #   ∬_S g · n dS = -4πG M_enclosed
    #
    # Since all three masses lie inside the closed surface S:
    #
    #   M_enclosed = m1 + m2 + m3
    #
    # Therefore:
    #
    #   ∬_S g · n dS = -4πG (m1 + m2 + m3)
    #
    # IMPORTANT:
    # The flux depends only on total enclosed mass, not on where the
    # masses are located within the closed surface.
    # -----------------------------------------------------------------

    M_total = m1 + m2 + m3
    flux = -4.0 * np.pi * G * M_total

    # -----------------------------------------------------------------
    # PART (b): NUMERICAL VALUE OF THE FLUX
    # -----------------------------------------------------------------
    #
    # Just substitute numerical values into:
    #
    #   flux = -4πG M_total
    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    # PART (c): EQUIVALENT SURFACE DENSITY
    # -----------------------------------------------------------------
    #
    # The closed surface S consists of:
    #   1. curved hemisphere
    #   2. flat circular disk
    #
    # Hemisphere area:
    #   A_hemi = 2πr^2
    #
    # Disk area:
    #   A_disk = πr^2
    #
    # Total closed-surface area:
    #   A_S = A_hemi + A_disk
    #       = 2πr^2 + πr^2
    #       = 3πr^2
    #
    # If the enclosed mass were spread uniformly over the whole surface S,
    # the equivalent surface density would be:
    #
    #   sigma_eq = M_total / A_S
    #
    # Units:
    #   sigma_eq has units of kg/m^2
    #
    # This is NOT the same as the true volumetric density of the anomalies,
    # which would have units of kg/m^3.
    # -----------------------------------------------------------------

    A_hemi = 2.0 * np.pi * r ** 2
    A_disk = np.pi * r ** 2
    A_S = A_hemi + A_disk

    sigma_eq = M_total / A_S

    # -----------------------------------------------------------------
    # PART (d): VERTICAL GRAVITY EFFECT g_z(x, y) ON z = 0
    # -----------------------------------------------------------------
    #
    # For one point mass m at (x0, y0, z0), the gravity vector is:
    #
    #   g = -Gm (r - r0) / |r - r0|^3
    #
    # At an observation point on the plane z = 0:
    #
    #   r  = (x, y, 0)
    #   r0 = (x0, y0, z0)
    #
    # so
    #
    #   r - r0 = (x-x0, y-y0, -z0)
    #
    # The vertical component is:
    #
    #   g_z(x, y) = -Gm(-z0) / [(x-x0)^2 + (y-y0)^2 + z0^2]^(3/2)
    #             =  Gm z0   / [(x-x0)^2 + (y-y0)^2 + z0^2]^(3/2)
    #
    # Since the masses are below the plane, z0 < 0, so g_z is negative.
    #
    # For three masses:
    #
    #   g_z(x, y) = Σ_i [ G m_i z_i / ((x-x_i)^2 + (y-y_i)^2 + z_i^2)^(3/2) ]
    #
    # We choose a grid wide enough that:
    #
    #   |g_z(edge)| / |g_z,max| < 1%
    #
    # The excess-mass formula is:
    #
    #   M_total = -(1 / (2πG)) ∬ g_z(x, y) dA
    #
    # The minus sign is required because g_z is negative for buried
    # positive masses.
    #
    # We compute the area integral numerically using the trapezoidal rule:
    #
    #   ∬ g_z dA ≈ trapz(trapz(g_z, x), y)
    # -----------------------------------------------------------------

    dx = 5.0
    dy = 5.0

    x_min, x_max = -300.0, 300.0
    y_min, y_max = -300.0, 300.0

    x_vals = np.arange(x_min, x_max + dx, dx)
    y_vals = np.arange(y_min, y_max + dy, dy)

    X, Y = np.meshgrid(x_vals, y_vals)

    gz = np.zeros_like(X, dtype=float)

    masses = [m1, m2, m3]
    positions = [x1, x2, x3]

    for m, pos in zip(masses, positions):
        gz += gz_point_mass(X, Y, m, pos[0], pos[1], pos[2], G)

    # Maximum anomaly magnitude
    gz_abs = np.abs(gz)
    gz_max_abs = np.max(gz_abs)

    # Edge check
    top_edge = gz_abs[0, :]
    bottom_edge = gz_abs[-1, :]
    left_edge = gz_abs[:, 0]
    right_edge = gz_abs[:, -1]

    edge_max = max(
        np.max(top_edge),
        np.max(bottom_edge),
        np.max(left_edge),
        np.max(right_edge)
    )

    edge_percent = 100.0 * edge_max / gz_max_abs

    # Numerical area integral
    integral_gz = np.trapezoid(np.trapezoid(gz, x_vals, axis=1), y_vals, axis=0)

    # Excess-mass estimate
    M_est = -integral_gz / (2.0 * np.pi * G)

    # Error measures
    signed_error = M_est - M_total
    absolute_error = abs(signed_error)
    percent_error = 100.0 * signed_error / M_total

    # -----------------------------------------------------------------
    # FINAL RESULTS WITH DERIVATIONS
    # -----------------------------------------------------------------
    print("=" * 80)
    print("MIDTERM PART 3 SOLUTION")
    print("=" * 80)

    print("\nGIVEN VALUES")
    print("-" * 80)
    print(f"G   = {G:.8e} m^3 kg^-1 s^-2")
    print(f"m1  = {m1:.8e} kg")
    print(f"m2  = {m2:.8e} kg")
    print(f"m3  = {m3:.8e} kg")
    print(f"x1  = {x1} m")
    print(f"x2  = {x2} m")
    print(f"x3  = {x3} m")
    print(f"r   = {r:.2f} m")

    # ---------------------------- PART (a) ----------------------------
    print("\n" + "=" * 80)
    print("PART (a): FLUX INTEGRAL THROUGH S")
    print("=" * 80)

    print("\nGauss's law for gravity:")
    print("    ∬_S g · n dS = -4πG M_enclosed")

    print("\nSince all three masses are inside S:")
    print("    M_enclosed = m1 + m2 + m3")

    print("\nTherefore:")
    print("    ∬_S g · n dS = -4πG (m1 + m2 + m3)")

    print("\nTotal enclosed mass:")
    print(f"    M_total = {M_total:.8e} kg")

    # ---------------------------- PART (b) ----------------------------
    print("\n" + "=" * 80)
    print("PART (b): NUMERICAL VALUE OF THE FLUX")
    print("=" * 80)

    print("\nSubstitute into:")
    print("    Flux = -4πG M_total")

    print(f"\nFlux = {flux:.8e} m^3/s^2")

    # ---------------------------- PART (c) ----------------------------
    print("\n" + "=" * 80)
    print("PART (c): EQUIVALENT SURFACE DENSITY")
    print("=" * 80)

    print("\nSurface S consists of:")
    print("    curved hemisphere + flat circular disk")

    print("\nAreas:")
    print("    A_hemi = 2πr^2")
    print("    A_disk = πr^2")
    print("    A_S    = 3πr^2")

    print(f"\nA_hemi = {A_hemi:.8e} m^2")
    print(f"A_disk = {A_disk:.8e} m^2")
    print(f"A_S    = {A_S:.8e} m^2")

    print("\nEquivalent surface density:")
    print("    sigma_eq = M_total / A_S")

    print(f"\nsigma_eq = {sigma_eq:.8e} kg/m^2")

    print("\nEXPLAINATION:")
    print("The equivalent surface density sigma_eq has units of kg/m^2 " \
    "because it represents the total enclosed mass distributed uniformly over " \
    "the closed surface S. In contrast, the true density of the buried mass anomalies "
    "is a volumetric density with units of kg/m^3. Therefore sigma_eq does not represent " \
    "the physical density of the anomalies; it is only an equivalent average mass per unit area that" \
    " produces the same total enclosed mass when spread over the surface.")

   # ---------------------------- PART (d) ----------------------------
    print("\n" + "=" * 80)
    print("PART (d): VERTICAL GRAVITY EFFECT g_z(x, y)")
    print("=" * 80)

    print("\nFor one point mass m at (x0, y0, z0), observed at (x, y, 0):")
    print("    g_z(x, y) = G m z0 / [(x-x0)^2 + (y-y0)^2 + z0^2]^(3/2)")

    print("\nFor three masses:")
    print("    g_z(x, y) = Σ_i [ G m_i z_i / ((x-x_i)^2 + (y-y_i)^2 + z_i^2)^(3/2) ]")

    print("\nGrid used:")
    print(f"    x from {x_min:.1f} m to {x_max:.1f} m with Δx = {dx:.1f} m")
    print(f"    y from {y_min:.1f} m to {y_max:.1f} m with Δy = {dy:.1f} m")

    print("\nGrid check:")
    print(f"    max |g_z| on grid      = {gz_max_abs:.8e} m/s^2")
    print(f"    max |g_z| on grid edge = {edge_max:.8e} m/s^2")
    print(f"    edge / max × 100       = {edge_percent:.4f} %")

    if edge_percent < 1.0:
        print("    Condition satisfied: edge values are < 1% of the maximum anomaly.")
    else:
        print("    Condition NOT satisfied: enlarge the domain.")

    print("\nExcess-mass formula:")
    print("    M_total = -(1 / (2πG)) ∬ g_z(x, y) dA")

    print("\nNumerical integration method:")
    print("    ∬ g_z dA ≈ trapezoid(trapezoid(g_z, x), y)")

    print(f"\nIntegral of g_z over grid = {integral_gz:.8e} m^3/s^2")
    print(f"Estimated total mass      = {M_est:.8e} kg")
    print(f"Actual total mass         = {M_total:.8e} kg")
    print(f"Signed error              = {signed_error:.8e} kg")
    print(f"Absolute error            = {absolute_error:.8e} kg")
    print(f"Percent error             = {percent_error:.6f} %")

    print("\nEXPLAINATION:")
    print("""
    The vertical gravity effect on the plane z = 0 is given by
    g_z(x,y) = Σ_i [G m_i z_i / ((x-x_i)^2 + (y-y_i)^2 + z_i^2)^(3/2)].

    A grid with Δx = Δy = 5 m was used over the domain -300 m ≤ x ≤ 300 m
    and -300 m ≤ y ≤ 300 m. This domain is wide enough that the anomaly at
    the grid edge is less than 1 percent of the maximum anomaly. The circular
    survey radius required to enclose this region is approximately
    424.26 m from the centre.

    Using the excess-mass formula
    M_hat_total = -(1/(2πG)) ∬ g_z(x,y) dA
    and numerically integrating g_z over the grid gives an estimate of the
    total mass that can be compared with the true total mass
    M_total = m1 + m2 + m3. Any difference between the estimated and true
    mass arises from numerical integration error and the finite grid size.
    """)
    # -----------------------------------------------------------------
    # PLOT
    # -----------------------------------------------------------------
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(X, Y, gz, levels=40)
    plt.colorbar(contour, label=r"$g_z(x,y)$ [m/s$^2$]")
    plt.scatter(
        [x1[0], x2[0], x3[0]],
        [x1[1], x2[1], x3[1]],
        marker="x",
        s=80,
        label="Mass projections"
    )
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Vertical gravity effect $g_z(x,y)$ on z = 0")
    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()