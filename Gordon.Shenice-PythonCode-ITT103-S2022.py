#Author:Shenice Renae Gordon
#Date Created:May 1, 2022
#Course: ITT103
#Purpose: To calculate the commission for different salesmen in a company.



"""
Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.

Class=2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent.
Page 4 of 7

Class=3
The rate is 4.5 percent for all sales amount
Class=any other value
"""

#define function to calculate commission

def calc_commission():

#define variables and prompt user for input    

    sales_num=int(input("Enter Sales person number "))
    sales_amt=int(input("Enter Sales amount "))
    emp_class=int(input("Enter Sales class "))

    if emp_class==1:
        if sales_amt <=1000:
            commission=sales_amt*(6/100)
            print("Employee", sales_num,"sales commission is",commission)

        elif  1000 < sales_amt <= 2000:
            commission=sales_amt*(7/100)
            print("Employee", sales_num,"sales commission is",commission)
    
        else:
            commission=sales_amt*(10/100)
            print("Employee", sales_num,"sales commission is",commission)

    elif emp_class==2:
        if sales_amt <1000:
            commission=sales_amt*(4/100)
            print("Employee", sales_num,"sales commission is",commission)

        elif sales_amt>=1000:
            commission=sales_amt*(6/100)
            print("Employee", sales_num,"sales commission is",commission)

    elif emp_class==3:
        commission=sales_amt*(4.5/100)
        print("Employee", sales_num,"sales commission is",commission)

    else:
        return("Inavalid Employee Class entered")



