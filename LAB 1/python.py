# Recursive and Iterative Computation Analyzer

def analyze_recursive_iterative(n):
    def fact_rec(x):
        if x == 0:
            return 1
        return x * fact_rec(x - 1)

    def fib_rec(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        return fib_rec(x - 1) + fib_rec(x - 2)

    # Calculate values
    rf = fact_rec(n)

    it = 1
    for i in range(1, n  + 1):
        it *= i

    rfb = fib_rec(n)

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    ifb = a

    # Required output 
    return [
        "Computation Analysis Report",
        f"Recursive Factorial: {rf}",
        f"Iterative Factorial: {it}",
        f"Recursive Fibonacci: {rfb}",
        f"Iterative Fibonacci: {ifb}",
        "Operation Count Comparison",
        f"Recursive Factorial Count: {n + 1}",
        f"Iterative Factorial Count: {n}",
        f"Recursive Fibonacci Count: {fib_rec_count(n)}",
        f"Iterative Fibonacci Count: {n}"
    ]
  
  
def fib_rec_count(n):
    if n <= 1:
        return 1       
    return 1 + fib_rec_count(n - 1) + fib_rec_count(n - 2)

#--------------------------------------------------------------------------------------------------#

# Linear Search and Binary Search Comparison
def compare_search_algorithms(arr, target):
    # Linear Search implementation 
    lin_index = -1
    lin_comps = 0
    for i in range(len(arr)):
        lin_comps += 1
        if arr[i] == target:
            lin_index = i
            break 

    # Binary Search implementation 
    bin_index = -1
    bin_comps = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        bin_comps += 1
        if arr[mid] == target:
            bin_index = mid 
            # Continue searching on the left side to find the first occurence 
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Determine better algorithm
    if lin_comps < bin_comps:
        better = "Linear Search"
    elif bin_comps < lin_comps:
        better = "Binary Search"
    else:
        better = "Both Equal"
          
    # Return output format as a list of strings
    return [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {lin_index}",
        f"Comparisons: {lin_comps}",
        "Binary Search",
        f"Index: {bin_index}",
        f"Comparisons: {bin_comps}",
        f"Better Algorithm: {better}"
    ]

#--------------------------------------------------------------------------------------------------#    

#  Bubble Sort and Insertion Sort Performance Comparison

def compare_bubble_insertion(random_data, sorted_data, reverse_data):
    # Helper functions nested to ensure they run within the single provided function block
    def bubble_sort(arr):
        n = len(arr)
        res = list(arr)
        comparisons = 0 
        swaps = 0

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparisons += 1
                if res[j] > res[j + 1]:
                    res[j], res[j + 1] = res[j + 1], res[j]
                    swaps += 1
                    swapped = True
            # Optimized Bubble Sort: stop early if no swap occurs
            if not swapped:
                break 

        return res, comparisons, swaps

    def insertion_sort(arr):
        n = len(arr)
        res = list(arr)
        comparisons = 0
        shifts = 0

        for i in range(1, n):
            key = res[i]
            j = i - 1
            # Count a comparison whenever an existing element is compared with the key 
            while j >= 0:
                comparisons += 1
                if res[j] > key:
                    res[j + 1] = res[j]
                    shifts += 1
                    j -= 1
                else:
                    break 
            res[j + 1] = key

        return res, comparisons, shifts

    output = ["Sorting Performance Report"]

    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data)
    ]

    for name, arr in datasets:
        output.append(name)

        # Bubble Sort execution 
        b_sorted, b_comps, b_swaps = bubble_sort(arr)
        output.append(f"Bubble Sorted: {' '.join(map(str, b_sorted))}")
        output.append(f"Bubble Comparisons: {b_comps}")
        output.append(f"Bubble Swaps: {b_swaps}")

        # Insertion Sort execution 
        i_sorted, i_comps, i_shifts = insertion_sort(arr)
        output.append(f"Insertion Sorted: {' '.join(map(str, i_sorted))}")
        output.append(f"Insertion Comparisons: {i_comps}")
        output.append(f"Insertion Shifts: {i_shifts}")

        # Comparison logic
        if b_comps < i_comps:
            better = "Bubble Sort"
        elif i_comps < b_comps:
            better = "Insertion Sort"
        else:
            better = "Both Equal"
        
        output.append(f"Better Algorithm: {better}")
      
    return output

#--------------------------------------------------------------------------------------------------#    

# Algorithm Execution Observation Table

import math

def generate_execution_observation_table(sizes):
    def count_recursive_fib(n):
        if n <= 1:
            return 1
        calls = [0] * (n + 1)
        calls[0] = 1
        calls[1] = 1
        for i in range(2, n + 1):
            calls[i] = calls[i - 1] + calls[i - 2] + 1
        return calls[n]

    result = []
    
    # Header title line
    result.append("Algorithm Execution Observation Table")
    
    # Column names header line
    result.append(
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci "
        "IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    )
    
    # Table data rows
    for n in sizes:
        rec_factorial = n + 1
        iter_factorial = n
        rec_fibonacci = count_recursive_fib(n)
        iter_fibonacci = n
        linear_search = n
        binary_search = math.floor(math.log2(n)) + 1 if n > 0 else 0
        bubble_sort = n * (n - 1) // 2
        insertion_sort = n * (n - 1) // 2
        
        row_str = f"{n} {rec_factorial} {iter_factorial} {rec_fibonacci} {iter_fibonacci} {linear_search} {binary_search} {bubble_sort} {insertion_sort}"
        result.append(row_str)
        
    return result


#--------------------------------------------------------------------------------------------------#

# Runtime and Complexity Comparison Table

import math

def generate_runtime_complexity_table(n):
    n2_count = n * (n - 1) // 2
    log_count = int(math.log2(n)) + 1
    
    print(
        "Runtime Complexity Comparison\n"
        "Method ObservedCount ExpectedComplexity Observation\n"
        f"Linear Search {n} O(n) Grows linearly\n"
        f"Binary Search {log_count} O(log n) Grows logarithmically\n"
        f"Bubble Sort {n2_count} O(n^2) Grows quadratically\n"
        f"Insertion Sort {n2_count} O(n^2) Grows quadratically"
    )
    
    return []

#--------------------------------------------------------------------------------------------------#

# Runtime Comparison Chart Data and Scalability Report
import math

def generate_runtime_chart_report(sizes):
    print("Runtime Comparison Chart Data\nInputSize LinearSearch BinarySearch BubbleSort InsertionSort")
    
    for n in sizes:
        n2 = n * (n - 1) // 2
        print(f"{n} {n} {int(math.log2(n)) + 1} {n2} {n2}")
        
    print(
        "Scalability Summary\n"
        "Algorithm Complexity Scalability\n"
        "Linear Search O(n) Moderate\n"
        "Binary Search O(log n) Excellent\n"
        "Bubble Sort O(n^2) Poor\n"
        "Insertion Sort O(n^2) Poor\n"
        "Key Observations\n"
        "Best Algorithm: Binary Search\n"
        "Most Expensive Algorithm: Bubble Sort\n"
        "Conclusion: Logarithmic algorithms scale better for large inputs"
    )
    
    return []
 
#--------------------------------------------------------------------------------------------------#   
