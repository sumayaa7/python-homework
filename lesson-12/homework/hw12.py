#Exercise1
import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Worker function for each thread
def check_primes(start, end, result_list):
    for num in range(start, end + 1):
        if is_prime(num):
            result_list.append(num)

if __name__ == "__main__":
    # Range to check
    start_range = 1
    end_range = 100
    num_threads = 4
    threads = []
    primes = []

    # Divide the work among threads
    step = (end_range - start_range + 1) // num_threads
    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1
        if i == num_threads - 1:  # last thread gets the rest
            end = end_range
        t = threading.Thread(target=check_primes, args=(start, end, primes))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Prime numbers:", sorted(primes))



import threading
from collections import Counter
from pathlib import Path

def count_words_in_lines(lines):
    counter = Counter()
    for line in lines:
        words = line.strip().split()
        counter.update(word.lower().strip(",.!?") for word in words)
    return counter

def worker(lines, counter, lock):
    local_counter = count_words_in_lines(lines)
    with lock:
        counter.update(local_counter)

def threaded_word_count(file_path: str, num_threads: int = 4):
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with p.open("r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = len(lines) if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(
            target=worker,
            args=(lines[start_idx:end_idx], counter, lock)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter

if __name__ == "__main__":
    # Make sure big_text.txt exists in the same folder
    result = threaded_word_count("big_text.txt", num_threads=4)
    print("Word counts:", result.most_common(10))

