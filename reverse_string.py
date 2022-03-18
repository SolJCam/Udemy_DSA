import pdb, sys

input = input()
# input = "Sol Cameron"
# input = 12345

def reverse(string: str) -> str:
    # pdb.set_trace()
    if type(string) == str:
        reversing = string[::-1]
        print(reversing)
    else: 
        print("not a string")


reverse(input)
