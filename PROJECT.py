import time 
print("Please insert Your CARD")

time.sleep(5)

password=1234

pin = int(input("Enter Your PIN "))
balance = 5000

if pin==password:
    print("""
        1==balance
        2==withdraw balance
        3==deposite balance
        4==balance inquary
        5=exit
        """)
    try :
        option=int(input("please enter your choice "))
    except:
        print("please enter valid option ")   

    if option==1:
        print(f"your current balance is {balance}")   
    if option==2:

        withdraw_amount=int(input("please enter withdraw amount "))

        balance=balance-withdraw_amount

        print(f"{withdraw_amount}is dabited from your account...")      

        print(f"your updated balance is {balance}")

    if option==3:

        deposite_amount=int(input("please enter deposite amount "))

        balance=balance+deposite_amount

        print(f"{withdraw_amount}is credited  your account...")      

        print(f"your current balance is {balance}")

    if option==4:
        break    







else:
    print("Wrong pin please try again.")

