
import os 
import shutil 

def remove_tree(path):
    path = abs_path(path)
    os.chdir(os.path.dirname(__file__))
    try:
        shutil.rmtree(path)
        print("Tree Removed:",path)
    except:
        pass

def create_tree(path):
    path = abs_path(path)
    subfolders = [  "/c//other_courses/cpp", 
                    "/c/other_courses/python",
                    "/cpp/other_courses/c",
                    "/cpp/other_courses/python",
                    "/python/other_courses/c",
                    "/python/other_courses/cpp"]
    os.chdir(os.path.dirname(__file__))
    remove_tree(path)
    for subfold in subfolders:
        os.makedirs(path + subfold)
    print("\nTree Created:",path)

def abs_path(path):
    if path[0:2] == "..":
        os.chdir("..")
        path = os.getcwd() + path[2:]
    elif path[0] == ".":
        path = os.getcwd() + path[1:]
    elif path[0] == "/":
        path = os.getcwd() + path
    return path.replace("\\","/")

def find(path,dir):
    path = abs_path(path)
    os.chdir(path)
    if dir in os.listdir():
        print(path + "/" + dir)
    for next_fold in os.listdir():
        find(path + "/" + next_fold,dir)
    os.chdir(os.path.dirname(__file__))

try:
    for path in ["/tree","./tree","../tree","c:/tree"]:
        create_tree(path)
        find(path,"python")
        remove_tree(path)
    print("\nCompleted successfully\n")
except:
    print("An error occurred")
