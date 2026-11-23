def total_salary(path):
    """Return the total and average salary from a file with lines 'Name,salary'."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(",")
                salaries.append(int(salary))
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except ValueError:
        print("Invalid data in file")
        return 0, 0

    if not salaries:
        return 0, 0

    total = sum(salaries)
    average = total // len(salaries)
    return total, average


total, average = total_salary("salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")