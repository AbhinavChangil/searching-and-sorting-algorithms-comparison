import time
import random
import tkinter as tk
from tkinter import ttk
def counting_algorithm(arr):
    # Example counting algorithm
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    result = []
    for i in range(len(counts)):
        result.extend([i] * counts[i])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def linear_search_unordered(arr):
    target=random.choice(data)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

class HashTable:
    def init(self):
        self.dict['table'] = {}

    def insert(self, key, value):
        self.dict['table'][key] = value

    def search(self, key):
        return self.dict['table'].get(key, None)

def binary_search(arr):
    target = target=random.choice(data)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(algorithm, *args, **kwargs):
    start_time = time.time()
    algorithm(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# Generate random data for testing
data_sizes = [20000]
random_data = {size: random.sample(range(size * 10), size) for size in data_sizes}




# Compare and print the time taken by each algorithm for each data size
for size in data_sizes:
    print(f"\nData Size: {size}")
    data = random_data[size]





import sys
import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

class AlgorithmComparisonApp:
    def __init__(self, master):
        self.master = master
        master.title('Algorithm Performance Comparison')
        master.geometry('600x400')

        self.algorithm1_label = Label(master, text='Algorithm 1:')
        self.algorithm1_combobox = ttk.Combobox(master, values=['counting_algorithm', 'insertion_sort', 'selection_sort', 'quick_sort', 'linear_search_unordered', 'binary_search'])
        self.algorithm1_combobox.set('counting_algorithm')

        self.algorithm2_label = Label(master, text='Algorithm 2:')
        self.algorithm2_combobox = ttk.Combobox(master, values=['counting_algorithm', 'insertion_sort', 'selection_sort', 'quick_sort', 'linear_search_unordered', 'binary_search'])
        self.algorithm2_combobox.set('insertion_sort')

        self.run_button = Button(master, text='Run Comparison', command=self.run_comparison)

        self.results_label = Label(master, text='Results:')
        self.results_text = Text(master)

        self.algorithm1_label.pack()
        self.algorithm1_combobox.pack()
        self.algorithm2_label.pack()
        self.algorithm2_combobox.pack()
        self.run_button.pack()
        self.results_label.pack()
        self.results_text.pack()

        self.fastest_label = Label(master, text='Fastest Algorithm:')
        self.fastest_text = Text(master, height=2, state=tk.DISABLED)

        self.algorithm1_label.pack()
        self.algorithm1_combobox.pack()
        self.algorithm2_label.pack()
        self.algorithm2_combobox.pack()
        self.run_button.pack()
        self.results_label.pack()
        self.results_text.pack()
        self.fastest_label.pack()
        self.fastest_text.pack()

    def run_comparison(self):
        algorithm1_name = self.algorithm1_combobox.get().strip()
        algorithm2_name = self.algorithm2_combobox.get().strip()

        if not algorithm1_name or not algorithm2_name:
            self.show_error('Error', 'Please enter names for both algorithms.')
            return

        algorithm1 = globals().get(algorithm1_name)
        algorithm2 = globals().get(algorithm2_name)

        if not algorithm1 or not algorithm2:
            self.show_error('Error', 'One or both of the specified algorithms are not defined.')
            return

        self.results_text.delete(1.0, tk.END)
        for size in [20000]:
            result = f"\nData Size: {size}\n"
            data = random.sample(range(size * 10), size)

            algorithm1_time = measure_time(algorithm1, data.copy())
            result += f"{algorithm1_name} Time: {algorithm1_time:.6f} seconds\n"

            algorithm2_time = measure_time(algorithm2, data.copy())
            result += f"{algorithm2_name} Time: {algorithm2_time:.6f} seconds\n"

            
            if(algorithm1_time<algorithm2_time):
                result += f"\n{algorithm1_name}\n"
            else:
                result += f"\n{algorithm2_name}\n"

            self.results_text.insert(tk.END, result)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

if __name__ == '__main__':
    root = tk.Tk()
    app = AlgorithmComparisonApp(root)
    root.mainloop()