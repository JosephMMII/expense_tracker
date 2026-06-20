import constants

class ChooseCategory:

    def __init__(self, num: int):
        self.num = num
        self.categories = [
            "Utilities:", "Transportation:", "Food:", "Insurance:",
            "Entertainment:", "Personal Care:", "Credit:"
        ]

    def add_to_cat(self) -> bool:
        while True:
            cat = self.categories[(self.num - 1) % len(self.categories)]

            try:
                amount = float(input(f"Amount for {cat}: "))
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



