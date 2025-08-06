import os

from playwright.sync_api import sync_playwright, expect
from loguru import logger

from helpers import (
    click_next_by_index, fill_step_one_form, fill_step_two_form, fill_step_three_form, \
    fill_step_four_form, fill_step_five_form, fill_step_six_form, verify_ad_added_to_stock, login
)

URL = "https://homme.co.il"
EMAIL = os.getenv("HOMME_EMAIL")
PASSWORD = os.getenv("HOMME_PASSWORD")
IMAGE_PATH = "./files/ad_photo.png"

STEP_ONE_DATA = {'type': 'דירה', 'status': 'משופץ', 'city': 'כרמיאל', 'street': 'אביב'}
STEP_TWO_DATA = {
    "floor": "1",
    "number_of_rooms": "2",
    "terrace": "2",
    "parking": "1",
    "built_area_mr": "120",
    "elevator": "עם"
}
STEP_THREE_DATA = {
    "features": ["מחסן", "משופצת"],
    "description": "דירה מדהימה"
}

STEP_FOUR_DATA = {
    "credits": "3",
    "price": "5000",
    "start_date": "27/10/2025"  # format: DD/MM/YYYY
}

STEP_SIX_DATA = {
    "full_name": "אלירם שמש",
    "phone": "0501234567"
}


def test_publish_ad_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        logger.info("Navigating to site...")
        page.goto(URL, wait_until="load")

        logger.info("Accepting terms of service")
        page.click("text=אני מסכים לתנאי השימוש באתר", timeout=5000)

        logger.info("Logging in...")
        logger.info("Filling login credentials...")
        login(page, email=EMAIL, password=PASSWORD)

        logger.info("Navigating to 'פרסם מודעה'...")
        page.click("text=פרסם מודעה")
        page.wait_for_load_state("networkidle")

        logger.info("Filling Step 1 (Basic Details)...")
        fill_step_one_form(page, STEP_ONE_DATA)
        click_next_by_index(page, 0)

        logger.info("Filling Step 2 (Property Info)...")
        fill_step_two_form(page, STEP_TWO_DATA)
        click_next_by_index(page, 1)

        logger.info("Adding more property details...")
        fill_step_three_form(page, STEP_THREE_DATA)
        click_next_by_index(page, 2)

        logger.info("Filling payment terms")
        fill_step_four_form(page, STEP_FOUR_DATA)
        click_next_by_index(page, 3)

        logger.info("Uploading image...")
        fill_step_five_form(page, IMAGE_PATH)
        click_next_by_index(page, 4)

        logger.info("Filling contact details...")
        fill_step_six_form(page, STEP_SIX_DATA)
        page.click('button:has-text("פרסום הנכס")')
        page.screenshot(path="./files/screenshots/success.png")
        page.wait_for_load_state("networkidle")

        logger.info("Verifying ad appearance")
        verify_ad_added_to_stock(page, STEP_SIX_DATA["full_name"])
        logger.success("Ad published successfully.")

        context.close()
        browser.close()
