from selenium import webdriver
from selenium.webdriver.common.keys import Keys

INPUTS = {
    "teva_card_owner_name": "field[927607]",
    "ten_bis_card_num": "field[5342431]",
    "teva_castle_card_num": "field[927611]",
    "phone_num": "field[927609]",
    "amount_to_charge": "field[927613]"
}


class TevaCastleCharger:
    def __init__(self, teva_card_owner_name, ten_bis_card_num, teva_castle_card_num, phone_num, amount_to_charge):
        self.teva_card_owner_name = teva_card_owner_name
        self.ten_bis_card_num = ten_bis_card_num
        self.teva_castle_card_num = teva_castle_card_num
        self.phone_num = phone_num
        self.amount_to_charge = str(int(amount_to_charge))

    def charge_card(self):
        driver = webdriver.Firefox()
        try:
            driver.get("http://lp.infopage.mobi/index.php?page=landing&id=29871&token=cd6274314204f0b7342f35ae9dfa0165")
            for attr, value in self.__dict__.iteritems():
                element = driver.find_element_by_name(INPUTS[attr])
                element.send_keys(value)
            submit_button = driver.find_element_by_class_name("PageSubmitButton")
            submit_button.click()
        finally:
            driver.close()

    def lala(self):
        for attr, value in self.__dict__.iteritems():
            print attr, value
