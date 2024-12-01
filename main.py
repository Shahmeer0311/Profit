Buy = int(input("How much did you buy the oranges for? "))
Sell = int(input("How much did you sell the oranges for? "))

if (Sell > Buy):
    Profit = Sell - Buy 
    print("Its a Profit of rupees" , Profit)
else:
    Profit = Sell - Buy 
    print("Its a Loss of rupees" , Profit)