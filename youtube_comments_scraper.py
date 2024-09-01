from playwright.sync_api import sync_playwright
from datetime import datetime
import csv
import re

def main():
  with sync_playwright() as p:
    browser = p['chromium'].launch()
    try:
        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 2080})
        page.goto("https://www.youtube.com/watch?v=x8VkB8ap_FQ")
        
        page.locator("#leading-section").get_by_text("Comments").click()
        inner_comments = page.locator("#main").all()

        # datetime object containing current date and time
        now = datetime.now()
        
        print("now =", now)
        
        with open('comments-{}.csv'.format(now), 'x') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(['author','comment'])
            # writing the data rows
            for index in range(15):
                author_name = re.sub('\n.*','', inner_comments[index].locator("#header-author").inner_text())
                inner = re.sub('"','', inner_comments[index].locator("#content-text").inner_text())
                csvwriter.writerow([author_name, inner])
    
    finally:
        browser.close()
    

main()