from TenBisBalanceChecker import TenBisBalanceChecker
from TevaCastelCharger import TevaCastleCharger
from data import persons


def main():
    for person in persons:
        ten_bis_balance_checker = TenBisBalanceChecker(token=person["ten_bis_token"])
        ten_bis_balance = ten_bis_balance_checker.check_balance()
        print ten_bis_balance

        if ten_bis_balance > 0:
            teva_castle_charger = TevaCastleCharger(
                teva_card_owner_name=person["teva_card_owner_name"],
                ten_bis_card_num=person["ten_bis_card_num"],
                teva_castle_card_num=person["teva_castle_card_num"],
                phone_num=person["phone_num"],
                amount_to_charge=ten_bis_balance
            )
            teva_castle_charger.charge_card()


if __name__ == "__main__":
    main()
