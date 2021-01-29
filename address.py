#! /usr/bin/env python3

import os
import time
import random

from tkinter import *

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException

root = Tk()

root.geometry('800x900')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("Verify Deliverable Addresses")

def get_info(arg):
    print(tow.get("1.0", "current lineend"))


def clear_output():
    tow.delete(1.0, END)
    
    
def clear_entry(entry):
    entry.delete(0, 'end')
    
    
def Exit():
    exit()    
    

def address_verify():
    
    try:
    
        ff_dwnld_path = "/path to your folder/"
        usps_entry_url = "https://tools.usps.com/zip-code-lookup.htm?byaddress"
        
        firefoxOptions = Options()
        firefoxOptions.headless = True
        firefoxOptions.set_preference("browser.download.folderList", 2)
        firefoxOptions.set_preference("browser.download.manager.showWhenStarting", 
            False)
        firefoxOptions.set_preference("browser.download.dir", ff_dwnld_path)
        firefoxOptions.set_preference("browser.helperAppsneverAsk.saveToDisk", 
            "application/octet-stream,application/vnd.ms-excel")
        driver = webdriver.Firefox(options=firefoxOptions, 
            executable_path=GeckoDriverManager().install())
            
        driver.get(usps_entry_url)
        time.sleep(random.uniform(5, 12))
        
        scroll = "window.scroll(0, document.body.scrollHeight);"
        driver.execute_script(scroll)
        time.sleep(random.uniform(3, 7))
        
        street = entry_street.get()
        apt = entry_apt.get()
        city = entry_city.get()
        state = entry_state.get()
        zip_code = entry_zip.get()
        
        full_address = ("\n" + street.title() + ", " + apt.title() + 
            ", " + city.title() + ", " + state.upper()  + " " + zip_code)
        
        tow.insert(END, "\nSearching for the following address: ")
        tow.insert(END, full_address)
        tow.update_idletasks()
        tow.see(END)
        
        
        street_input_srch = '//input[@id="tAddress"]'
        street_input = driver.find_element_by_xpath(street_input_srch)
        street_input.send_keys(street.upper())
        
        apt_input_srch = '//input[@id="tApt"]'
        apt_input = driver.find_element_by_xpath(apt_input_srch)
        apt_input.send_keys(apt)
        
        city_input_srch = '//input[@id="tCity"]'
        city_input = driver.find_element_by_xpath(city_input_srch)
        city_input.send_keys(city.upper())
        
        state_select_srch = '//select[@id="tState"]'
        state_select = driver.find_element_by_xpath(state_select_srch)
        for option in state_select.find_elements_by_tag_name('option'):
            if option.get_attribute('value') == state.upper():
                option.click()
                
        zip_input_srch = '//input[@id="tZip-byaddress"]'
        zip_input = driver.find_element_by_xpath(zip_input_srch)
        zip_input.send_keys(zip_code)
        
        time.sleep(random.uniform(3, 8))
        
        find_btn_srch = '//a[@id="zip-by-address"]'
        find_btn = driver.find_element_by_xpath(find_btn_srch)
        find_btn.click() 
        
        time.sleep(5)
        
        try:
        
            error_srch = '//div[@class="server-error address-tAddress help-block"]'
            error_msg = driver.find_element_by_xpath(error_srch)
            if error_msg:
                tow.insert(END, error_msg.text)
                tow.insert(END, "That address was not found ... please " + 
                    "enter a valid address")
                tow.update_idletasks()
                tow.see(END)
                
                driver.quit()
            elif error_msg is None:
                tow.insert(END, "\nNo address errors; Submitting Address" +
                    " for verification ...")
                tow.update_idletasks()
                tow.see(END)
                
        
        except Exception as err:
            tow.insert(END, "\nChecking for confirmation ... ")
            tow.update_idletasks()
            tow.see(END)
            
               
        
        driver.execute_script(scroll)
        time.sleep(random.uniform(3, 7))
        
        dropdown_srch = '//div[@id="zipByAddressDiv"]'
        dropdown = driver.find_element_by_xpath(dropdown_srch)
        dropdown.click()
        
        time.sleep(2)
        
        result_srch = '//div[@class="col-sm-12 col-xs-6 row-detail-wrapper"]'
        result = driver.find_elements_by_xpath(result_srch)
                    
        if result[13].text == 'Y':
            tow.insert(END, "\nYes, this address is deliverable!! ")
            tow.update_idletasks()
            tow.see(END)
            
            
        elif result[13].text == 'N':
            tow.insert(END, "\nNo, this address is NOT deliverable!! ")
            tow.update_idletasks()
            tow.see(END)
            
            
        else:
            tow.insert(END, "\nMultiple pages of addresses returned. Please " +
                "revise your address search and try again ... ") 
            tow.insert(END, result[13].text)
            tow.update_idletasks()
            tow.see(END)
            
        
        time.sleep(4)
        
        driver.quit()
    
    
    except Exception as err:
        print("\nAddress Find has exited ...")
        
        
