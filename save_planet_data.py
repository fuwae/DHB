import pandas as pd
from datetime import datetime

# 平均日運動量（簡略版）
mean_daily_motion = {
    'sun': 0.9856,
    'moon': 13.1764,
    'mercury': 1.607,
    'venus': 1.174,
    'mars': 0.524,
    'jupiter': 0.083,
    'saturn': 0.033,
    'uranus': 0.0119,
    'neptune': 0.0061,
    'pluto': 0.0036
}

# 2025年6月15日基準（仮の黄経）
base_longitudes = {
    'sun': 84.0,
    'moon': 280.0,
    'mercury': 110.0,
    'venus': 190.0,
    'mars': 320.0,
    'jupiter': 20.0,
    'saturn': 330.0,
    'uranus': 50.0,
    'neptune': 360.0,
    'pluto': 280.0
}

dates = pd.date_range(start="2025-05-16", end="2025-07-15", freq='D')
data = []

for date in dates:
    days_diff = (date - datetime(2025, 6, 15)).days
    row = {'date': date.strftime("%Y-%m-%d")}
    for planet, base_lon in base_longitudes.items():
        motion = mean_daily_motion[planet]
        lon = (base_lon + motion * days_diff) % 360
        row[planet] = round(lon, 3)
    data.append(row)

df = pd.DataFrame(data)
df.to_csv("planet_sample_2025.csv", index=False)

print("✅ 保存完了：planet_sample_2025.csv")
