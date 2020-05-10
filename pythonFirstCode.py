# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:54:02 2020

@author: 3731545
"""
import math
def calc_mortgage(principal, interest, years):
    '''
    given mortgage loan principal, interest(%) and years to pay
    calculate and return monthly payment amount
    '''
    # monthly rate from annual percentage rate
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    return payment

def present_value_annuity(PMT, discount, years):
    present = PMT * (1 - (1 / pow(1 + discount / (100 * 12), years * 12))) / (discount / (100 * 12))
    return present

#parameter input
principal_initial = 396000
principal = 385256
discount_rate = 1.5

loan_period_initial = 15
loan_period_left = 14.5
loan_period_new  = 15
refi_cost = 0
old_interest_rate = 2.75
new_interest_rate = 2.5
print("The new monthly payment is: " + str(calc_mortgage(principal, new_interest_rate, loan_period_new)))

p_old = present_value_annuity(calc_mortgage(principal_initial, old_interest_rate, loan_period_initial), discount_rate, loan_period_left)
p_new = present_value_annuity(calc_mortgage(principal, new_interest_rate, loan_period_new), discount_rate, loan_period_new)
#present_diff = present_value_annuity(calc_mortgage(principal_initial, old_interest_rate, loan_period_initial) - calc_mortgage(principal, new_interest_rate, loan_period_new), discount_rate, loan_period_left)

print(p_old)
print(p_new)
total_diff = loan_period_left * 12 * calc_mortgage(principal_initial, old_interest_rate, loan_period_initial) - loan_period_new * 12 *calc_mortgage(principal, new_interest_rate, loan_period_new)
print("The total difference in payment between old and new interest rate without discounting : " + str(total_diff))
#print("The present value of monthly payment difference minus cost is : " + str(present_diff - refi_cost))

if p_old - p_new - refi_cost >= 0:
    print("You can save money by refinancing, the amount you can save is : " + str(p_old - p_new - refi_cost))
else:
    print("You will loose money by refinancing, the amount you will loose is : " + str(p_old - p_new - refi_cost))
    
