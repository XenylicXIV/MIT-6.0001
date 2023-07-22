 

# annual_salary= float(input('Please enter your annual salary:\n$'))


#Need conditions for invalid str input coversion
# per_save=float(input('What percentage of your annual salary are you saving?\n'))
# portion_saved=(annual_salary*per_save/12)

# total_cost=float(input('What is the cost of your dream home?\n$'))
# portion_down_payment=total_cost*.25

# per_raise= float(input('Please enter your semi-annual raise percentage.\n'))
#raise percentage
def savings_test(portion_down_payment, per_raise, per_save, annual_salary):
    current_savings=0
    months=1
    portion_saved=(annual_salary*per_save/12)
    while current_savings < portion_down_payment:
        if months != 0 and months % 6 == 0:
            semi_raise=annual_salary*per_raise
            annual_salary+=semi_raise
            portion_saved=(annual_salary*per_save/12)

        inv_per=.04/12
        invest_earn=current_savings*inv_per
        current_savings += portion_saved + invest_earn
        months+=1
    return months

# savings_test(250000, .07, , 1000000)

per_save = list(range(10001))
target = 36
max=per_save[len(per_save) - 1]
min=per_save[0]
months= target + 1
steps=0

while months != target:
    mid=int((min+max)/2)
    months= savings_test(250000, .07, (mid/10000), 150000)
    # print("Months: " + str(months) + ", Mid: " + str(mid/10000))
    if target < months:
        if min==mid:
            print('You\'re too poor lol')
            break
        min=mid
    elif target > months:
        max=mid
    steps+=1
print(mid/10000)
print(months)
print(steps)
# print('It will take ' + str(months) + ' months to reach the down payment of $'+ 
#       str("{:.2f}".format(portion_down_payment)))
