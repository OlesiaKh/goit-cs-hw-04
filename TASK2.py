import multiprocessing
import time
import os

# Функція для пошуку ключових слів у файлах
def search_keywords_in_file(file_path, keywords, queue):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    queue.put((keyword, file_path))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Основна функція для багатопроцесорного пошуку
def multiprocess_search(file_paths, keywords):
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    processes = []
    
    for file_path in file_paths:
        process = multiprocessing.Process(target=search_keywords_in_file, args=(file_path, keywords, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    results = {}
    while not queue.empty():
        keyword, file_path = queue.get()
        if keyword not in results:
            results[keyword] = []
        results[keyword].append(file_path)
    
    return results

# Тестування
if __name__ == "__main__":
    keywords = ['keyword1', 'keyword2']
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  
    start_time = time.time()
    results = multiprocess_search(file_paths, keywords)
    end_time = time.time()
    print("Multiprocess Search Results:", results)
    print("Execution Time:", end_time - start_time)
