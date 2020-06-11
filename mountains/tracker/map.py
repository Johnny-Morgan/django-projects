import os
import folium
from .models import Mountain

def generate_map():
    ''' function that generates map of mountains'''
    mountains = Mountain.objects.all()
    mountain_name = []
    mountain_height = []
    mountain_long = []
    mountain_lat = []
    date_climbed = []
    
    for mountain in mountains:
        mountain_name.append(mountain.name)
        mountain_height.append(mountain.height)
        mountain_long.append(mountain.longitude)
        mountain_lat.append(mountain.latitude)
        date_climbed.append(mountain.date_climbed)
        
    html = '''
    <b>Name:</b> %s<br>
    <b>Height:</b> %sm<br>
    <b>Climbed:</b> %s<br>
    '''

    map_of_mountains = folium.Map(location=[53.124, -5.650], zoom_start=9)

    fg_mountains = folium.FeatureGroup(name='Mountains')
    fg_hills = folium.FeatureGroup(name='Hills')

    for lat, lon, name, height, date in zip(mountain_lat,
                                            mountain_long,
                                            mountain_name,
                                            mountain_height,
                                            date_climbed):

        iframe = folium.IFrame(html=html % (name, str(height), date), width=200, height=100)

        if height > 500:  # mountains are 500m+
            fg_mountains.add_child(folium.CircleMarker(location=(lat, lon),
                                                    popup=folium.Popup(iframe),
                                                    radius=9,
                                                    fill=True,
                                                    fill_color='red',
                                                    color='black',
                                                    fill_opacity=0.8))
        else:
            fg_hills.add_child(folium.CircleMarker(location=(lat, lon),
                                                    popup=folium.Popup(iframe),
                                                    radius=9,
                                                    fill=True,
                                                    fill_color='green',
                                                    color='black',
                                                    fill_opacity=0.8))

    map_of_mountains.add_child(fg_mountains)
    map_of_mountains.add_child(fg_hills)
    map_of_mountains.add_child(folium.LayerControl())
    map_of_mountains.save('map.html')

    # open map in browser
    os.system('start Map.html')

