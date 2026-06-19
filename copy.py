import sys
from expense_tracker.my_functions import Category as C

while True:
    print("\n==== Expense Tracker ====\n")
    print("1. Add Expense\n2. View Expenses\n3. View Total Spending")
    print("4. Search by Category\n5. Save Expenses")
    print("6. Load Expenses\n7. Exit")

    category = {
        "Utilities": [],
        "Transportation": [],
        "Food": [],
        "Insurance": [],
        "Entertainment": [],
        "Personal Care": [],
        "Credit": []
    }

    while True:
        try:
            choice = int(input("Select category: "))
        except ValueError as e:
            print("Invalid entry: ({e})")
            continue

        if choice not in range(1,8):
            print("Invalid entry")
            continue

        if choice == 1:
            print("What category?\n")
            print("1. Utilities\n2.Transportation\n3. Food\n4. Insurance\n5. Entertainment\n6. Personal Care\n7. Credit")
            
            try:
                cat = int(input("Enter number: "))
            except ValueError as e:
                print(f"Invalid entry: ({e})")

            if cat not in range(1,8):
                print("Invalid entry. Number must be between 1-7.")
                continue

            while True:
                if cat == 1:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Utilities"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Utilities'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 2:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Transportation"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Transportation'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 3:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Food"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Food'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 4:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Insurance"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Insurance'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 5:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Entertainment"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Entertainment'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 6:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Personal Care"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Personal Care'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                if cat == 7:
                    try:
                        num = float(input(print("Amount: ")))
                        category["Credit"].append(num)
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")
                        continue

                    try:
                        cont = str(input("Want to add more to 'Credit'? (Y/N): "))
                        if cont.lower() == "y":
                            continue
                        else:
                            break
                    except ValueError as e:
                        print(f"Invalid entry: ({e})")

                break