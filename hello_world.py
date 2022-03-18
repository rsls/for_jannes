"""
Prints 'Hello World' to a variety of files
Prints results of user input to file
"""
from optparse import OptionParser
import os

"""
Commandline options
"""
parser = OptionParser()

parser.add_option("-a", "--alpha", default = "1", help = "any integer")
parser.add_option("-b", "--bravo", default = "1.0", help = "any float")
parser.add_option("-c", "--charlie", default = "False", help = "any boolean")
parser.add_option("-d", "--delta", default = "rabbits", help = "any string")

(options, args) = parser.parse_args()

"""
Making commandline options into the variables in your code, necessary to get expected types
"""
integer = int(options.alpha)
floating = float(options.bravo)
boolean = bool(options.charlie)
string = str(options.delta)


# Insert code here 

"""
Output files using print statements
"""
print("This is the output from python print statements")
print("Hello World!")
print("Your chosen integer is " + str(integer))
print("Your chosen float is " + str(floating))
print("Your chosen bool is " + str(boolean))
print("Your chosen string is " + str(string))

"""
Output files using .write
"""
filename = "hello_world_{0}_py.txt".format(string)
open_file = open(filename, "w")

open_file.write("This is the output from .write statements\n")
open_file.write("Hello World!\n")
open_file.write("Your chosen integer is " + str(integer) + "\n")
open_file.write("Your chosen float is " + str(floating) + "\n")
open_file.write("Your chosen bool is " + str(boolean) + "\n")
open_file.write("Your chosen string is " + str(string) + "\n")

open_file.close()
