# Satellite-image-generator-using-geographical-libraries-of-python
A model made using the geographical libraries of python which returns the satellite image of a place by taking the latitudes and longitudes as input.

Generate and visualize high-resolution satellite images for any geographic region using popular Python geospatial libraries.

🚀 Overview

This project provides a simple Python pipeline to:

● Fetch satellite imagery from open map/imagery providers.

● Generate images based on user-defined coordinates, bounding boxes, or shapefiles.

● Save outputs as static images or interactive maps.

It is useful for tasks like:

● Urban planning & resource monitoring

● Educational demos of geospatial analysis

● Quick visualization of geographic datasets

✨ Features

● Flexible Input: Accepts latitude/longitude, GeoJSON, or shapefile polygons.

● Multiple Sources: Supports providers such as OpenStreetMap, NASA Earthdata, and Google Earth Engine*.

● Custom Resolution: Control zoom levels and output image size.

● Optional Overlays: Add boundaries, points of interest, or custom layers.

*Google Earth Engine requires a free API key and account.

🛠️ Tools used 

● Python 3.9+

● geopandas
 for spatial data handling

● matplotlib
To plot and display static graphs or images, including map layers.

● contextily
Add high-resolution basemap tiles (e.g., satellite or street maps) to GeoPandas plots.

● shapely
Create and manipulate geometric shapes such as points for spatial analysis.

● functools
Cache function results to speed up repeated computations.

● re (Regular Expressions)
Search, match, and manipulate strings using pattern matching.


We can also see an example:


<img width="1118" height="68" alt="image" src="https://github.com/user-attachments/assets/5ab07a20-408c-4689-b3f1-e681d0c437d3" />


