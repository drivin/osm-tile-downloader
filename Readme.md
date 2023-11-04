# OSM Tile Downloader

This Python script is designed to download map tiles from a specified map tile server for a given geographical area and zoom level range. It utilizes multithreading to optimize the download process.

**Please Note: Do not use this script on public servers, as it may lead to a ban. This script is intended for personal use on a local server.**

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Requirements

Before using this script, ensure you have the following dependencies installed:

- Python 3.x
- `concurrent.futures`
- `pygeotile`

You can install the required packages using `pip`:

```bash
pip install concurrent.futures pygeotile

## Usage

1. Clone or download this repository to your local machine.

2. Configure the script by editing the [Configuration](#configuration) section in the script to suit your needs.

3. Run the script using the following command:

   ```bash
   python tile_downloader.py

The script will start downloading map tiles for the specified geographical area and zoom level range. Downloaded tiles will be saved in the "tiles" folder (or the folder you specified in the configuration).

## Configuration

Before using the script, you can customize its behavior by editing the configuration section at the beginning of the script. Here are the configurable options:

- `output_folder`: The folder where downloaded map tiles will be saved. Default is "tiles."

- `tile_host`: The URL of the map tile server. Update this to the URL of your map tile server.

- `max_concurrent_downloads`: The maximum number of concurrent downloads. Adjust this based on your system's capabilities.

- `zoom_start`: The starting zoom level for downloading map tiles.

- `zoom_end`: The ending zoom level for downloading map tiles.

- `square`: Define the geographical area to download tiles. Specify the latitude and longitude of the top-left (top, left) and bottom-right (bottom, right) corners.

Make sure to adjust these settings to match your specific requirements.

## License
tba

Happy map tile downloading!
