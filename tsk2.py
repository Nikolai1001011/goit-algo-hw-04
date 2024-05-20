def get_cats_info(path: str) -> list:
    cats = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat_info)
                except ValueError:
                    print(f"Line format error: {line.strip()}")
                    continue

    except FileNotFoundError:
        print(f"Error: The file at {path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats