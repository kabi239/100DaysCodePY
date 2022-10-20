from logo import logo
from Data import MENU,resources



PROFIT=0
def resource_sufficent(ordered_ingredents):
    for item in ordered_ingredents:
        if ordered_ingredents[item]>resources[item]:
            print(f"(┬┬﹏┬┬) Sorry there is not enough {item}. ")
            return False
    return True

def process_coins():
    print("Please enter coins 🪙 ")
    quarters=int(input("How many Quarters ? "))*0.25
    dimes=int(input("How many Dimes ? "))*0.1
    nickles=int(input("How many Nickles ? "))*0.05
    pennies=int(input("How many Pennies ? "))*0.01
    total=quarters+dimes+nickles+pennies
    return total
    
def transaction(payment,drink_cost):
    if payment>=drink_cost:
        change=round(payment-drink_cost,2)
        print(f"Here is your change of ${change} .")
        global PROFIT
        PROFIT+=drink_cost
        return True
    else:
        print("Sorry that's not enough mony. Money refunded.")
        print()
        return False
    
def make_coffee(user_choice,drink_ingredients):
    for items in drink_ingredients:
        resources[items]-= drink_ingredients[items]
    print(f"Here is your {user_choice} ☕.")
    print("Have a Nice Day 😊")
    print()
    
def main():
    print(logo)
    machine_is_on=True
    while machine_is_on:
        user_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice=="off":
            machine_is_on=False
        elif user_choice=="report":
            print(f"Water {resources['water']} ml. ")
            print(f"Milk {resources['milk']} ml. ")
            print(f"coffee {resources['coffee']} g. ")
            print()
        else:
            drink=MENU[user_choice]
            if  resource_sufficent(drink["ingredients"]):
                payment=process_coins()
                if transaction(payment,drink["cost"]):
                    make_coffee(user_choice,drink["ingredients"])

                    

main()

 