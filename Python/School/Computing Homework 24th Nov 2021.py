choice = 0

products = ["the product", "them products", "these products", "all of these products"]
stock = [1,2,3,4]
while choice != 7:

    print("Menu \n")
    print("")
    print("1. View products\n")
    print("2. Add product\n")
    print("3. Remove Product\n")
    print("4. Sell\n")
    print("5. Replenish\n")
    print("6. View stock\n")
    print("7. Exit")
    print("")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        print("The products in your basket are:", products)
        print("")

    elif choice == 2:

        productToAppend = input("Product name: ")
        stockToAppend = input("Product stock: ")
        if stockToAppend.isnumeric() == True:
          products.append(productToAppend)
          stock.append(int(stockToAppend))
          verify = False
        else:
          print("Invalid")
        print("")

    elif choice == 3:

        productToRemove = input("Product index: ")
        if productToRemove.isnumeric() == True:
          if int(productToRemove)<len(products):
            products.pop(int(productToRemove))
            stock.pop(int(productToRemove))
          else:
            print ("Invalid, you don't have this item.")
        else:
          print("Invalid")
        print("")

    elif choice == 4:

        productToSell = input("Product index: ")
        if productToSell.isnumeric() == True:
          numberOfProduct = input("Number sold: ")
          if int(productToSell)<len(products):
            if numberOfProduct.isnumeric() == True:
              if stock[int(productToSell)]-int(numberOfProduct) > 0:
                stock[int(productToSell)] = stock[int(productToSell)]-int(numberOfProduct)
              else:
                print("Not enough stock")
            else:
              print("Invalid")
          else:
            print("Invalid, you don't have this item")
        else:
          print("Invalid")
        print("")

    elif choice == 5:

        productToReplensish = input("Product index: ")
        if productToReplensish.isnumeric() == True:
          if int(productToReplensish)<len(products):
            numberToReplenish = input("Number replenished: ")
            if productToReplensish.isnumeric() == True:
              stock[int(productToReplensish)] = stock[int(productToReplensish)]+int(numberToReplenish)
            else:
              print("Invalid")
          else:
            print("Invalid, you don't have this item")
        else:
          print("Invalid")

        print("")

    elif choice == 6:

        print(stock)
        print("")

    elif choice == 7:
        exit()
