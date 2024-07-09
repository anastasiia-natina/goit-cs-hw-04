import time
import multiprocessing
from queue import Queue

def process_file(filename, keywords, results_queue):
    with open(filename, 'r') as file:
        file_content = file.read()
        for keyword in keywords:
            if keyword in file_content:
                results_queue.put((keyword, filename))

def main(filenames, keywords):
    start_time = time.time()

    num_processes = 4  
    pool = multiprocessing.Pool(num_processes)

    results_queue = Queue()

    results = pool.map(process_file, zip(filenames, [keywords] * len(filenames), [results_queue] * len(filenames)))

    all_results = {}
    for results_from_process in results:
        for keyword, filename in results_from_process:
            if keyword not in all_results:
                all_results[keyword] = []
            all_results[keyword].append(filename)

    end_time = time.time()
    print(f"Загальний час виконання: {end_time - start_time} секунд")

    print(f"Результати пошуку:")
    for keyword, filenames in all_results.items():
        print(f"Ключове слово: {keyword}")
        for filename in filenames:
            print(f"- {filename}")

if __name__ == "__main__":
    filenames = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    keywords = ["слово1", "слово2", "слово3"]

    main(filenames, keywords)