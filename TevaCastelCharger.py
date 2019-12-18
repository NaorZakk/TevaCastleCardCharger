import requests
from selenium import webdriver

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
        self.charge_card_using_request()

    def charge_card_using_request(self):
        url = "http://lp.infopage.mobi/index.php"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
                  "name=\"page\"\r\n\r\nlanding.action\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent" \
                  "-Disposition: form-data; name=\"id\"\r\n\r\n29871\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r" \
                  "\nContent-Disposition: form-data; " \
                  "name=\"token\"\r\n\r\ncd6274314204f0b7342f35ae9dfa0165\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW" \
                  "\r\nContent-Disposition: form-data; " \
                  "name=\"force\"\r\n\r\ndesktop\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"elementAction\"\r\n\r\nsubmit\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r" \
                  "\nContent-Disposition: form-data; name=\"field[" \
                  "778049]\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
                  "name=\"{teva_card_owner_name}\"\r\n\r\nShoham Savir\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent" \
                  "-Disposition: form-data; name=\"field[" \
                  "927609]\"\r\n\r\n{phone_num}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"field[927611]\"\r\n\r\n{teva_castle_card_num}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r" \
                  "\nContent-Disposition: form-data; name=\"field[" \
                  "927613]\"\r\n\r\n{amount_to_charge}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
                  "name=\"field[927615]\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"field[" \
                  "5342431]\"\r\n\r\n{ten_bis_card_num}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent" \
                  "-Disposition: form-data; name=\"output\"\r\n\r\njson\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- " \
            .format(amount_to_charge=self.amount_to_charge, teva_castle_card_num=self.teva_castle_card_num,
                    teva_card_owner_name=self.teva_card_owner_name, ten_bis_card_num=self.ten_bis_card_num,
                    phone_num=self.phone_num)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Connection': "keep-alive",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Origin': "http://lp.infopage.mobi",
            'X-Requested-With': "XMLHttpRequest",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            'Content-Type': "application/x-www-form-urlencoded",
            'Referer': "http://lp.infopage.mobi/index.php?page=landing&id=29871&token=cd6274314204f0b7342f35ae9dfa0165",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "en-US,en;q=0.9,he;q=0.8",
            'Cookie': "PHPSESSID=ihedd0il1vpv3afvhurbt0v60r; InfoPagesvisitorcode=%3DkzN2YDOjljN0cjZkVjN1UjN4QjN3UTM; __utmc=209785288; InfoPagesREFERER_29871=%3D8SbvNmLlx2Zv92Zuc3d39yL6MHc0RHa; __utma=209785288.548138244.1576486555.1576502512.1576568484.4; __utmz=209785288.1576568484.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=209785288.1.10.1576568484,PHPSESSID=ihedd0il1vpv3afvhurbt0v60r; InfoPagesvisitorcode=%3DkzN2YDOjljN0cjZkVjN1UjN4QjN3UTM; __utmc=209785288; InfoPagesREFERER_29871=%3D8SbvNmLlx2Zv92Zuc3d39yL6MHc0RHa; __utma=209785288.548138244.1576486555.1576502512.1576568484.4; __utmz=209785288.1576568484.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=209785288.1.10.1576568484; InfoPagesvisitorcode=%3DYTMyEDZjJWY0cjZkVjMxYzN4QjN3UTM",
            'Cache-Control': "no-cache",
            'Postman-Token': "85519246-ed77-4daa-ace8-dfe516484ca4,f77361e5-28de-4011-962f-43a7489ac482",
            'Host': "lp.infopage.mobi",
            'Content-Length': "1413",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def charge_card_using_selenium(self):
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
