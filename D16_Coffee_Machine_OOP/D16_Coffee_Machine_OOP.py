from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()


def main():
    print(logo)
    
    machine_is_on=True
    while machine_is_on:
        option=menu.get_items()
        user_choice=input(f"What would you like? ({option})")
        if user_choice=="off":
            machine_is_on=False
        elif user_choice=="report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink=menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                   coffee_maker.make_coffee(drink)
       
main()

