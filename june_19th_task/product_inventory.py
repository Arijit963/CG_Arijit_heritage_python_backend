inventory = {}

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Search Product")
    print("4. Remove Product")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        product = input("Product Name: ")
        quantity = int(input("Quantity: "))
        inventory[product] = quantity

    elif choice == "2":
        product = input("Product Name: ")
        quantity = int(input("New Quantity: "))
        inventory[product] = quantity

    elif choice == "3":
        product = input("Search Product: ")
        print(inventory.get(product, "Product Not Found"))

    elif choice == "4":
        product = input("Remove Product: ")
        inventory.pop(product, None)

    elif choice == "5":
        break

    print(inventory)