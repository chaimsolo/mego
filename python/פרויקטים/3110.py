scores = {"Moshe": "97", "Benjamin": "83", "Shaul": "77", "Tuvia": "54"}

grades = {}

for name in scores:
    if int(scores[name]) > 90:
        grades[name] = "amazing"
    elif int(scores[name]) > 80:
        grades[name] = "very good"
    elif int(scores[name]) > 70:
        grades[name] = "you can do better"
    else:
        grades[name] = "you didn't pass"
    print(f"{name} {grades[name]}")

