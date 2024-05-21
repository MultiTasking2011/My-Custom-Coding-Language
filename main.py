import time
import turtle
import math
import random
import pygame
import re

#in case you don't realize, quiver is the name of the language, that means that everything including the print function is going to be inside quiver method

def read_file(filename):
    f = open(filename, "r")
    x = f.read()

    req_list = x.split("\n")
    req_list = [i for i in req_list if i != ""]
    return req_list
    
x = read_file("language.txt")

class fullcode:
    def __init__(self, code):
        self.code = code
        self.a = False
        self.b = False
        self.c = False
        self.d = False
        self.e = False
        self.f = False
        self.display_pattern = r'^display \.(.*?)\.'
        self.display_var_pattern = r'^display \|([^|]*)\|'
        self.draw_forward = 0
        self.draw_left = 0
        self.draw_right = 0
        self.draw_square = 0
        self.draw_circle = 0
        self.draw_turn = 0
        self.draw_polygon = 0
        self.syntax_help = 0
        self.random_range = 0
        self.random_int = 0
        self.random_float = 0
        self.clock_tick = 0
        self.output_window = 0
        self.output_size = 0
        self.threedimension_square = 0
        self.loop_count = 0
        self.loop_infinite = 0
        self.loop_variable = 0
        self.function_define = 0
        self.function_call = 0
        self.define_variable = r'^var:(.*?): = (.*?):(.*?):'
        self.define_list = r'^list:(.*?): = ([^|]*)'
        self.define_lists = 0
        self.multiplication = 0
        self.addition = 0
        self.subtraction = 0
        self.division = 0
        self.exponentiation = 0
        self.string_conversion = 0
        self.ifstatement = 0
        self.end = 0
        self.break_turtle = 0
        self.liststorage = r'^(.*?):([^|]*):'
        self.listcalling = r'^(.*?)<([^|]*)>'

    def err(self):
        return "err"

    def importing(self):
        if "bring all from draw" in self.code:
            self.a = True
        if "bring all from quiver" in self.code:
            self.b = True
        if "bring all from rand" in self.code:
            self.c = True
        if "bring all from output" in self.code:
            self.d = True
        if "bring all from threedimensions" in self.code:
            self.e = True
        if "bring all from clock" in self.code:
            self.f = True
        if "bring all from math" in self.code:
            self.g = True

    def drawdot(self):
        if self.a:
            pass
        else:
            self.err()

    def quiver(self):
        self.importing()
        store = list()
        varstore = dict() 
        liststore = list()
        liststorage = dict()
        if self.b:
            for i in self.code:
                # Display Pattern
                display = re.search(self.display_pattern, i)
                if display:
                    store.append(display.group(1))
                else:
                    self.err()

                # Variable
                variable = re.search(self.define_variable, i)
                if variable:
                    if variable.group(2) == "str":
                        varstore[variable.group(1)] = str(variable.group(3))
                    if variable.group(2) == "float":
                        varstore[variable.group(1)] = float(variable.group(3))
                    if variable.group(2) == "int":
                        varstore[variable.group(1)] = int(variable.group(3))

                # display variable
                display_variable = re.search(self.display_var_pattern, i)
                if display_variable:
                    store.append(varstore.get(display_variable.group(1)))

                #lists
                lists = re.search(self.define_list, i)
                if lists:
                    liststore.append(lists.group(2).split(', '))
                    listname = lists.group(1)
                    for item in liststore:
                        for a in item:
                            listchecker = re.search(self.liststorage, a)
                            itempos = int(item.index(a)+1)
                            dictkeyname = [listname+'_'+str(itempos)]
                            if listchecker:
                                if listchecker.group(1) == "str":
                                    liststorage[str(dictkeyname[0])] = str(listchecker.group(2))
                                if listchecker.group(1) == "float":
                                    liststorage[str(dictkeyname[0])] = float(listchecker.group(2))
                                if listchecker.group(1) == "int":
                                    liststorage[str(dictkeyname[0])] = int(listchecker.group(2))
                
                #display lists
                display_lists = re.search(self.display_var_pattern, i)
                if display_lists:
                    listcall = re.search(self.listcalling, display_lists)
            return store
    def rand(self):
        if self.c:
            pass
        else:
            self.err()

    def output(self):
        if self.d:
            pass
        else:
            self.err()

    def pthreedimension(self):
        if self.e:
            pass
        else:
            self.err()

    def clock(self):
        if self.f:
            pass
        else:
            self.err()
    
    def math(self):
        if self.g:
            pass
        else:
            self.err()
    
    def __str__(self) -> str:
        return "Do not print the class"

sourcecode = fullcode(x)
for i in sourcecode.quiver():
    print(i+"\n")