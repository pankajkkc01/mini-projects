import os
def create_file(file_name):
    try:
        with open(file_name,'x') as f:    # key word with just eliminate the  close the file every time now it is done byself
            print(f"filename {file_name}: craeted successfully!")
    except FileExistsError:
        print(f"filename{file_name}: exits already")
    except Exception as E:
        print("An error has occured") 

def view_all_files():
    files=os.listdir  ## this just represent the list of all files in current dir.
    if not files:
        print("No files in the directory")
    else:
        print("files in directories are :")
        for file in files:
            print(file)
           
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"file is deleted seccessfully {file_name}")
    except FileNotFoundError:
        print("file does not exits")   
    except Exception as E:
        print("An error has occured") 
def read_file(file_name):
    try:
        with open('sample.txt' , 'r') as f:
            content=f.read()  
            print(f"content of the file '{file_name}':\n {content}")
    except FileNotFoundError:
        print("file does not exits")
    except Exception as E:
        print("An error has occured")

def edit_file(file_name):
    try:
        with open('sample.txt', 'a')  as f:
            content=input("enter the content you want to add to the file:")
            f.write(content + "\n")
            print(f"content added to {file_name} seccessfully")
    except FileNotFoundError:
        print("the file not fount") 
    except Exception as E:
        print("An error has occured") 
def main():
    while True:
        print("FILE MANAGER APP")
        print("1. Create a file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. edit file")
        print("6. Exit")

        choice=int(input("enter any number 1-6="))
        if choice==1:
            file_name=input("Enter the name of the file you want to create= ")
            create_file(file_name)
        elif choice==2:
            view_all_files()
        elif choice==3:
            file_name=input("enter the name of file you wants to delete= ")
            delete_file(file_name)
        elif choice==4:
            file_name=input("enter the file name you want to read ") 
            read_file(file_name)
        elif choice==5:
            file_name=input("enter the file name you want to edit ")
            edit_file(file_name)
        elif choice==6:
            print("Thank you for using the file manager app its clossing.......")
        else:
            print("invalid syntax")   


if __name__=="__main__":
 main()










