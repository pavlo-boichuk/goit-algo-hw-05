def total_salary(path):
    
    salary_sum = 0 # Загальна сума заробітної плати
    lines_count = 0 # Кількість записів (розробників)
   
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                
                salary_sum += int(line.strip().split(',')[1])
                lines_count += 1
    except FileNotFoundError as error:
        print(f'Помилка шляху до файлу: {error}')
    except Exception as general_error:
        print(f'Не можливо прочитати файл: {general_error}')

    average_salary = 0 if lines_count == 0 else int(salary_sum/lines_count)
    
    return (salary_sum, average_salary)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")