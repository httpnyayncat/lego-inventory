#lego inventory
lego_inventory = []

print("🧱 Welcome to LEGO Inventory Tracker!")

while True:
    print("\nChoose an option:")
    print("1. Add LEGO piece")
    print("2. View inventory")
    print("3. Remove LEGO piece")
    print("4. Count pieces")
    print("5. Exit")

    choice = input("Enter number: ")

    # ADD PIECE
    if choice == "1":
        piece = input("Enter LEGO piece: ")

if piece in lego_inventory:
    lego_inventory[piece] += 1
else:
    lego_inventory[piece] = 1

    # VIEW INVENTORY
    elif choice == "2":
        print("\nYour LEGO Inventory:")

        if len(lego_inventory) == 0:
            print("Inventory is empty.")
        else:
            for item in lego_inventory:
                print("-", item)

    # REMOVE PIECE
    elif choice == "3":
        remove_piece = input("Enter piece to remove: ")

        if remove_piece in lego_inventory:
            lego_inventory.remove(remove_piece)
            print(remove_piece, "removed!")
        else:
            print("Piece not found.")

    # COUNT PIECES
    elif choice == "4":
        print("Total pieces:", len(lego_inventory))

    # EXIT
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
