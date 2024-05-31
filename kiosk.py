class Drink:

    menu = {'커피': 3000, '녹차': 2500, '아이스티': 3000}
    def calculate(name, quantity):
        if name in Drink.menu:
            return Drink.menu[name] * quantity
        else:
            return None

def run_kiosk():
    print("메뉴표")
    for drink, price in Drink.menu.items():
        print(f"{drink}: {price}원")

    selected_drink = input("음료를 선택하세요: ")
    quantity = int(input("수량을 입력하세요: "))

    total_price = Drink.calculate(selected_drink, quantity)
    if total_price :
        print(f"총 가격은 {total_price}원 입니다.")
    else:
        print("선택하신 음료는 메뉴에 없습니다.")

run_kiosk()