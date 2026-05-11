import json
from colorama import Fore
import time
import os
from datetime import datetime

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

def clear_screen():
        os.system("cls")      
while True:
    clear_screen()
    print("\n" + "=" * 40)
    print(Fore.CYAN + "💰 EXPENSE TRACKER")
    print("=" * 40)
    print(Fore.LIGHTBLUE_EX + "1 . Add Expense")
    print(Fore.LIGHTBLUE_EX +"2 . View Expense")
    print(Fore.LIGHTBLUE_EX +"3 . Show Total")
    print (Fore.LIGHTBLUE_EX +"4 . Delete Expense")
    print(Fore.LIGHTBLUE_EX+"5 . Search Expense")
    print(Fore.LIGHTBLUE_EX +"6 . Search By Category")
    print(Fore.LIGHTBLUE_EX + "7 . Expense Statistics")
    print(Fore.LIGHTBLUE_EX + "8 . Reset Expenses")
    print(Fore.LIGHTBLUE_EX +"9 . Exit Program")
    choice = input("enter your choce : ")

    if choice == "1":
        name = input("enter expense name : ")
        category = input("enter category: ")
        amount = float(input("enter the expense amount in rupees :"))
        date =datetime.now().strftime("%d-%m-%Y %H:%M")
        expense = { "name" : name, "amount" : amount, "category": category, "date": date}
        expenses.append(expense)
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print(Fore.GREEN + "\n✅ Expense added successfully!")   
        time.sleep(1)


    elif choice =="2":
        print("view expense selected")
        if len(expenses) == 0:
            print (Fore.RED + "no expense addd yet")

        else :
            print("----expenses-----")
            for expense in expenses:
                print("-" * 40)
                print(f"📌 Name     : {expense['name']}")
                print(f"📂 Category : {expense['category']}")
                print(f"💵 Amount   : ₹{expense['amount']}") 
                print(f"📅 Date      : {expense['date']}")   
                time.sleep(10)

    elif choice == "3":
        print("show total selected")
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
            print("\n" + "=" * 40)
            print(Fore.YELLOW + f"💰 Total Expenses: ₹{total}")
            print("=" * 40)
            time.sleep(8)

    elif choice == "4":
        delete_name = input("enter expense name to delete: ")
        found = False
        for expense in expenses:
            if expense["name"].lower() == delete_name.lower():
                expenses.remove(expense)
                with open("expenses.json", "w") as file:
                   json.dump(expenses, file, indent=4)
                print(Fore.LIGHTMAGENTA_EX + "\n🗑️ Expense deleted successfully!")
                found = True
                break
            if not found:
                print(Fore.RED + "\n❌ Expense not found.")
                time.sleep(1)        

    elif choice == "5":
        print("search expense")
        search_name = input("enter expense name to search: ")
        found = False
        for expense in expenses:
            if expense["name"].lower() == search_name.lower():
                print("expense found")
                print("-" * 40)
                print(f"📌 Name     : {expense['name']}")
                print(f"📂 Category : {expense['category']}")
                print(f"💵 Amount   : ₹{expense['amount']}")
                print(f"📅 Date      : {expense['date']}")
                found = True
                if not found:
                    print(Fore.RED + "\n❌ Expense not found.")
                    time.sleep(10)

    elif choice == "6":
        print("search by category")
        search_caegory = input("enetr category name: ")
        found = False
        print("matching expenses")
        for expense in expenses:
            if expense["category"].lower() == search_caegory.lower():
                print("-" * 40)
                print(f"📌 Name     : {expense['name']}")
                print(f"📂 Category : {expense['category']}")
                print(f"💵 Amount   : ₹{expense['amount']}")
                print(f"📅 Date      : {expense['date']}")
                found = True
                if not found:
                    print(Fore.RED + "\n❌ No such category exist.")
                    time.sleep(10)

    elif choice == "7":


         if len(expenses) == 0:
          print(Fore.RED + "No expenses available.")

         else:

          total = 0
          highest = expenses[0]["amount"]
          lowest = expenses[0]["amount"]

          for expense in expenses:

            amount = expense["amount"]

            total += amount

            if amount > highest:
                highest = amount

            if amount < lowest:
                lowest = amount

            print("\n" + "=" * 40)
            print(Fore.YELLOW + "📊 EXPENSE STATISTICS")
            print("=" * 40)

            print(f"💰 Total Expenses : ₹{total}")
            print(f"📈 Highest Expense : ₹{highest}")
            print(f"📉 Lowest Expense : ₹{lowest}")
            print(f"🧾 Total Entries : {len(expenses)}")

            print("=" * 40)

            time.sleep(10)

    elif choice == "8":

     confirm = input(Fore.RED + "Are you sure you want to delete ALL expenses? (yes/no): ")

     if confirm.lower() == "yes":

        expenses.clear()

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print(Fore.GREEN + "\n✅ All expenses reset successfully!")

     else:
        print(Fore.YELLOW + "\nReset cancelled.")

     time.sleep(4)        

     
    
    
    elif choice == "9":
      print("exiting program")

    else:
      print("invalid choice")

