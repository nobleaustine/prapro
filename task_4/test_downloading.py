from task_4 import df, file_path, get_image
import pandas as pd
from pathlib import Path
import pytest
import os


@pytest.fixture
def get_urls():
    urls = [
        "https://images.squarespace-cdn.com/content/54efd71fe4b06377d0b2fb17/1525152563529-4XIS44FIBU4N7JCZLEXD/20180429+-+Juanes+-+Toronto+Music+Photography+-+Captive+Camera-5391.jpg?content-type=image%2Fjpeg",
        "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_10248639.jpg?crop=pad&amp;pad_color=FFF&amp;format=jpeg&amp;w=704&amp;h=1080",
        "https://img.sharetv.com/shows/characters/thumbnails/blue_bloods.det_danny_reagan.jpg",
    ]
    return urls


# test if a pandas datafram is extracted
def test_dataframe():
    assert isinstance(df, pd.DataFrame) == True


# test if file exsist and its a parquet file
def test_path():
    assert Path(file_path).is_file() and file_path.endswith(".parquet")


# testing downloading
def test_index(get_urls):
    for i in range(1, 4):
        image_path = get_image(get_urls[i - 1], i)
    assert (
        os.path.exists(image_path) == True
        or image_path == "Download failed: an error occured"
    )
