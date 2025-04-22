from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# Setting up the driver properly using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.orangehrm.com/en/contact-sales")

# def select_values(element,value):
#     select=Select(element)
#     select.select_by_visible_text(value)


# ele_country=driver.find_element(By.ID,"Form_getForm_Country")
# ele_employeno=driver.find_element(By.ID,"Form_getForm_NoOfEmployees")

# select_values(ele_country,"Nepal")
# select_values(ele_employeno,"< 10")


# select = Select(ele_country)
# country_list=select.options

# for ele in country_list:
#     print(ele.text)
#     if(ele.text =='Nepal'):
#         ele.click()
#         break

 


# ele_country=driver.find_element(By.ID,"Form_getForm_Country")
# select=Select(ele_country)

# # select.select_by_index(2)
# select.select_by_visible_text("Nepal")
# # select.select_by_value("Argentina") #we have to select by option value by inspecting it


# print(select.is_multiple)  # it is used to check whether the select is multiple slect values or not.



#we can also do same proceess of selecting dropdown using xpath
def select_values(element,value):
    select=Select(element)
    select.select_by_visible_text(value)





def select_values_from_dropdown(dropdownlist,value):
    print(len(dropdownlist))
    for ele in dropdownlist:
        print(ele.text)
        if ele.text==value:
            ele.click()
            break


ele_country=driver.find_elements(By.XPATH,'//select[@id="Form_getForm_Country"]/option')
select_values_from_dropdown(ele_country,'Nepal')
select_values_from_dropdown(ele_country,"India")












# ele_country=driver.find_elements(By.XPATH,'//select[@id="Form_getForm_Country"]/option')
# print(len(ele_country))
# for ele in ele_country:
#     print(ele.text)
#     if ele.text=='Nepal':
#         ele.click()
#         break

















time.sleep(5)
driver.quit()