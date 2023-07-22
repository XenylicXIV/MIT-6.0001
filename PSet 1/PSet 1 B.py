current_savings=0
months=0

annual_salary= float(input('Please enter your annual salary:\n$'))


#Need conditions for invalid str input coversion
per_save=float(input('What percentage of your annual salary are you saving?\n'))
portion_saved=(annual_salary*per_save/12)

total_cost=float(input('What is the cost of your dream home?\n$'))
portion_down_payment=total_cost*.25

per_raise= float(input('Please enter your semi-annual raise percentage.\n'))
#raise percentage

while current_savings < portion_down_payment:
    if months != 0 and months % 6 == 0:
        semi_raise=annual_salary*per_raise
        annual_salary+=semi_raise
        portion_saved=(annual_salary*per_save/12)

    inv_per=.04/12
    invest_earn=current_savings*inv_per
    current_savings += round(portion_saved + invest_earn, 2)
    months+=1
    
print('It will take ' + str(months) + ' months to reach the down payment of $'+ 
      str("{:.2f}".format(portion_down_payment)))
