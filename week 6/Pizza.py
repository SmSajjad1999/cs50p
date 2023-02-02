import sys
import csv
from tabulate import tabulate



def main():
    check()
    student=[]
    try:
        with open(sys.argv[1]) as file:
            reader=csv.reader(file)
            for l in reader:
                student.append(l)
    except:
        sys.exit("FAIL")
    
    
    print(tabulate(student,headers="firstrow",tablefmt="grid"))
    
    #table()


def table():
    pass


def check():
    if len(sys.argv) > 2:
        sys.exit("Too many argument")
    elif len(sys.argv) < 2:
        sys.exit("Too few argument")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
        
    else:
        pass







if __name__ == "__main__":
    main()