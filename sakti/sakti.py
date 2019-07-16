import selenium

def run():

    from selenium import webdriver

    import time


    wb = webdriver.Chrome("/Users/apple/PycharmProjects/sakti/chromedriver")


    for i in range(0,100):

        wb.get("https://bsm.yupl.us/IRCTC/train_list.html")


        time.sleep(2)

        wb.close()


run()