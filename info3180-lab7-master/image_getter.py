import requests
import BeautifulSoup
import urlparse
from app import app, db
from flask import render_template, request, redirect, url_for, Flask, flash, jsonify


url = "http://www.amazon.com/gp/product/1783551623"
result = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(result.text)
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']

thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']

@app.route('/images/', methods=['GET', 'POST'])
def image_dem():
    imageList = []
    
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
       if "sprite" not in img["src"]:
           results= image % urlparse.urljoin(url, img["src"])
           imageList.append(results)
           if request.headers['Content-Type']=='application/json' or request.method == 'POST':
               return jsonify(imageList)
               
            
        return render_template('images.html', imageList=imageList)
        

# image_dem()
# url = "http://www.amazon.com/gp/product/1783551623"
# result = requests.get(url)
# soup = BeautifulSoup.BeautifulSoup(result.text)
# og_image = (soup.find('meta', property='og:image') or
#                     soup.find('meta', attrs={'name': 'og:image'}))
# if og_image and og_image['content']:
#     print og_image['content']

# thumbnail_spec = soup.find('link', rel='image_src')
# if thumbnail_spec and thumbnail_spec['href']:
#     print thumbnail_spec['href']


# @app.route('/images/', methods = ['GET', 'POST'])
# def image_dem():
#     imageList = list()
    
#     image = """<img src="%s"><br />"""
#     for img in soup.findAll("img", src=True):
#           if "sprite" not in img["src"]:
#               if request.headers['Content-Type']=='application/json' or request.method == 'POST':
#                   imageList.append(image % urlparse.urljoin(url, img["src"]))
#                   return jsonify(imageList)
                      
                      
                  
    # results = image % urlparse.urljoin(url, img["src"])
    
    # for i in imageList:
    #     i = 0
    #     s = len(imageList)
        
        
        
        
    #     while i < s:
    #         i = i + 1            
            
            
            
            
    
    
    
    
    # print imageList



# image_dem()1