result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Значення a менше ніж b.")
        if b > 100:
            raise IndexError("Значення b більше ніж 100.")
        return a / b
    except (ValueError, IndexError):
        print(f"Помилка")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except:
        print(f"Помилка при обробці")

print(result)