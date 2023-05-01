import urllib.request
import requests
import os
from datetime import datetime

 
 # function to download an image using it's url.
 # the name parameter is to name the image.
def download_image_by_url(url, name):
    
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
            print('Image could not be retrieved, image status is not OK')
    
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
        
        # checking if the file is empty
        if os.stat(file_name).st_size != 0 :
        
            # openning the file and reading urls line by line.
            with open(file_name) as images_file:
                                
                # saving the images one by one in this folder.
                for image_url in images_file : 
                    
                    # using (minutes, seconds, milliseconds) to name the images in the loop.
                    current_time = datetime.now()
                    time_str = current_time.strftime("%M%S%M")
                    
                    # getting the extention of the image and deleting new lines
                    ext = os.path.splitext(image_url)[1].strip("\n")        
                    download_image_by_url(image_url, f'image{str(time_str)}{str(ext)}')
                    
        else:
            print(" the file is empty.")
                    
    else:
        print("File is not a text file")

# calling the fuction to test it 
download_images('images.txt')
