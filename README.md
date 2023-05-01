<h1> Image Downloader </h1> 
<h3> A script that takes this plaintext file as an argument and downloads all images, storing them on the local hard disk. </h3>


<h3> This is a Python script that downloads images from URLs in a text file. It uses the requests and urllib libraries to download the images and verify the image file type, and os and datetime to manage file and time-related operations. </h3>

<h2> download_images('images.txt') </h2>
<h3>The script will download each image in the 'images.txt' and save it with a unique name in the same folder as the script.</h3>

<h3> This script validates the file type of the downloaded image and deletes the file if it is not a valid image file type. it also uses HTTPS to retrieve the images.</h3>

<h3> The script uses the current time (in minutes, seconds, and milliseconds) to name the downloaded images and ensure unique names. </h3>