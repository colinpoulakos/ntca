file_name = "base.cfg"

try:
    with open(file_name, "r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
