from collections import deque

def is_palindrome(s: str) -> bool:
    # Очищуємо рядок від пробілів, приводимо до нижнього регістру та залишаємо тільки букви і цифри
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Створюємо двосторонню чергу
    char_deque = deque(cleaned_str)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються, це не паліндром
    
    return True  # Якщо всі символи збігаються, це паліндром

# Приклад використання
input_str = "A man, a plan, a canal: Panama"
print(is_palindrome(input_str))  # Виведе: True
