import time


def get_card_data(driver, url, num_of_pages, card_type):
    rarity_names = ['Common', 'Uncommon', 'Rare', 'Promo', 'Holo Rare', 'Ultra Rare', 'Secret Rare', 'Shiny Holo Rare',
                    'Prism Rare', 'Rare BREAK', 'Rare Ace', 'Amazing Rare']
    total_rarities = []
    total_names = []
    total_prices = []
    total_sets = []
    total_types = []

    driver.get(url)
    time.sleep(10)
    select_btn = driver.find_element_by_css_selector("div.select select")
    select_btn.click()
    time.sleep(2)
    market_price_high = driver.find_element_by_xpath("//option[@value='market-high-low']")
    market_price_high.click()
    time.sleep(2)

    while num_of_pages > 0:
        rarity_items = driver.find_elements_by_css_selector("section.search-result__rarity span")
        card_names = driver.find_elements_by_class_name("search-result__title")
        market_prices = driver.find_elements_by_class_name("search-result__market-price--value")
        set_names = driver.find_elements_by_class_name("search-result__subtitle")

        page_rarity = []
        for item in rarity_items:
            if item.text in rarity_names:
                page_rarity.append(item.text)

        for i in range(len(card_names)):
            total_types.append(card_type)
            total_rarities.append(page_rarity[i])
            total_names.append(card_names[i].text)
            try:
                price = market_prices[i].text.split("$")[1]
            except IndexError:
                price = "0.00"
            finally:
                total_prices.append(price)
            total_sets.append(set_names[i].text)

        button = driver.find_element_by_id("nextButton")
        num_of_pages -= 1
        if num_of_pages != 0:
            button.click()
        time.sleep(10)

    return total_rarities, total_names, total_prices, total_sets, total_types
