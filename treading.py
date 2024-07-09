import threading
import time

def search_files(keyword, files):
    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if keyword in line:
                    results.append(file)
    return results

def main(keyword, files):
    start_time = time.time()

    num_threads = 4  
    threads = []

    file_chunks = [files[i:i + len(files) // num_threads] for i in range(num_threads)]
    
    for files_chunk in file_chunks:
        thread = threading.Thread(target=search_files, args=(keyword, files_chunk))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    all_results = []
    for thread_results in [thread.result() for thread in threads]:
        all_results.extend(thread_results)

    print(f"Пошукове слово: {keyword}")
    print(f"Знайдено у файлах: {all_results}")
    print(f"Загальний час: {total_time:.2f} секунд")

if __name__ == "__main__":
    keyword = "слово_для_пошуку" 
    files = ["file1.txt", "file2.txt", ...]  
    main(keyword, files)