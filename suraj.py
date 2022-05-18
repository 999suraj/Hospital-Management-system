dict = {}
i=0
dict2={}
def userinput():
    l=["Dr.A","Dr.B","Dr.C",'Dr.D']
    while True:
        try:
            PatientName = input("Enter your name: ")
            Patientid = input("Enter your id number: ")
            Patientage = int(input("Enter your age:")) 
            Patientheight = float(input("Enter your height: "))
            Patientweight = float(input("Enter your weight: "))
            Patientbodytemperature = float(input("Enter your body temperature: "))
            Patientbloodgroup = input("Enter your blood group: ")
            Patientsex = input("Enter your sex: ")
            # Patientbill = int(input("Enter your bill: "))
            Doctorfees = int(input("Enter your doctor fees:"))
            Roomcharges = int(input( "Enter your room charges:") )
            Otherfees = int(input("Enter your other fees:"))
            i=+1
        except:
            print("invalid Input")
            continue
        Totalfees = ( Roomcharges + Otherfees + Doctorfees)
        BMI = (Patientweight/Patientheight**2)
        dict2[PatientName]=Totalfees
        print(l[i%3],end=" ")
        print(" is your allocated doctor")
        print()
        dict[PatientName] = BMI
        print(dict)
        print("if you want to add patient press Y  else press N")
        x=input().lower()
        if x=="y":
            continue
        else:
            print("enter the name of patient to display bmi and bill")
            k=input()
            print("your bmi is ",dict[k])
            print("your bill is ",dict2[k])
            print("Thank You ")
            break
userinput()