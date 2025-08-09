import random
import time
import multiprocessing

def is_sorted_desc(arr):
    return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))

def bogosort_worker(arr, stop_flag, return_dict, proc_id):
    attempts = 0
    local_arr = arr[:]
    while not is_sorted_desc(local_arr):
        if stop_flag.value:
            return_dict[proc_id] = attempts
            return
        random.shuffle(local_arr)
        attempts += 1
    print(f"Process {proc_id} sorted after {attempts} attempts")
    return_dict[proc_id] = attempts
    stop_flag.value = True

def run_multiprocessing_bogosort(arr, proc_count=4, timeout=5):
    manager = multiprocessing.Manager()
    stop_flag = manager.Value('b', False)
    return_dict = manager.dict()
    processes = []

    for i in range(proc_count):
        p = multiprocessing.Process(target=bogosort_worker, args=(arr, stop_flag, return_dict, i))
        processes.append(p)
        p.start()

    start = time.time()
    while time.time() - start < timeout:
        if stop_flag.value:
            break
        time.sleep(0.1)

    stop_flag.value = True
    for p in processes:
        p.join()

    total_attempts = sum(return_dict.values()) if return_dict else 0
    elapsed = time.time() - start
    print(f"Total attempts across processes: {total_attempts}")
    print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(10)]
    run_multiprocessing_bogosort(arr, proc_count=12, timeout=5000)
