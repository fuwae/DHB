
import os
import pandas as pd
from datetime import datetime

# 🌟 天体名のリスト（ファイル名とカラム識別に使用）
PLANET_LIST = [
    'sun', 'moon', 'mercury', 'venus', 'mars',
    'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'
]

# 🌠 サイドリアル→トロピカル変換（簡易歳差補正）
def approximate_precession(year: int) -> float:
    return 0.01397 * (year - 2000)

def convert_sidereal_to_tropical(sidereal_longitude: float, year: int) -> float:
    return sidereal_longitude - approximate_precession(year)

def zodiac_wrap(degree: float) -> tuple[str, float]:
    zodiac_signs = ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']
    sign_index = int(degree // 30) % 12
    degree_in_sign = degree % 30
    return zodiac_signs[sign_index], degree_in_sign

# 📁 入力フォルダと出力ファイル設定
INPUT_DIR = "./ephemeris_project"
OUTPUT_PATH = "./tropical_ephemeris_2025.csv"

def extract_data_block(filepath):
    """$SOE〜$EOE間の行だけ抽出し、parts[0]=日付, parts[2]=度数"""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_data = False
    results = []
    for line in lines:
        if '$$SOE' in line:
            in_data = True
            continue
        if '$$EOE' in line:
            break
        if in_data:
            parts = line.strip().split()
            if len(parts) >= 3:
                date_str = f"{parts[0]} {parts[1]}"
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%b-%d %H:%M")
                    deg = float(parts[2])
                    results.append((date_obj.strftime("%Y-%m-%d"), deg))
                except:
                    continue
    return results

# 🚀 メイン処理：10ファイル統合

def merge_ephemeris_to_csv():
    planet_data = {}
    date_index = None

    for planet in PLANET_LIST:
        filename = f"{planet}_2025.txt"
        path = os.path.join(INPUT_DIR, filename)
        rows = extract_data_block(path)

        # トロピカル変換＋DataFrame化
        df = pd.DataFrame(rows, columns=["date", planet])
        df[planet] = df[planet].apply(lambda x: round(convert_sidereal_to_tropical(x, 2025), 6))

        signs[planet], deg_in_signs[planet] = zip(*df[planet].apply(zodiac_wrap))

        if date_index is None:
            date_index = df["date"]
        planet_data[planet] = df[planet].values

    df_out = pd.DataFrame({"date": date_index})
    for planet in PLANET_LIST:
        df_out[planet] = planet_data[planet]

    df_out.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ 統合トロピカルCSV出力完了: {OUTPUT_PATH}")


if __name__ == '__main__':
    merge_ephemeris_to_csv()

    df_out = pd.DataFrame({"date": date_index})
for planet in PLANET_LIST:
    df_out[f"{planet}"] = planet_data[planet]                     # トロピカル度数
    df_out[f"{planet}_sign"] = signs[planet]                     # 星座記号
    df_out[f"{planet}_deg_in_sign"] = deg_in_signs[planet]       # 星座内度数
