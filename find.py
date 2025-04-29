from playwright.sync_api import sync_playwright, expect

def test_example_website():
    with sync_playwright() as p:
        # Запускаем браузер (по умолчанию Chromium)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # 1. Открываем веб-страницу
            page.goto("https:/example.com")
            
            # 2. Проверяем, что заголовок страницы содержит слово "Example"
            expect(page).to_have_title("Example Domain")
            print("Заголовок страницы содержит 'Example'")
            
            # 3. Находим элемент с текстом "More information" и кликаем по нему
            more_info_link = page.locator('css=a:has-text("More information")')
            more_info_link.click()
            
            # 4. Проверяем перенаправление на нужный URL
            expect(page).to_have_url("https://www.iana.org/domains/example")
            print("Перенаправление на правильный URL выполнено")
            
        except Exception as e:
            print(f"Тест не пройден: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    test_example_website()