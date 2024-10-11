# include required libraries
import time

#specify the start timer for the entire test suite
test_suite_start_timer = time.time()


import os
import random
import string
from datetime import datetime, timedelta
import pytz

# include selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    fp.write('"App Name","Metrics App Location","Web App Location","Network","Date/Time (UTC)","Date/Time (HST)","Page Name","Action","# Files","Total File Size (KB)","Total Response Time (s)","Screenshot File"'+"\n")


# set the selenium options:
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,1080")
# options.add_argument('--enable-javascript')
options.add_argument('ignore-certificate-errors')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

prefs = {"download.default_directory" : "/app/data"};

options.add_experimental_option("prefs",prefs);

# create the chrome webdriver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# enable the network cache
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":False})

# custom_functions.log_value("load the page", print_log_messages)


"""
START - 1. Request the base_web_url defined in the application configuration
"""

# Login to web application:
custom_functions.log_value("1. Request the base_web_url defined in the application configuration", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)


# check the value of the web_app_location
if (project_scenario_config.web_app_location == "Remote"):
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
return_value = custom_functions.wait_for_response (None, By.ID, "P101_USERNAME", start_timer, driver, print_log_messages, fp, None, "Page Load")

"""
END - 1. Request the base_web_url defined in the application configuration
"""

"""
START - 2. Login to the web app
"""

# Login to web application:
custom_functions.log_value("2. login to the application", print_log_messages)


# find the username/password fields
username_field = driver.find_element("id", "P101_USERNAME")
password_field = driver.find_element("id", "P101_PASSWORD")

# find the login button
login_button = driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]/span[contains(., 'Log In')]/..")

# click the login button
custom_functions.log_object(login_button, print_log_messages)

# specify the username/password for the web app
username_field.send_keys(login_credentials.login_username)
password_field.send_keys(login_credentials.login_password)

# custom_functions.log_value("submit the login button", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# submit the login form
login_button.click()

# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P1_REGION_ID", start_timer, driver, print_log_messages, fp, None, "Login/Page Load")

"""
END - 2. Login to the web app
"""


"""
START - 3. Update the Region select element to filter the Full Sampling Report Page
"""

custom_functions.log_value("3. Update the Region select element to filter the Full Sampling Report Page", print_log_messages)

# change the selection of the region to reload the page:
region_element = driver.find_element("id", "P1_REGION_ID")
region_select = Select(region_element)

# start the timer
start_timer=round(time.time()*1000)

# change the region select element value which will reload the page:
region_select.select_by_visible_text("Western North Pacific")

# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (region_element, By.ID, "P1_REGION_ID", start_timer, driver, print_log_messages, fp, "filter", "Page Reload/Filter Report")


"""
END - 3. Update the Region select element to filter the Full Sampling Report Page
"""

"""
START - 4. Open the View All Specimens Page
"""
# Open the View All Specimens Page - Begin:

custom_functions.log_value("4. Open the View All Specimens Page", print_log_messages)


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
return_value = custom_functions.wait_for_response (None, By.ID, "P200_REGION_ID", start_timer, driver, print_log_messages, fp, None, "Page Load")

"""
END - 4. Open the View All Specimens Page
"""


"""
START - 5. Open the View/Edit Specimen Page
"""

custom_functions.log_value("5. Open the View/Edit Specimen Page", print_log_messages)



# Open the View/Edit Specimen Page - Begin
# custom_functions.log_value("Open the Create specimen page", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the create specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]/span[contains(., 'Create Specimen')]/..").click()

# wait for the response from the page load until the region select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P210_START_CATCH_DATE", start_timer, driver, print_log_messages, fp, None, "Page Load")

"""
END - 5. Open the View/Edit Specimen Page
"""

# Open the View/Edit Specimen Page - Complete


"""
START - 6. Submit the specimen form to create a new record
"""

# Submit the specimen form and create a new record - Begin:

custom_functions.log_value("6. Submit the specimen form to create a new record", print_log_messages)

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
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]/span[contains(., 'Create')]/..").click()

# wait for the response from the create specimen form submission until the start catch date element is stale and the new start catch date element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (start_catch_date, By.ID, "P210_START_CATCH_DATE", start_timer, driver, print_log_messages, fp, "post specimen record insert", "Form submission")

"""
END - 6. Submit the specimen form to create a new record
"""



"""
START - 7. Submit the specimen form to update an existing record
"""

# Submit the specimen form and create a new record - Begin:

custom_functions.log_value("7. Submit the specimen form to update an existing record", print_log_messages)

# create a new specimen record by filling out all the form fields with test values
current_field = driver.find_element("id", "P210_NEW_TRIP_ID")
current_field.clear()
current_field.send_keys("ABC-123*!");



# save the start catch date field element
current_field = driver.find_element("id", "P210_START_CATCH_DATE")
current_field.clear()
current_field.send_keys("01/10/2023")

current_field = driver.find_element("id", "P210_END_CATCH_DATE")
current_field.clear()
current_field.send_keys("02/01/2023")

