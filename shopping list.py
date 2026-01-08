def display_menu():
    print("\n--- Shopping List Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View all items")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == "2":
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the list.")

        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
