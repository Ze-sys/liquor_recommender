from selenium import webdriver
import time
import numpy as np
import pandas as pd
import re
import math

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.support.ui import Select



class Liquor:
    '''
    Does most of the scraping. Detail to come...
    '''
    def __init__(self, products):
        beer_data = pd.DataFrame(columns=['product_name','availability_info','package_info',
                                          'reg_price(CAD)','sale_price(CAD)','savings(%)','sale_until',
                                          'star_rating','total_volume(ml)','cents_per_ml','cents_per_ml_per_ratings']) 

        for product_list in products:

            # product name
            product_name = product_list.find_element_by_tag_name('h3').text

            # packaging and volume info
            package_info = product_list.find_element_by_class_name("product-subtitle-info").text.split('\n')[0]

            cnt_vol = re.findall(r'\d+',package_info)

            if len(cnt_vol) == 2: 
                cnt, vol = cnt_vol
            else: 
                cnt, vol = 1, cnt_vol[0]

            total_volume = math.prod([int(cnt),float(vol)])

            # price info
            sale_price = product_list.find_element_by_class_name("onsale-product-price").text
            reg_price = float(product_list.find_element_by_class_name("product-price").text.strip('$'))  # (small values are good)
            cents_per_ml = np.round(reg_price/total_volume,4)*100
            
#             print(product_name,sale_price)
            # availability_info
            availability_info = product_list.find_element_by_id("availability").text

            # sale end date info, also drop dollar sign
            if sale_price:
                sale_price = float(sale_price.strip('$'))
                sale_until = product_list.find_element_by_class_name("offer-date").text
                savings = np.round(((reg_price-sale_price)/reg_price),2)*100
            else:
                sale_price = np.nan
                sale_until = np.nan
                savings= np.nan

            # star ratings
            full_stars = product_list.find_elements_by_class_name("fa.fa-star") 
            half_stars = product_list.find_elements_by_class_name("fa.fa-star-o") 
            no_stars = product_list.find_elements_by_class_name("fa.fa-star-half-o") 

            if half_stars or full_stars:
                star_rating = len(full_stars) + .5*len(half_stars)
            else:
                star_rating = np.nan

            cents_per_ml_per_ratings = np.round(cents_per_ml/star_rating,4)  # (small values are good)


            df = pd.DataFrame({'product_name':[product_name],'availability_info':[availability_info],'package_info':[package_info],
                               'reg_price(CAD)':[reg_price],'sale_price(CAD)':[sale_price],'savings(%)':[savings],'sale_until':[sale_until],
                               'star_rating':[star_rating],'total_volume(ml)':total_volume, 'cents_per_ml':[cents_per_ml],'cents_per_ml_per_ratings':[cents_per_ml_per_ratings]})
            beer_data = pd.concat([beer_data, df], axis=0)
            beer_data.reset_index(drop=True, inplace=True)
        self.liquor_data = beer_data


# Driver setup
# ! pkill -f "(chrome)?(--headless)"

p_type,pkg_type = 'beer', 'can'

df = pd.DataFrame(columns=['product_name','availability_info','package_info',
                                          'reg_price(CAD)','sale_price(CAD)','savings(%)','sale_until',
                                          'star_rating','total_volume(ml)','cents_per_ml','cents_per_ml_per_ratings'])
    
for page in range(1,20):
    try:
        url = f'http://www.bcliquorstores.com/product-catalogue?search={p_type}%20{pkg_type}&sort=consumerRating:desc&page={page}'

        opts = Options()
        opts.add_argument("--incognito")
        opts.add_argument("--disable-popup-blocking")
        opts.headless =True
        driver = Chrome(options=opts)
        driver.get(url)
        driver.implicitly_wait(2)
        products = driver.find_elements_by_class_name("product-description-container")
        beer = Liquor(products)
        beer = beer.liquor_data
        df = pd.concat([df,beer], axis=0, ignore_index=True)
        driver.close()
        time.sleep(1)
    except IndexError:
        pass