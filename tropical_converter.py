import pandas as pd

def approximate_precession(year):
    return 0.01397 * (year - 2000)

def convert_sidereal_to_tropical(sidereal_deg, year):
    return (sidereal_deg - approximate_precession(year)) % 360

# 読み込み
df = pd.read_csv("cleaned_ephemeris.csv")

df["sidereal_deg"] = df["sidereal_deg"].astype(float)


# 年を抽出（例：2025-Jun-01 → 2025）
df["date_obj"] = pd.to_datetime(df["date"], format="%Y-%b-%d %H:%M")
df["year"] = df["date_obj"].dt.year
df["month"] = df["date_obj"].dt.month
df["day"] = df["date_obj"].dt.day
df["hour"] = df["date_obj"].dt.hour
df["minute"] = df["date_obj"].dt.minute

# トロピカル変換
df["tropical_deg"] = df.apply(lambda row: convert_sidereal_to_tropical(row["sidereal_deg"], row["year"]), axis=1)

# サイン（星座）名と星座内度数を追加（オプション）
def zodiac_wrap(deg):
    signs = ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']
    index = int(deg // 30)
    deg_in_sign = deg % 30
    return pd.Series([signs[index], round(deg_in_sign, 2)])

df[["sign", "deg_in_sign"]] = df["tropical_deg"].apply(zodiac_wrap)

# 書き出し
df.to_csv("tropical_ephemeris.csv", index=False)

print("🌟 トロピカル変換完了！ → tropical_ephemeris.csv ができたよ♡")
