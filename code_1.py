import urllib.request
import requests
import os
 
 # function to download an image using it's url.
 # the name parameter is to name the image.
def download_images_by_url(url, name):
    try:
        res = requests.get(url, verify = False)
        
        # checking if the code status is OK or failed.
        if res.status_code == 200: 
                                
            # validate the image file type.
            ext = os.path.splitext(name)[1]
            if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
                os.remove(name)
                print(f"{name} deleted : invalid file type.")
                
            else:
                # download the image.
                urllib.request.urlretrieve(url,name)
                print(f"{name} downloaded successfully.")
        
        
        else:
            print('Image could not be retrieved')
    
    # exceptions         
    except requests.exceptions.ConnectionError as E:
        print(f"Request failed: {E}")

    except requests.RequestException as E:
        print(f"Request failed: {E}")
          
    except OSError as E:
        print(f"Request failed: {E}")
        
    except Exception as E:
        print(f"Request failed: {E}") 
           

 # function to download all the images from a file.
def download_images(file_name):
    
    # validate the file type - only text files accepted.
    if os.path.splitext(file_name)[1].lower() == ".txt":
        
        # openning the file and reading urls line by line.
        with open(file_name) as images_file:
            
            # to name the images in the loop.
            count = 0
            
            # saving the images one by one in this folder.
            for image_url in images_file :         
                download_images_by_url(image_url, f'image{str(count)}.jpg')
                count += 1 
                
    else:
        print("File is not a text file")

download_images('images.txt')
