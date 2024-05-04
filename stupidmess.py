#importing
import turtle
import time
import math
import random
a = ""
# x = open("language.txt", 'r')

# def countlineno(filename):
#     with open (filename) as file:
#         lines = file.readlines()
#         total_lines = len(lines)
#         return total_lines

# lineno = countlineno("language.txt")


def read_file(filename):
    f = open(filename, "r")
    x = f.read()

    req_list = x.split("\n")
    req_list = [i for i in req_list if i != ""]
    return req_list
    
x = read_file("language.txt")

# for i in x:
#     if 'display' in i:
#          print("Display present")
#     else:
#         print(i)
    


# print(lineno)
print(x)


z = False
for code in x:
    print(code)
    if "display" in code:
        if "." in code:
            code1 = code.replace("display ", "")
            code1 = code.replace(".", "")
            code1 = str(code1)
            print(code1)
            z = False

    elif "bring all from draw" in code:
        a = ""
        print("Type 'help()' for syntax information")
        time.sleep(2)
        coding = turtle.Turtle()
        coding.pensize(1)
        coding.speed(1)
        coding.shape("arrow")
        coding.left(90)
        z = True
    
    elif "draw.forward" in code and z:
        code1 = code.replace("draw.forward", "")
        code1 = code1.replace("(", "")
        code1 = code1.replace(")", "")
        a = 1
        code1 = float(code1)

    elif "draw.left" in code and z:
        code1 = code.replace("draw.left", "")
        code1 = code1.replace("(", "")
        code1 = code1.replace(")", "")
        a = 2
        code1 = float(code1)
    
    elif "draw.back" in code and z:
        code1 = code.replace("draw.back", "")
        code1 = code1.replace("(", "")
        code1 = code1.replace(")", "")
        a = 3
        code1 = float(code1)
        
    elif "draw.right" in code and z:
        code1 = code.replace("draw.right", "")
        code1 = code1.replace("(", "")
        code1 = code1.replace(")", "")
        a = 4
        code1 = float(code1)
    
    elif "draw.turn" in code and z:
        code1 = code.replace("draw.turn", "")
        code1 = code1.replace("(", "")
        code1 = code1.replace(")", "")
        a = 5
        code1 = float(code1)
    
    elif "draw.square" in code and z:
        code1 = code.replace("draw.square(", "")
        code1 = code1.replace(")", "")
        a = 6
        code1 = float(code1)
        coding.forward(code1)
        coding.left(90)
        coding.forward(code1)
        coding.left(90)
        coding.forward(code1)
        coding.left(90)
        coding.forward(code1)
    
    elif "draw.circle" in code and z:
        code1 = code.replace("draw.circle(", "")
        code1 = code1.replace(")", "")
        a = 7
        code1 = float(code1)
    
    elif code1 == "draw.help()" and z:
        print("Syntax for making a straight line: draw.forward(length of the line)")
        print("Syntax for turning left and making a straight line: draw.left(length of the line)")
        print("Syntax for turning right and making a straight line: draw.right(length of the line")
        print("Syntax for going backwards and making a straight line: draw.back(length of the line)")
        print("Syntax for turning at an angle: draw.turn(degree of the angle, positive for left and negative for right)")
        print("Syntax for making a square: draw.square(length of a side of the square)")
        print("Syntax for making a circle: draw.circle(radius of the circle)")
    
    if a == 1:
        coding.forward(code1)
    
    if a == 2:
        coding.left(90)
        coding.forward(code1)
    
    if a == 3:
        coding.left(180)
        coding.forward(code1)
    
    if a == 4:
        coding.right(90)
        coding.forward(code1)
    
    if a == 5:
        coding.right(code1)
    
    if a == 6:
        pass
    
    if a == 7:
        coding.circle(code1)

from test import package_exists

class abc:
    def __init__(self) -> None:
        pass
    
    @package_exists
    def draw_circle(self):
        pass
    
    def print_s(self, w):
        pass

#display .hi.

c = abc()
c.print_s("display .hi.")