with open("example.txt", "w") as file:
    file.write("Hello there")

with open("example.txt", "a") as file:
    file.write("\nHello there!")

with open("example.txt", "r") as file:
    content = file.read()

    print(content)
