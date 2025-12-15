import math

def bell_crank_solver_official_method():
    print("=" * 70)
    print("  BELL CRANK MOMENT CALCULATOR – OFFICIAL TEXTBOOK METHOD")
    print("  (Uses your exact steps: P resolved at 28° to arm, OA at 45°)")
    print("=" * 70)
    print()

    # ------------------- USER INPUT -------------------
    P_mag = float(input("Magnitude of force P (N)                 : ") or 250)
    angle_P_to_arm = float(input("Angle of force P from arm OA (degrees)   : ") or 28)
    L_OA_mm = float(input("Length OA (mm)                           : ") or 280)
    angle_OA_from_horizontal = float(input("Angle of arm OA from horizontal (degrees): ") or 45)

    # Convert length to meters for consistency (optional, but clean)
    L_OA = L_OA_mm / 1000.0  # now in meters

    # ------------------- STEP 1: Resolve force P (as per your method) -------------------
    # You said: P = 250 sin(28°) i + 250 cos(28°) j
    # This means: the force is at 28° to the ARM, and the arm is at 45° to horizontal
    # So the force components are relative to the ARM direction, not horizontal!

    rad_28 = math.radians(angle_P_to_arm)

    Px = P_mag * math.sin(rad_28)   # i-component (horizontal)
    Py = P_mag * math.cos(rad_28)   # j-component (vertical)

    print(f"\nForce components (relative to arm):")
    print(f"   Px = {Px:.2f} N (horizontal)")
    print(f"   Py = {Py:.2f} N (vertical)")
    print(f"   → P = ({Px:.2f} i + {Py:.2f} j) N")

    # ------------------- STEP 2: Position vector r_OA -------------------
    rad_OA = math.radians(angle_OA_from_horizontal)
    rx = L_OA * math.cos(rad_OA)
    ry = L_OA * math.sin(rad_OA)

    print(f"\nPosition vector from O to A:")
    print(f"   r = {rx*1000:.1f} i + {ry*1000:.1f} j mm")
    print(f"     = ({rx:.4f} i + {ry:.4f} j) m")

    # ------------------- STEP 3: Moment M_O = r × F (determinant method) -------------------
    # 2D cross product: M = rx * Py - ry * Px   (k direction)
    M_Nm = rx * Py - ry * Px

    # ------------------- STEP 4: Perpendicular distance d = |M| / P -------------------
    d_m = abs(M_Nm) / P_mag
    d_mm = d_m * 1000

    # Direction
    direction = "Counterclockwise" if M_Nm > 0 else "Clockwise"

    # ------------------- FINAL RESULTS -------------------
    print("\n" + "="*70)
    print("                    OFFICIAL RESULTS")
    print("="*70)
    print(f"Moment about O (M_O)     : {M_Nm:.3f} N·m")
    print(f"                         → {direction} (+k)")
    print(f"                         = {M_Nm:.3f} N·m ")
    print()
    print(f"Perpendicular distance d : {d_mm:.1f} mm")
    print("="*70)

# =============================================================================
if __name__ == "__main__":
    bell_crank_solver_official_method()