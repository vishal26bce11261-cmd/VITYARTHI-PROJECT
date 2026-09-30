def save_data(filename, data):
    with open(filename, "w") as file:
        file.write(data)


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""