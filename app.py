import os
import sys
import re
import time

from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime, date
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from application.Repeater import Repeater


def scrape_utahvhf_org():
    driver = None
    url = 'http://utahvhfs.org/rptr.html'
    headless = False
    cwd = os.getcwd()
    try:
        # https://github.com/mozilla/geckodriver/releases/tag/v0.24.0
        # https://w3c.github.io/webdriver/#element-send-keys
        # https://w3c.github.io/webdriver/#dfn-strict-file-interactability
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['strictFileInteractability'] = True

        options = Options()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            options=options,
            executable_path=cwd+'/geckodriver',
            service_log_path=cwd+'/logs/utah-repeater-map.log',
            desired_capabilities=capabilities
        )

        driver.maximize_window()
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        driver = None
    finally:
        pass

    if driver and driver.title == 'Repeater List for Utah':
        # Setup Excel file
        wb = Workbook()
        wb.active.title = 'Utah Repeaters'
        column_headers = Repeater().column_headers()
        wb.active.append(column_headers)
        # Bold the first row, doesn't seem worth it
        len_column_headers = len(column_headers)
        for cell in range (0,len_column_headers):
            tmp_cell = cell
            if cell > 25:
                tmp_cell = cell - 26
            letter = chr(ord('a')+tmp_cell).upper()
            # TODO: wrapping more than once
            if cell > 25:
                letter = 'A' + letter
            wb.active[letter+'1'].font = Font(bold=True)
        # Make sure cell isn't on row one - freeze_panes will freeze rows above the given cell and columns to the left.
        wb.active.freeze_panes = wb.active['A2']

        # Grab 2 Meter 
        count = len(driver.find_elements_by_xpath("/html/body/div/a[2]/table/tbody/tr"))
        for rptr in range(2, count+1):
            repeater = Repeater()
            innerHTML = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[1]').get_attribute('innerHTML')
            repeater.url = 'http://utahvhfs.org/' + re.findall('cgi-bin/rptdtl\.pl\?Nr\=[0-9]+\d', innerHTML)[0]
            tmp = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[1]').text
            repeater.output_freq = float(tmp.replace('§ ', '').replace('(+)', '').replace('(–)', ''))
            repeater.offset = '+600 Mhz' if '(+)' in tmp else '-600 Mhz' if '(–)' in tmp else None
            repeater.location = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[2]').text
            repeater.area = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[3]').text
            repeater.site_name = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[4]').text
            repeater.call_sign = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[5]').text
            repeater.sponsor = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[6]').text
            repeater.ctcss = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[7]').text
            repeater.info = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[8]').text
            repeater.links = driver.find_element_by_xpath('/html/body/div/a[2]/table/tbody/tr['+str(rptr)+']/td[9]').text

            # Open Repeater page
            driver.get(repeater.url)
            tmp = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/b').text
            repeater.open = True if tmp == 'Open' else False if tmp == 'Closed' else None
            repeater.ctcss = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/b').text
            repeater.latitude = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[12]/td[2]/table/tbody/tr[1]/td[2]/b').text.strip()
            repeater.longitude = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[12]/td[2]/table/tbody/tr[2]/td[2]/b').text.strip()
            repeater.elevation = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[13]/td[2]/b').text
            if driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[18]/td[2]/b').text == 'Link':
                repeater.website = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[18]/td[2]/b/a').get_attribute('href')

            # Additional Information
            # repeater.features = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]').text
            # repeater.erp = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]').text
            # repeater.last_coordinated = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]').text
            # repeater.last_updated = driver.find_element_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]').text
            # coverage_notes = driver.find_elements_by_xpath('/html/body/center[2]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[10]/td/ul/li')
            # for coverage_note in coverage_notes:
            #     repeater.coverage_notes = coverage_note.text

            # Save results
            wb.active.append(repeater.to_list())
            repeater.clear()
            del repeater

            # Go back to main list
            driver.get(url)
        
        # Save Excel File
        wb.save(filename=cwd+'/utah_repeaters.xlsx')
    driver.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Scrape utahvhfs.org/rptr.html for info')
    scrape_utahvhf_org()
