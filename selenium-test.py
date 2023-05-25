CODE 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_webpage_ui(url):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # You may need to download and configure the appropriate WebDriver for your browser

    # Load the web page
    driver.get(url)

    try:
        # Test case 1: Verify the presence of a specific element on the page
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'example-element-id'))
        )
        print("Element found on the page")

        # Test case 2: Verify the text of an element
        expected_text = "Example text"
        element_text = element.text
        assert expected_text == element_text, f"Expected text: {expected_text}, Actual text: {element_text}"

        # Test case 3: Verify the value of an input field
        expected_value = "Example value"
        input_field = driver.find_element(By.ID, 'example-input-id')
        input_value = input_field.get_attribute("value")
        assert expected_value == input_value, f"Expected value: {expected_value}, Actual value: {input_value}"

        # Test case 4: Verify the visibility of an element
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'example-class'))
        )
        print("Element is visible on the page")

        # Add more test cases as needed

    except AssertionError as ae:
        print(f"UI test failed: {str(ae)}")
    except Exception as e:
        print(f"An error occurred during UI testing: {str(e)}")

    finally:
        # Clean up
        driver.quit()

# Example usage
test_webpage_ui("https://www.example.com")
