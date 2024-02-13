# Part 1:
# Optimize download speeds in Downloader class by using threads.
# Monitor CPU usage and time taken.

# References:
# concurrent.futures.ThreadPoolExecutor

# Part 2:
# Pick an open-source software on GitHub
# Write a script that showcases the basic usage of the software

import concurrent.futures
import pyarrow.parquet as pq
import requests
import os 

class Downloader:

    # constructor equivalent function gets called at Downloader(link)
    def __init__(self, pq_file: str):

        self.df = pq.read_table(pq_file,columns=["URL"]).to_pandas()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'}
    
    # special function to implement [] bracket gets called at d[]
    def __getitem__(self, key):
        # checking if its a slice(i,j)(i:j) or i
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
            return self.download_range(start, stop+1)
        else:
            return self.download_image(key)
        
    # download an image provided the index
    def download_image(self, index: int) -> str:
        
        # setting up url and image name
        url = self.df["URL"][index]
        root,ext = os.path.splitext(url)
        # removing the arguments part of url
        ext = ext.split('?')[0]
        image_name = f"image_{index}{ext}"
        image_path = os.path.join("./downloads", image_name)


        if len(ext) > 4 or len(ext) < 1 :
            print("Download failed: invalid file extension") 
        else:
            try:
               response = requests.get(url,headers=self.header)

               if response.url.startswith("https://"):
                    if response.status_code == 200:
                        with open(image_path,'wb') as f:
                            f.write(response.content)
                        print(f"Download successful: {image_path}")
                        return image_path
                    else:
                        print(f"Download failed: Failed to retrieve image. Status code: {response.status_code}")
               else:
                   print("Download failed: connection not secure(HTTP)")
            except Exception as e:
                print(f"Download failed:  Exception occured : {e}")
        return "Download failed: an error occured"
        
    # downloading images within a range
    def download_range(self, start: int, stop: int) -> list:
        image_paths = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(start, stop):
              future = executor.submit(self.download_image,i)
              image_paths.append(future.result())

        return image_paths


#  demo testing     
# d = Downloader("../task_4/links.parquet")
# image_path = d[13]