"""
Gravitational field assignment solution using NumPy only.

This script covers:
(a) Gravitational field g = -∇U in Cartesian coordinates
(b) Divergence of g for r > 0, and total gravitational flux through a sphere
(c) Unit vector in the latitudinal direction i_theta

ASSUMPTIONS
-----------
1. The mass M is spherically symmetric, so for points outside the mass:
       U = -GM/r
2. The field point is away from the origin, so r > 0 and derivatives are defined.
3. The coordinate definitions are:
       x = r cos(theta) cos(phi)
       y = r cos(theta) sin(phi)
       z = r sin(theta)
   so theta is latitude measured from the equatorial plane.
4. The radial unit vector is:
       r_hat = <x, y, z> / r
5. The radial component of g is:
       g_r = g · r_hat
6. For the flux calculation, the spherical surface is centered on the mass M.
7. Inside the mass, Gauss' law for gravity is used:
       div(g) = -4*pi*G*rho
   and for the full enclosed mass:
       flux = ∬ g·n dS = -4*pi*G*M

NOTES
-----
- NumPy is used for all numerical calculations.
- The derivation steps required for full marks are documented in the comments
  and echoed in the printed output.
"""

import numpy as np


def main():
    # -----------------------------------------------------------------
    # GIVEN CONSTANTS AND COORDINATES
    # -----------------------------------------------------------------
    G = 6.67430e-11          # m^3 kg^-1 s^-2
    M = 8.681e25             # kg

    x = 55.0e6               # m
    y = 55.0e6               # m
    z = 32.5e6               # m

    R_flux = 75.0e6          # radius for flux sphere, m

    # -----------------------------------------------------------------
    # PART (a): GRAVITATIONAL FIELD g = -∇U
    # -----------------------------------------------------------------
    #
    # Potential:
    #   U = -GM/r
    # where
    #   r = sqrt(x^2 + y^2 + z^2)
    #
    # To get g = -∇U, use the Cartesian derivatives:
    #
    #   ∂U/∂x = -GM * ∂(1/r)/∂x
    #         = -GM * (-x/r^3)
    #         = GMx/r^3
    #
    # Therefore:
    #   gx = -∂U/∂x = -GMx/r^3
    #   gy = -∂U/∂y = -GMy/r^3
    #   gz = -∂U/∂z = -GMz/r^3
    #
    # So:
    #   g = <-GMx/r^3, -GMy/r^3, -GMz/r^3>
    # -----------------------------------------------------------------

    r = np.sqrt(x**2 + y**2 + z**2)

    gx = -G * M * x / r**3
    gy = -G * M * y / r**3
    gz = -G * M * z / r**3

    g = np.array([gx, gy, gz])

    # Magnitude of g
    g_mag = np.linalg.norm(g)

    # Radial unit vector
    r_hat = np.array([x, y, z]) / r

    # Radial component
    g_r = np.dot(g, r_hat)

    # -----------------------------------------------------------------
    # PART (b): DIVERGENCE OF g AND TOTAL FLUX
    # -----------------------------------------------------------------
    #
    # Using:
    #   gx = -GMx/r^3
    #   gy = -GMy/r^3
    #   gz = -GMz/r^3
    #
    # The Cartesian divergence is:
    #   div(g) = ∂gx/∂x + ∂gy/∂y + ∂gz/∂z
    #
    # Work each term out:
    #
    #   ∂/∂x (x/r^3) = 1/r^3 + x * ∂(r^-3)/∂x
    #                = 1/r^3 + x * (-3r^-4)(∂r/∂x)
    #                = 1/r^3 - 3x^2/r^5
    #
    # Therefore:
    #   ∂gx/∂x = -GM(1/r^3 - 3x^2/r^5)
    #   ∂gy/∂y = -GM(1/r^3 - 3y^2/r^5)
    #   ∂gz/∂z = -GM(1/r^3 - 3z^2/r^5)
    #
    # Adding:
    #   div(g) = -GM[3/r^3 - 3(x^2+y^2+z^2)/r^5]
    #
    # Since:
    #   x^2+y^2+z^2 = r^2
    #
    # then:
    #   div(g) = -GM[3/r^3 - 3r^2/r^5]
    #          = -GM[3/r^3 - 3/r^3]
    #          = 0
    #
    # Hence for r > 0:
    #   div(g) = 0
    #
    # Total gravitational flux through a sphere enclosing mass M:
    #   ∬ g·n dS = -4*pi*G*M
    # -----------------------------------------------------------------

    d_gx_dx = -G * M * (1.0 / r**3 - 3.0 * x**2 / r**5)
    d_gy_dy = -G * M * (1.0 / r**3 - 3.0 * y**2 / r**5)
    d_gz_dz = -G * M * (1.0 / r**3 - 3.0 * z**2 / r**5)

    div_g = d_gx_dx + d_gy_dy + d_gz_dz

    flux = -4.0 * np.pi * G * M

    # Optional independent check using field on a sphere of radius R_flux:
    # On a sphere centered at the mass:
    #   |g| = GM/R^2
    # and g is inward while outward normal is outward, so:
    #   g·n = -GM/R^2
    # Then:
    #   flux = (-GM/R^2)(4*pi*R^2) = -4*pi*GM
    flux_check = (-G * M / R_flux**2) * (4.0 * np.pi * R_flux**2)

    # -----------------------------------------------------------------
    # PART (c): UNIT VECTOR IN THE LATITUDINAL DIRECTION i_theta
    # -----------------------------------------------------------------
    #
    # Given:
    #   x = r cos(theta) cos(phi)
    #   y = r cos(theta) sin(phi)
    #   z = r sin(theta)
    #
    # Position vector:
    #   a = <r cos(theta) cos(phi), r cos(theta) sin(phi), r sin(theta)>
    #
    # Differentiate with respect to theta:
    #   ∂a/∂theta =
    #   <-r sin(theta) cos(phi), -r sin(theta) sin(phi), r cos(theta)>
    #
    # Magnitude:
    #   |∂a/∂theta|
    #   = r * sqrt[sin^2(theta)cos^2(phi) + sin^2(theta)sin^2(phi) + cos^2(theta)]
    #   = r * sqrt[sin^2(theta)(cos^2(phi)+sin^2(phi)) + cos^2(theta)]
    #   = r * sqrt[sin^2(theta) + cos^2(theta)]
    #   = r
    #
    # Therefore the unit vector in the latitudinal direction is:
    #   i_theta = (1/r) ∂a/∂theta
    #           = <-sin(theta)cos(phi), -sin(theta)sin(phi), cos(theta)>
    #
    # Convert to Cartesian form:
    #   sin(theta) = z/r
    #   cos(theta) = sqrt(x^2+y^2)/r
    #   cos(phi)   = x/sqrt(x^2+y^2)
    #   sin(phi)   = y/sqrt(x^2+y^2)
    #
    # Hence:
    #   i_theta = <-zx/(r*sqrt(x^2+y^2)),
    #              -zy/(r*sqrt(x^2+y^2)),
    #               sqrt(x^2+y^2)/r>
    # -----------------------------------------------------------------

    rho = np.sqrt(x**2 + y**2)  # distance from z-axis

    i_theta = np.array([
        -z * x / (r * rho),
        -z * y / (r * rho),
        rho / r
    ])

    i_theta_mag = np.linalg.norm(i_theta)

    # -----------------------------------------------------------------
    # PRINT FULL WORKING
    # -----------------------------------------------------------------
    print("=" * 78)
    print("GRAVITATIONAL FIELD ASSIGNMENT SOLUTION (NUMPY ONLY)")
    print("=" * 78)

    print("\nGIVEN VALUES")
    print("-" * 78)
    print(f"G = {G:.8e} m^3 kg^-1 s^-2")
    print(f"M = {M:.8e} kg")
    print(f"x = {x:.8e} m")
    print(f"y = {y:.8e} m")
    print(f"z = {z:.8e} m")
    print(f"Sphere radius for flux = {R_flux:.8e} m")

    # ------------------------ PART (a) ------------------------
    print("\n" + "=" * 78)
    print("PART (a): GRAVITATIONAL FIELD g = -∇U")
    print("=" * 78)

    print("\nPotential:")
    print("U = -GM/r")
    print("where r = sqrt(x^2 + y^2 + z^2)")

    print("\nDerived Cartesian field components:")
    print("gx = -GMx/r^3")
    print("gy = -GMy/r^3")
    print("gz = -GMz/r^3")

    print("\nStep 1: Calculate radial distance")
    print(f"r = {r:.8e} m")

    print("\nStep 2: Calculate Cartesian components of g")
    print(f"gx = {gx:.8e} m/s^2")
    print(f"gy = {gy:.8e} m/s^2")
    print(f"gz = {gz:.8e} m/s^2")

    print("\nVector form:")
    print(f"g = <{gx:.8e}, {gy:.8e}, {gz:.8e}> m/s^2")

    print("\nStep 3: Magnitude of g")
    print("|g| = sqrt(gx^2 + gy^2 + gz^2)")
    print(f"|g| = {g_mag:.8e} m/s^2")

    print("\nStep 4: Radial unit vector")
    print("r_hat = <x, y, z> / r")
    print(f"r_hat = <{r_hat[0]:.8e}, {r_hat[1]:.8e}, {r_hat[2]:.8e}>")

    print("\nStep 5: Radial component")
    print("g_r = g · r_hat")
    print(f"g_r = {g_r:.8e} m/s^2")

    # ------------------------ PART (b) ------------------------
    print("\n" + "=" * 78)
    print("PART (b): DIVERGENCE AND TOTAL GRAVITATIONAL FLUX")
    print("=" * 78)

    print("\nUsing:")
    print("gx = -GMx/r^3")
    print("gy = -GMy/r^3")
    print("gz = -GMz/r^3")

    print("\nCartesian derivative terms:")
    print("∂gx/∂x = -GM(1/r^3 - 3x^2/r^5)")
    print("∂gy/∂y = -GM(1/r^3 - 3y^2/r^5)")
    print("∂gz/∂z = -GM(1/r^3 - 3z^2/r^5)")

    print("\nNumerical values of those terms at the given point:")
    print(f"∂gx/∂x = {d_gx_dx:.8e} s^-2")
    print(f"∂gy/∂y = {d_gy_dy:.8e} s^-2")
    print(f"∂gz/∂z = {d_gz_dz:.8e} s^-2")

    print("\nDivergence:")
    print("div(g) = ∂gx/∂x + ∂gy/∂y + ∂gz/∂z")
    print(f"div(g) = {div_g:.8e} s^-2")

    print("\nThis is numerically zero (up to floating-point rounding),")
    print("so for r > 0:")
    print("div(g) = 0")

    print("\nInside the mass, Gauss' law for gravity gives:")
    print("div(g) = -4*pi*G*rho")

    print("\nTotal flux through a spherical surface enclosing the mass:")
    print("Flux = ∬ g·n dS = -4*pi*G*M")
    print(f"Flux = {flux:.8e} m^3/s^2")

    print("\nCheck using field-on-a-sphere formula:")
    print(f"Flux check = {flux_check:.8e} m^3/s^2")

    # ------------------------ PART (c) ------------------------
    print("\n" + "=" * 78)
    print("PART (c): UNIT VECTOR IN THE LATITUDINAL DIRECTION i_theta")
    print("=" * 78)

    print("\nFrom the position vector:")
    print("a = <r cos(theta) cos(phi), r cos(theta) sin(phi), r sin(theta)>")

    print("\nDifferentiate with respect to theta:")
    print("∂a/∂theta = <-r sin(theta) cos(phi), -r sin(theta) sin(phi), r cos(theta)>")

    print("\nMagnitude:")
    print("|∂a/∂theta| = r")

    print("\nTherefore:")
    print("i_theta = <-sin(theta)cos(phi), -sin(theta)sin(phi), cos(theta)>")

    print("\nCartesian form:")
    print("i_theta = <-zx/(r*sqrt(x^2+y^2)), -zy/(r*sqrt(x^2+y^2)), sqrt(x^2+y^2)/r>")

    print("\nNumerical value at the given point:")
    print(f"(i_theta)_x = {i_theta[0]:.8e}")
    print(f"(i_theta)_y = {i_theta[1]:.8e}")
    print(f"(i_theta)_z = {i_theta[2]:.8e}")

    print("\nVector form:")
    print(f"i_theta = <{i_theta[0]:.8e}, {i_theta[1]:.8e}, {i_theta[2]:.8e}>")

    print("\nCheck that i_theta is a unit vector:")
    print(f"|i_theta| = {i_theta_mag:.8e}")

    # ------------------------ FINAL SUMMARY ------------------------
    print("\n" + "=" * 78)
    print("FINAL ANSWERS")
    print("=" * 78)

    print("\n(a) Gravitational field:")
    print("g = <-GMx/r^3, -GMy/r^3, -GMz/r^3>")
    print(f"g = <{gx:.8e}, {gy:.8e}, {gz:.8e}> m/s^2")
    print(f"|g| = {g_mag:.8e} m/s^2")
    print(f"g_r = {g_r:.8e} m/s^2")

    print("\n(b) Divergence and flux:")
    print("div(g) = 0 for r > 0")
    print(f"Flux through sphere of radius 75.0×10^6 m = {flux:.8e} m^3/s^2")

    print("\n(c) Latitudinal unit vector:")
    print("i_theta = <-sin(theta)cos(phi), -sin(theta)sin(phi), cos(theta)>")
    print(f"i_theta = <{i_theta[0]:.8e}, {i_theta[1]:.8e}, {i_theta[2]:.8e}>")


if __name__ == "__main__":
    main()