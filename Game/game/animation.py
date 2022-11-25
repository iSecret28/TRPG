import time
def animate(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        print(line.strip("\n"))
    time.sleep(0.5)