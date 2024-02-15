# Create a class Downloader with the following template:

# class Downloader:
#     ...
#     def __init__(self, pq_file: str):
#         ...

# where pq_file is the path to the parquet file.

# At the end of the task, the following things should work on an instance of Downloader called d:

# d[i] will download the i'th image and return its local path
# d[i : j] will download i to j images and return their local paths in a list

import pyarrow.parquet as pq
import requests
import os


class Downloader:

    # constructor equivalent function gets called at Downloader(link)
    def __init__(self, pq_file: str):

        self.df = pq.read_table(pq_file, columns=["URL"]).to_pandas()
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
        }

    # special function to implement [] bracket gets called at d[]
    def __getitem__(self, key):
        # checking if its a slice(i,j)(i:j) or i
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
            return self.download_range(start, stop + 1)
        else:
            return self.download_image(key)

    # download an image provided the index
    def download_image(self, index: int) -> str:

        # setting up url and image name
        url = self.df["URL"][index]
        root, ext = os.path.splitext(url)
        # removing the arguments part of url
        ext = ext.split("?")[0]
        image_name = f"image_{index}{ext}"
        image_path = os.path.join("./downloads", image_name)

        if len(ext) > 4 or len(ext) < 1:
            print("Download failed: invalid file extension")
        else:
            try:
                response = requests.get(url, headers=self.header)

                if response.url.startswith("https://"):
                    if response.status_code == 200:
                        with open(image_path, "wb") as f:
                            f.write(response.content)
                        print(f"Download successful: {image_path}")
                        return image_path
                    else:
                        print(
                            f"Download failed: Failed to retrieve image. Status code: {response.status_code}"
                        )
                else:
                    print("Download failed: connection not secure(HTTP)")
            except Exception as e:
                print(f"Download failed:  Exception occured : {e}")
        return "Download failed: an error occured"

    # downloading images within a range
    def download_range(self, start: int, stop: int) -> list:
        image_paths = []
        for i in range(start, stop):
            image_path = self.download_image(i)
            image_paths.append(image_path)
        return image_paths


# # Testing
# d = Downloader("./task_4/links.parquet")
# i = int(input("Enter the index of the image to be downloaded: "))
# image_path = d[i]
# print(f"Local path of image {i}:", image_path)
# print(" ")

# code_string = str(input("Enter index range: "))
# s,e=code_string.split(":")
# image_paths = d[int(s):int(e)]
# print(f"Local paths of images in the range {code_string}: ")
# for path in image_paths:
#     print(path)
