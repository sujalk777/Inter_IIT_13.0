print("coordinate.py is being imported")
import folium
import pandas as pd
import random
from shapely.geometry import Point, Polygon
import os

# Define file paths and corresponding elements
BASE_DIR = os.getcwd()

file_paths = {
    'Na': os.path.join(BASE_DIR, 'data', 'Mg_vs_Na.csv'),
    'Ca': os.path.join(BASE_DIR, 'data', 'Mg_vs_Ca.csv'),
    'Fe': os.path.join(BASE_DIR, 'data', 'Mg_vs_Fe.csv'),
    'Al': os.path.join(BASE_DIR, 'data', 'Mg_vs_Al.csv'),
    'Si': os.path.join(BASE_DIR, 'data', 'Mg_vs_Si.csv'),
}

def generate_map(target_lat, target_lon):
    """Generate a map highlighting polygons based on the target latitude and longitude."""
    # Generate random distinct colors for each element
    element_colors = {element: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for element in file_paths.keys()}

    # Initialize a Folium map centered on the Moon
    map_center = [0, 0]
    m = folium.Map(location=map_center, zoom_start=3, tiles=None)
    m.fit_bounds([[-90, -180], [90, 180]])

    # Add NASA Moon imagery as a base map
    folium.TileLayer(
        tiles="https://trek.nasa.gov/tiles/Moon/EQ/LRO_WAC_Mosaic_Global_303ppd_v02/1.0.0/default/default028mm/{z}/{y}/{x}.jpg",
        attr="NASA Moon Imagery",
        name="Lunar Surface",
        overlay=False,
        control=True,
        max_zoom=8,
        min_zoom=0,
        tms=False,
        no_wrap=True,
        transparent=True
    ).add_to(m)

    highest_snr = -1
    highest_snr_element = None
    highest_snr_polygon = None
    target_point = Point(target_lon, target_lat)  # Shapely point for the target location

    # Iterate through all elements and their corresponding CSV files
    for element, path in file_paths.items():
        try:
            # Check if the CSV file exists
            if not os.path.exists(path):
                print(f"CSV file for {element} not found at path: {path}")
                continue

            # Load the CSV data
            data = pd.read_csv(path)

            # Apply the filtering logic to handle longitude crossings
            data = data[
                ~(
                    ((data['v0_lon'] > 170) & (data['v1_lon'] < -170)) |
                    ((data['v0_lon'] > 170) & (data['v2_lon'] < -170)) |
                    ((data['v0_lon'] > 170) & (data['v3_lon'] < -170)) |
                    ((data['v1_lon'] > 170) & (data['v2_lon'] < -170)) |
                    ((data['v1_lon'] > 170) & (data['v3_lon'] < -170)) |
                    ((data['v2_lon'] > 170) & (data['v3_lon'] < -170))
                )
            ]

            # Ensure required columns exist
            required_columns = ['v0_lat', 'v0_lon', 'v1_lat', 'v1_lon', 'v2_lat', 'v2_lon', 'v3_lat', 'v3_lon', 'Ratio SNR']
            if not all(col in data.columns for col in required_columns):
                print(f"Missing required columns in {path}. Required: {required_columns}")
                continue

            # Convert "Ratio SNR" to numeric, coercing errors to NaN
            data['Ratio SNR'] = pd.to_numeric(data['Ratio SNR'], errors='coerce')

            # Drop rows with NaN in "Ratio SNR"
            data = data.dropna(subset=['Ratio SNR'])

            # Iterate through each polygon in the CSV
            for _, row in data.iterrows():
                try:
                    # Define the corners of the polygon
                    corners = [
                        [row['v0_lat'], row['v0_lon']],
                        [row['v1_lat'], row['v1_lon']],
                        [row['v2_lat'], row['v2_lon']],
                        [row['v3_lat'], row['v3_lon']],
                    ]

                    # Create a Shapely Polygon object
                    polygon = Polygon(corners)

                    # Check if the target point lies within this polygon
                    if polygon.contains(target_point):
                        snr = row['Ratio SNR']

                        # Update the highest SNR polygon if applicable
                        if snr > highest_snr:
                            highest_snr = snr
                            highest_snr_element = element
                            highest_snr_polygon = corners

                        # Add the polygon to the map
                        tooltip_text = (
                            f"Detected Element: {element}<br>"
                            f"V0: ({row['v0_lat']}, {row['v0_lon']})<br>"
                            f"V1: ({row['v1_lat']}, {row['v1_lon']})<br>"
                            f"V2: ({row['v2_lat']}, {row['v2_lon']})<br>"
                            f"V3: ({row['v3_lat']}, {row['v3_lon']})<br>"
                            f"SNR: {snr}"
                        )
                        folium.Polygon(
                            locations=corners,
                            color="black",
                            fill=True,
                            fill_color=element_colors[element],
                            fill_opacity=0.3,
                            weight=1.5,
                            tooltip=tooltip_text
                        ).add_to(m)

                except Exception as e:
                    print(f"Error processing polygon in {path}: {e}")
                    continue

        except Exception as e:
            print(f"Error processing {element}: {e}")
            continue

    # Highlight the polygon with the highest SNR, if any
    if highest_snr_polygon:
        folium.Polygon(
            locations=highest_snr_polygon,
            color="red",
            fill=True,
            fill_color="red",
            fill_opacity=0.4,
            weight=3,
            tooltip=f"Highest SNR: {highest_snr} (Element: {highest_snr_element})"
        ).add_to(m)
        print(f"Element with highest SNR: {highest_snr_element}, SNR: {highest_snr}")
    else:
        print("No polygons found containing the specified coordinates.")
        return None

    return m
