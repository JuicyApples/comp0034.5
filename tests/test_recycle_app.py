from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# test case id format is an abbreviation in the pattern of mmffddd where m stands for module,
# f for file, and d for three digits which convey the number of your test case.
def test_rere001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'Waste and recycling' (not case sensitive)
    """
    app = import_app(app_file='apps.recycle_app.recycle_app')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == 'Waste and recycling'.casefold()


def test_rere002_dropdown_default(dash_duo):
    """
    GIVEN the app is running
    WHEN the dropdown selector on the home page is located
    THEN the value of the default selection should be 'London'
    """
    app = import_app(app_file='apps.recycle_app.recycle_app')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    WebDriverWait(dash_duo.driver, 3)
    assert 'London' in dash_duo.find_element("#area-select").text, "'London' should appear in the area dropdown"


def test_rere002_area_dropdown_changes_stats(dash_duo):
    """
    GIVEN the dash app page is loaded
    WHEN the area dropdown is changed to Hackney
    THEN the card title for the stats panel is also changed to Hackney.

    Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
    """
    app = import_app(app_file='apps.recycle_app.recycle_app')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#area-select", timeout=4)
    select_input = dash_duo.find_element("#area-select input")
    select_input.send_keys("Hackney")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert 'HACKNEY' in dash_duo.find_element("#card-name").text, "'HACKNEY' should appear in the card name"
