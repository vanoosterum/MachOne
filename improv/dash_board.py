from splinter import Browser
import elements
import time


class DashBoard(elements.Elements):
    if Browser.__getattribute__('Dashboard'):
        f = open("Dboard.txt", "w")
        f.write(time.strftime("%c"))
        f.write(" Login Passed. \n")
    else:
        f = open("Dboard.txt", "w")
        f.write(time.strftime("%c"))
        f.write(" Login Failed. \n")
        f.close()