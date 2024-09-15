import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
admin_username="Admin"
admin_password="admin123"
d_ques={}
d_stu={}
answers={}
L1=[]

def add():
    a=input("Enter category:")
    if a in d_ques:
        n=input("Input Question:")
        d_ques[a].append(n)
        ans=(input("Enter Answer for the question:"))
        #L1.append(ans)
        answers[a].append(ans)
        print(d_ques)
        print(answers)
        print("Would you like to add more elements?")
        c=input("Y or N:")
        if c=="Y" or c=="y":
            add()
        else:
            ("")
    else:
        q=input("Input Question:")
        ans=input("Enter Answer for the question:")
    
        d_ques[a]=[q]
        answers[a]=[ans]
        print(d_ques)
        print("Would you like to add more elements?")
        c=input("Y or N:")
        if c=="Y" or c=="y":
            add()
        else:
            ("")
        
        
def delete():
    print("","1. Delete a question.","\n","2. Delete a category")
    delt=int(input("Enter Choice:"))
    if delt==1:
        a=input("Enter category in which you would like to delete a question:")
        if a in d_ques:
            q=int(input("Input position number of the question.:"))
            if q <= len(d_ques[a]):
                del d_ques[a][q-1]
                del answers[a][q-1]
                print(f"Element at index {q} removed from '{a}'.")
                print(d_ques)
                print("Would you like to delete more elements?")
                c=input("Y or N:")
                if c=="Y" or c=="y":
                    delete()
                else:
                    ("")
                
            else:
                print("Out of range")
        else:
            print("Category doesn't exist")
                    

    else:
        a=input("Enter category:")
        del d_ques[a]
        del answers[a]
        print(d_ques)
        print("Would you like to delete more elements?")
        c=input("Y or N:")
        if c=="Y" or c=="y":
            delete()
        else:
            ("")
    
def modify():
    print("Edit a question")
    a=input("Enter category:")
    if a in d_ques:
        no=int(input("Position of question in the category:"))
        eq=input("Enter New Question:")
        an=input("Enter answer to that question:")
        d_ques[a].pop(no-1)
        answers[a].pop(no-1)
        d_ques[a].insert(no-1,eq)
        answers[a].insert(no-1,an)
        print(d_ques)
        print("Would you like to modify more elements?")
        c=input("Y or N:")
        if c=="Y" or c=="y":
            modify()
        else:
            ("")
    else:
        print("Category does'nt exist.")

def stu_info():
        n=int(input("How many students want to play?:"))
        for i in range(n):
                stu_name = input("Student Name:")
                d_stu[stu_name]=0

def cat():
        print("Wanna play the quiz?","\n","Y/N")
        chi=input()
        if chi=="Y" or chi=="y":
                na=input("Enter Student Name:")
                if na in d_stu:
                        print("Choose a Category")
                        print(d_ques.keys())
                        inp=input("Write Name of category:")
                        if inp in d_ques:
                                val=d_ques[inp]
                                answ=answers[inp]
                                ind=int(input("Index of the question in category:"))
                                if ind<len(d_ques[inp]):
                                        question=val[ind]
                                        answer = input(f"{question} ")
                                        dict1={}
                                        if answer==answ[ind]:
                                            d_stu[na]+=1
                                            print(d_stu)
                                        else:
                                            print("Wrong answer")
                                        
                                else:
                                    print("Out of Range")
                        else:
                            ("Category not available")
                else:
                    ("Student not registered")
        else:
            exit()


        
        
while True:
    print("*********************MENU*********************")
    print("1. Admin Login")
    print("2. Register Student")
    print("3. Play Quiz")
    print("4. Show Results")
    print("5. Exit")
    choice = int(input("Select an option: "))

    if choice==1:
        aid=input("User id:")
        if aid=="Admin" or aid=="admin":
            aip=input("Password:")
            if aip=="admin123":
                print("----------------------MENU----------------------")
                print("","1. Add question","\n","2. Delete Question","\n","3. Modify Question","\n","4. Exit ")
                ch=int(input("Enter Choice:"))
                if ch==1:
                    add()
                        
                elif ch==2:
                    delete()
                    
                elif ch==3:
                    modify()
                    
                else:
                    exit()
      

            else:
                print("Incorrect Password")

        else:
            print("Incorrect User")

    elif choice==2:
        stu_info()

    elif choice==3:
        cat()

    elif choice==4:
        df1=pd.DataFrame([d_stu])
        df1.plot(kind="bar")
        plt.xlabel("Students")
        plt.ylabel("Score")
        plt.show()

    else:
        exit()
        
            


        
                
    

                
        
                
        
        
        
        


