menu = {  "biryani" : 120 
        , "pasta" : 300
        , "noodles" :100
        , "chicken kharai" :1200 
        , "coldrink": 100 
            }

print ("welcome to tingo Resturant")
print("biryani : Rs 120 \npasta : Rs 300 \nnoodles :Rs 100\nchicken kharai : Rs 1200 \ncoldrink :Rs 100")
total_amount = 0

item_1 = input("enter you first item ")
if item_1 in menu :
    total_amount += menu[item_1]
    print (f"you item has beeb added {item_1}")
else:
    print(f"this {item_1} is not available  ")
    

another_order = input("do you want to take another item  yes/no")
if another_order == "yes":
    item_2 = input("enter you second item =")
    if item_2 in menu :
        total_amount += menu[item_2]
        print(f" {item_2}has been added ")
    else:
        print(f"{item_2}is not available ")
print(f"the total amount is {total_amount }")   
