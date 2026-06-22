import sys
import constants
import my_functions as mf

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

    # Restart loop if 'choice' not in range 
    # and exit program if 'choice' is 7
    if choice not in range(1,8): 
        print("\nInvalid entry. Number must be between 1-7.")
        continue
    elif choice == 7:
        sys.exit()

    # Add expenses by category
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

    # View all lists of expenses
    elif choice == 2: 
        print("\n==== List of Expenses ====")

        # Print key, value pair to user
        for key, value in constants.final_category.items():
            print(key, value)
        print("=" * 26)

    # View total expense
    elif choice == 3: 
        total = sum(sum(arr) for arr in constants.final_category.values())
        print(f"Total spending: (${total:.2f})")

    # Search list of expense by category
    elif choice == 4: 
        categories = list(constants.final_category.keys())

        while True:
            print("\n==== Search category ====")

            for idx, category in enumerate(categories, 1):
                print(f"{idx}. {category}")
            print("=" * 26)

            try:
                var = int(input("Select category to search: "))
            except ValueError as e:
                print(f"Invalid entry ({e})")
                continue

            if var not in range(1,8):
                print("invalid entry. Number must be between 1-7.")
                continue

            target_key = categories[var - 1]

            ans = input("Would you like to search another category? (Y/N): ").strip().lower()
            if ans != "y":
                break
            
    # Save expenses to excel file
    elif choice == 5: 
        df = mf.save_data()
        
        print("\n==== Expenses Saved ====")
        print(df)
        print("=" * 26)

    # Load expenses dataframe
    elif choice == 6: 
        mf.load_data()
