class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()

filename = input("Name of the file you want to open: ")
studens_with_grades = {}

#opening the file
try:
    grades = open(filename,'rt')
except FileNotFoundError:
    print("Could not find the file you were looking for")
except:
    print("Some errror occured while opening the file")

#initialize the first line
try:
    line = grades.readline()
except:
    print("Something went wrong while reading the file")
    raise FileEmpty("The file you tried to open is empty")

try:
    while line != "":
        line_content = line.strip().split()
        fullname = f'{line_content[0]} {line_content[1]}'
        studens_with_grades[fullname] = studens_with_grades.get(fullname,0) + float(line_content[2])
        line = grades.readline()
except:
    raise BadLine(f'Bad line: {line_content}')

grades.close()

#print list of sorted results to the console
print(sorted(studens_with_grades.items(),key=lambda x: x[1]))
