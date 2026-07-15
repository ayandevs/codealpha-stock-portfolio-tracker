stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 150,
    "MSFT" : 300
}

total_amount = 0
stock_details = {}
quantity_details = 0

print("="*35)
print("Welcome to Stock Portfolio Tracker")
print("="*35 , "\n")

for key,value in stock_prices.items() :
    print(f"{key} : {value}")

print("\n")

while True :
    stock = input("Enter the stock name you have : ").upper()

    if stock not in stock_prices :
        print("Sorry, Stock not found!")
        continue

    quantity = int(input("Enter the quantity you have : "))

    if quantity < 0 :
        print("Invalid quantity! Please enter a positive number.")
        continue
    
    stock_details.update({stock:quantity})

    quantity_details += quantity

    total_amount += stock_prices[stock]*quantity

    choice = input("You want to add another stock?? (Yes/No) : ").lower()

    if(choice == "no") :
        break
    
    print("\n")

print("\nYour Stock Portfolio Details : \n")

for i  in stock_details :
    print(f"Stock Name : {i} | Price : {stock_prices[i]}$")

print(f"Your total investment in stocks is : {str(total_amount)}$")

with open("portfolio.txt" , "w") as f:

    f.write("Your Stock Portfolio Details : \n")
    f.write("\n")

    for i  in stock_details :
        f.write(f"Stock Name : {i} | Price : {stock_prices[i]}$\n")
    
    f.write("\n")

    for i in stock_details :
        f.write(f"you have \"{stock_details[i]}\" stocks of \"{i}\" \n")
    
    f.write(f"\nYour total stocks quantity is : {str(quantity_details)}")
    f.write(f"\nYour total investment in stocks is : {str(total_amount)}$")

print("\nYour investment detail is stored in portfolio.txt")