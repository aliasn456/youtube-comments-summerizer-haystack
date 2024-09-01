import re
import csv
from datetime import datetime
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.set_viewport_size({"width": 1920, "height": 2080})
    page.goto("https://www.youtube.com/watch?v=x8VkB8ap_FQ") # Put link the youtube video 

    # Expect a title "to contain" a substring.
    page.get_by_role("heading", name="Sabrina Carpenter - Bed Chem (Official Lyric Video)", exact=True).click()
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
            author_name = re.sub('\n.*','',inner_comments[index].locator("#header-author").inner_text())
            inner = re.sub('"','',inner_comments[index].locator("#content-text").inner_text())
            csvwriter.writerow([author_name, inner])