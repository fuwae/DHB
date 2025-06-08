def get_zodiac_sign(longitude):
    signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    index = int(longitude // 30)
    degree = longitude % 30  # ← 修正ポイント
    return signs[index], degree
