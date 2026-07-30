from playwright.sync_api import sync_playwright
import os

html_path = "file://" + os.path.abspath("V4.html")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # Desktop Context
    context_desktop = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context_desktop.new_page()
    page.goto(html_path)
    page.wait_for_timeout(1000) # Wait for initial animations
    page.screenshot(path='desktop.png', full_page=True)
    
    # Mobile Context
    context_mobile = browser.new_context(viewport={'width': 375, 'height': 812}, is_mobile=True)
    page = context_mobile.new_page()
    page.goto(html_path)
    page.wait_for_timeout(1000)
    page.screenshot(path='mobile_top.png')
    
    # Check if Hamburger Menu works
    page.click('#mobile-menu-toggle')
    page.wait_for_timeout(1000) # Wait for slide-in animation
    page.screenshot(path='mobile_menu_open.png')
    
    # Click link to close it
    page.click('.mobile-link:first-child')
    page.wait_for_timeout(1000)
    page.screenshot(path='mobile_menu_closed.png')

    # Test reverse scroll
    # Scroll down
    page.evaluate('window.scrollTo(0, 500)')
    page.wait_for_timeout(500)
    page.screenshot(path='mobile_scrolled_down.png')
    
    # Scroll up (reverse scroll)
    page.evaluate('window.scrollTo(0, 400)')
    page.wait_for_timeout(500)
    page.screenshot(path='mobile_scrolled_up.png')

    browser.close()
    print("Screenshots taken successfully.")
