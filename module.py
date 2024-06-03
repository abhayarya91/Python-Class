# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> import calendar
# >>> print(calendar.month(2003,10))
#     October 2003
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31

# >>> import os
# >>> os.name
# 'nt'
# >>> os.getcwd
# <built-in function getcwd>
# >>> os.getcwd
# <built-in function getcwd>
# >>> import os
# ... 
# ... # Get the current working directory
# ... current_directory = os.getcwd()
# ... 
# ... print("Current Working Directory:", current_directory)
# ... 
# SyntaxError: multiple statements found while compiling a single statement
# >>> import os
# >>> currentDirectory = os.getcwd()
# >>> print("current working diretory:",currentDirectory)
# current working diretory: C:\Users\abhay\AppData\Local\Programs\Python\Python312
# >>> os.chdir('C:\Users\abhay')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# >>> os.chdir(r'C:\Users\abhay')
# >>> print("current working Directory:",os.getcwd)
# current working Directory: <built-in function getcwd>
# >>> os.mkdir('C:\Users\abhay')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
