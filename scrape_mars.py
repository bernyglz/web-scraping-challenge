def scrape():

    # Dependencies
    import pandas as pd
    import pdb
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    from selenium import webdriver
    import pymongo

    #Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    #Assign the text to variables that you can reference later.

    # define browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html= browser.html
    soup = bs(html, "html.parser")

    contents={}
    contents["title"] = soup.find("div", class_="content_title").text
    contents["paragraph"] = soup.find("div", class_="article_teaser_body").text
    contents["date"] = soup.find('div', class_='list_date').text

    #JPL Mars Space Images!
    # visit website


    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_image_url)

    html= browser.html
    soup = bs(html, "html.parser")

    # create html object and parse with beautifulsoup
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')

    base_url = "https://www.jpl.nasa.gov"
    mars_image = image_soup.find(id='full_image').get('data-fancybox-href')
    mars_image_full_url = base_url + mars_image

    #Mars Weather from twitter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    base_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(base_weather_url)

    html = browser.html
    soup = bs(html, "html.parser")

    #twitter["mars_weather"] = soup.find("div", class_="js-tweet-text-container").text()

    #twitter

    # create html object and parse with beautifulsoup
    #time.sleep(1)
    weather_html = browser.html
    weather_soup = bs(weather_html, 'lxml')
    #weather_soup = bs(weather_html, 'html.parser')

    # scrape the weather information
    weather = weather_soup.find('title')
    weather = weather.text

    listings = {}

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    listings["mars_weather"] = soup.find("div", class_="css-1dbjc4n").get_text()

    #listings["mars_weather"] = soup.find("img", class_="imagen").get_image()

    tweetoutcome = listings["mars_weather"]

    #Mars Facts

    facts1_url = 'https://space-facts.com/mars/'

    # extract mars facts and make it a dataframe
    facts1 = pd.read_html(facts1_url)
    facts1_df = facts1[0]

    facts2_url = 'https://space-facts.com/mars/'

    # extract mars facts and make it a dataframe
    facts2 = pd.read_html(facts2_url)
    facts2_df = facts2[1]

    #Mars Hemispheres
    # visit the webse
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    base_hemi_url = 'https://astrogeology.usgs.gov'
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)

    # create html object and parse with beautifulsoup
    hemi_html = browser.html
    hemi_soup = bs(hemi_html, 'html.parser')

    # scrape the hemisphere titles and images
    hemisphere_image_urls = []
    hemi_container = hemi_soup.find('div', id='product-section')
    hemi_images = hemi_container.find_all('div', class_='item')
    for images in hemi_images:
        title = images.find('h3').text
        link = images.find('a')['href']
        browser.visit(base_hemi_url + link)
        soup = bs(browser.html, 'html.parser')
        downloads = soup.find('div', class_='downloads')
        url = downloads.find('a')['href']
        hemisphere_image_urls.append({'title': title, 'img_url' : url})

    hemi1 = hemisphere_image_urls[0]
    hemi1_title = hemi1["title"]
    hemi1_title

    hemi1 = hemisphere_image_urls[0]
    hemi1_img = hemi1["img_url"]
    hemi1_img

    hemi2 = hemisphere_image_urls[1]
    hemi2_title = hemi2["title"]
    hemi2_title

    hemi2 = hemisphere_image_urls[1]
    hemi2_img = hemi2["img_url"]
    hemi2_img

    hemi3 = hemisphere_image_urls[2]
    hemi3_title = hemi3["title"]
    hemi3_title

    hemi3 = hemisphere_image_urls[2]
    hemi3_img = hemi3["img_url"]
    hemi3_img

    hemi4 = hemisphere_image_urls[3]
    hemi4_title = hemi4["title"]
    hemi4_title

    hemi4 = hemisphere_image_urls[3]
    hemi4_img = hemi4["img_url"]
    hemi4_img

    mars_dict={"news_title":title,
               "news_paragraph": paragraph,
               "featured_image_url":mars_image_full_url,
               "weather":tweetoutcome,
               "facts1":facts1_df,
               "facts2":facts2_df,
               "hemisphere_images_urls":hemisphere_image_urls,
               "hemi1_title": hemi1_title,
               "hemi1_img": hemi1_img,
               "hemi2_title": hemi2_title,
               "hemi2_img": hemi2_img,
               "hemi3_title": hemi3_title,
               "hemi3_img": hemi3_img,
               "hemi4_title": hemi4_title,
               "hemi4_img": hemi4_img,

              }

    return mars_dict