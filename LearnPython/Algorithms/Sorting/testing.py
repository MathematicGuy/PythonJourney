import time
from BubbleSort import list_to_sort, BubbleSort  # Clean Import

BubbleSort(lts=list_to_sort)
#  Calculate code execution time
start_time = time.time()
end_time = time.time()
# total time
final_time = end_time - start_time
print()
print('Execution times:', float(final_time))
