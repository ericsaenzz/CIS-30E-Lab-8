import sys
import pstats
import gc
import random
import timeit
import cProfile
from io import StringIO

#generate a list of a million random numbers
def generate_list(size = 1_000_000):
    return[random.randint(1,100) for _ in range(size)]

#generate random num
def generator_num(size=1_000_000):
    for _ in range(size):
        yield random.randint(1, 100)

#Check and print the memory usage of the list and the generator
def measure_memory_usage():
    num_list = generate_list()
    list_mem = sys.getsizeof(num_list)+sum(sys.getsizeof(i)for i in num_list)


    number_gen = generator_num()
    generator_memory = sys.getsizeof(number_gen)

    print(f"Memory usage of list: {list_mem / 1024:.2f} KB")
    print(f"Memory usage of Number generator: {generator_memory / 1024:.2f} KB")

    return num_list,number_gen

#Implement Performance Optimization (program that sums numbers)
def sum_num_list(num):
    return sum(num)

def sum_number_gen(num):
    return sum(num)

def benchmark_performance(num_list,number_gen):
    list_setup = '''
from __main__ import sum_num_list, generate_list
num_list = generate_list()
'''
    generator_setup = '''
from __main__ import sum_number_gen, generator_num
number_gen = generator_num()
'''
    generator_time = timeit.timeit('sum_number_gen(number_gen)', setup = generator_setup, number=100)

    list_time = timeit.timeit('sum_num_list(num_list)', setup= list_setup, number=100)

    print(f"Generator sum time: {generator_time:.4f} seconds")
    print(f"List sum time: {list_time:.4f} seconds")

    return list_time, generator_time

def profile_memory():
    number_list = generate_list()
    mem_before = sys.getsizeof(number_list) + sum(sys.getsizeof(i) for i in number_list)
    del number_list
    gc.collect()
    #empty list.
    memory_after = sys.getsizeof([])
    print(f"Memory before initial garbage collection: {mem_before / 1024:.2f} KB")
    print(f"Memory after garbage collection: {memory_after / 1024:.2f} KB")

def profile_function(): 
    number_list = generate_list()
    profiler = cProfile.Profile()
    profiler.enable()
    result = sum_num_list(number_list)
    profiler.disable()

    #profiler stat
    s = StringIO()
    profs = pstats.Stats(profiler,stream=s).sort_stats('cumulative')
    profs.print_stats()
    print("\nPROFILER STATS: ")
    print(s.getvalue())
    return result

def main():
    print(">> Memory management function: ")
    num_list,number_gen = measure_memory_usage()

    print("\n>> Performance Optimization: ")
    list_time,generator_time = benchmark_performance(num_list,number_gen)

    print("\n>> Memory Profile: ")
    profile_memory()

    print("\n>> Function Profile: ")
    result = profile_function()
    print(f">> sum result: {result}")

if __name__=="__main__":
    main()