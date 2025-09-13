import logging
import sys
from playwright.sync_api import expect
import re

logger = logging.getLogger(_name_)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def test_open_gmail(page):
    EMAIL = "trainer@way2automation.com"
    PASSWORD = "trainer123"
    page.goto("http://gmail.com")
    page.locator("//input[@id='identifierId']").fill(EMAIL)
    page.wait_for_timeout(2000)
    # page.locator("//input[@id='identifierNext']").click()

    # assert page.title() == "Gmail"
    logger.info(f"Page title is: {page.title()}")

    page.wait_for_timeout(2000)

    page.get_by_text("Next").click()
    page.wait_for_timeout(2000)
    logger.info("Clicked Next button")
    page.pause()

    page.locator("//input[@type='password']").fill(PASSWORD)
    logger.info("Filled password field")
    page.get_by_text("Next").click()
    page.wait_for_timeout(5000)


def test_handling_dropdown(page):
    page.goto("http://www.wikipedia.org/")

    # page.select_option("select", label="Eesti")  # index, text
    # page.select_option("select", value="hi")
    page.select_option("select", index=1)

    # page.locator("//select[@id='searchLanguage']").select("Deutsch")
    page.wait_for_timeout(2000)

    options = page.locator("option").all()

    print("Total Values are :", len(options))
    print("Total dropdown options are :", [option.inner_text() for option in options])


def test_handling_links(page):
    page.goto("http://www.wikipedia.org/")

    block = page.locator("//*[@id='www-wikipedia-org']/footer/nav")
    print("Footer block text is:", block.inner_text())
    sys.stdout.flush()

    links = block.locator("a").all()
    print(f"Total links found: {len(links)}")
    sys.stdout.flush()

    for link in links:
        text = link.inner_text()
        lang = link.get_attribute("href")
        print(f"Link Text: {text}, Link URL: {lang}")
        logger.info(f"Link Text: {text}, Link URL: {lang}")
        sys.stdout.flush()

    """
    //tagName[@attribute='value'] - Relative Xpath 

    //input[@id='identifierId']  -

    //input[@name='identifier'][@id='identifierId']

    #CSS Selector
    
    # In console Tab
    $x("//input[@name='identifier' and @id='identifierId']"

    <input type="submit" class="button" value="Submit">
    
     $x("//input['starts-with']"

    

    Absoulute Xpath:





    """


def test_checkboxes(page):
    page.goto("http://tizag.com/htmlT/htmlcheckboxes.php")

    block = page.locator("//table/tbody/tr/td/div[4]")
    check_boxes = block.locator("[name='sports']")
    check_boxes_count = check_boxes.count()

    logger.info(f"Total checkboxes found: {check_boxes_count}")
    for i in range(check_boxes_count):
        check_boxes.nth(i).check()
        logger.info(f"Checkbox {i+1} is checked")
        page.wait_for_timeout(1000)


def test_assertions(page):
    page.goto("http://tizag.com/htmlT/htmlcheckboxes.php")

    expect(page).to_have_url("http://tizag.com/htmlT/htmlcheckboxes.php")
    print("URL assertion passed")

    expect(page).not_to_have_url("error")
    print("Negative URL assertion passed")

    expect(page).to_have_title("HTML Tutorial - Checkboxes")
    print("Title assertion passed")

    link = page.locator("//a[normalize-space()='HTML - Forms']")
    expect(link).to_have_text("HTML - Forms")
    print("Link text assertion passed")

    checkbox = page.locator("//div[4]//input[1]")
    expect(checkbox).to_be_visible()

    print("Checkbox is visible")

    # logger.info("All assertions passed successfully")


def test_webtables(page):
    page.goto("https://money.rediff.com/indices/nse/nifty-50")

    row_page_content = page.locator("#leftcontainer > table > tbody")
    print("Row text is:", row_page_content.inner_text())

    row_count = page.locator("#leftcontainer > table > tbody > tr").count()
    print("Row count is:", row_count)

    col_count = page.locator(
        "#leftcontainer > table > tbody > tr:nth-child(1) > td"
    ).count()
    print("Column count is:", col_count)

    # text = page.locator(
    #     "#leftcontainer > table > tbody > tr:nth-child(2) > td:nth-child(1)"
    # ).inner_text()
    # print("3rd row 1st column text is:", text)

    text = page.locator(
        "#leftcontainer > table > tbody > tr:nth-child(2) > td:first-child"
    )
    expect(text).to_have_text("Adani")

    print("3rd row 1st column text assertion passed")