from src.services.mercadolibre_service import MercadoLibreService

class RealEstateApp:
    def __init__(self):
        self.service = MercadoLibreService()

    def run(self):
        print("Buscando apartamentos...")
        apartments = self.service.search_apartments()
        self.service.process_apartments(apartments)
