import json
class Transaction:
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display_info (self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type:{self.type}\n Note: {self.note}"

class Bank:
    def __init__(self):
        self.wallet = []

        #add a transaction
    def add_transaction(self, transaction):
            self.wallet.append(transaction)

        #remove a transaction 
    def del_transaction(self, title):
            for trans in self.wallet:
                if trans.title == title:
                    self.wallet.remove(trans)
                    return f"{title} has been removed"
            return f"{title} not found..."


        #display all transactions
    def display(self):
            if not self.wallet:
                return f"no transactions in your wallet"
            return f"\n".join([transaction.display_info() for transaction in self.wallet])

        #search for a transaction
    def search_wallet(self, query):
            found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in
            trans.type.lower()]
            if not found:
                return f"no transactions"
            return f"\n".join([transaction.display_info() for transaction in found])

        #save a transaction
    def save_file(self, filename="wallet.json"):
            data = [{'Expense': transaction.title, 'Amount':transaction.amount, 'Type': transaction.type, 'Note': transaction.note} for transaction in self.wallet]
            with open(filename, "w") as file:
                json.dump(data, file)

        
        #loading 
    def load_file(self, filename="wallet.json"):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                    self.wallet = [Transaction(trans['Expense'], trans['Amount'], trans['Type'], trans['Note']) for trans in data]
            except FileNotFoundError:
                print("we cannot find this file")


def main():
            wallet = Bank()

            while True:
                print("\n==== Personal Banking System ===")
                print("1. Add a transaction")
                print("2. Remove a transaction")
                print("3. Display all transactions")
                print("4. Search for a transaction")
                print("5. Save transaction")
                print("6. Load transactions from file")
                print("7. Exit")
                choice = input("Enter your choice (1....7):")

                if choice =="1":
                    title = input("Enter the title: ")
                    amount = float(input("Enter the amount: "))
                    type = input("Expense or Deposit: ")
                    transaction = Transaction(title, amount, type)
                    wallet.add_transaction(transaction)
                    print(f"{title} added succesfully")

                elif choice == "2":
                    title = input("Enter title: ")
                    print(wallet.del_transaction(title))

                elif choice == "3":
                    print(wallet.display())
                
                elif choice == "4":
                    query = input("Enter title or type: ")
                    print(wallet.search_wallet(query))

                elif choice =="5":
                    wallet.save_file()
                    print("Saved file as JSON")

                elif choice =="6":
                    wallet.load_file()
                    print("Loaded JSON")
                
                elif choice =="7":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
if __name__ in "__main__":
    main()


               
               
               

        
