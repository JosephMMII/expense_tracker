import sys
import constants
from func import Category as C

# category = {
#     "Utilities": [],
#     "Transportation": [],
#     "Food": [],
#     "Insurance": [],
#     "Entertainment": [],
#     "Personal Care": [],
#     "Credit": []
# }

while True:
    print("\n==== Expense Tracker ====\n")
    print("1. Add Expense\n2. View Expenses\n3. View Total Spending")
    print("4. Search by Category\n5. Save Expenses")
    print("6. Load Expenses\n7. Exit")

    try:
        choice = int(input("Select category: "))
    except ValueError as e:
        print(f"Invalid entry: ({e})")
        continue

    if choice not in range(1,8):
        print("Invalid entry")
        continue
    elif choice == 7:
        sys.exit()

    if choice == 1:
        print("\nWhat category?")
        print("1. Utilities\n2. Transportation\n3. Food\n4. Insurance\n5. Entertainment\n6. Personal Care\n7. Credit")
        
        try:
            cat = int(input("\nEnter number: "))
        except Exception as e:
            print(f"Invalid entry: ({e})")
            continue

        if cat not in range(1,8):
            print("Invalid entry. Number must be between 1-7.")
            continue

        while True:
            var = C.add_to_cat(cat)

            if var == False:
                break







            # if cat == 1:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Utilities"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Utilities'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 2:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Transportation"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Transportation'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 3:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Food"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Food'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 4:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Insurance"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Insurance'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 5:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Entertainment"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Entertainment'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 6:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Personal Care"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Personal Care'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            # elif cat == 7:
            #     try:
            #         num = float(input("Amount: "))
            #         category["Credit"].append(num)
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")
            #         continue

            #     try:
            #         cont = str(input("Want to add more to 'Credit'? (Y/N): "))
            #         if cont.lower() == "y":
            #             continue
            #         else:
            #             break
            #     except ValueError as e:
            #         print(f"Invalid entry: ({e})")

            break
    break