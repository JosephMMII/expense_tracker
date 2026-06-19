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
    print("\n==== Expense Tracker ====\n")
    print("1. Add Expense\n2. View Expenses\n3. View Total Spending")
    print("4. Search by Category\n5. Save Expenses")
    print("6. Load Expenses\n7. Exit")

    try:
        choice = int(input("\n--Select category: "))
    except ValueError as e:
        print(f"Invalid entry: ({e})")
        continue

    if choice not in range(1,8): # Prevent input outside of category range
        print("Invalid entry")
        continue
    elif choice == 7:            # Exit program by user input
        sys.exit()

    if choice == 1:
        print("\n--What category?")
        print("1. Utilities\n2. Transportation\n3. Food\n4. Insurance\n5. Entertainment\n6. Personal Care\n7. Credit")
        
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
        for key, value in constants.final_category.items():
            print(key, value)
