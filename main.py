from concurrent.futures import ThreadPoolExecutor
from pygeotile.tile import Tile
import os
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen





################################
#### USER_INPUT#################
################################
output_folder = "tiles"
tile_host = "http://localhost:8888/maps"
zoom_start = 6
zoom_end = 16
square = {
        "top": 55.1,            #lat
        "right": 15.31,         #lon
        "bottom": 47.1,         #lat
        "left": 5.7             #lon
}
###############################
###############################

def downloader(url, fdest):
    if os.path.isfile(fdest):
        print(f"Übersprungen: {url} > {fdest}. Datei existiert.")
    else:
        print(f"Download: {url} > {fdest}")     
        u = urlopen(url)
        f = open(fdest, 'wb')
        f.write(u.read())
        f.close()

def download_tile_row(x):
    dest = f"{output_folder}/{z}/{x}"
    try:
        os.makedirs(dest)
    except FileExistsError as e:
        pass 
    with ThreadPoolExecutor(max_concurrent_downloads) as executor:
        futures = []
        for y in tiles_y:
            url = f"{tile_host}/{z}/{x}/{y}.png"
            fdest = f"{dest}/{y}.png"
            futures.append(executor.submit(downloader, url, fdest))
        
        for future in futures:
            future.result()


max_concurrent_downloads = 200                  #max DL per row


zoom_range = range(zoom_start, zoom_end)

for zoom in zoom_range:
        tile = Tile

        top_left = tile.for_latitude_longitude(square["top"], square["left"], zoom)
        bottom_right = tile.for_latitude_longitude(square["bottom"], square["right"], zoom)

        tms = {
                "zoom": top_left[2],
                "x_start": top_left[0]-1,
                "x_end": bottom_right[0]+1,
                "y_end": top_left[1]+1,
                "y_start": bottom_right[1]-1,
        }

        tiles_x = range(tms["x_start"], tms["x_end"])
        tiles_y = range(tms["y_start"], tms["y_end"])
        z = tms["zoom"]

        for x in tiles_x:
                download_tile_row(x)
