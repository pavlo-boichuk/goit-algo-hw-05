def get_cats_info(path):
    
    result_list = []
   
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                
                line_lst = line.strip().split(',') # читання чергового рядка і розбиття на проміжний список з потрібних елементів
                result_list.append({"id": line_lst[0], "name": line_lst[1], "age": line_lst[2]}) # наповнення результуючого списку словником з елементів
                
    except FileNotFoundError as error:
        print(f'Помилка шляху до файлу: {error}')
    except Exception as general_error:
        print(f'Не можливо прочитати файл: {general_error}')

    return result_list


cats_info = get_cats_info("cats_file.txt")
print(cats_info)