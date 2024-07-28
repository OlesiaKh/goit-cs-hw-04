import threading
import time
import os

# Функція для пошуку ключових слів у файлах
def search_keywords_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Основна функція для багатопотокового пошуку
def threaded_search(file_paths, keywords):
    results = {}
    threads = []
    
    for file_path in file_paths:
        thread = threading.Thread(target=search_keywords_in_file, args=(file_path, keywords, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results

# Тестування
if __name__ == "__main__":
    keywords = ['keyword1', 'keyword2']
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt'] 
    start_time = time.time()
    results = threaded_search(file_paths, keywords)
    end_time = time.time()
    print("Threaded Search Results:", results)
    print("Execution Time:", end_time - start_time)