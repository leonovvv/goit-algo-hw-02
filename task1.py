from queue import Queue
import random
import time

# Створити чергу заявок
request_queue = Queue()

# Функція для генерації нових заявок
def generate_request():
    # Створити нову заявку
    request_id = random.randint(1000, 9999)
    #Додати заявку до черги
    request_queue.put(f"Заявка #{request_id}")
    print(f"Додано: Заявка #{request_id}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        #Видалити заявку з черги
        request = request_queue.get()
        #Обробити заявку
        print(f"Обробляється: {request}")
    else:
        print("Черга пуста, чекаємо нових заявок...")

# Запуск генерації заявок та їх обробки
def main():
    while True:
        generate_request()
        process_request()
        time.sleep(1)

if __name__ == "__main__":
    main()

