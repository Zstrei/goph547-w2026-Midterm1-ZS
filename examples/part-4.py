"""
Part 4 - Theoretical gravity / rotating frame

This script solves parts (a), (b), and (c) of the problem using NumPy.

NOTE: The derivations required for the assignment are written in the comments
so that the logical steps are clearly documented.

NOTE: Questions requiring written components are written at the bottom under final answers, headed explanation.

PARTS
-----
(a) Derive the theoretical radial gravity expression using the equation
    of motion in a rotating reference frame.
(b) Use the ellipsoid radius r(theta) ≈ a_e(1 − f sin²θ) to compute
    theoretical gravity at latitude 25.05°N.
(c) Use the International Gravity Formula (IGF) from the course notes (GRAVP7)
    (Equation 6) to estimate gravity at the same latitude and compare.

ASSUMPTIONS
-----------
1. Earth is approximated as a rotating oblate ellipsoid.
2. Gravity is approximated by a central field GM/r².
3. The rotating frame introduces centrifugal acceleration.
4. Latitude θ is measured from the equator.
"""

import numpy as np


def main():

    # ------------------------------------------------------------------
    # GIVEN CONSTANTS
    # ------------------------------------------------------------------

    G = 6.67430e-11             # gravitational constant (m^3 kg^-1 s^-2)
    M = 5.9722e24               # mass of Earth (kg)

    a_e = 6378137.0             # equatorial radius (m)
    f = 1 / 298.257             # flattening factor

    latitude_deg = 25.05        # degrees N
    longitude_deg = -77.36      # degrees W (not used in this axisymmetric model)

    rotation_period_hours = 23.93

    theta = np.deg2rad(latitude_deg)

    # ------------------------------------------------------------------
    # PART (a) – DERIVE RADIAL GRAVITY IN ROTATING FRAME
    # ------------------------------------------------------------------
    #
    # In a rotating reference frame the effective acceleration includes:
    #
    #   gravitational acceleration
    #   centrifugal acceleration
    #
    # The gravitational acceleration magnitude is
    #
    #   g_grav = GM / r²
    #
    # directed toward the Earth's center.
    #
    # The centrifugal acceleration magnitude is
    #
    #   a_cf = ω² s
    #
    # where
    #
    #   s = distance to the rotation axis
    #
    # At latitude θ:
    #
    #   s = r cosθ
    #
    # therefore
    #
    #   a_cf = ω² r cosθ
    #
    # This acceleration is horizontal relative to the axis,
    # so we take the radial component:
    #
    #   a_cf,rad = a_cf cosθ
    #            = ω² r cos²θ
    #
    # Therefore the effective radial gravity is
    #
    #   g_rad(θ) = GM/r² − ω² r cos²θ
    #
    # ------------------------------------------------------------------

    T = rotation_period_hours * 3600
    omega = 2 * np.pi / T

    # ------------------------------------------------------------------
    # PART (b) – COMPUTE THEORETICAL GRAVITY AT LATITUDE
    # ------------------------------------------------------------------
    #
    # The ellipsoid radius varies with latitude:
    #
    #   r(θ) ≈ a_e (1 − f sin²θ)
    #
    # Substitute this into the expression derived in part (a).
    #

    r_theta = a_e * (1 - f * np.sin(theta) ** 2)

    g_grav = G * M / r_theta ** 2

    a_cf_rad = omega ** 2 * r_theta * np.cos(theta) ** 2

    g_rad = g_grav - a_cf_rad

    # ------------------------------------------------------------------
    # PART (c) – INTERNATIONAL GRAVITY FORMULA (IGF)
    # ------------------------------------------------------------------
    #
    # Use Equation (6) from the notes:
    #
    # g_t(θ) = 9.780327 [1 + 0.0053024 sin²θ − 0.0000058 sin²(2θ)]
    #
    # where θ is latitude and g_t is in m/s².
    #

    g_igf = 9.780327 * (
        1
        + 0.0053024 * np.sin(theta) ** 2
        - 0.0000058 * np.sin(2 * theta) ** 2
    )

    difference = g_rad - g_igf
    difference_mgal = difference * 1e5

    # ------------------------------------------------------------------
    # PRINT RESULTS
    # ------------------------------------------------------------------

    print("=" * 70)
    print("PART 4 THEORETICAL GRAVITY / ROTATING FRAME")
    print("=" * 70)

    print("\nGiven values")
    print("-" * 70)
    print(f"Latitude = {latitude_deg:.2f} deg")
    print(f"a_e = {a_e:.2f} m")
    print(f"flattening f = {f:.8f}")
    print(f"rotation period = {rotation_period_hours:.2f} hours")

    print("\n" + "=" * 70)
    print("PART (a) RESULT")
    print("=" * 70)

    print("Derived radial gravity expression:")
    print("g_rad(theta) = GM/r^2 − ω^2 r cos^2(theta)")

    print("\n" + "=" * 70)
    print("PART (b) NUMERICAL RESULT")
    print("=" * 70)

    print(f"r(theta) = {r_theta:.6e} m")
    print(f"gravitational term = {g_grav:.8e} m/s^2")
    print(f"centrifugal term = {a_cf_rad:.8e} m/s^2")

    print(f"\nTheoretical gravity (rotating-frame model) = {g_rad:.8f} m/s^2")

    print("\n" + "=" * 70)
    print("PART (c) IGF RESULT")
    print("=" * 70)

    print("IGF formula used:")
    print("g_t(theta) = 9.780327[1 + 0.0053024 sin^2(theta) − 0.0000058 sin^2(2theta)]")

    print(f"\nIGF gravity = {g_igf:.8f} m/s^2")

    print("\nDifference between models:")
    print(f"{difference:.8e} m/s^2")
    print(f"{difference_mgal:.4f} mGal")

    print("\nExplanation:")
    print("The gravity expression derived in part (a) assumes a simplified "
    "Earth model where gravity is approximated by a central field GM/r^2 and only "
    "the radial component of centrifugal acceleration is included, using the "
    "approximate ellipsoid radius r(theta) ≈ a_e(1 − f sin^2θ). The International "
    "Gravity Formula (IGF), however, is an empirical normal-gravity model derived "
    "from geodetic observations and incorporates a more accurate representation "
    "of the Earth's reference ellipsoid and latitude dependence of gravity. "
    "Because the IGF accounts for the Earth's true mass distribution and uses "
    "parameters fitted to measurements, it produces a slightly different gravity "
    "value than the simplified rotating-frame model."
)
    


if __name__ == "__main__":
    main()