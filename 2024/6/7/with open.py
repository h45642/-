with open("python.txt", "r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')