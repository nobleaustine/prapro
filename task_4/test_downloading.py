from task_4 import df,file_path,get_image
import pandas as pd
from pathlib import Path
import pytest
import os

# test if a pandas datafram is extracted
def test_dataframe():
    assert isinstance(df,pd.DataFrame) == True

# test if file exsist and its a parquet file
def test_path():
    assert Path(file_path).is_file() and file_path.endswith('.parquet')

# testing downloading
@pytest.mark.parametrize("url, i, index",[("https://images.squarespace-cdn.com/content/54efd71fe4b06377d0b2fb17/1525152563529-4XIS44FIBU4N7JCZLEXD/20180429+-+Juanes+-+Toronto+Music+Photography+-+Captive+Camera-5391.jpg?content-type=image%2Fjpeg",13,1),
                                ("https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_10248639.jpg?crop=pad&amp;pad_color=FFF&amp;format=jpeg&amp;w=704&amp;h=1080",34,2),
                                ("https://img.sharetv.com/shows/characters/thumbnails/blue_bloods.det_danny_reagan.jpg",58,3)])
def test_index(url,i,index):
    image_path = get_image(url,i,index)

    assert os.path.exists(image_path) == True or image_path== "Download failed: an error occured"


