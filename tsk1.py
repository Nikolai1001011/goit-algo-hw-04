def total_salary(path: str) -> tuple:
    total_salary = 0
    num_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
                
        if num_developers == 0:
            print("Файл порожній.")
            return (0, 0)
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Помилка: {e}")
        return (0, 0)
    
    average_salary = total_salary / num_developers
    return total_salary, average_salary