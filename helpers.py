from playwright.sync_api import expect


def click_next_by_index(page, index):
    nav = page.locator(".step-nav").nth(index)
    nav.locator('[data-action="next"]').click()


def fill_step_one_form(page, data):
    page.locator('#ff_8_asset_type').select_option(label=data['type'])
    page.locator('#ff_8_asset_status').select_option(label=data['status'])
    page.locator('#ff_8_city').select_option(label=data['city'])
    page.locator('#ff_8_street_1').select_option(label=data['street'])

def fill_step_two_form(page, data):
    page.fill('input[name="floor"]', data["floor"])
    page.locator('#ff_8_room_num').select_option(label=data["number_of_rooms"])
    page.locator('#ff_8_terrace').select_option(label=data["terrace"])
    page.locator('#ff_8__parking').select_option(label=data["parking"])
    page.fill('input[name="built_mr"]', data["built_area_mr"])
    page.locator('#ff_8_elevator_1').select_option(label=data["elevator"])

def fill_step_three_form(page, data):
    for feature in data["features"]:
        page.locator(f"text={feature}").click()

    page.fill('#ff_8_asset_description', data["description"])

def fill_step_four_form(page, data):
    page.fill('input[name="credits"]', data["credits"])
    page.fill('input[name="price"]', data["price"])
    page.evaluate(f"""
        document.querySelector("#ff_8_date_start")._flatpickr.setDate({data['start_date']});
    """)

def fill_step_five_form(page, image_path):
    page.set_input_files("#ff_8_pictures_1", image_path)
    progress = page.locator('span.ff-upload-progress-inline-text')
    expect(progress).to_have_text("100% Completed", timeout=10000)

def fill_step_six_form(page, data):
    page.fill('input[name="name_full"]', data["full_name"])
    page.fill('input[name="phone_number"]', data["phone"])

def verify_ad_added_to_stock(page, advertiser_name):
    page.locator('div[data-id="41187522"]').nth(0).click()
    publisher_locator = page.locator("h5.elementor-heading-title.elementor-size-default").nth(4)
    expect(publisher_locator).to_contain_text(advertiser_name)

def login(page, email, password):
    page.click("text=התחבר")
    page.fill('input[name="log"]', email)
    page.fill('input[name="pwd"]', password)
    page.click('button:has-text("התחברות")')
    page.wait_for_load_state("networkidle")