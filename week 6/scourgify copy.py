import csv
import sys



def main():
    
    x=input("name:")
    y=input("name:")

    #check()
    
    data=[]
    



    try:
        with open(x,"r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                last , first = row["name"].split(",")
                data.append({"first":first,"last":last,"house":row["house"]})           
    except:       
        sys.exit("File not found")
    
    def get_firstname(data):
        return data.get("first")
    
    data.sort(key=get_firstname)
    
    

    with open(y,"w",newline="") as newfile:
        fieldnames = ["first_name","last_name","house"]     
        write=csv.DictWriter(newfile,fieldnames=fieldnames)
        write.writerow({"first_name":"First Name","last_name":"Last Name","house":"House"})
        for row in data:
            
            write.writerow({"first_name":row["first"],"last_name":row["last"],"house":row["house"]})


    #print(data)
    
    
    #print(data[1:])







def check():
    if len(sys.argv) > 3:
        sys.exit("Too many Argument")
    if len(sys.argv) < 3:
        sys.exit("Too few Argument")        









if __name__ == "__main__":
    main()






