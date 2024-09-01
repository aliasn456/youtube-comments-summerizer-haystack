import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.set_viewport_size({"width": 1920, "height": 2080})
    page.goto("https://www.youtube.com/watch?v=x8VkB8ap_FQ") # Put link the youtube video 

    # Expect a title "to contain" a substring.
    page.get_by_role("heading", name="Sabrina Carpenter - Bed Chem (Official Lyric Video)").click()
    page.wait_for_timeout(30000)
    # page.keyboard.down("ControlOrMeta")
    # page.keyboard.press("+")
    # page.keyboard.press("+")
    # page.keyboard.press("+")
    # page.keyboard.press("+")
    page.locator("#leading-section").get_by_text("Comments").click()
    inner_text = page.locator("#main").all_text_contents()

    for index in range(inner_text):
        inner_text[index] = re.sub(r'a', 'b', inner_text[index])
    assert inner_text == ['her lyrics are so unserious']

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()