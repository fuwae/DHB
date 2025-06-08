import pandas as pd
from datetime import datetime

# 月の平均日運動量（度/日）
moon_daily_motion = 13.1764

# 基準日：2025-06-15（仮の黄経）
moon_base_date = datetime(2025, 6, 15)
moon_base_longitude = 280.0  # ←例：しし座10度

# 補間データ：±45日を3日刻み
dates = pd.date_range(start="2025-05-01", end="2025-07-31", freq='3D')
data = []

for date in dates:
    days_diff = (date - moon_base_date).days
    lon = moon_base_longitude + moon_daily_motion * days_diff
lon = lon % 360
if lon < 0:
    lon += 360

    data.append({
        'date': date.strftime("%Y-%m-%d"),
        'moon': round(lon, 3)
    })

# CSVとして保存！
df = pd.DataFrame(data)
df.to_csv("moon_sample_2025.csv", index=False)

print("🌙 moon_sample_2025.csv を保存したよ！")
