import selenium.webdriver
import time
import selenium.webdriver.common.keys as Keys



browser = selenium.webdriver.Chrome()
browser.get("https://www.oanda.com/fx-for-business/historical-rates")

#element = browser.find_element_by_id("hcc")
#element = element.find_element_by_class_name('nav')
#element = element.find_element_by_class_name('')

element = browser.find_element_by_id('datepicker-container')

element.click()

element = browser.find_element_by_id('datepicker-obj-container')
element = browser.find_element_by_class_name('buttonArea')
element = element.find_elements_by_class_name('apply blue')
element.click()



#element.click()



#element=element.find_element_by_class_name('table textArea')
#element=element.find_element_by_class_name('tableCell ranges')
element.click()
#element=element.find_element_by_class_name('dropdown')
#element=element.find_element_by_class_name('table item')
#element = element.find_element_by_class_name('tableCell lable')
#element.click()
#element = browser.find_element_by_id('datepicker-obj-container')
#element = browser.find_element_by_class_name('day-inner-container')
#print element.get_attribute('day-inner-container')
#element = element.find_element_by_class_name('expansion noselect')

#element = browser.find_element_by_class_name('secondary')
#element = browser.click()
#element = browser.find_element(str,'container have')
#element = browser.click()
#element = browser.find_element_by_class_id('havePicker')
#element = browser.find_element_by_class_name("have-select active")
#element = browser.find_element_by_id("core_content")
#element = browser.find_element_by_id("menu_content")
#element = browser.find_element_by_name('c')
#element.click()
#pageSrc = (browser.page_source).encode('utf-8')
#file =open('test.','w')
#file.write((browser.page_source).encode('utf-8'))

#element= browser.find_element_by_id('lst-ib')
#element = browser.find_element_by_name('q')
#element.send_keys('selenium')


#element = browser.find_element_by_name('btnK')
#element.click()*/
#time.sleep()

#time.sleep(5)
#pageSrc = (browser.page_source).encode('utf-8')

#file =open('test.txt','w')
#file.write((browser.page_source).encode('utf-8'))
#file.close()
#element = browser.find_element_by_name("python")
#element = browser.find_element_by_xpath('https://www.google.co.in/?gfe_rd=cr&ei=BMmCWeKBBbOl8welkpygBw')
#element.send_keys("selenium " + Keys.RETURN)

#browser.quit()