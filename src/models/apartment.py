# src/models/apartment.py

import math

class Apartment:
    def __init__(self, id, title, city, price, url, attributes, latitude = None, longitude=None, created_at=None):
        self.id = id
        self.title = title
        self.city = city
        self.price = price
        self.url = url
        self.attributes = attributes
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = created_at

    def get_maintenance_fee(self):
        fee = self.find_attribute("MAINTENANCE_FEE")
        return fee["values"][0]["struct"]["number"] if fee else None

    def get_area(self):
        area = self.find_attribute("COVERED_AREA")
        return area.get("value_name", " ") if area else " "

    def get_rooms(self):
        rooms = self.find_attribute("ROOMS")
        return rooms.get("value_name", " ") if rooms else " "

    def get_bedrooms(self):
        bedrooms = self.find_attribute("BEDROOMS")
        return bedrooms.get("value_name", " ") if bedrooms else " "

    def find_attribute(self, attribute_id):
        for attribute in self.attributes:
            if attribute.get("id") == attribute_id:
                return attribute
        return None

    # Método para calcular la distancia entre dos apartamentos utilizando la fórmula de Haversine
    def distance_to(self, other_apartment):
        R = 6371e3  # Radio de la Tierra en metros
        phi1 = math.radians(self.latitude)
        phi2 = math.radians(other_apartment.latitude)
        delta_phi = math.radians(other_apartment.latitude - self.latitude)
        delta_lambda = math.radians(other_apartment.longitude - self.longitude)

        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c  # Distancia en metros
        return distance

    def __str__(self):
        return f"{self.title} - {self.city}\nPrecio: ${self.price}\nURL: {self.url}"
