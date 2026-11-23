def get_cats_info(path):
    """Return a list of dicts with cat info from a file with lines 'id,name,age'."""
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid data in file")
    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)