from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menuitem=MenuItem("latte",200,10,20,2.5)
menu=Menu()
choice=input("What do you want"+" "+menu.get_items())
drink=menu.find_drink(choice)
coffe=CoffeeMaker()
resource=coffe.is_resource_sufficient(drink)
money=MoneyMachine()
if(resource):
    if(money.make_payment(drink.cost)):
        print("Hurray")
        money.report()
else:
    print("False")