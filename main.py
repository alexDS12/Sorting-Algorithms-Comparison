import random
import numpy as np
from datetime import datetime
from typing import Final
from memory_profiler import memory_usage
import cocktailsort as csort
import insertionsort as isort
import bubblesort as bsort
import combsort as combsort
import mergesort as msort

N: Final = 100
MAX_VALUE: Final = 1000
METHODS_LOOP: Final = 10

def write_tofile(file, content):
  with open(file, 'a') as txt_file:
    txt_file.write(content + '\n')

def print_info(function, i, average_runtimes, instructions, memory_usage):
  print('({}){} - {:.5f}\t{}\t\t{}'.format(function, i, average_runtimes, instructions, memory_usage))

def main():
  for i in range(2, N):
    print('%d started!' % i)
    #print('(M)i - T\t\tI\t\tM')
    runtimes = np.zeros(5)
    total_mem_usage = np.zeros(5)
    instructions = []
    numberlist = np.sort([random.randint(1, MAX_VALUE) for _ in range(i)])[::-1]
    
    for m, method in enumerate([csort, isort, bsort, combsort, msort]):
      for j in range(METHODS_LOOP):
        start = datetime.now()
        mem_usage = memory_usage((method.sort, (numberlist,)))
        end = datetime.now()
        runtimes[m] += (end - start).total_seconds()
        total_mem_usage[m] += np.average(mem_usage)
      instructions.append(method.count_instructions(len(numberlist)))
      #print_info(m, i, (runtimes[m]/METHODS_LOOP), instructions[m], total_mem_usage[m])
  
    average_runtimes = np.divide(runtimes, METHODS_LOOP)
    for j, method in enumerate(['cocktail.txt', 'insertion.txt', 'bubble.txt', 'comb.txt', 'merge.txt']):
      write_tofile(method, str(i)+'\t'+str(average_runtimes[j])+'\t'+str(instructions[j])+'\t'+str(total_mem_usage[j]))
        
if __name__ == '__main__':
  main()