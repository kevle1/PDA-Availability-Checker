from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import time 

parser = argparse.ArgumentParser()
parser.add_argument("--permitnum", dest="permitnum", help="Permit Number", metavar="PERMITNUM")
parser.add_argument("--expiry", dest="expiry", help="Permit Expiry Date", metavar="EXPIRY")
parser.add_argument("--firstname", dest="firstname", help="First Name", metavar="FIRSTNAME")
parser.add_argument("--lastname", dest="lastname", help="Last Name", metavar="LASTNAME")
parser.add_argument("--dob", dest="dob", help="Date of Birth", metavar="DOB")
args = parser.parse_args()

print("Using Details:")
print(args.permitnum)
print(args.expiry)
print(args.firstname)
print(args.lastname)
print(args.dob)

driver = webdriver.Firefox()

driver.get("https://online.transport.wa.gov.au/pdabooking/manage/")

print("Populating Permit Details Form...")

#Non driving instructor, Non Overseas licence. Class C, Non single name 
driver.find_element_by_xpath("/html/body/span/div/div[3]/div/form/div[4]/div/span/ol/li[5]/div/input").send_keys(args.permitnum)
driver.find_element_by_xpath("//*[@id=\"licenceExpiryDatePicker\"]").send_keys(args.expiry)
driver.find_element_by_xpath("/html/body/span/div/div[3]/div/form/div[4]/div/span/ol/li[9]/div/input").send_keys(args.firstname)
driver.find_element_by_xpath("/html/body/span/div/div[3]/div/form/div[4]/div/span/ol/li[10]/div/input").send_keys(args.lastname)
driver.find_element_by_xpath("//*[@id=\"dateOfBirthPicker\"]").send_keys(args.dob)

time.sleep(1)

print("Clicking Continue...")
btn = driver.find_element_by_xpath("//*[@id=\"id5\"]").click() #Submit 

time.sleep(2)

print("Selecting Class...") 
driver.find_element_by_xpath("//*[@id=\"id12\"]").click() #Just Clicks "Search Availability" - By Default C-Car is already selected. 

time.sleep(2)

#Hardcoded Metro Centres 
metro_centres = ["/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[2]", #Cannington 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[3]", #Joondalup 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[4]", #Kelmscott 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[5]", #Mandurah 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[6]", #Midland 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[7]", #Mirrabooka
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[8]", #Rockingham 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[9]", #Success 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[10]", #Welshpool 
                "/html/body/span/div/div[3]/div/form/div[2]/div[1]/ol/li[3]/div/select/option[11]"] #West Perth

#Default to "Earliest"

print("Checking Each Centre...") 
for c in metro_centres: 
    element = driver.find_element_by_xpath(c) 
    element.click() #Select one of the centres 

    time.sleep(1) 

    driver.find_element_by_xpath("//*[@id=\"id1d\"]").click() #Click Search 

    time.sleep(1) #Give it a bit of time to load 

    try:
        driver.find_element_by_xpath("/html/body/span/div/div[3]/div/form/div[2]/span[2]/span") #Check if "Available bookings" list is present, if not no availability. 

        avail = driver.find_elements_by_id("searchResultRadioLabel") #Get all entries (Identified by the radio labels)

        for a in avail:
            print("DOT "  + str(element.text) + " has availability: " + str(a.text))
    except:
        print("DOT " + str(element.text) + " has no availability")

driver.close()