import selenium

from selenium import webdriver

import time


wb = webdriver.Chrome("/Users/apple/PycharmProjects/sakti/chromedriver")


for i in range(0,1000000):

    wb.get("https://demo-widget.yupl.us/IRCTC/train_list.html")

    time.sleep(2)

    wb.switch_to_frame("yp_widget_iframe")

    time.sleep(2)
    #wb.switch_to_frame(wb.find_element_by_id("yp_widget_iframe"))

    a = wb.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/div[4]").text

    print("View count of this video:",a)
    time.sleep(2)

    wb.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/div[4]").click()
    print("Click operation has been  performed successfully")

wb.close()


'''
    wb.refresh()
    #wb.find_element_by_xpath("//div[@class='swiper-slide styles_slide_wrapper__1qTxS swiper-no-swiping swiper-slide-duplicate swiper-slide-duplicate-prev']//div[@class='styles_gradient__2oOJM']").click()

    time.sleep(2)

    wb.get("https://demo-widget.yupl.us/IRCTC/train_list.html")

    wb.get("https://demo-widget.yupl.us/IRCTC/train_list.html")

    wb.get("https://demo-widget.yupl.us/IRCTC/train_list.html")


    wb.get("https://demo-widget.yupl.us/IRCTC/train_list.html")
'''