current_field = driver.find_element("id", "P210_SET_ID")
current_field.clear()
current_field.send_keys("127")

current_field = driver.find_element("id", "P210_NAT_SAMP_ID")
random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
custom_functions.log_value("The new random Nation Sample ID value is: "+random_string, print_log_messages)
current_field.clear()
current_field.send_keys(random_string)

current_field = driver.find_element("id", "P210_SPEC_NOTES")
current_field.clear()
current_field.send_keys("Test specimen notes - Update")

current_field = driver.find_element("id", "P210_LOC_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("2x2 degree cell")

current_field = driver.find_element("id", "P210_FISH_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("US recreational fishing")

current_field = driver.find_element("id", "P210_LAT_DD")
current_field.clear()
current_field.send_keys("18.52")

current_field = driver.find_element("id", "P210_LON_DD")
current_field.clear()
current_field.send_keys("179.152")

current_field = driver.find_element("id", "P210_REGION_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Central North Pacific")

current_field = driver.find_element("id", "P210_SPP_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Swordfish")

current_field = driver.find_element("id", "P210_SEX_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Unknown")

current_field = driver.find_element("id", "P210_LEN_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("eye to fork length")

current_field = driver.find_element("id", "P210_LEN_ORIG_UOM_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("ft")

current_field = driver.find_element("id", "P210_LEN_ORIG_VAL")
current_field.clear()
current_field.send_keys("6.12")

current_field = driver.find_element("id", "P210_WT_TYPE_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("trunked")

current_field = driver.find_element("id", "P210_WT_ORIG_UOM_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("kg")

current_field = driver.find_element("id", "P210_WT_ORIG_VAL")
current_field.clear()
current_field.send_keys("104.32")

current_field = driver.find_element("id", "P210_OTO_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_GONAD_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_GONAD_FROZEN_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_DNA_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

current_field = driver.find_element("id", "P210_SPINE_COLL_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P210_SPINE_NOTES")
current_field.clear()


custom_functions.log_value("Submit the update specimen form", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)


# click the create specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]/span[contains(., 'Confirm')]/..").click()

# wait for the response from the create specimen form submission until the start catch date element is stale and the new start catch date element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P200_REGION_ID", start_timer, driver, print_log_messages, fp, "post specimen record update", "Form submission")


"""
END - 7. Submit the specimen form to update an existing record
"""

"""
START - 8.  Download the specimen .csv file
"""

# Download the specimen .csv file
custom_functions.log_value("8.  Download the specimen .csv file", print_log_messages)



#check if the specimen csv file already exists (could be leftover from a previous script execution if it was interrupted)
if custom_functions.specimen_csv_file_exists("/app/data", "IBBS_SPEC_DATA_"):
    custom_functions.log_value ("the specimen csv file already exists, delete it from the file system before attempting to download it since it will appear that the csv download was already completed", print_log_messages)

    # get the file size of the csv file and delete it from the file system
    total_file_size = custom_functions.get_specimen_csv_file_info("/app/data", "IBBS_SPEC_DATA_")



# click the Admin expand span element

custom_functions.log_value("click the Admin expand span element", print_log_messages)

# driver.find_element(By.XPATH, "//div[contains(@class, 't-TreeNav')]//span[contains(@class, 'a-TreeView-label')]/../../span[contains(@class, 'a-TreeView-toggle')]").click()

driver.find_element(By.XPATH, "//div[contains(@class, 't-TreeNav')]//span[contains(@class, 'a-TreeView-label')][text()='Admin']/../../span[contains(@class, 'a-TreeView-toggle')]").click()

# screenshot_file = driver.title.replace("/", " ")+' toggle admin menu.png'

# save the screenshot from the web request/page load
# driver.save_screenshot('/app/data/screenshots/'+screenshot_file)


#capture today's datetime value
today = datetime.now()

#capture tomorrow's datetime value
tomorrow = today + timedelta(1)

# generate csv file names for today and tomorrow:
today_csv_file_name = "IBBS_SPEC_DATA_"+today.strftime("%Y%m%d")+".csv"
tomorrow_csv_file_name = "IBBS_SPEC_DATA_"+tomorrow.strftime("%Y%m%d")+".csv"
today_csv_file_path = "/app/data/"+today_csv_file_name
tomorrow_csv_file_path = "/app/data/"+tomorrow_csv_file_name

# custom_functions.log_value("today's csv file name is: "+today_csv_file_name, print_log_messages)

# custom_functions.log_value("tomorrow's csv file name is: "+tomorrow_csv_file_name, print_log_messages)

custom_functions.log_value("click the D/L Specimens link", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the D/L Specimens link
driver.find_element(By.XPATH, "//a[@class='a-TreeView-label'][text()='D/L Specimens']").click()


custom_functions.log_value("Wait until the file download has completed", print_log_messages)


# wait until the file download has completed:
while not custom_functions.specimen_csv_file_exists("/app/data", "IBBS_SPEC_DATA_"):

    custom_functions.log_value("The .csv file does not exist yet, sleep for 0.01 seconds and check the loop condition again", print_log_messages)
    time.sleep(0.01)


# calculate the elapsed time based on the start/end timer variables
total_time_ms=round(time.time()*1000)-start_timer
custom_functions.log_value("The csv file download has completed: "+str(total_time_ms)+" ms", print_log_messages)

#retrieve the file size for the downloaded file and delete
total_file_size = custom_functions.get_specimen_csv_file_info("/app/data", "IBBS_SPEC_DATA_")

# define the UTC and HST timezones:
utc_timezone = pytz.timezone("UTC")
hst_timezone = pytz.timezone("Pacific/Honolulu")


# convert the start_timer to a datetime object using the current timezone (UTC)
start_datetime_utc = datetime.fromtimestamp(start_timer /1000)

# Convert the UTC datetime object to the Pacific/Honolulu timezone so it can be logged separately
start_datetime_hst = start_datetime_utc.astimezone(hst_timezone)


custom_functions.log_value("The downloaded file size is: "+str(total_file_size), print_log_messages)


screenshot_file = driver.title.replace("/", " ")+' specimen download complete.png'

# save the screenshot from the web request/page load
driver.save_screenshot('/app/data/screenshots/'+screenshot_file)

fp.write('"'+app_config.app_name+'","'+project_scenario_config.container_location+'","'+project_scenario_config.network_location+'","'+project_scenario_config.web_app_location+'","'+start_datetime_utc.strftime('%m/%d/%Y %I:%M:%S %p')+'","'+start_datetime_hst.strftime('%m/%d/%Y %I:%M:%S %p')+'","IBBS_SPEC_DATA_YYYYMMDD.csv","Download Specimen Data","1","'+str(total_file_size)+'","'+str(round(total_time_ms / 1000, 3))+'","'+screenshot_file+'"'+"\n")

"""
END - 8.  Download the specimen .csv file
"""

"""
START - 9. Load Regional Sampling Charts
"""

# Load Regional Sampling Charts
custom_functions.log_value("9. Load Regional Sampling Charts", print_log_messages)


# click the Admin expand span element

custom_functions.log_value("click the Admin expand span element", print_log_messages)

# driver.find_element(By.XPATH, "//div[contains(@class, 't-TreeNav')]//span[contains(@class, 'a-TreeView-label')][text()='Sampling Plan']/../../span[contains(@class, 'a-TreeView-toggle')]").click()

driver.find_element(By.XPATH, "//div[contains(@class, 't-TreeNav')]//a[contains(@class, 'a-TreeView-label')][text()='Sampling Plan']/../../span[contains(@class, 'a-TreeView-toggle')]").click()


# screenshot_file = driver.title.replace("/", " ")+' toggle sampling plan menu.png'

# save the screenshot from the web request/page load
# driver.save_screenshot('/app/data/screenshots/'+screenshot_file)


custom_functions.log_value("click the Regional Sampling Plan link", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the D/L Specimens link
driver.find_element(By.XPATH, "//a[@class='a-TreeView-label'][text()='Region']").click()



# wait for the response from the page load until the "Length Bins (cm)" label is visible in the swordfish chart region
return_value = custom_functions.wait_for_response (None, By.XPATH, "//h2[contains(@class, 't-Region-title')][text()='Swordfish']/../../..//*[name()='text'][text()='Length Bins (cm)']", start_timer, driver, print_log_messages, fp, None, "Page Load")




"""
END - 9. Load Regional Sampling Charts
"""

"""
START - 10. Filter/Reload Regional Sampling Charts
"""

custom_functions.log_value("10. Filter/Reload Regional Sampling Charts", print_log_messages)

# change the selection of the region to reload the page:
region_element = driver.find_element(By.ID, "P10_REGION_ID")
region_select = Select(region_element)

# start the timer
start_timer=round(time.time()*1000)

# change the region select element value which will reload the page:
region_select.select_by_visible_text("Eastern North Pacific")

# wait for the response from the page load until the "Length Bins (cm)" label is visible in the swordfish chart region
return_value = custom_functions.wait_for_response (region_element, By.XPATH, "//h2[contains(@class, 't-Region-title')][text()='Swordfish']/../../..//*[name()='text'][text()='Length Bins (cm)']", start_timer, driver, print_log_messages, fp, 'filter', "Page Reload/Filter Report")



"""
END - 10. Filter/Reload Regional Sampling Charts
"""







# Submit the specimen form and create a new record - Complete

custom_functions.log_value("All of the web actions in the test suite have completed", print_log_messages)

# calculate the elapsed time in minutes based on the test_suite_start_timer variable and the current time
total_time_min=round(((time.time()-test_suite_start_timer)/60), 2)

# log the elapsed time for the entire test suite
custom_functions.log_value('total elapsed time (min): '+str(total_time_min), print_log_messages)

# selenium driver session cleanup:

# close the selenium driver
driver.close()

# quit the selenium driver
driver.quit()
