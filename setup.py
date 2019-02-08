import os
import sys
import pymysql
from cx_Freeze import setup, Executable 

os.environ['TCL_LIBRARY'] = r'C:\\Users\\Nishu\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\Nishu\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6' 


                     
base = None
setup(name = "Test" , 
      version = "0.1" , 
      description = "" , 
      
      executables = [Executable("login.py", base=base)])