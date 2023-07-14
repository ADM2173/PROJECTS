import pandas as pd
import matplotlib.pyplot as plt
a='y'
while a=='y':
    print("~~~~~~~~*******************************~~~~~~~~")
    print("~~~~~~~~~~~~~~~WELCOME DEAR USER~~~~~~~~~~~~~~~")
    print("~~~~~~~~*******************************~~~~~~~~")
    print("COMPREHEND THE DATA IN DIFFERENT WAYS")
    print("1.TO READ THE DATA IN TABULAR FORM.")
    print("2.RETRIVE DATA IN LINE GRAPH FORM.")
    print("3.RETRIVE DATA IN BAR GRAPH FORM.")
    print("4.RETRIVE DATA FOR INDIA IN DIFFERENT WAYS.")
    print("5.READING DATA IN CONDITIONAL WAYS.")
    print("6.EXIT")
    print("~~~~~~~~*******************************~~~~~~~~")
    print("~~~~~~~~*******************************~~~~~~~~")
    print("~~~~NOTE:YOU WILL GET THE DATA UPTO 1-JANUARY 2021~~~~")
    x=int(input("Enter an option for which you are looking:"))
    if x==1:
        print("Whole data")
        df1=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\ORIGINAL.csv")
        print(df1)
    elif x==2:
          df1=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\ORIGINAL.csv")
          print("USING LINE GRAPHS")
          st=df1["State"]
          conf=df1["Confirmed"]
          rec=df1["Recovered"]
          dc=df1["Deaths"]
          ts=df1["Tested"]
          plt.xlabel("State")
          plt.xticks(rotation="vertical")
          print("SELECT AN OPTION FROM THE FOLLOWING:")
          print("1.RETRIVE DATA FOR STATE VS CONFIRMED CASES.")
          print("2.RETRIVE DATA FOR STATE VS RECOVERED CASES.")
          print("3.RETRIVE DATA FOR STATE VS DEATHS.")
          print("4.RETRIVE DATA FOR STATE VS PEOPLE TESTED.")
          print("5.DISPLAY ALL THE LINE GRAPH.")
          print("~~~~~~~~*******************************~~~~~~~~")
          x1=int(input("Enter an option for which you are looking:"))
          if x1==1:
                 plt.ylabel("Confirmed cases")
                 plt.plot(st,conf,color='indigo')
                 plt.title("State vs Confirmed cases")
                 plt.show()
          elif x1==2:
                 plt.ylabel("Recovered cases")
                 plt.title("State vs Recovereded cases")
                 plt.plot(st,rec,color='blue')
                 plt.show()
          elif x1==3:
                 plt.ylabel("Deaths")
                 plt.title("State vs Deaths")
                 plt.plot(st,dc,color='green')
                 plt.show()
          elif x1==4:
                 plt.ylabel("Total people tested")
                 plt.title("State vs people Tested")
                 plt.plot(st,ts,color='orange')
                 plt.show()
          elif x1==5:
                 plt.ylabel("Number of cases")
                 plt.plot(st,conf,label='state vs confirmed cases')
                 plt.plot(st,rec,label="state vs recovered cases")
                 plt.plot(st,dc,label='state vs death cases')
                 plt.legend()
                 plt.show()
          else :
                 print("Enter a valid option")
    elif x==3:
          df1=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\ORIGINAL.csv")
          st=df1["State"]
          conf=df1["Confirmed"]
          rec=df1["Recovered"]
          dc=df1["Deaths"]
          ts=df1["Tested"]
          plt.xlabel("State")
          plt.xticks(rotation="vertical")
          print("1.RETRIVE THE DATA FOR STATE VS CONFIRMED CASES.")
          print("2.RETRIVE THE DATA FOR STATE VS RECOVERED CASES.")
          print("3.RETRIVE THE DATA FOR STATE VS DEATHS.")
          print("4.RETRIVE THE DATA FOR STATE VS PEOPLE TESTED.")
          print("5.RETRIVE THE DATA FOR STATE VS ALL CASES IN STACK BAR FORM.")
          print("USING BAR GRAPH:")
          print("~~~~~~~~*******************************~~~~~~~~")
          x2=int(input("Enter an option for which you are looking:"))
          if x2==1:
                 plt.ylabel("Confirmed cases")
                 plt.title("State vs Confirmed cases")
                 plt.bar(st,conf,color='indigo',width=.50)
                 plt.show()
          elif x2==2:
                  plt.ylabel("Recovered cases")
                  plt.title("State vs Recovered cases")
                  plt.bar(st,rec,color='red',width=.50)
                  plt.show()
          elif x2==3:
                  plt.ylabel("Deaths")
                  plt.title("State vs Death")
                  plt.bar(st,dc,color='green',width=.50)
                  plt.show()
          elif x2==4:
                  plt.ylabel("People tested")
                  plt.title("State vs People tested")
                  plt.bar(st,ts,color='purple')
                  plt.show()
          elif x2==5:
                  plt.ylabel("Cases")
                  plt.title("State vs Cases")
                  plt.bar(st,conf,width=0.2,label="State wise confirmed cases")
                  plt.bar(st,rec,width=0.2,label="State wise recovered cases")
                  plt.bar(st,dc,width=0.2,label="State wise death cases")
                  plt.legend()
                  plt.show()
          else:
                 print("Enter valid option")
    elif x==4:
        print("1.READ THE CSV FILE")
        print("2.READ THE GRAPH OF NUMBER OF CONFIRMED CASES IN INDIA.")
        print("3.READ THE GRAPH OF NUMBER OF ACTIVE CASES IN INDIA.")
        print("4.READ THE GRAPH OF NUMBER OF RECOVERED CASES IN INDIA.")
        print("5.READ THE GRAPH OF NUMBER OF DEATHS CASES IN INDIA.")
        print("6.READ THE GRAPH OF NUMBER OF PEOPLE TESTED IN INDIA.")
        print("7.DISPLAY ALL THE LINE GRAPH.")
        print("~~~~~~~~*******************************~~~~~~~~")
        xx=int(input('Enter an option for which you are looking:'))
        if xx==1:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            print(df2)
        if xx==2:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            conf1=df2["Confirmed cases"]
            plt.xlabel("Dates")
            plt.ylabel("Confirmed cases")
            plt.xticks(rotation="vertical")
            plt.plot(st1,conf1,color='red')
            plt.title("Number of Confirmed cases")
            plt.show()
        elif xx==3:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            ac1=df2["Active cases"]
            plt.xlabel("Dates")
            plt.ylabel("Active cases")
            plt.xticks(rotation="vertical")
            plt.plot(st1,ac1,color='orange')
            plt.title("Number of active cases")
            plt.show()
        elif xx==4:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            rc1=df2["Recovered cases"]
            plt.xlabel("Dates")
            plt.ylabel("Recovered cases")
            plt.xticks(rotation="vertical")
            plt.plot(st1,rc1,color='green')
            plt.title("Number of Recovered cases")
            plt.show()    
        elif xx==5:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            dc1=df2["Deaths"]
            plt.xlabel("Dates")
            plt.ylabel("Death cases")
            plt.xticks(rotation='vertical')
            plt.plot(st1,dc1,color='indigo')
            plt.title("Number of death cases")
            plt.show()
        elif xx==6:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            ts1=df2["Tested"]
            plt.xlabel("Dates")
            plt.ylabel("People tested")
            plt.xticks(rotation="vertical")
            plt.plot(st1,ts1,color='gold')
            plt.title("Nummber of people tested")
            plt.show()
        elif xx==7:
            df2=pd.read_csv("C:\\Users\\adity\\OneDrive\\Desktop\\activemh.csv")
            st1=df2["Date"]
            conf1=df2["Confirmed cases"]
            ac1=df2["Active cases"]
            rc1=df2["Recovered cases"]
            dc1=df2["Deaths"]
            ts1=df2["Tested"]
            plt.ylabel("No. of cases")
            plt.plot(st1,ac1,label='Date vs Active cases')
            plt.plot(st1,dc1,label='Date vs Death cases')
            plt.plot(st1,ts1,label='Date vs People tested')
            plt.plot(st1,rc1,label="Date vs Recovered cases")
            plt.plot(st1,conf1,label='Date vs Confirmed cases')
            plt.xticks(rotation="vertical")
            plt.legend()
            plt.show()
        else :
            print("Enter a valid option")
    elif x==5:
            print("1.RETRIVE DATA FOR TOP VALUES")
            print("2.RETRIVE DATA FOR BOTTOM VALUES")
            op=int(input("Enter an option for which you are looking:"))
            if op==1:
                print("1.STATE WITH MOST CONFIRMED CASES")
                print("2.STATE WITH MOST RECOVERED CASES")
                print("3.STATE WITH MOST DEATHS")
                print("4.STATE WITH MOST PEOPLE TESTED")
                op1=int(input("Enter an option for which you are looking:"))
                print("NOTE:MAXIMUM ROWS ARE 20")
                if op1==1:
                    dff=pd.read_csv('Book1.csv',index_col=0)
                    x=int(input("Enter the number of state u want from top:"))
                    if x==1:
                        print("\n\nTHE STATE HAVING HIGHEST NUMBER OF CONFIRMED CASES:")
                        print(dff.head(1))
                    elif x>1 and x<=20: 
                        print("\n\nThe top",x,"State having highest number of Confirmed cases")
                        dff1=dff.head(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")     
                elif op1==2:
                    dff=pd.read_csv('book3.csv',index_col=0)
                    x=int(input("Enter an option for which you are looking:"))
                    print("NOTE:MAXIMUM ROWS ARE 20")
                    if x==1:
                        print("\n\nTHE STATE HAVING HIGHEST NUMBER OF RECOVERED CASES:")
                        print(dff.head(1))
                    elif x>1 or x<=19:  
                        print("\n\nThe top",x,"State having highest number of Recovered cases")
                        dff1=dff.head(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")    
                elif op1==3:
                    dff=pd.read_csv('Book2.csv')
                    x=int(input("Enter the number of state u want from top:"))
                    print("NOTE:MAXIMUM ROWS ARE 20")
                    if x==1:
                        print("\n\nTHE STATE HAVING HIGHEST NUMBER OF DEATHS IS:")
                        print(dff.head(1))
                    elif x>1 or x<=19:    
                        print("\n\nThe top",x,"State having highest number of Deaths")
                        dff1=dff.head(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")     
                elif op1==4:
                    dff=pd.read_csv('check1.csv',index_col=0)
                    x=int(input("\n\nEnter the number of state u want from top:"))
                    print("NOTE:MAXIMUM ROWS ARE 20")
                    if x==1:
                        print("THE STATE HAVING HIGHEST NUMBER OF PEOPLE TESTED:")
                        print(dff.head(1))
                    elif x>1 or x<=19:   
                        print("\n\nThe top",x,"State having highest number of people tested")
                        dff1=dff.head(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")
                else:
                    print("Enter a valid option")
            elif op==2:
                print("1.STATE WITH LEAST CONFIRMED CASES")
                print("2.STATE WITH LEAST RECOVERED CASES")
                print("3.STATE WITH LEAST DEATHS")
                print("4.STATE WITH LEAST PEOPLE TESTED")
                op1=int(input("Enter an option for which you are looking:"))
                if op1==1:
                    dff=pd.read_csv('Book1.csv',index_col=0)
                    x=int(input("Enter the number of state u want from Bottom:"))
                    if x==1:
                        print("\n\nTHE STATE HAVING LOWEST NUMBER OF CONFIRMED CASES:")
                        print(dff.tail(1))
                    elif x>1 or x<=19:    
                        print("\n\nThe bottom",x,"State having lowest confirmed cases")
                        dff1=dff.tail(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")    
                elif op1==2:
                    dff=pd.read_csv('book3.csv',index_col=0)
                    x=int(input("\n\nEnter the number of state u want from bottom:"))
                    if x==1:
                        print("THE STATE HAVING LOWEST NUMBER OF RECOVERED CASES:")
                        print(dff.tail(1))
                    elif x>1 or x<=19:
                        print("\n\nThe bottom",x,"State having lowest Recovered cases")
                        dff1=dff.tail(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")
                elif op1==3:
                    dff=pd.read_csv('Book2.csv',index_col=0)
                    x=int(input("\n\nEnter the number of state u want from bottom:"))
                    if x==1:
                        print("THE STATE HAVING LOWEST NUMBER OF DEATHS:")
                        print(dff.tail(1))
                    elif x>1 or x<=19:
                        print("\n\nThe bottom",x,"State having lowest Deaths")
                        dff1=dff.tail(x)
                        print(dff1)
                    else:
                        print("Enter a valid option")
                elif op1==4:
                    dff=pd.read_csv('check1.csv',index_col=0)
                    x=int(input("\n\nEnter the number of state u want from bottom:"))
                    if x==1:
                        print("THE STATE HAVING LOWEST NUMBER OF PEOPLE TESTED:")
                        print(dff.tail(1))
                    else:
                        print("\n\nThe bottom",x,"State having lowest number of people tested")
                        dff1=dff.tail(x)
                        print(dff1)    
                else:
                    print("Enter a valid option")
            else:
                print("Enter a valid option")
    elif x==6:
        print("~~~~~~~~~~~*************!!!!!!!!!!!!THANK YOU!!!!!!!!!!!!*************~~~~~~~~~~~")
        print("~~~~~~~~~~~*************!!!!!!!!HAVE A GREAT DAY!!!!!!!!!*************~~~~~~~~~~~")
        exit()
    else:
        print("Enter a valid option")
        
     while a!='y'and'n':
            print("Enter a valid option")
            print("Want to run the program y/n?")
            a=str(input("Enter you're choice:"))
