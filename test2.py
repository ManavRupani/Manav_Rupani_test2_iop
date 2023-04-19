phoneDirectory={}

def teNdig_Test(y):
        while True:
            number = y
            if not number.isdigit(): # check if a string contains a number with .isdigit()
                print ("\nEnter only numbers !(error) \n")
                break
            elif len(number) != 10:
                print ("\nEnter 10 digits !(error)\n")
                break
            else:
                return y 
# print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY\n")
# print("1. Add a record\n")
# print("2. Search a record\n")
# print("3. Update a record\n")
# print("4. Delete a record\n")
# print("5. Quit\n")
loop_=1
count=0
while(loop_==1):
    main_=True
    while(main_):
        if count==0:
            print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY\n")
        else:
            print("\nMenu\n")
        count+=1
        print("1. Add a record\n")
        print("2. Search a record\n")
        print("3. Update a record\n")
        print("4. Delete a record\n")
        print("5. Quit\n")
        user_input=input("\nEnter your choice: ")
        if user_input=="1":
            try:
                x1=input("\nEnter name: ")
                if not x1.isalpha():
                    print("\nPlease enter only alphabetical characters for name")
                    break
                else:
                    y1=input("\nEnter your 10-digit phone number: ")
                    if y1==teNdig_Test(y1):
                        phoneDirectory[x1]=y1
                        print("\nRecord added")
                        break
                    else:
                        break
            except:
                print("\nUnable to add Record")
                break
        elif user_input=="2":
            try:
                x2=input("\nEnter name to search: ")
                if x2 in phoneDirectory:
                    print("\n"+x2+": "+phoneDirectory[x2])
                    break
                else:
                    print("\nNo Such Record Found")
                    break
            except:
                print("\nError 101")
                break
        elif user_input=="3":
            # try:
            #     x3=input("Enter name: ")
            #     y3=input("Enter new 10-digit phone number: ")
            #     phoneDirectory[x3]=y3
            #     print("Record updated")
            #     break
            # except:
            #     print("Error 101")
            #     break
            try:
                x3=input("\nEnter name: ")
                if x3 in phoneDirectory:
                    y3=input("\nEnter new 10-digit phone number: ")
                    if y3==teNdig_Test(y3):
                        phoneDirectory[x3]=y3
                        print("\nRecord updated")
                        break
                    else:
                        print("\nError")
                        break
                else:
                    print("\nNo record found")
            except:
                print("\nUnable to add Record")
                break
        elif user_input=="4":
            try:
                x4=input("\nEnter name: ")
                phoneDirectory.pop(x4)
                print("\nRecord deleted")
                break
            except:
                print("\nNo Record found")
                break
        elif user_input=="5":
            loop_=0
            break
        else:
            print("\nWrong Input")
            break
        