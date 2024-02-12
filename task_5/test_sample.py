from task_5 import Downloader
import pytest
import os

@pytest.mark.parametrize("index",[8,22,34])
def test_index(index):

    d = Downloader("./task_4/links.parquet")
    image_path = d[index]

    # test case for downloading one file
    assert os.path.exists(image_path) == True or image_path== "Download failed: an error occured"

@pytest.mark.parametrize("part",[slice(13,15),slice(25,29),slice(40,45)])   
def test_slice(part):
    s = part.start
    e = part.stop
    d = Downloader("./task_4/links.parquet")

    image_paths = d[s:e]
    for path in image_paths:
        assert os.path.exists(path) == True or path== "Download failed: an error occured"
        s+=1

