import multiprocessing
import time

def square_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Square of {i}: {i ** 2}")

def cube_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Cube of {i}: {i ** 3}")

if __name__ == "__main__":
    start_time = time.time()

    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Elapsed time: ", time.time() - start_time)

