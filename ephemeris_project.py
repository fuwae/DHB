# ephemeris_cleaner.py

input_file = "horizons_results.txt"
output_file = "cleaned_ephemeris.csv"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("date,sidereal_deg\n")

    in_data = False
    for line in f_in:
        if "$$SOE" in line:
            in_data = True
            continue
        if "$$EOE" in line:
            break
        if in_data:
            parts = line.strip().split()
            if len(parts) >= 3:
                date = f"{parts[0]} {parts[1]}"      # 例: 2025-Jun-01 00:00
                deg = parts[2]                       # ← ここが黄経！！
                f_out.write(f"{date},{deg}\n")
