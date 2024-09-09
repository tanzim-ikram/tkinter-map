import tkinter as tk
import folium
import os
import webview

def create_map(lat_long_data):
    # Create a folium map centered at the first location (latitude and longitude)
    start_coords = (lat_long_data[0][0], lat_long_data[0][1])  # Only use lat and lon for the map center
    folium_map = folium.Map(location=start_coords, zoom_start=13)

    # Add markers for each location
    for lat, lon, place in lat_long_data:
        folium.Marker([lat, lon], popup=place).add_to(folium_map)

    # Save the map to an HTML file in the current working directory
    map_file = os.path.join(os.getcwd(), "map.html")
    folium_map.save(map_file)
    return map_file

def load_map_in_webview(map_file):
    # Create a simple WebView window that shows the map
    webview.create_window('Map Viewer', map_file)
    webview.start()

# Example list of (latitude, longitude, place) tuples
lat_long_data = [
    (37.7749, -122.4194, "San Francisco"),
    (34.0522, -118.2437, "Los Angeles"),
    (40.7128, -74.0060, "New York"),
    (51.5074, -0.1278, "London"),
]

# Create the map with the given lat/long data and get the map file path
map_file = create_map(lat_long_data)

# Load the map using webview (instead of Tkinter)
load_map_in_webview(map_file)
