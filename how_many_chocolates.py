#m=chocolates, c=cost of one chocolate, 3*c[w]=1m
def number_of_chocolates(total_money, cost_of_one):
    if cost_of_one > total_money:
        return "no money"
    else:
        chocolates = total_money // cost_of_one     # total chocolates that he can get
        wrappers = chocolates               # number of wrappers
        while(wrappers // 3 != 0):          # 3 wrappers = 1 chocolate. so wrappers should be >= 3
            wrappers = wrappers // 3        # number of chocolates we get from wrappers
            chocolates += chocolates % 3 + wrappers    # adding together
   
    return chocolates

print(number_of_chocolates(18, 2))  