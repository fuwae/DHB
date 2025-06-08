# 📘 DHB補間仕様（太陽・月・惑星対応）

def interpolate_degree(A: float, B: float, T: float) -> float:
    return A + (B - A) * (T / 24)

def zodiac_wrap(degree: float) -> tuple[str, float]:
    zodiac_signs = ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']
    sign_index = int(degree // 30) % 12
    degree_in_sign = degree % 30
    return zodiac_signs[sign_index], round(degree_in_sign, 2)

def motion_flag(A: float, B: float) -> str:
    delta = B - A
    if abs(delta) < 0.01:
        return 'S'
    elif delta < 0:
        return 'R'
    else:
        return 'D'

retrograde_periods = {
    'Mercury': [
        ('2025-05-15', '2025-06-03'),
        ('2025-08-05', '2025-08-28')
    ],
    # 他惑星も追記できるよ
}

def is_in_retrograde(planet: str, date_str: str) -> bool:
    for start, end in retrograde_periods.get(planet, []):
        if start <= date_str <= end:
            return True
    return False

def approximate_precession(year: int) -> float:
    return 0.01397 * (year - 2000)

def convert_sidereal_to_tropical(sidereal_longitude: float, year: int) -> float:
    return sidereal_longitude - approximate_precession(year)

def interpolate_with_status(planet: str, A: float, B: float, T: float, date_str: str, year: int) -> dict:
    A_trop = convert_sidereal_to_tropical(A, year)
    B_trop = convert_sidereal_to_tropical(B, year)

    if B_trop < A_trop:
        B_trop += 30

    raw = interpolate_degree(A_trop, B_trop, T)
    corrected = raw if raw < 360 else raw - 360

    sign, deg = zodiac_wrap(corrected)

    flag = motion_flag(A, B)
    if is_in_retrograde(planet, date_str):
        flag = 'R'

    return {
        'degree': corrected,
        'sign': sign,
        'deg_in_sign': deg,
        'motion': flag
    }
