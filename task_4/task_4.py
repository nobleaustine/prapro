# Download links.parquet from https://drive.google.com/file/d/1ym_RbsjN41cwXZLeB3NibN7h7Vbz1AgP/view?usp=sharing
# Download and save the first 10,000 images from the links in the parquet file.
# - Monitor CPU and network usage during download.

# References:
# pyarrow package
# requests package

import pyarrow.parquet as pq
import requests
import os

def get_image(url,i):

    URL = url.split('/')[-1]
    extension = URL.split('?')[0]
    ext = extension.split('.')[-1]
    if len(ext) < 4 or len(ext) > 0 :
    
        #creating image name and path
        image_name = f"image_{i}.{ext}"
        image_path = os.path.join("downloads", image_name)
        
        # downloading the images and storing 
        # putting try catch to check if link is valid and extension is there
        try:
            response = requests.get(url, headers=headers,timeout=(10,40))

            if response.url.startswith('https://'):

                if response.status_code == 200 :
                    with open(image_path, "wb") as file:
                        file.write(response.content)
                    print(f"Downloaded {image_name}")
                    return image_path
                    i+=1
                else:
                    print(f"Failed to retrieve image. Status code: {response.status_code}")
            else:
                print("Connection is not secure (HTTP)")
                
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"invalid extension {ext}")

    return "Download failed: an error occured"

file_path = "links.parquet"
# extracting all info in links.parquet and storing it as a pandas table
table = pq.read_table(file_path,columns=["URL"])
df = table.to_pandas()

# keeping header to make as if the requests is coming from a server
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'}

if __name__ == "__main__":
    # downloading the first n images and storing it
    n = int(input("Enter no. of images: "))
    i = 1
    for index,url in df['URL'].items():
        if i == n+1:
            break
        print(f"df index: ",index)
        get_image(url,i)
        print(" ")

