import os

if not os.path.exists("jsons"):
    os.makedirs("jsons")

with open("jsons/output.txt", "w") as file:
    file.write("Hello, World!")