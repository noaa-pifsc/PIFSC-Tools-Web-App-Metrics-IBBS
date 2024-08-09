# include required libraries
import os
import random
import string
import time

# include selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# import custom .py include files:
from lib import custom_functions     # defines custom functions used to 
from lib import app_config           # defines runtime application configuration values
from lib import login_credentials    # defines web login credentials
from lib import project_scenario_config

    
    
# set the variable to also print all log messages or not:
print_log_messages = True

# create the .csv file to capture the web performance metrics

# check if the .csv file exists
if os.path.isfile('/app/data/'+app_config.csv_output_file):
    # the .csv file exists

    # open the .csv file in append mode
    fp = open("/app/data/"+app_config.csv_output_file, "a")
else:
    # the .csv file does not exist

    # create the .csv file in write mode:
    fp = open("/app/data/"+app_config.csv_output_file, "x")

    # create the .csv header row
    fp.write('"App Name","Metrics App Location","Test App Location","Date/Time","Page Name","Action","# Files","Total File Size (KB)","Total Response Time (s)","Screenshot File"'+"\n")


# set the selenium options:
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--enable-javascript')
options.add_argument('ignore-certificate-errors')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})


# create the chrome webdriver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# enable the network cache
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":False})


# custom_functions.log_value("load the page", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)


# Open Login Page - Begin:

#request the base_web_url defined in the application configuration

# check the value of the app_location
if (project_scenario_config.app_location == "remote"):
    # this a remote application, use the remote_web_url

    custom_functions.log_value("This is a remote application: "+app_config.remote_web_url, print_log_messages)
    
    # load the URL in the web browser
    driver.get(app_config.remote_web_url) 
else:
    # this a local application, use the local_web_url

    custom_functions.log_value("This is a local application: "+app_config.local_web_url, print_log_messages)
    
    # load the URL in the web browser
    driver.get(app_config.local_web_url) 
    


# wait for the response from the page load until the username field is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, "P101_USERNAME", start_timer, driver, print_log_messages, fp, None, "Page Load")


# Open Login Page - Complete


# Login to web application/Load Full Sampling Report Page - Begin:

# custom_functions.log_value(driver.page_source, False)

custom_functions.log_value("login to the application", print_log_messages)
    
# find the username/password fields
username_field = driver.find_element("id", "P101_USERNAME")
password_field = driver.find_element("id", "P101_PASSWORD")

# find the login button
login_button = driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Log In')]/..")
# click the create specimen button

custom_functions.log_object(login_button, print_log_messages)

# specify the username/password for the web app
username_field.send_keys(login_credentials.login_username)
password_field.send_keys(login_credentials.login_password)

custom_functions.log_value("submit the login button", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# submit the login form
login_button.click()

# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, "P1_REGION_ID", start_timer, driver, print_log_messages, fp, None, "Login/Page Load")

# Login to web application/Load Full Sampling Report Page - Complete

# Update the Region Select element to filter the Full Sampling Report Page - Begin:

# custom_functions.log_value(driver.page_source, False)

# change the selection of the region to reload the page:
region_element = driver.find_element("id", "P1_REGION_ID")
region_select = Select(region_element)

# custom_functions.log_value ("the value of the region select element is:", print_log_messages)
# custom_functions.log_value (region_element.id, print_log_messages)
# custom_functions.log_object (region_element, print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# change the region select element value which will reload the page:
region_select.select_by_visible_text("Western North Pacific")
        

# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (region_element, "P1_REGION_ID", start_timer, driver, print_log_messages, fp, "filter", "Page Reload/Filter Report")

# Update the Region Select element to filter the Full Sampling Report Page - Complete


# Open the View All Specimens Page - Begin:

# navigate to the specimen interactive report
custom_functions.log_value("navigate to the specimen interactive report", print_log_messages)

# get the view/edit specimens link element
specimen_link = driver.find_element(By.XPATH, "//a[text()='Specimens']")

# custom_functions.log_object(specimen_link, print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the link
driver.execute_script("arguments[0].click()", specimen_link)


# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, "P200_REGION_ID", start_timer, driver, print_log_messages, fp, None, "Page Load")
            
# Open the View All Specimens Page - Complete

# Open the View/Edit Specimen Page - Begin
custom_functions.log_value("Open the Create specimen page", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the create specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Create Specimen')]/..").click()
                
# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, "P210_START_CATCH_DATE", start_timer, driver, print_log_messages, fp, None, "Page Load")

# Open the View/Edit Specimen Page - Complete



# Submit the specimen form and create a new record - Begin:


# create a new specimen record by filling out all the form fields with test values
current_field = driver.find_element("id", "P210_NEW_TRIP_ID")
current_field.send_keys("ABC-123*!");



# save the start catch date field element
start_catch_date = driver.find_element("id", "P210_START_CATCH_DATE")
start_catch_date.send_keys("01/23/2023")

current_field = driver.find_element("id", "P210_END_CATCH_DATE")
current_field.send_keys("02/15/2023")

current_field = driver.find_element("id", "P210_SET_ID")
current_field.send_keys("124")

current_field = driver.find_element("id", "P210_NAT_SAMP_ID")
random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
custom_functions.log_value("The new random Nation Sample ID value is: "+random_string, print_log_messages)
current_field.send_keys(random_string)

current_field = driver.find_element("id", "P210_SPEC_NOTES")
current_field.send_keys("Test specimen notes")

current_field = driver.find_element("id", "P210_LOC_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("4x4 degree cell")

current_field = driver.find_element("id", "P210_FISH_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("US Hawaii deep-set longline")

current_field = driver.find_element("id", "P210_LAT_DD")
current_field.send_keys("15.52")

current_field = driver.find_element("id", "P210_LON_DD")
current_field.send_keys("120.152")

current_field = driver.find_element("id", "P210_REGION_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Western North Pacific")

current_field = driver.find_element("id", "P210_SPP_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Blue Marlin")

current_field = driver.find_element("id", "P210_SEX_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Male")
                    
current_field = driver.find_element("id", "P210_LEN_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("eye to fork length")

current_field = driver.find_element("id", "P210_LEN_ORIG_UOM_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("ft")

current_field = driver.find_element("id", "P210_LEN_ORIG_VAL")
current_field.send_keys("7.54")

current_field = driver.find_element("id", "P210_WT_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("trunked")

current_field = driver.find_element("id", "P210_WT_ORIG_UOM_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("kg")

current_field = driver.find_element("id", "P210_WT_ORIG_VAL")
current_field.send_keys("115")

current_field = driver.find_element("id", "P210_OTO_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

current_field = driver.find_element("id", "P210_GONAD_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

current_field = driver.find_element("id", "P210_GONAD_FROZEN_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_DNA_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_SPINE_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

current_field = driver.find_element("id", "P210_SPINE_NOTES")
current_field.send_keys("test spine notes")


custom_functions.log_value("Submit the create specimen form", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)


# click the create specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Create')]/..").click()

# wait for the response from the create specimen form submission until the start catch date element is stale and the new start catch date element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (start_catch_date, "P210_START_CATCH_DATE", start_timer, driver, print_log_messages, fp, "post specimen record insert", "Form submission")


# Submit the specimen form and create a new record - Complete


# selenium driver session cleanup:

# close the selenium driver
driver.close()

# quit the selenium driver
driver.quit()