tow = Text(root, 
    height=35, 
    width=85, 
    borderwidth=1, 
    relief='ridge', 
    bg='gray7', 
    fg='lime green',
    )
    
tow.place(x=50, y=200)

entry_street = Entry(root, 
    font='arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green',
    )
    
entry_apt = Entry(root, 
    font='arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green',
    )
    
entry_city = Entry(root, 
    font='arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green',
    )
    
entry_state = Entry(root, 
    font='arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green',
    )
    
entry_zip = Entry(root, 
    font='arial 10', 
    width=15, 
    bg='gray7', 
    fg='lime green',
    )
    
entry_street.place(x=50, y=50)
entry_apt.place(x=350, y=50)
entry_city.place(x=50, y=110)
entry_state.place(x=350, y=110)
entry_zip.place(x=350, y=160)

label_street = Label(root, 
    text = "Enter Street Address",
    font = 'arial 12', 
    bg = 'gray7', 
    fg = 'lime green', 
    )
    
label_apt = Label(root, 
    text = "Enter Apt or Suite No.",
    font = 'arial 12', 
    bg = 'gray7', 
    fg = 'lime green', 
    )
    
label_city = Label(root, 
    text = "Enter City Name",
    font = 'arial 12', 
    bg = 'gray7', 
    fg = 'lime green', 
    )
    
label_state = Label(root, 
    text = "Enter 2 Letter State Abbrev.",
    font = 'arial 10', 
    bg = 'gray7', 
    fg = 'lime green', 
    )
    
label_zip = Label(root, 
    text = "Enter ZIP Code",
    font = 'arial 10', 
    bg = 'gray7', 
    fg = 'lime green', 
    )
    
label_street.place(x=50, y=25)
label_apt.place(x=350, y=25)
label_city.place(x=50, y=85)
label_state.place(x=350, y=85)
label_zip.place(x=350, y=135)



btn_exit = Button(root, 
    command = Exit,
    width=6, 
    padx=2, 
    pady=1, 
    text = 'EXIT', 
    font = 'arial 10 bold', 
    bg = 'OrangeRed'
    )
    
btn_clear_output = Button(root, 
    command = clear_output, 
    text = 'Clear Output', 
    font = 'arial 10',
    bg = 'gray7', 
    fg = 'lime green',
    )
    
btn_clear_street = Button(root, 
    command = lambda: clear_entry(entry_street),
    text = 'CLEAR',
    font = 'arial 7',
    bg = 'gray7',
    fg = 'lime green',
    )    

btn_clear_apt = Button(root, 
    command = lambda: clear_entry(entry_apt),
    text = 'CLEAR',
    font = 'arial 7',
    bg = 'gray7',
    fg = 'lime green',
    )   
    
btn_clear_city = Button(root, 
    command = lambda: clear_entry(entry_city),
    text = 'CLEAR',
    font = 'arial 7',
    bg = 'gray7',
    fg = 'lime green',
    )
    
btn_clear_state = Button(root, 
    command = lambda: clear_entry(entry_state),
    text = 'CLEAR',
    font = 'arial 7',
    bg = 'gray7',
    fg = 'lime green',
    )
    
btn_clear_zip = Button(root, 
    command = lambda: clear_entry(entry_zip),
    text = 'CLEAR',
    font = 'arial 7',
    bg = 'gray7',
    fg = 'lime green',
    )
    
btn_address_verify = Button(root, 
    command = address_verify,
    text = 'VERIFY ADDRESS',
    font = 'arial 9',
    bg = 'lime green',
    fg = 'gray7',
    ) 

    
btn_exit.place(x=680, y=810)
btn_clear_output.place(x=50, y=810)
btn_clear_street.place(x=240, y=48)
btn_clear_apt.place(x=540, y=48)
btn_clear_city.place(x=240, y=108)
btn_clear_state.place(x=540, y=108)
btn_clear_zip.place(x=470, y=158)
btn_address_verify.place(x=50, y=158)

        
if __name__ == '__main__':
    root.mainloop()
