import os

def directories():
    for d in range(1, 10):
       name_folder = f"Dir_{d}"
       os.mkdir(name_folder)
        
        
def del_directories():
    for i in range(1, 10):
       name_folder = f"Dir_{i}"
       os.rmdir(name_folder)
    
