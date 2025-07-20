import random
import pandas as pd
from tqdm import tqdm
# Генерируем 100 000 случайных точек
num_tests = 100_000
coordinates = [(random.random() * 9, random.random() * 9) for _ in range(num_tests)]

test_data = [
    (x, y, x + y, x - y)
    for x, y in [(random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(num_tests)]
]

df = pd.DataFrame(
    test_data,
)

# Сохраняем в CSV
file_path = "edu_file.csv"
open(file_path, 'w').close()  # Очищаем файл перед записью
df.to_csv(file_path, index=False, header=False)


