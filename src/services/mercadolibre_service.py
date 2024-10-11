import requests
from time import sleep
from src.models.apartment import Apartment
import config.settings as settings

class MercadoLibreService:
    SEARCH_URL = settings.SEARCH_URL
    ITEM_URL = settings.ITEM_URL
    WANTED_CITIES = settings.WANTED_CITIES
    BLOCKED_SELLERS = settings.BLOCKED_SELLERS

    def __init__(self, category=settings.DEFAULT_CATEGORY, price_range=settings.DEFAULT_PRICE_RANGE, state=settings.DEFAULT_STATE):
        self.params = {
            "category": category,
            "state": state,
            "price": price_range,
            "total_area": settings.DEFAULT_AREA,
            "since": settings.SEARCH_SINCE,
            "property_type": settings.DEFAULT_PROPERTY_TYPE,
            "currency_id": settings.DEFAULT_CURRENCY,
            "city": ",".join(self.WANTED_CITIES),
            "limit": settings.DEFAULT_LIMIT,
            "offset": settings.DEFAULT_OFFSET
        }
        self.filtered_apartments = []

    def search_apartments(self):
        apartments = []
        total_pages = 5  # Máximo de 5 páginas
        current_page = 0
        offset = 0

        while current_page < total_pages:
            self.params["offset"] = offset  # Actualizamos el offset en los parámetros
            response = requests.get(self.SEARCH_URL, params=self.params)

            if response.status_code == 200:
                data = response.json()
                # Agregamos los resultados de esta página a la lista total
                for item in data["results"]:
                    apartment = self.create_apartment(item)
                    if self.filter_apartment(apartment):
                        apartments.append(apartment)
                
                # Verificamos el número total de resultados y calculamos cuántas páginas hay en total
                total_results = data["paging"]["total"]
                total_pages = min((total_results // settings.DEFAULT_LIMIT) + 1, 5)

                print(f"Página {current_page + 1}/{total_pages}, Total resultados: {total_results}")

                # Si ya no hay más resultados, terminamos el bucle
                if len(data["results"]) == 0:
                    break

                # Avanzamos a la siguiente página
                current_page += 1
                offset += settings.DEFAULT_LIMIT  # Incrementamos el offset en 50 para la siguiente página
            else:
                print(f"Error en la solicitud: {response.status_code}")
                break
        
        return apartments

    def create_apartment(self, item):
        return Apartment(
            id=item["id"],
            title=item["title"],
            city=item["location"]["city"]["id"],
            price=item["price"],
            url=item["permalink"],
            attributes=item.get("attributes", []),
            latitude=item["location"]["latitude"],
            longitude=item["location"]["longitude"]
        )

    def filter_apartment(self, apartment):
        # Filtro por ciudades
        if apartment.city not in self.WANTED_CITIES:
            return False

        # Filtro por distancia, precio y área
        for filtered_apartment in self.filtered_apartments:
            if (apartment.price == filtered_apartment.price and
                apartment.get_area() == filtered_apartment.get_area() and
                apartment.distance_to(filtered_apartment) <= 100):
                # Si hay un apartamento con el mismo precio, misma área y está a menos de 100 metros, lo descartamos
                return False

        # Si pasa el filtro, lo agregamos a la lista de apartamentos filtrados
        self.filtered_apartments.append(apartment)
        return True

    def get_apartment_details(self, apartment_id):
        response = requests.get(self.ITEM_URL + apartment_id)
        if response.status_code == 200:
            return response.json()
        return None

    def process_apartments(self, apartments):
        for apartment in apartments:
            details = self.get_apartment_details(apartment.id)
            if details:
                apartment_data = Apartment(
                    id=details["id"],
                    title=details["title"],
                    city=details["location"]["city"]["name"],
                    price=details["price"],
                    url=details["permalink"],
                    attributes=details.get("attributes", []),
                    latitude=apartment.latitude,
                    longitude=apartment.longitude
                )
                maintenance_fee = apartment_data.get_maintenance_fee()
                if maintenance_fee and (maintenance_fee + apartment_data.price) > 18000:
                    sleep(settings.REQUEST_DELAY)
                    continue
                self.display_apartment(apartment_data)
            sleep(settings.REQUEST_DELAY)

    def display_apartment(self, apartment):
        print("-" * 60)
        print(apartment)
        print(f"Gastos comunes: ${apartment.get_maintenance_fee()}")
        print(f"Área: {apartment.get_area()} - Cuartos: {apartment.get_rooms()} - Dormitorios: {apartment.get_bedrooms()}")
