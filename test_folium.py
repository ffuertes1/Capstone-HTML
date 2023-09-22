import folium

# Create a simple map
m = folium.Map(location=[18.2766908, -65.9909139], zoom_start=9.9)

# Add a marker to a specific location
folium.Marker(location=[18.214400, -65.735646], tooltip='Supermercado Econo Naguabo').add_to(m)

# Display the map and save it to an HTML file
m.save('PRmap.html')