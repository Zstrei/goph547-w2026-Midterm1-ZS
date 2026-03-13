"""
Part 2 - Vector operations and curvilinear coordinates
Full NumPy solution with derivations included in comments and printed output.

This script covers:
(a) Gravitational field g = -∇U in Cartesian coordinates
(b1) Divergence of g for points far from the mass using Cartesian derivatives
(b2) Total gravitational flux through a spherical surface enclosing the mass
(c) Unit vector in the latitudinal direction i_theta

NOTE: The derivations required for the assignment are written in the comments
so that the logical steps are clearly documented.

NOTE: Questions requiring written components are written at the bottom under final answers, headed explanation
ASSUMPTIONS

-----------
1. The mass M is sufficiently far from the field point that the potential is:
       U = -GM/r
2. The Cartesian coordinates are related to the spherical coordinates by:
       x = r cos(theta) cos(phi)
       y = r cos(theta) sin(phi)
       z = r sin(theta)
   where theta is latitude and phi is longitude.
3. The radial distance is:
       r = sqrt(x^2 + y^2 + z^2)
4. The radial unit vector is:
       r_hat = <x, y, z> / r
5. For part (b1), the field point is far from the mass, so r > 0 and rho = 0.
6. For part (b2), the spherical surface encloses the mass M at the centre.
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

    R_flux = 75.0e6          # m

    # -----------------------------------------------------------------
    # PART (a)
    # -----------------------------------------------------------------
    #
    # Given:
    #   U = -GM/r
    # where
    #   r = sqrt(x^2 + y^2 + z^2)
    #
    # We need:
    #   g = -∇U
    #
    # First take the partial derivatives of U:
    #
    #   ∂U/∂x = -GM * ∂(1/r)/∂x
    #         = -GM * (-x/r^3)
    #         = GMx/r^3
    #
    #   ∂U/∂y = GMy/r^3
    #   ∂U/∂z = GMz/r^3
    #
    # Therefore:
    #
    #   gx = -∂U/∂x = -GMx/r^3
    #   gy = -∂U/∂y = -GMy/r^3
    #   gz = -∂U/∂z = -GMz/r^3
    #
    # So:
    #
    #   g = <-GMx/r^3, -GMy/r^3, -GMz/r^3>
    # -----------------------------------------------------------------

    r = np.sqrt(x**2 + y**2 + z**2)

    gx = -G * M * x / r**3
    gy = -G * M * y / r**3
    gz = -G * M * z / r**3

    g = np.array([gx, gy, gz])

    g_mag = np.linalg.norm(g)
    r_hat = np.array([x, y, z]) / r
    g_r = np.dot(g, r_hat)

   
    # -----------------------------------------------------------------
    # Part B
    # NOTE: Part (b) is split into two sections for clarity:
    #   (b1) Computes the divergence of the gravitational field using the Cartesian
    #      definition of the ∇ operator for points far from the mass where rho = 0,
    #      showing that div(g) = 0 for r > 0. This is required as stated in the first part of the question.
    #
    #   (b2) Uses Poisson's equation (div(g) = -4*pi*G*rho) together with the
    #      Divergence Theorem to compute the total gravitational flux through
    #      a closed spherical surface that encloses the mass M.  
    #
    # PART (b1)
    # -----------------------------------------------------------------
    #
    # For points far from the mass:
    #   g = <-GMx/r^3, -GMy/r^3, -GMz/r^3>
    #
    # The Cartesian divergence is:
    #
    #   div(g) = ∂gx/∂x + ∂gy/∂y + ∂gz/∂z
    #
    # Compute each derivative using the product rule:
    #
    #   ∂/∂x (x/r^3)
    #   = ∂/∂x (x r^-3)
    #   = r^-3 + x(-3r^-4)(∂r/∂x)
    #   = 1/r^3 - 3x^2/r^5
    #
    # Therefore:
    #
    #   ∂gx/∂x = -GM(1/r^3 - 3x^2/r^5)
    #   ∂gy/∂y = -GM(1/r^3 - 3y^2/r^5)
    #   ∂gz/∂z = -GM(1/r^3 - 3z^2/r^5)
    #
    # Adding:
    #
    #   div(g) = -GM[3/r^3 - 3(x^2+y^2+z^2)/r^5]
    #
    # Since:
    #
    #   x^2 + y^2 + z^2 = r^2
    #
    # then:
    #
    #   div(g) = -GM[3/r^3 - 3r^2/r^5]
    #          = -GM[3/r^3 - 3/r^3]
    #          = 0
    #
    # Hence:
    #
    #   div(g) = 0   for r > 0
    # -----------------------------------------------------------------

    d_gx_dx = -G * M * (1.0 / r**3 - 3.0 * x**2 / r**5)
    d_gy_dy = -G * M * (1.0 / r**3 - 3.0 * y**2 / r**5)
    d_gz_dz = -G * M * (1.0 / r**3 - 3.0 * z**2 / r**5)

    div_g_far = d_gx_dx + d_gy_dy + d_gz_dz

    # -----------------------------------------------------------------
    # PART (b2)
    # -----------------------------------------------------------------
    #
    # For gravity in general:
    #
    #   div(g) = -4*pi*G*rho(x,y,z)
    #
    # By the Divergence Theorem:
    #
    #   ∬_S g · n dS = ∭_V div(g) dV
    #
    # Substituting Poisson's equation:
    #
    #   ∬_S g · n dS = ∭_V [-4*pi*G*rho(x,y,z)] dV
    #
    # Factor out constants:
    #
    #   ∬_S g · n dS = -4*pi*G ∭_V rho(x,y,z) dV
    #
    # But:
    #
    #   ∭_V rho(x,y,z) dV = M
    #
    # Therefore:
    #
    #   ∬_S g · n dS = -4*pi*G*M
    # -----------------------------------------------------------------

    flux = -4.0 * np.pi * G * M

    # Independent check using the field on a sphere:
    #
    # On r = R_flux:
    #   |g| = GM/R_flux^2
    #
    # The field points inward, while the outward normal points outward, so:
    #
    #   g · n = -GM/R_flux^2
    #
    # Surface area of a sphere:
    #
    #   A = 4*pi*R_flux^2
    #
    # Hence:
    #
    #   flux = (g·n)A
    #        = (-GM/R_flux^2)(4*pi*R_flux^2)
    #        = -4*pi*G*M

    flux_check = (-G * M / R_flux**2) * (4.0 * np.pi * R_flux**2)

    # -----------------------------------------------------------------
    # PART (c) 
    # -----------------------------------------------------------------
    #
    # Position vector:
    #
    #   a = <r cos(theta) cos(phi), r cos(theta) sin(phi), r sin(theta)>
    #
    # Differentiate with respect to theta:
    #
    #   ∂a/∂theta =
    #   <-r sin(theta) cos(phi), -r sin(theta) sin(phi), r cos(theta)>
    #
    # Magnitude:
    #
    #   |∂a/∂theta|
    #   = r * sqrt[sin^2(theta)cos^2(phi) + sin^2(theta)sin^2(phi) + cos^2(theta)]
    #   = r * sqrt[sin^2(theta)(cos^2(phi)+sin^2(phi)) + cos^2(theta)]
    #   = r * sqrt[sin^2(theta) + cos^2(theta)]
    #   = r
    #
    # Therefore the latitudinal unit vector is:
    #
    #   i_theta = (1/r) ∂a/∂theta
    #           = <-sin(theta)cos(phi), -sin(theta)sin(phi), cos(theta)>
    #
    # Convert to Cartesian form:
    #
    #   sin(theta) = z/r
    #   cos(theta) = sqrt(x^2+y^2)/r
    #   cos(phi)   = x/sqrt(x^2+y^2)
    #   sin(phi)   = y/sqrt(x^2+y^2)
    #
    # Hence:
    #
    #   i_theta = <-zx/(r*sqrt(x^2+y^2)),
    #              -zy/(r*sqrt(x^2+y^2)),
    #               sqrt(x^2+y^2)/r>
    # -----------------------------------------------------------------

    rho_cyl = np.sqrt(x**2 + y**2)

    i_theta = np.array([
        -z * x / (r * rho_cyl),
        -z * y / (r * rho_cyl),
        rho_cyl / r
    ])

    i_theta_mag = np.linalg.norm(i_theta)


    # -----------------------------------------------------------------
    # PRINT SOLUTIONS
    # -----------------------------------------------------------------
    print("=" * 80)
    print("PART II - VECTOR OPERATIONS AND CURVILINEAR COORDINATES")
    print("=" * 80)

    print("\nGIVEN VALUES")
    print("-" * 80)
    print(f"G = {G:.8e} m^3 kg^-1 s^-2")
    print(f"M = {M:.8e} kg")
    print(f"x = {x:.8e} m")
    print(f"y = {y:.8e} m")
    print(f"z = {z:.8e} m")
    print(f"R_flux = {R_flux:.8e} m")

    # ======================== PART (a) ========================
    print("\n" + "=" * 80)
    print("PART (a)")
    print("=" * 80)

    print("\nPotential:")
    print("U = -GM/r")
    print("r = sqrt(x^2 + y^2 + z^2)")

    print("\nGravitational field:")
    print("g = -∇U")
    print("gx = -GMx/r^3")
    print("gy = -GMy/r^3")
    print("gz = -GMz/r^3")

    print(f"\nr = {r:.8e} m")
    print(f"gx = {gx:.8e} m/s^2")
    print(f"gy = {gy:.8e} m/s^2")
    print(f"gz = {gz:.8e} m/s^2")

    print(f"\ng = <{gx:.8e}, {gy:.8e}, {gz:.8e}> m/s^2")
    print(f"|g| = {g_mag:.8e} m/s^2")

    print("\nRadial unit vector:")
    print(f"r_hat = <{r_hat[0]:.8e}, {r_hat[1]:.8e}, {r_hat[2]:.8e}>")

    print("\nRadial component:")
    print(f"g_r = {g_r:.8e} m/s^2")

    # ======================== PART (b1) ========================
    print("\n" + "=" * 80)
    print("PART (b1) - DIVERGENCE FAR FROM THE MASS")
    print("=" * 80)

    print("\nUsing:")
    print("gx = -GMx/r^3")
    print("gy = -GMy/r^3")
    print("gz = -GMz/r^3")

    print("\nCartesian derivative terms:")
    print("∂gx/∂x = -GM(1/r^3 - 3x^2/r^5)")
    print("∂gy/∂y = -GM(1/r^3 - 3y^2/r^5)")
    print("∂gz/∂z = -GM(1/r^3 - 3z^2/r^5)")

    print("\nNumerical values at the given point:")
    print(f"∂gx/∂x = {d_gx_dx:.8e} s^-2")
    print(f"∂gy/∂y = {d_gy_dy:.8e} s^-2")
    print(f"∂gz/∂z = {d_gz_dz:.8e} s^-2")

    print("\nDivergence:")
    print("div(g) = ∂gx/∂x + ∂gy/∂y + ∂gz/∂z")
    print(f"div(g) = {div_g_far:.8e} s^-2")

    print("\nTherefore, for r > 0:")
    print("div(g) = 0")

    # ======================== PART (b2) ========================
    print("\n" + "=" * 80)
    print("PART (b2) - TOTAL FLUX THROUGH A SPHERE ENCLOSING M")
    print("=" * 80)

    print("\nUse the Divergence Theorem:")
    print("∬_S g · n dS = ∭_V div(g) dV")

    print("\nUse Poisson's equation for gravity:")
    print("div(g) = -4*pi*G*rho(x,y,z)")

    print("\nSubstitute into the volume integral:")
    print("∬_S g · n dS = ∭_V [-4*pi*G*rho(x,y,z)] dV")

    print("\nFactor out constants:")
    print("∬_S g · n dS = -4*pi*G ∭_V rho(x,y,z) dV")

    print("\nRecognize that:")
    print("∭_V rho(x,y,z) dV = M")

    print("\nTherefore:")
    print("∬_S g · n dS = -4*pi*G*M")

    print(f"\nFlux = {flux:.8e} m^3/s^2")
    print(f"Flux check = {flux_check:.8e} m^3/s^2")

    # ======================== PART (c) ========================
    print("\n" + "=" * 80)
    print("PART (c)")
    print("=" * 80)

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

    print(f"\ni_theta = <{i_theta[0]:.8e}, {i_theta[1]:.8e}, {i_theta[2]:.8e}>")
    print(f"|i_theta| = {i_theta_mag:.8e}")

   
    # ======================== FINAL ANSWERS ========================
    print("\n" + "=" * 80)
    print("FINAL ANSWERS")
    print("=" * 80)

    print("\n(a)")
    print(f"g = <{gx:.8e}, {gy:.8e}, {gz:.8e}> m/s^2")
    print(f"|g| = {g_mag:.8e} m/s^2")
    print(f"g_r = {g_r:.8e} m/s^2")

    print("\n(b1)")
    print("div(g) = 0 for r > 0")

    print("\n(b2)")
    print(f"∬_S g · n dS = {flux:.8e} m^3/s^2")

    print("\n(c)")
    print(f"i_theta = <{i_theta[0]:.8e}, {i_theta[1]:.8e}, {i_theta[2]:.8e}>")


if __name__ == "__main__":
    main()