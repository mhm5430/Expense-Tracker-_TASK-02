def run_expense_tracker():
    
    total_spent = 0.0

    print("==========================================")
    print("      DECODELABS - EXPENSE TRACKER        ")
    print("==========================================")
    print("Enter expense amounts. Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter expense amount (or 'quit'): ").strip()

        if user_input.lower() == 'quit':
            print("\n------------------------------------------")
            print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
            print("------------------------------------------")
            print("Execution halted safely. Goodbye!")
            break

        try:
            expense = float(user_input)
            
           
            if expense < 0:
                print("⚠️ Invalid Input: Expense cannot be negative.\n")
                continue

            
            total_spent += expense
            print(f"✅ Added ${expense:.2f} | Current Total: ${total_spent:.2f}\n")

        except ValueError:
        
            print("❌ Invalid Data: Please enter a numeric amount or 'quit'.\n")

if __name__ == "__main__":
    run_expense_tracker()