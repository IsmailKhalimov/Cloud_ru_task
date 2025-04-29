def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
    return min_num

def custom_sort(numbers):
    # Пузырьковая сортировка
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def main():
    input_str = input("Введите список чисел через запятую: ")
    
    try:
        numbers = list(map(int, input_str.split()))
    except ValueError:
        print("Ошибка: введите только числа, разделенные пробелом!")
        return
    
    if not numbers:
        print("Список чисел пуст!")
        return
    
    even_numbers = get_even_numbers(numbers)
    max_num = find_max(numbers)
    min_num = find_min(numbers)
    sorted_numbers = custom_sort(numbers.copy())
    
    print(f"Четные числа: {even_numbers}")
    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")
    print(f"Отсортированный список: {sorted_numbers}")

if __name__ == "__main__":
    main()