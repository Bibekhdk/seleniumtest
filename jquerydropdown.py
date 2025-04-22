from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def select_values(dropdown_list,value):

    if  not value[0] == "all":

        for ele in dropdown_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text==value[k]:
                  ele.click()
                  break

    else:
        try:
            for ele in dropdown_list:
                ele.click()
        except Exception as e:
            print(e)

service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(2)

dropdown_list= driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')

value_list=["all"]

# value_list = ['choice 2','choice 3','choice 6 2 1']
select_values(dropdown_list, value_list)


# select_values(dropdown_list,'choice 2')
# select_values(dropdown_list,'choice 6 2 1')






# for ele in dropdown_list:
#     print(ele.text)
#     if ele.text == 'choice 2 1':
#         ele.click()
#         break

time.sleep(5)
driver.quit()