from concurrent.futures import ThreadPoolExecutor
import time
from concurrent.futures import as_completed

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")
    return f"Result of task {name}"

with ThreadPoolExecutor(max_workers=3) as executor:

    # Case 1 = Using the submit() method where the futures are collected and results are fetched individually.It is used when you need more control over individual tasks.Also, you can handle exceptions for each future separately.And you want the result as they complete, not in order.
    # futures = []

    # for i in range(5):
    #     future = executor.submit(task, i)
    #     futures.append(future)

    # for future in futures:
    #     print(future.result())

    # Case 2 = Using the map() method where results are collected in order of submission.It is used when you want simplicity and don't need individual control over tasks.And you want results in the order of submission.Not used to much only used when order matters and task is less complex and there are no exceptions to handle.
    # results = list(executor.map(task, range(5)))

    # for result in results:
    #     print(result)

    # Case 3 = Using the as_completed() method where results are processed as they complete.It is used when you want to process results as soon as they are available.And you don't care about the order of results.And you want to handle exceptions as they occur.Is is the recommeded to used with the submit() method.

    # Case 3.1 = Used with a list comprehension when you don't want to keep track of which future corresponds to which task.
    # futures = [executor.submit(task, i) for i in range(5)]  
    # for future in as_completed(futures):
    #     # Handle exceptions if any
    #     try:
    #         result = future.result()    
    #     except Exception as e:
    #         print(f"Task generated an exception: {e}")  

    # Case 3.2 = Used with a dictionary comprehension when you want to keep track of which future corresponds to which task.
    future = {
        executor.submit(task,i):i
        for i in range(5)
    }

    for future in as_completed(future):
        task_id = future[future]
        try:
            result = future.result()
            print(f"Task {task_id} completed with result: {result}")
        except Exception as e:
            print(f"Task {task_id} generated an exception: {e}")
    
    # Note = you offently see using threading.lock() in the threadpoolexecutor realted task because it is used when multiple threads need to access a shared resource safely to prevent data corruption or inconsistencies.Like global variables,file operations,or shared data structures,etc.

print("All tasks completed")
