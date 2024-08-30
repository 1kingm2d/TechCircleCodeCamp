import json

filePath = "IMSDB.json"

def loadDB():
    try:
        with open(filePath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def saveToDB(products):
    with open(filePath, "w") as file:
        json.dump(products, file, indent=4)

def addProduct(name, price, quantity):
    product = loadDB()
    newName = name.lower()
    product[newName] = {"quantity": quantity, "price": price}
    saveToDB(product)
    print(f"Product '{name}' added successfully")

def deleteProduct(product):
    
    products = loadDB()
    if product in products:
        del products[product]
        saveToDB(products)
        print(f"{product} deleted successfully")
    else:
        print(f"No records found for {product}")

def viewAllProducts():
    products = loadDB()

    if products:
        print("\n-- Product List --")
        for name, details in products.items():
            print(f"Product: {name}")
            print(f"Quantity: {details['quantity']}")
            print(f"Price: ${details['price']}")
            print("-" * 20)
    else:
        print("No products found")

def searchProduct(productName):
    products = loadDB()

    productName = productName.lower()

    if productName in products:
        details = products[productName]
        print(f"Found: {productName} - Price: {details['price']} - quantity: {details['quantity']}")
    else:
        print(f"No record found for {productName}")

def updateStock(name, quantity):
    products = loadDB()
    if name in products:
        products[name]['quantity'] += quantity
    else:
        print(f"Product {name} not found in inventory.")


while True:
    print("\nProduct Management Menu")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search for a Product")
    print("4. modify a Product")
    print("5. Delete a Product")
    print("6. Quit")

    choice = input("Choose an option (1 - 6 ): ")

    if choice == "1":
        productName = input("Enter name of product: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity in stock: "))

        addProduct(productName, price, quantity)

    elif choice == "2":
        viewAllProducts()
    elif choice == "3":
        productName = input("Enter name of product: ")
        searchProduct(productName)
    elif choice == "4":
        name = input("Product name: ")
        quantity = int(input("Add quantity: "))
        updateStock(name, quantity)
    elif choice == "5":
        name = input("Enter a name: ")
        cho = input(f"Are you sure you want to delete {name}: ")
        if cho.lower() == "y" or cho.lower() == "yes":
            deleteProduct(name)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("invalid operation number")