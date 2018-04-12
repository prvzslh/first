import os
from string import digits

"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=''),
    print()
"""


def rename_files():
    file_names = os.listdir("/home/parvez/PycharmProjects/first/samples/prank")
    print(file_names)

    #print("parvez said \"how are you\"")

    current_working_directory = os.getcwd()
    print(current_working_directory)

    os.chdir("/home/parvez/PycharmProjects/first/samples/prank")

    #current_working_directory = os.getcwd()
    #print(current_working_directory)
    #os.rename("2chennai.jpg","chennai.jpg")

    for filename in file_names:
        os.rename(filename,filename.translate(str.maketrans('','',digits)))
    new_files = os.listdir("/home/parvez/PycharmProjects/first/samples/prank")
    print(new_files)




#rename_files()