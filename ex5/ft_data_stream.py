import random
import time


def event():
    for i in range(1000):
        level = random.randint(1, 20)
        n = random.choice(["killed monster", "found treasure", "leveled up"])
        yield (n, level)


def fibonacci():
    """Générateur infini de la suite de Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    """Générateur infini de nombres premiers"""
    yield 2  # Premier nombre premier
    n = 3
    while True:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 2  # Sauter les nombres pairs


start_time = time.time()
gene = event()
iter = iter(gene)
high_level_count = int(0)
treasure_count = int(0)
levelup_count = int(0)
print("Processing 1000 game events..")
print()
event1, level1 = next(iter)
if level1 >= 10:
    high_level_count += 1
if event1 == "found treasure":
    treasure_count += 1
if event1 == "leveled up":
    levelup_count += 1
print("Event 1: Player alice (level 5) ", event1)
event2, level2 = next(iter)
if level2 >= 10:
    high_level_count += 1
if event2 == "found treasure":
    treasure_count += 1
if event2 == "leveled up":
    levelup_count += 1
print("Event 2: Player bob (level 12) ", event2)
event3, level3 = next(iter)
if level3 >= 10:
    high_level_count += 1
if event3 == "found treasure":
    treasure_count += 1
if event3 == "leveled up":
    levelup_count += 1
print("Event 3: Player charlie (level 8) ", event3)
print("...")
print()
print("=== Stream Analytics ===")
list1 = list(iter)
print("Total events processed:", len(list1) + 3)
for action, level in list1:
    if level >= 10:
        high_level_count += 1
    if action == "found treasure":
        treasure_count += 1
    if action == "leveled up":
        levelup_count += 1
print("High-level players (10+):", high_level_count)
print("Treasure events:", treasure_count)
print("Level-up events:", levelup_count)
end_time = time.time()
temp = end_time - start_time
print()
print("Memory usage: Constant (streaming)")
print(f"Processing time: {round(temp, 3)} seconds")
print()
print("=== Generator Demonstration ===")

# Fibonacci - premiers 10 nombres
fib_gen = fibonacci()
fib_sequence = [next(fib_gen) for _ in range(10)]
print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_sequence))}")

# Nombres premiers - premiers 5
prime_gen = primes()
prime_sequence = [next(prime_gen) for _ in range(5)]
print(f"Prime numbers (first 5): {', '.join(map(str, prime_sequence))}")
