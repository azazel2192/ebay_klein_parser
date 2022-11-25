import requests
from bs4 import BeautifulSoup
import time
import os


headers = {
    'Content-Type': 'application/json',
    'cookie': 'route_97385225_bd99_4ddb_a1c6_c108f3714d67=b1af5d2e3ed44a24f91dacabd3b68e5e; CSRF-TOKEN=9b3858b9-e90a-485e-92cf-e21601e94650; GCLB=COjnsOrymcO6Lg; ekConsentBucketTcf2=full2-exp; ekConsentTcf2={%22customVersion%22:5%2C%22encodedConsentString%22:%22CPiq0GyPiq0GyE1ABADECQCgAP_AAAAAAAYgIxNd_X__bX9n-_7_7ft0eY1f9_r3_-QzjhfNs-8F3L_W_L0X32E7NF36tq4KuR4ku3bBIQNtHMnUTUmxaolVrzHsak2cpyNKJ7LkknsZe2dYGH9Pn9lD-YKZ7_5___f53T___9_-39z3_9f___d__-__-vjf_599n_v9fV_7___________-_________wAAAEhIAMAAQRiDQAYAAgjEIgAwABBGIVABgACCMQyADAAEEYh0AGAAIIxEIAMAAQRiJQAYAAgjEUgAwABBGIA.YAAAAAAAA6sA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true%2C%22googleAnalyticsAllowed%22:true%2C%22infonlineAllowed%22:true%2C%22theAdexAllowed%22:true%2C%22snowplowAllowed%22:true%2C%22criteoAllowed%22:true}}; overlayV21=seen; googtrans=/auto/en; googtrans=/auto/en; __gsas=ID=ae44a527f825aec2:T=1668788509:S=ALNI_MaqzROISfrrpo-zWT_4HqB6hO8GHw; iom_consent=0103ff03ff&1668788509872; POPUPCHECK=1668874909906; _ga=GA1.2.322153241.1668788510; _gid=GA1.2.1294233091.1668788510; clientId=322153241.1668788510; _clck=xhcidz|1|f6o|0; axd=4311597103235281822; __gads=ID=8b848c9637038171:T=1668788618:S=ALNI_MaMct7dskuzofSouiDwESGx9QqFVg; __gpi=UID=00000b82dae28937:T=1668788618:RT=1668788618:S=ALNI_MbYXN3aZf6ne6SpYWWwhwDLO2uRYg; cto_bundle=1mT5RV9jbTUzRDJKWTdiSG9TTkNsZEdlOVJuWmQlMkI4SWFpakJtUjE3YyUyQkVpYiUyRlFrYzF1RlJvVXJsNnFqVFczemVYVkdlNGtMRzRteWFLUzJHJTJCYWNheWNrOG9yOUhhR1hiMzBObnk2ZVRhSjVNbnVsSHdtSkF5ekFKdTREU2puekZjVEhKSyUyQlVwNGdiQkp5azFJT2VmT0UyMUVZWkg0Z05TSXNYRWFLbmplbXZJS2JFJTNE; rbzid=n/xXAHXGJUFdczX/6nN9Er823VtIJC1U7DCahP/oaAW4nNWhZdmumU4lh3wzjlwYqCJjF7Ih74sWCFb/Sj5npH8dYxltJYyw8bj1FigGxdiICWy5XNABtBdsiWnXTQsVZU0uSt4KDh4fy00THol1jW/SIYatHhmG5e4OO5Dn4Ut5X8OOxSljP2aF9KotFmBVY0HCpTI78O/0LeTK9hZ4iXT6EKxe948rPGnHzUfZ0qNvnn8y0roc1W4DWOD9lCwG; rbzsessionid=40c5be5c3fe63e77f1aba001f7a98973; sc=%7B%22va%22%3A%222273327367%2C3706456%2C-378%2C-12769648%2C-461359993%2C474136253%2C-6%2C-13%2C-19%2C-4%2C-83%2C57%2C13%2C5231%2C34%2C188242%2C18255%2C66435%22%7D; ioam2018=001b38f31f3490ecf6377b11e:1695313309905:1668788509905:.ebay-kleinanzeigen.de:16:ebaykanz:ebayK-3-154:noevent:1668794849739:wk18lj; _uetsid=1afabb90675d11eda5389f7345579dd6; _uetvid=1afb2480675d11ed8e1f87cf9c3de16a; uh=%7B%22sh%22%3A%22p%3D2%26c%3D154%26map%3D100%26mip%3D10%26pt%3DPRIVATE%22%7D; up=%7B%22ln%22%3A%22493351762%22%2C%22lln%22%3A%227a9f588a-b8bb-46f1-829c-f3fcbdee5db9%22%2C%22llstv%22%3A%22BLN-18532_highlight%3DB%7CBLN-20955_Buy_now_kill%3DA%7CBLN-22726_buyer_banner%3DB%7CEBAYKAD-3536_floor_ai%3DC%7CDesktop_Test%3DB%7CBLN-21710_Buy_now_filter%3DB%7CEKMO-25_MyAdsC2b%3DB%7Cga-behind-consent%3DB%7Cclv_click_tracking_desk%3DE%7CEKMO-100_reorder_postad%3DB%7Crebranding-m2www%3DA%7Cdesktop_decision_engine%3DC%7CEKMO-131_fake_door_test%3DA%7CBLN-19787-biz-upselling%3DB%7CBLN-21783_testingtime%3DG%7CEBAYKAD-2252_group-assign%3DC%7Cliberty-experiment-style%3DA%7C97-js-errorlog%3DA%7Cpromotion-desktop%3DA%7CEKMO-11%3DB%7Cconsent-banner%3DA%7CBLN-22766_GS-anim-desktop%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7Cgoogle-ads-behind-consent%3DB%7Cprebid-update%3DA%7Cliberty_gcp_desktop%3DA%7Cdesktop_payment_badge_SRP%3DB%22%2C%22ls%22%3A%22p%3D2%26c%3D154%26map%3D100%26mip%3D10%26pt%3DPRIVATE%22%2C%22va%22%3A%222277033823%2C-378%2C-474129641%2C474136253%2C-42%2C-26%2C-3712622%2C3712684%2C-32%2C-87%2C106%2C-36%2C-12776205%2C12781436%2C34%2C188242%2C18255%2C66435%22%7D; GCLB=CIXn3dzDtaDDTA',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
payload = {}
sellers = []


def get_numbers(text):
    num_list = []
    num = ''
    for char in text:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list


def save_sellers():
    with open(os.getcwd() + '/sellers.txt', 'w') as f:
        for seller in sellers:
            f.write(seller + '\n')


def load_sellers():
    with open(os.getcwd() + '/sellers.txt', 'r') as f:
        for seller in f.read().split('\n'):
            sellers.append(seller)


class Parser:
    def __init__(self):
        self.s = requests.session()
        self.items = {}
        self.pages = []
        self.timeout = 0

    def grab_items(self, end_page):
        start_grab_time = time.time()
        for i in range(1, end_page+1):
            url = f'https://www.ebay-kleinanzeigen.de/s-kleidung-damen/anbieter:privat/preis:10:2500/seite:{i}/c154'
            self.pages.append(self.s.get(url=url, headers=headers).text)
            time.sleep(1)

        for page in self.pages:
            soup = BeautifulSoup(page, features="lxml")
            for a in soup.find_all("a", class_="ellipsis"):
                self.items[a['href']] = ''
        print("--- parsing item pages took %s seconds ---" % (time.time() - start_grab_time))

    def get_sellers(self):
        start_get_time = time.time()
        for item in self.items:
            page = self.s.get('https://www.ebay-kleinanzeigen.de' + item, headers=headers, data=payload).text
            soup = BeautifulSoup(page, features="lxml")
            anch = soup.find("span", class_="text-body-regular-strong")
            try:
                self.items[item] = anch.find("a", {'href': True})['href']
            except AttributeError:
                pass
            self.timeout += 1
        print("--- getting seller links took %s seconds ---" % (time.time() - start_get_time))

    def check_sellers(self):
        start_check_time = time.time()
        pop_items = []
        for item, seller in self.items.items():
            page = self.s.get('https://www.ebay-kleinanzeigen.de' + seller, headers=headers, data=payload).text
            try:
                soup = BeautifulSoup(page, features="lxml")
                sell_text = soup.find_all("span", class_="userprofile-details")[2].text.replace('  ', '')
                if sum(get_numbers(sell_text)) <= 5:
                    sellers.append(seller)
                    pass
                else:
                    pop_items.append(item)
            except IndexError:
                print(BeautifulSoup(page, features="lxml").find_all("span", class_="userprofile-details"))
                pass
            except Exception as e:
                print(str(e))
                pass

        for i in pop_items:
            self.items.pop(i)
        print("--- checking sellers' rating took %s seconds ---" % (time.time() - start_check_time))


if __name__ == "__main__":
    start_time = time.time()
    load_sellers()
    x = Parser()
    x.grab_items(end_page=10)
    x.get_sellers()
    x.check_sellers()
    save_sellers()

    with open('items.txt', 'w') as f:
        for i, _ in x.items.items():
            f.write(i + '\n')

    print("--- getting sellers with low rating took %s seconds ---" % (time.time() - start_time))