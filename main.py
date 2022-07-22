# author: Fransiskus Agapa
# Deal with file
import shutil
import os

print("\n== File Menu ==")
print("1. Read file")
print("2. Overwrite file")
print("3. Write to file")
print("4. Copy file")
print("5. Move file to directory")
print("6. Delete file")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Read file ]\n")
        try:
            with open("ThePeacock.txt") as file:
                print(file.read())
        except FileNotFoundError:
            print("\n[ File is not found ]")
    elif choice == '2':
        print("\n[ Overwrite file ]")
        text = input("Input text: ")
        try:
            with open("ThePeacock.txt", 'w') as file:
                file.write(text)
                print("\n[ File has been overwritten ]")
        except FileNotFoundError:
            print("\n[ File is not found ]")
    elif choice == '3':
        print("\n[ Write to file ]")
        text = input("Input text: ")
        try:
            with open("ThePeacock.txt", 'a') as file:
                file.write(text)
                print("\n[ File has been appended ]")
        except FileNotFoundError:
            print("\n[ File is not found ]")
    elif choice == '4':
        print("\n[ Copy file ]")
        place = input("\na. Directory\nb. Project folder\n")
        if place == 'a':
            print("\n> Directory")
            name_file = input("Would you like to name the file (y/n): ")
            if name_file == 'y' or name_file == 'Y':
                new_name = input("input name for the file: ")
                new_name += ".txt"
                shutil.copyfile("one.txt", r"C:\Users\XaveF\Documents" + '\\' + new_name)
                print("\n[ File has been copied to directory ]")
            elif name_file == 'n' or name_file == 'N':
                shutil.copyfile("one.txt", "CopiedOne.txt")
                print("\n[ File has been copied to directory ]")
            else:
                print("\n[ Invalid input ]")
        elif place == 'b':
            print("\n> Project folder")
            name_file = input("Would you like to name the file (y/n): ")
            if name_file == 'y' or name_file == 'Y':
                new_name = input("input name for the file: ")
                new_name += ".txt"
                shutil.copyfile("two.txt", new_name)
                print("\n[ File has been copied to directory ]")
            elif name_file == 'n' or name_file == 'N':
                shutil.copyfile("two.txt", "CopiedTwo.txt")
                print("\n[ File has been copied to directory ]")
            else:
                print("\n[ Invalid input ]")
        else:
            print("\n[ Invalid input ]")
    elif choice == '5':
        print("\n[ Move file ]")
        path = r"C:\Users\XaveF\Documents"
        name_file = input("Would you like to name the file (y/n): ")
        if name_file == 'y' or name_file == 'Y':
            new_name = input("input name for the file: ")
            new_name += ".txt"
            path += '\\' + name_file
            try:
                if os.path.exists(path):
                    print("[ File is already exist ]")
                else:
                    os.replace("three.txt",path)
                    print("[ File has been moved to directory ]")
            except FileNotFoundError:
                print("[ File is not found ]")
        elif name_file == 'n' or name_file == 'N':
            path += '\\' + "Copiedtree.txt"
            try:
                if os.path.exists(path):
                    print("[ File is already exists ]")
                else:
                    os.replace("three.txt", path)
                    print("[ File has been moved to directory ]")
            except FileNotFoundError:
                print("[ File is not found ]")
        else:
            print("[ Invalid input ]")
    elif choice == '6':
        print("\n[ Delete file ]")
        to_delete = input("\na. File\nb. Empty folder\nc. Folder\n")
        if to_delete == 'a':
            try:
                file_to_delete = "FileToDelete.txt"
                os.remove(file_to_delete)
                print("\n[ File has been deleted ]")
            except FileNotFoundError:
                print("\n[ File is not found ]")
        elif to_delete == 'b':
            try:
                folder_to_delete = "JustEmpty"
                os.rmdir(folder_to_delete)
                print("\n[ Empty folder has been deleted ]")
            except FileNotFoundError:
                print("\n[ File is not found ]")
        elif to_delete == 'c':
            try:
                folder_to_delete = "PoestryInside"
                shutil.rmtree(folder_to_delete)
                print("\n[ Folder has been deleted ]")
            except FileNotFoundError:
                print("\n[ File is not found ]")
    else:
        print("\n[ Invalid choice ]")

    print("\n== File Menu ==")
    print("1. Read file")
    print("2. Overwrite file")
    print("3. Write to file")
    print("4. Copy file")
    print("5. Move file to directory")
    print("6. Delete file")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")