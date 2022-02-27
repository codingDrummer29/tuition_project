#imports
import mysql.connector #connecting DB
from pickle import load, dump 
import time 
import random

# DB connection
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "railway_reservation"
)

# connection to DB
cursorObject = dataBase.cursor()

#ticket class
class tickets:
    def __init__(self):
        self.resno=0
        self.name=''
        self.age=''
        self.no_ofac1stclass=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.no_oftickets=0
        self.totaf=0
        self.status=''
        self.trainno=0

    # returns reservation number
    def ret(self):
        return(self.resno)

    # will return name
    def retname(self):
        return(self.name)

    # will display datas
    def display(self):
        f=0
        # cursorObject = dataBase.cursor()
        # query = """SELECT * FROM train WHERE trainno = %s"""
        # cursorObject.execute(query, (selectedTrain, ))
        # allTicke = cursorObject.fetchall()
        print('')
        pnr=int(input("ENTER PNR NUMBER : "))
        print ("\n\nFETCHING DATA . . .".center(80))
        cursorObject = dataBase.cursor()
        query = """SELECT * FROM ticket WHERE resno = %s"""
        cursorObject.execute(query, (pnr, ))
        pnrStatus = cursorObject.fetchall()
        print(pnrStatus)
        time.sleep(1)
        tick=pnrStatus
        print('\nPLEASE WAIT...!!'.center(80))
        time.sleep(1)
        # os.system('cls')
        for row in pnrStatus:
            if pnr == row[0]:
                print("="*80)
                print("PNR STATUS".center(80))
                print("="*80)
                print("\nPNR NO :",row[0])
                print("PASSENGER'S NAME :",row[1])
                print("PASSENGER'S AGE :",row[2])
                print("NO OF SEATS BOOKED : ",row[8])
                print("STATUS :",row[9])
                print("\n")
            else:
                print("\nWRONG PNR NUMBER..!!\n\n")
           
    # handles pending status
    def pending(self):
         self.status="WAITING LIST"
         print("PNR NUMBER :",self.resno)
         print("\n")
         time.sleep(1.2)
         print("\nSTATUS = ",self.status)
         print("\nNO OF SEATS BOOKED : ",self.no_oftickets)
         print("\n")

    # handles confirmation
    def confirmation (self):
        self.status="CONFIRMED"
        print("PNR NUMBER : ",self.resno)
        print("\n")
        time.sleep(1.5)
        print("\nSTATUS = ",self.status)
        print("\n")

    # handles cancelation
    def cancellation(self):
        z=0
        f=0
        print
        pnr= int(input("ENTER PNR NUMBER : "))
        try:
            cursorObject = dataBase.cursor()
            query = """SELECT * FROM ticket WHERE resno = %s"""
            cursorObject.execute(query, (pnr, ))
            myresult = cursorObject.fetchall()

            if not myresult:
                print("\nNO SUCH RESERVATION NUMBER FOUND\n\n")
                time.sleep(2)
            else:
                cursorObject = dataBase.cursor()
                query = """DELETE FROM ticket WHERE resno = %s"""
                cursorObject.execute(query, (pnr, ))
                dataBase.commit()
                print("\n\nTICKET CANCELLED\n\n")
                
        except:
            pass

    #reserves ticket
    def reservation(self):
        trainno=int(input("ENTER THE TRAIN NO: "))
        z=0
        f=0
        trCl=train()

        cursorObject = dataBase.cursor()
        query = """SELECT * FROM train WHERE trainno = %s"""
        cursorObject.execute(query, (trainno, ))
        trainDetails = cursorObject.fetchall()
        # print('trainDetails: ', trainDetails)
        time.sleep(2)
        
        adOk='y'
        while (adOk.lower() == 'y'):
            tr = trainDetails
            for row in tr:
                z = row[0]
                n = row[5]
                if (trainno == z):
                    print("\nTRAIN NAME IS : ",n)
                    f=1
                    print("\n")
                    print("-"*80)
                    no_ofac1st=row[1]
                    no_ofac2nd=row[2]
                    no_ofac3rd=row[3]
                    no_ofsleeper=row[4]
                
                    if(f==1):
                        self.trainno=z
                        self.name=input("ENTER THE PASSENGER'S NAME ")
                        self.age=int(input("PASSENGER'S AGE : "))
                        print("\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN :- ")
                        print("1.AC FIRST CLASS")
                        print("2.AC SECOND CLASS")
                        print("3.AC THIRD CLASS")
                        print("4.SLEEPER CLASS")
                        c=int(input("\n\nENTER YOUR CHOICE: "))
                    
                        amt1=0
                        if(c==1):
                            self.no_oftickets=int(input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=1000*self.no_oftickets
                                i=i+1
                            print('\n')
                            print("PROCESSING. .")
                            time.sleep(0.5)
                            print( ".")
                            time.sleep(0.3)
                            print('.')
                            time.sleep(2)
                            print("TOTAL AMOUNT TO BE PAID: ",amt1)
                            self.resno=int(random.randint(1000,2546))
                            x=no_ofac1st-self.totaf
                            print("\n")
                            if(x>0):
                                self.setDataToDB()
                                self.confirmation()
                            else:
                                self.setDataToDB()
                                self.pending()
                                break
                        
                        elif(c==2):
                            self.no_oftickets=int(input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED :  "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=900*self.no_oftickets
                                i=i+1
                            print
                            print("PROCESSING. .")
                            time.sleep(0.5)
                            print(".")
                            time.sleep(0.3)
                            print('.')
                            time.sleep(2)
                            print( "TOTAL AMOUNT TO BE PAID = ",amt1)
                            self.resno=random.randint(1000,2546)
                            x=no_ofac2nd-self.totaf
                            print('')
                            if(x>0):
                                self.setDataToDB()
                                self.confirmation()
                                break
                            
                            else:
                                self.setDataToDB()
                                self.pending()
                                break
                        
                        elif(c==3):
                            self.no_oftickets=int(input("ENTER NO_OF THIRD CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=800*self.no_oftickets
                                i=i+1
                            print('')
                            print( "PROCESSING. .",time.sleep(0.5))
                            print(".")
                            time.sleep(0.3)
                            print('.')
                            time.sleep(2)
                            # os.system('cls')
                            print("TOTAL AMOUNT TO BE PAID = ",amt1)
                            self.resno=random.randint(1000,2546)
                            x=no_ofac3rd-self.totaf
                            print
                            if(x>0):
                                self.setDataToDB()
                                self.confirmation()
                                break
                            
                            else:
                                self.setDataToDB()
                                self.pending()
                                break                      
                        
                        elif(c==4):
                            self.no_oftickets=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=550*self.no_oftickets
                                i=i+1
                            print
                            print( "PROCESSING. .",time.sleep(0.5))
                            print(".",time.sleep(0.3))
                            print('.',time.sleep(2))
                            print("TOTAL AMOUNT TO BE PAID = ",amt1)
                            self.resno=random.randint(1000,2546)
                            x=no_ofsleeper-self.totaf
                            print
                            if(x>0):
                                self.setDataToDB()
                                self.confirmation()
                                break
                            
                            else:
                                self.setDataToDB()
                                self.pending()
                                break        
            
                    
                    if(f==0):
                        time.sleep(2)
                        print("\n\n\t\t\t\tNO SUCH TRAINS FOUND !!")
                        time.sleep(2)
                        print("\n")
            print("")
            adOk=input("\tDO YOU WANT TO CONTINUE ? ")
            continue

    def setDataToDB(self):

        cursorObject = dataBase.cursor()
        sql = "INSERT INTO ticket (resno, name, age, no_ofac1stclass, no_ofac2ndclass,no_ofac3rdclass, no_ofsleeper, no_oftickets, totaf, status, trainno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.resno, self.name, self.age, self.no_ofac1stclass, self.no_ofac2ndclass,self.no_ofac3rdclass, self.no_ofsleeper, self.no_oftickets, self.totaf, self.status, self.trainno)
        cursorObject.execute(sql, val)
        dataBase.commit()

# class for train
class train:
    def __init__(self):
        self.trainno=0
        self.no_ofac1stclass=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.totalseats=0
        self.trainname=''
        self.startingpt=""
        self.destination=''        
    
    # takes input
    def getinput(self):
        print("="*80)
        print("\t\t\t  ENTER THE TRAIN DETAILS\n")
        print("="*80)
        self.trainname=input("ENTER THE TRAIN NAME : ").upper()
        self.trainno=int(input("ENTER THE TRAIN NUMBER: "))
        self.no_ofac1stclass=int(input("\nENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED : "))
        self.no_ofac2ndclass=int(input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED : "))
        self.no_ofac3rdclass=int(input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED : "))
        self.no_ofsleeper=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED : "))
        self.startingpt=input("\nENTER THE STARTING POINT : ")
        self.destination=input("ENTER THE DESTINATION POINT : ")
    # display data
    def output(self):
        print("="*80)
        print("THE ENTERED TRAIN NAME IS : ",self.trainname)
        print("THE TRAIN  NUMBER IS : ",self.trainno)
        print("\nSTARTING POINT ENTERED IS : ",self.startingpt)
        print("DESTINATION POINT ENTERED IS : ",self.destination)
        print("\nNO_OF AC FIRST CLASS SEATS RESERVED ARE :",self.no_ofac1stclass)
        print("NO_OF AC SECOND CLASS SEATS RESERVED ARE :",self.no_ofac2ndclass)
        print("NO_OF AC THIRD CLASS SEATS RESERVED ARE :",self.no_ofac3rdclass)
        print("NO_OF SLEEPER CLASS SEATS RESERVED ARE :",self.no_ofsleeper)
        print("\n")
        print("="*80)
    # returns train details
    def gettrainname(self):
        return (self.trainname)
    def gettrainno(self):
        return(self.trainno)
    def getno_ofac1stclass(self):
        return(self.no_ofac1stclass)
    def getno_ofac2ndclass(self):
         return(self.no_ofac2ndclass)
    def getno_ofac3rdclass(self):
        return(self.no_ofac3rdclass)
    def getno_ofsleeper(self):
        return (self.no_ofsleeper)
    def getstartingpt(self):
        return (self.startingpt)
    def getdestination(self):
        return (self.destination)

def handleTrainDetails():
    tr=train()
    print('CHOOSE YOUR OPTION: ')
    print('\n\n1. ADD NEW TRAIN DETAILS: ')
    print('2. UPDATE EXISTING TRAIN DETAILS: ')
    print('3. DELETE OLD TRAIN DETAILS: ')
    print('4. QUIT\n\n')
    ch = int(input('ENTER YOUR CHOICE:: '))

    if(ch == 1):
        tr.getinput()

        cursorObject = dataBase.cursor()
        sql = "INSERT INTO train (trainname, trainno, no_ofac1stclass, no_ofac2ndclass, no_ofac3rdclass, no_ofsleeper, startingpt, destination) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (tr.trainname, tr.trainno, tr.no_ofac1stclass, tr.no_ofac2ndclass, tr.no_ofac3rdclass, tr.no_ofsleeper, tr.startingpt, tr.destination)
        cursorObject.execute(sql, val)
        dataBase.commit()

    elif (ch==2):
        selectTrain = int(input("Enter the train number you want to update: "))
        
        cursorObject = dataBase.cursor()
        query = """SELECT * FROM train where trainno = %s"""
        cursorObject.execute(query, (selectTrain,))
        myresult = cursorObject.fetchall()
        
        for row in myresult:
            print("\n\n\tYour train details: \n")
            print("Train Number : ", row[0])
            print("Train name : ", row[5])
            print("Number of First Class : ", row[1])
            print("Number of Second Class : ", row[2])
            print("Number of Third Class : ", row[3])
            print("Number of Sleepers : ", row[4])
            print("Starting Point : ", row[6])
            print("Destination Point : ", row[7])
        
        print("\n\nChoose option to update: ")
        print("1. Train name")
        print("2. Number of First Class")
        print("3. Number of Second Class")
        print("4. Number of Third Class")
        print("5. Number of Sleepers")
        print("6. Starting Point")
        print("7. Destination Point")
        print("0. Quit")

        updateOpt=int(input("Enter choice: "))
        print('\n\n')
        if(updateOpt == 1):
            trName=input("Re-enter Train name: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set trainname = %s where trainno = %s"""
            cursorObject.execute(query, (trName, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 2):
            num1=input("Re-enter Number of First Class: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set no_ofac1stclass = %s where trainno = %s"""
            cursorObject.execute(query, (num1, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 3):
            num2=input("Re-enter Number of Second Class: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set no_ofac2ndclass = %s where trainno = %s"""
            cursorObject.execute(query, (num2, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 4):
            num3=input("Re-enter Number of Third Class: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set no_ofac3rdclass = %s where trainno = %s"""
            cursorObject.execute(query, (num3, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 5):
            numS=input("Re-enter Number of Sleepers: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set no_ofsleeper = %s where trainno = %s"""
            cursorObject.execute(query, (numS, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 6):
            sp=input("Re-enter Starting Point: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set startingpt = %s where trainno = %s"""
            cursorObject.execute(query, (sp, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        elif(updateOpt == 7):
            dp=input("Re-enter Destination Point: ")
            cursorObject = dataBase.cursor()
            query = """UPDATE train set destination = %s where trainno = %s"""
            cursorObject.execute(query, (dp, selectTrain,))
            myresult = cursorObject.fetchall()
            dataBase.commit()
            print(".")
            time.sleep(2)
            print('UPDATE SUCCESSFUL')
        else:
            print("Exiting...")
            time.sleep(1)
    
    elif (ch == 3):
        deleteTrain = int(input("Enter the train number you want to delete: "))
        cursorObject = dataBase.cursor()
        query = """DELETE FROM train WHERE trainno = %s"""
        cursorObject.execute(query, (deleteTrain, ))
        dataBase.commit()
        print(" ")
        time.sleep(2)
        print('DELETE SUCCESSFUL')

    else: 
        print("\nExiting...")
        time.sleep(2)

# drver function
def menu():
    tr=train()
    tick=tickets()
    print("\n")
    print( "WELCOME TO ALL BENGAL TRAVEL AGENCY\n\n")   
    while True:
            print("\n\n\n\t\t\t  RAILWAY")
            print("\t\t1. UPDATE TRAIN DETAILS (PASSWORD PROTECTED)")
            print("\t\t2. TRAIN DETAILS")
            print("\t\t3. RESERVATION OF TICKETS")
            print("\t\t4. CANCELLATION OF TICKETS")
            print("\t\t5. DISPLAY PNR STATUS")
            print("\t\t6. QUIT")
            
            ch=int(input("\t\t\tENTER YOUR CHOICE : "))
            print("\n\n\tLOADING. .")
            time.sleep(1)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(2)
            
            if ch==1:
                j="123456"
                r=input("\n\n\n\t\tENTER THE PASSWORD: ")
                if (j==r):
                    x='y'
                    while (x.lower() == 'y'):
                        handleTrainDetails()
                        print("\n\n\n\tUPDATING TRAIN LIST PLEASE WAIT . .")
                        time.sleep(1)
                        print(".")
                        time.sleep(0.5)
                        print (".")
                        time.sleep(2)
                        print("")
                        x=input("\tDO YOU WANT TO ADD ANY MORE TRAINS DETAILS ? ")
                    continue
                else:
                    print("\n\n")
                    print("WRONG PASSWORD".center(80))
            elif ch==2:              
                print("\n\n\tChoose from below: \n\n1. Details of All trains\n2. Details for specfic train\n\n")
                detailsChoice = int(input("What do you choose? : "))
                
                # fetch all / single as per choice GET
                if detailsChoice == 1 :
                    cursorObject = dataBase.cursor()
                    query = """SELECT * FROM train ORDER BY trainno ASC"""
                    cursorObject.execute(query)
                    myresult = cursorObject.fetchall()

                    for row in myresult :
                        print('='*80)
                        print("Train Number : ", row[0])
                        print("Train name : ", row[5])
                        print("Number of First Class : ", row[1])
                        print("Number of Second Class : ", row[2])
                        print("Number of Third Class : ", row[3])
                        print("Number of Sleepers : ", row[4])
                        print("Starting Point : ", row[6])
                        print("Destination Point : ", row[7])
                        print('='*80)
                else :
                    selectedTrain = int(input("\n\nEnter train number: "))
                    
                    cursorObject = dataBase.cursor()
                    query = """SELECT * FROM train WHERE trainno = %s"""
                    cursorObject.execute(query, (selectedTrain, ))
                    myresult = cursorObject.fetchall()

                    for row in myresult :
                        print("Your train details: \n")
                        print("Train Number : ", row[0])
                        print("Train name : ", row[5])
                        print("Number of First Class : ", row[1])
                        print("Number of Second Class : ", row[2])
                        print("Number of Third Class : ", row[3])
                        print("Number of Sleepers : ", row[4])
                        print("Starting Point : ", row[6])
                        print("Destination Point : ", row[7])
            elif ch==3:
                print('='*80)
                print("\t\t\t\tRESERVATION OF TICKETS")
                print('='*80)
                print("\n")
                tick.reservation()                
            elif ch==4:
                print("="*80)
                print("\t\t\t\tCANCELLATION OF TICKETS\n")
                print("="*80)
                print("\n")
                tick.cancellation()
            elif ch==5:
                print("="*80)
                print("PNR STATUS".center(80))
                print("="*80)
                print('')
                tick.display()
            elif ch==6:
                quit()               
            
            # Disconnecting from the server
            # dataBase.close()

            input("PRESS ENTER TO GO TO BACK MENU".center(80))


print("\t\tWELCOME TO EASTERN RAILWAYS\n")
print("\n\t\tBy:-")
print("\t\tARPAN SAHA\n")
print("\n\n\n\n\n\n\n\n\t\tLOADING. .")
time.sleep(1)
print (".")
time.sleep(0.5)
print (".")
time.sleep(2)

# creating database cursorObject.execute("CREATE DATABASE railway")
menu()


  