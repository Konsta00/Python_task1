import random

N = int(input("Syötä arvottavien pisteiden määrä: "))
n = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        n += 1

estimated_pi = 4 * n / N
print(f"Pi likiarvo: {estimated_pi}")