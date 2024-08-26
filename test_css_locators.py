from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_id_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in/")
        print("Visited page", page.url)
        print(page.title())
        
        # cssSelector: id - #, class - ., attr. - tagname[attr.="value"]
        page.locator('#email').highlight()
        emailTextBox = page.wait_for_selector('#email')
        emailTextBox.type('test@test.ing')
        page.locator('#enterimg').highlight()
        buttonLogin = page.wait_for_selector('#enterimg')
        buttonLogin.click()
        page.wait_for_timeout(3000)
        browser.close()
        
def test_other_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://example.cypress.io/todo")
        print("Visited page", page.url)
        print(page.title())
        page.locator('input[data-test="new-todo"]').highlight()
        newTodoInput = page.wait_for_selector('input[data-test="new-todo"]')
        newTodoInput.type('test@test.ing')
        newTodoInput.press("Enter")
        addedTodo = page.get_by_text("test@test.ing")
        expect(addedTodo).to_contain_text("test@test.ing")
        page.wait_for_timeout(3000)
        browser.close() 