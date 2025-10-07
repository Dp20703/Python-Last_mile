import os

if os.path.exists("data3.txt"):
    os.remove('data3.txt')
    print("File deteted")
else:
    print("File not found")