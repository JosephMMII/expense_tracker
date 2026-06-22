import os
import constants
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

class ChooseCategory:

    def __init__(self, num: int):
        self.num = num
        self.categories = [
            "Utilities:",
            "Transportation:",
            "Food:",
            "Insurance:",
            "Entertainment:",
            "Personal Care:",
            "Credit:"
        ]

    def add_to_cat(self) -> None:
        while True:
            cat = self.categories[(self.num - 1) % len(self.categories)]

            try:
                amount = float(input(f"Amount for {cat} "))
                constants.final_category[cat].append(amount)
            except ValueError as e:
                print(f"Invalid entry: ({e})")
                continue
            
            try:
                cont = input(f"Add more to '{cat}'? (Y/N): ")
                if str(cont.lower()) == "y":
                    continue
                else:
                    return False
            except ValueError as e:
                print(f"Invalid entry ({e})")
                continue

def get_storage_path() -> Path:
    env_path = os.getenv("EXPENSE_TRACKER_DIR")
    if env_path:
        return Path(env_path)
    
    # If no .env exists, resolve from parent folder
    return Path(__file__).parent.resolve()

def save_data() -> pd.DataFrame:
    cat_dict = constants.final_category
    
    # Change data into flat list
    flat_rows = []
    for expense, amounts in cat_dict.items():
        for amount in amounts:
            flat_rows.append({"Category": expense, "Amount": amount})

    # Build DataFrame 
    df = pd.DataFrame(flat_rows)

    # Use dynamic path tracker
    output_path = get_storage_path() / "expense_dataframe.xlsx"
    df.to_excel(output_path, index=False)

    return df
            

def load_data() -> pd.DataFrame:
    # Find file using dynamic path tracker
    file_path = get_storage_path() / "expense_dataframe.xlsx"

    if not file_path.exists():
        print("\nNo saved data file found.")
        return
    
    # Reset categories
    for key in constants.final_category:
        constants.final_category[key] = []

    # Read excel file and add to program dictionary
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        cat = row["category"]
        amt = row["Amount"]
        
        if cat in constants.final_category:
            constants.final_category[cat].append(amt)
        
        print("\n==== Expenses Loaded Successfully ====")
