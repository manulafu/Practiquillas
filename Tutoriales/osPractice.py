import os
from datetime import datetime

# The os module allows us to access functionality
# of the underlying operating system. So we can 
# perform tasks such as: navigate the file system,
# obtain file information, rename files, search 
# directory trees, fetch environment variables, 
# and many other operations.

os.chdir('C:\\Users\\Manuel\\Desktop')
# print(os.getcwd())
os.walk('top')