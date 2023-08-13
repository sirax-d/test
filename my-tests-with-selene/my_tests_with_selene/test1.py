from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('#rso>div').should(have.size_greater_than(5))\
    .first.should(have.text('Selenium automates browsers'))
browser.wait(5)
browser.quit()
