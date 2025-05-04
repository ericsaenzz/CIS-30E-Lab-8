# CIS-30E-Lab-8
# Instructions 
Demonstrate your understanding of Python optimization techniques, memory management, and performance tuning. The task will require you to write a Python program that incorporates these concepts, helping you optimize both memory usage and execution speed.

You will create a program that processes a large list of numbers and performs the following tasks:

Efficiently calculates the sum of the numbers using an optimized approach.
Uses memory-efficient data structures to store the numbers.
Benchmarks and optimizes performance using profiling and memory management techniques.
Assignment Instructions (Steps):
Create a Python File:

Create a Python file named optimize_memory_performance.py.
Implement Memory Management:

Generate a list of one million random numbers.
Use a generator to iterate over the list (instead of storing all the numbers in memory).
Use sys.getsizeof() to check and print the memory usage of the list and the generator.
Implement Performance Optimization:

Write a function that calculates the sum of the numbers.
Benchmark the performance using timeit and compare the performance of using a list versus a generator for the sum calculation.
Memory Profiling:

Use gc.collect() to force garbage collection and print the memory usage after collecting garbage.
Use Profiling Tools:

Use cProfile to profile the function and print a report on the time spent in each function call during the summing process.