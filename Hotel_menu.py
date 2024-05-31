# for defining mene we uses dictionary bcz it stores the data in form of "key" "value" pair.
menu={
    'pizza':40,
    'Burgger':30,
    'pasta':50,
    'salad':20,
    'shake':70
   
}
# greet
print("Welcome to the python Restorent")
print("pizza = 40\nBurgger = 30\npasta = 50\nsalad = 20\nshake = 70")
order_total=0
item_1=input("Enter name of your first order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order=")
else:
    print(f"ordered item {item_1} is not avialable yet!")

another_order=input("Do you want to add another item (Yes/NO)")    
if another_order=="Yes":
    item_2=input("Enter the name of anothe order=")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Item has been added to your order")
    else:
        print(f"the item2 {item_2} is not avialable")
print(f"the total amount to be pay {order_total}")        


