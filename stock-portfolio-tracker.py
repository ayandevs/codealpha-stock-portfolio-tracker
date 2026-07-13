stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 150,
    "MSFT" : 300
}

total_amount = 0
stock_details = []

print("="*35)
print("Welcome to Stock Portfolio Tracker")
print("="*35 , "\n")

while True :
    stock = input("Enter the stock name you have : ").upper()

    if stock not in stock_prices :
        print("Sorry, Stock not found!")
        continue
    
    stock_details.append(stock)

    quantity = int(input("Enter the quantity you have : "))

    total_amount += stock_prices[stock]*quantity

    choice = input("You want to add another stock?? (Yes/No) : ").lower()

    if(choice == "no") :
        break
    
for i  in stock_details :
    print(f"Stock Name : {i} | Price : {stock_prices[i]}$")

with open("portfolio.txt" , "w") as f:
    for i  in stock_details :
        f.write(f"Stock Name : {i} | Price : {stock_prices[i]}$\n")
    f.write(f"Your total investment in stocks is : {str(total_amount)}$")

print("Your investment detail is stored in portfolio.txt")