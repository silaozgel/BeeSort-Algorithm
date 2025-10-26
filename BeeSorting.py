import random
import time

def bee_sort(arr, num_scouts=5, patch_size=10, iterations=5):
    n = len(arr)
    arr = arr.copy()
    for _ in range(iterations):
        patches = []
        for _ in range(num_scouts):
            start = random.randint(0, max(0, n - patch_size))
            patch = arr[start:start + patch_size]
            quality = sum(patch) / len(patch)
            patches.append((quality, start, patch))
        patches.sort(key=lambda x: x[0])
        best_patches = patches[:max(1, num_scouts // 2)]
        for _, start, patch in best_patches:
            sorted_patch = sorted(patch)
            arr[start:start + patch_size] = sorted_patch
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def benchmark(sort_func, data):
    start = time.time()
    sort_func(data)
    end = time.time()
    return end - start

def print_ascii_chart(sizes, bee_times, quick_times):
    print("\nBeeSort vs QuickSort Time Comparison (ASCII Chart):\n")
    max_bar_length = 50
    max_time = max(max(bee_times), max(quick_times))
    for i in range(len(sizes)):
        bee_len = int((bee_times[i] / max_time) * max_bar_length)
        quick_len = int((quick_times[i] / max_time) * max_bar_length)
        print(f"Input Size: {sizes[i]}")
        print(f"  BeeSort   : {'#' * bee_len:<50} ({bee_times[i]:.6f} s)")
        print(f"  QuickSort : {'#' * quick_len:<50} ({quick_times[i]:.6f} s)\n")

try:
    user_input = input("Enter input sizes separated by commas (e.g. 10,100,1000): ")
    sizes = [int(x.strip()) for x in user_input.split(",")]
except:
    print("Invalid input. Using default sizes: 10, 100, 1000")
    sizes = [10, 100, 1000]

bee_times = []
quick_times = []

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]
    bee_times.append(benchmark(bee_sort, data))
    quick_times.append(benchmark(sorted, data))

print_ascii_chart(sizes, bee_times, quick_times)
