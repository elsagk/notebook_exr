# # ///////////////////////////////////////////////// example two Paralle
import time
from multiprocessing import Pool

#The Pool from the multiprocessing module allows for true parallel execution. Each task runs in its own process, allowing multiple tasks to execute truly simultaneously on different CPU cores
# from multiprocessing import cpu_count
# print(f"Number of available CPU cores: {cpu_count()}")


# Task to simulate some CPU-bound work
def simulate_work(task_id):
    print(f"Task {task_id} is starting.")
    time.sleep(2)  # Simulate a long-running task
    print(f"Task {task_id} is completed.")
    return f"Result from Task {task_id}"

# Using multiprocessing to handle tasks in parallel
def parallel_execution(tasks, num_processes):
    print("Starting parallel execution...")
    with Pool(num_processes) as pool:
        results = pool.map(simulate_work, tasks)
    return results

if __name__ == "__main__":
    tasks = [1, 2, 3, 4, 5, 6]  # Example Simulating 6 tasks
    num_processes = 4      # Number of parallel processes
    start_time = time.time()
    results = parallel_execution(tasks, num_processes)
    end_time = time.time()

    print(f"\nResults: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")