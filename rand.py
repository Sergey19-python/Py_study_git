import random


def rand(lst):
    if lst:
        return random.choice(lst)
 
 
 
if __name__ == "__main__":       
    print(rand([1,44,32,55,64,46]))
    print(rand([]))