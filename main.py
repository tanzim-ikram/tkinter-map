import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Example data: List of (latitude, longitude, place) tuples
lat_long_data = [
    (37.7749, -122.4194, "San Francisco"),
    (34.0522, -118.2437, "Los Angeles"),
    (40.7128, -74.0060, "New York"),
    (51.5074, -0.1278, ""),
]

# Update this path to the location of your downloaded shapefile
shapefile_path = os.path.join(os.getcwd(), "map", "ne_110m_admin_0_countries.shp")

# Function to plot the map using geopandas and matplotlib
def plot_map():
    # Load a world map from the downloaded shapefile
    world = gpd.read_file(shapefile_path)

    # Create a matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the world map
    world.plot(ax=ax, color='lightgray')

    # Plot each latitude and longitude as a red point
    for lat, lon, place in lat_long_data:
        ax.plot(lon, lat, marker='o', color='red', markersize=5)
        ax.text(lon + 0.5, lat + 0.5, place, fontsize=8)  # Add label next to the point

    # Set plot labels
    ax.set_title("World Map with Locations")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    return fig

# Function to embed the map plot into Tkinter
def show_map_in_tkinter():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Map Viewer")

    # Get the matplotlib figure
    fig = plot_map()

    # Embed the matplotlib figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # Add the canvas to the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the Tkinter event loop
    window.mainloop()

# Show the map in Tkinter
show_map_in_tkinter()
