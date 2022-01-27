import io
import folium

from production_code.ui.format_strings import format_float

from PyQt5.QtWebEngineWidgets import QWebEngineView


class Map(QWebEngineView):
    def __init__(self, current_location):
        super(Map, self).__init__()
        self._map = self._get_map_with_current_location(current_location)
        self._suitable_fishing_position_index = -1
        self._suitable_fishing_position_markers = []
        self._redraw_map()

    def show_suitable_fishing_locations(self, current_location, records):
        self._map = self._get_map_with_current_location(current_location)
        self._suitable_fishing_position_index = -1
        self._suitable_fishing_position_markers.clear()
        for record in records:
            marker = folium.Marker(
                [record.gps[0], record.gps[1]], popup=record.name + ", " + format_float(record.distance) + " km")
            self._suitable_fishing_position_markers.append(marker)
            self._suitable_fishing_position_markers[-1].add_to(self._map)
        self._redraw_map()

    def show_particular_fishing_location(self, location_index):
        if self._suitable_fishing_position_index != -1:
            default_icon = folium.Icon()
            self._suitable_fishing_position_markers[self._suitable_fishing_position_index].add_child(default_icon)
            self._suitable_fishing_position_markers[self._suitable_fishing_position_index].icon = default_icon

        self._map.location = self._suitable_fishing_position_markers[location_index].location
        particular_fishing_location_icon = folium.Icon(color="red", icon='info-sign')
        self._suitable_fishing_position_markers[location_index].add_child(particular_fishing_location_icon)
        self._suitable_fishing_position_markers[location_index].icon = particular_fishing_location_icon
        self._suitable_fishing_position_index = location_index
        self._redraw_map()

    @staticmethod
    def _get_map_with_current_location(current_position):
        temp_map = folium.Map(location=current_position, zoom_start=13)
        marker = folium.Marker(
            current_position, popup="Current position", icon=folium.Icon(color="black", icon="car", prefix="fa"))
        marker.add_to(temp_map)
        return temp_map

    def _redraw_map(self):
        data = io.BytesIO()
        self._map.save(data, close_file=False)
        self.setHtml(data.getvalue().decode())
