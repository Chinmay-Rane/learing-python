#generate a table book for a 13 year old

def gentable(n):
    table = ""
    for i in range(1,11):
        table += f"{n}X{i}={n*i}\n"

    with open(f"CHAPTER 9/tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,21):
    gentable(i)