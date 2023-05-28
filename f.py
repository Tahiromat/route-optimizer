import folium

def plot_nodes_on_map(locations):
    """Plot nodes on a map."""
    # Create a map object centered around the first node
    map_obj = folium.Map(location=locations[0], zoom_start=12)

    # Add markers for each node
    for loc in locations:
        folium.Marker(loc).add_to(map_obj)

    return map_obj


def plot_ways_on_map(locations, ways):
    """Plot ways between nodes on a map."""
    map_obj = plot_nodes_on_map(locations)

    # Add polylines for each way
    for way in ways:
        folium.PolyLine(locations[way], color='blue', weight=2.5, opacity=1).add_to(map_obj)

    return map_obj



def main():
    """Entry point of the program."""
    # Define the locations (latitude, longitude) and ways (indices of locations)
    locations = [
        (37.7749, -122.4194),  # San Francisco
        (34.0522, -118.2437),  # Los Angeles
        (38.5816, -121.4944),  # Sacramento
        (36.7372, -119.7871),  # Fresno
        (39.5296, -119.8138),  # Reno
    ]
    ways = [
        [0, 1],  # Way from San Francisco to Los Angeles
        [1, 2],  # Way from Los Angeles to Sacramento
        [2, 3],  # Way from Sacramento to Fresno
        [3, 4],  # Way from Fresno to Reno
        [4, 0],  # Way from Reno to San Francisco
    ]

    # Plot nodes on a map
    nodes_map = plot_nodes_on_map(locations)
    nodes_map.save('nodes_map.html')

    # Plot ways between nodes on a map
    ways_map = plot_ways_on_map(locations, ways)
    ways_map.save('ways_map.html')


if __name__ == '__main__':
    main()
