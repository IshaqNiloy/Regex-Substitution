# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class Regex():
    def __init__(self, string):
        self.string = string

    def substitute(self):
        word_list = string.split()

        print(re.sub(r'(?<=\s)(&&|\|\|)(?=\s)', lambda x : 'and' if x.group() == '&&' else 'or', string))
        
            
        




if __name__ == '__main__':
    num_of_lines = int(input())

    for _ in range(num_of_lines):
        string = input()
        my_object = Regex(string)
        my_object.substitute()
