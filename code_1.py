import urllib
import urllib.request
import requests
    
def download_img_by_url(url, name):
    res = requests.get(url, verify = False)
        
    if res.status_code == 200:
        try:
            urllib.request.urlretrieve(url,name)
                
        except requests.ConnectionError as E:
            print(str(E))

        except requests.RequestException as E:
            print(str(E))
            
        except OSError as E:
            print(str(E))
            
    else:
        print('Image Could not be retrieved')

# openning the file and reading urls line by line 
with open('images.txt') as images_file:
    images_url = images_file.readlines()

    # to name the images 
    count = 0
    # saving the images one by one in this folder 
    for image_url in images_url : 
        download_img_by_url(image_url, f'image{str(count)}.jpg')
        count += 1

