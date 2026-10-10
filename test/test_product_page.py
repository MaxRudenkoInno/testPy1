
def test_header_title(product_page):
    product_page.open_page()
    product_page.check_title_is('Category: Power Tools')