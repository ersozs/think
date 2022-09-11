from os import link
import urllib.request


for x in range(10):
    sayfa = 110
    current_page = sayfa + x
    urllib.request.urlretrieve("https://f.eba.gov.tr/ing-soru-bankasi/cambridge/Think-Turkiye-Presentation-Plus-Level-B1/TH_UP_L2/" + "69528" +
                               "/resources/paginas/th_be_l2_sb_p" + str(current_page) + ".jpg", "/Users/cihat.s.ersoz/Documents/WEB/B1/" + str(current_page) + ".jpg")
    print(current_page)
