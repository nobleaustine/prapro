from task_5 import Downloader

def test():

    d = Downloader("./task_4/links.parquet")
    i = 8
    image_path = d[i]

    # test case for downloading one file
    assert image_path.split(".") == f"./task_5/downloads/image_{i}" or "Download failed: an error occured"

    s,e=13,15 
    image_paths = d[s:int(e)]
    for path in image_paths:
        assert path.split(".") == f"./task_5/downloads/image_{s}" or "Download failed: an error occured"
        s+=1

