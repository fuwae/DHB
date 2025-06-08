import pandas as pd

# 太陽：planet_sample_2025.csv から読む
df_sun = pd.read_csv("planet_sample_2025.csv")

# 月：moon_sample_2025.csv から読む
df_moon = pd.read_csv("moon_sample_2025.csv")

target_date = "2025-06-05"

# 🌙 月の値を探す（近似日対応あり）
moon_row = df_moon[df_moon["date"] == target_date]

if moon_row.empty:
    df_moon["days_diff"] = pd.to_datetime(df_moon["date"]) - pd.to_datetime(target_date)
    df_moon["abs_days"] = df_moon["days_diff"].abs()
    nearest_row = df_moon.loc[df_moon["abs_days"].idxmin()]
    moon_deg = nearest_row["moon"]
else:
    moon_deg = moon_row["moon"].values[0]

# 🌞 太陽の値はストレートに取得
sun_row = df_sun[df_sun["date"] == target_date]
sun_deg = sun_row["sun"].values[0]

# サイン変換関数
def get_zodiac_sign(degree):
    signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    index = int(degree // 30)
    sign_degree = degree % 30
    return signs[index], round(sign_degree, 2)

# 出力
sun_sign, sun_pos = get_zodiac_sign(sun_deg)
moon_sign, moon_pos = get_zodiac_sign(moon_deg)

print(f"🌞 {target_date} の太陽は {sun_sign} {sun_pos:.2f}°")
print(f"🌙 {target_date} の月は   {moon_sign} {moon_pos:.2f}°")
