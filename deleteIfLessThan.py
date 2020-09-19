import os

directory = "D:\\output"
size = 1000 #in bytes

for item in os.listdir(directory):
    file_size = os.path.getsize(f"{directory}\\{item}")
    if file_size < size: 
        print(f"{item} is less than {size/1000}KB. Deleting.")
        os.remove(f"{directory}\\{item}")
    else: 
        print(f"{item} is not less than {size/1000}KB. Skipping.")
