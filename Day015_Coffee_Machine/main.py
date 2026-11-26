

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(type(MENU))
print(MENU)

def print_report():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${money}")

def check_resources(ingredients_water,ingredients_milk,ingredients_coffee):
    if  resources["water"] < ingredients_water:
        print("Sorry, you don't have enough water")
        check_resource = False
    elif resources["milk"] < ingredients_milk:
        print("Sorry, you don't have enough milk")
        check_resource = False
    elif resources["coffee"] < ingredients_coffee:
        print("Sorry, you don't have enough coffee")
        check_resource = False
    else:
        check_resource = True
    return check_resource

def to_make_coffee(ingradients_water,ingradients_milk,ingradients_coffee):
    resources["water"] -= ingradients_water
    resources["milk"] -= ingradients_milk
    resources["coffee"] -= ingradients_coffee


#変数
order =""
money = 0
check_resource = True
is_on = True
#While offになるまで

while is_on:
#ask user What would you like?
#espresso/latte/cappuccino report off
    order = input("What would you like? espresso/latte/cappuccino: ")
    #Turn off Machine
    if order == "off":
        is_on = False
        break

    #ToDo print report
    if order == "report":
        print_report()
        continue

    if order not in MENU:
        print("Invalid order. Please try again.")
        continue

#ToDo 必要リソースとコスト
    ingredients_water = MENU[order]["ingredients"]["water"]
    try:
        ingredients_milk = MENU[order]["ingredients"]["milk"]
    except KeyError:
        ingredients_milk = 0
    ingredients_coffee = MENU[order]["ingredients"]["coffee"]
    cost = MENU[order]["cost"]

#ToDo Check resources
    check_resource = check_resources(ingredients_water,ingredients_milk,ingredients_coffee)

    if check_resource:
        #コイン
    # ToDo Process coins
    #ToDo ユーザーにコインを促す
        print(f"{order}: {cost},please pay coin.")
        # *クォーター（quarters）= ** $0.25 **
        quarters = int(input("quarters($0.25): ") or 0)
        # *ダイム（dimes）= ** $0.10 **
        dimes = int(input("dimes($0.10): ") or 0)
        # *ニッケル（nickels）= ** $0.05 **
        nickels = int(input("nickels($0.05): ") or 0)
        # *ペニー（pennies）= ** $0.01 **
        pennies = int(input("pennies($0.01): ") or 0)

    #ToDo 合計する
        pay = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

# ToDo Check transaction successful
        if cost > pay:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += cost

            repay = pay - cost

            if repay > 0:
                print(f"Here is $ {repay} dollars in change.")

            # ToDo make coffee
            #リソース引く
            to_make_coffee(ingredients_water,ingredients_milk,ingredients_coffee)
            print(f"Here is your {order}. Enjoy!")

    else:
        break
