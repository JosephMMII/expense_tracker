import sys
import constants
import my_functions as mf

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
    ### Prompt to select what user wants to do ###
    print("\n==== Expense Tracker ====")
    print("1. Add Expense\n2. View Expenses\n3. View Total Spending")
    print("4. Search by Category\n5. Save Expenses")
    print("6. Load Expenses\n7. Exit")
    print("=" * 26)

    try:
        choice = int(input("\n--Select category: "))
    except ValueError as e:
        print(f"Invalid entry: ({e})")
        continue

    if choice not in range(1,8): # Prevent input outside of category range
        print("\nInvalid entry. Number must be between 1-7.")
        continue
    elif choice == 7:            # Exit program by user input
        sys.exit()

    if choice == 1:
        print("\n==== Enter category ====")
        print("1. Utilities\n2. Transportation\n3. Food\n4. Insurance\n5. Entertainment\n6. Personal Care\n7. Credit")
        print("=" * 26)
        
        try:
            cat = int(input("\n--Enter number: "))
        except Exception as e:
            print(f"Invalid entry: ({e})")
            continue

        if cat not in range(1,8):
            print("\nInvalid entry. Number must be between 1-7.")
            continue

        var = mf.ChooseCategory(cat)
        var.add_to_cat()

        if var == False:
            break
    elif choice == 2:
        print("\n==== List of Expenses ====")

        # Print key, value pair to user
        for key, value in constants.final_category.items():
            print(key, value)
        print("=" * 26)
    elif choice == 3:
        value = list(constants.final_category.values())
        total = 0

        for arr in value:
            total += sum(arr)
        
        print(f"Total spending: (${total})")
    elif choice == 4:
        print("\n==== Search category ====")
        print("1. Utilities\n2. Transportation\n3. Food\n4. Insurance\n5. Entertainment\n6. Personal Care\n7. Credit")
        print("=" * 26)

        while True:
            try:
                var = int(input("Select category to search: "))
            except ValueError as e:
                print(f"Invalid entry ({e})")
                continue

            if var not in range(1,8):
                print("Invalid entry. Number must be between 1-7.")
                continue

            count = 0
            for key, value in constants.final_category.items():
                count += 1
                if count == var:
                    print(key, value)
                    break


            try:
                ans = str(input("Would you like to search another category? (Y/N): "))
            except ValueError as e:
                print(f"Invalid entry ({e})")
                continue

            if ans.lower() == "y":
                continue
            else:
                break


