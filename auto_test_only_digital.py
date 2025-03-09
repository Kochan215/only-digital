from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("https://only.digital/")

    # Ожидание загрузки футера и его проверка
    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )
    assert footer is not None, "Футер не найден на странице"

    print("Все проверки пройдены успешно")

finally:
    driver.quit()  # Закрываем браузер после теста
