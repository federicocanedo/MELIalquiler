# 1. URLs de la API de MercadoLibre
API_BASE_URL = "https://api.mercadolibre.com"
SEARCH_URL = f"{API_BASE_URL}/sites/MLU/search"
ITEM_URL = f"{API_BASE_URL}/items/"

# 2. Parámetros de búsqueda por defecto
DEFAULT_CATEGORY = "MLU1459"  # Categoría de inmuebles en Uruguay (apartamentos)
DEFAULT_STATE = "TUxVUE1PTjQxN2E4"  # ID del estado (Montevideo)
DEFAULT_PRICE_RANGE = "13000UYU-18000UYU"  # Rango de precios por defecto
DEFAULT_CURRENCY = "UYU"
DEFAULT_PROPERTY_TYPE = "242062,242060"  # Tipos de propiedades: apartamento, casa
DEFAULT_AREA = "[20-*)"  # Área mínima de 20 m²

# 3. Ciudades permitidas
WANTED_CITIES = [
    "TUxVQ0xBWjk5YTE5",
    "TUxVQ1VOSTVkOGFk",
    "TUxVQ0NFTjVjMTM",
    "TUxVQ0NPUjZmZjNm",
    "TUxVQ1BPQzM5ZGRi",
    "TUxVQ01BTDE0YmY1",
    "TUxVQ0JVQzNlMDdl",
    "TUxVQ0NBUmRhYWU0",
    "TUxVQ1BBUjVkNGE4",
    "TUxVQ1BBUmU3Y2Nj",
    "TUxVQ1BPQzIwNDU",
    "TUxVQ1BVRTI0NDA",
    "TUxVQ1BVTjJmMjkx",
    "TUxVQ1BVTjYxODI",
    "TUxVQ1RSRTg3OGM3",
    "TUxVQ1ZJTDE2MDU",
    "TUxVQ1ZJTDk1MTY"
]

# 4. Vendedores bloqueados
BLOCKED_SELLERS = [
    579162526,
    126030388,
]

# 5. Parámetros de paginación y limitación de resultados
DEFAULT_LIMIT = 50  # Cantidad máxima de resultados por solicitud
DEFAULT_OFFSET = 0  # Desplazamiento inicial de los resultados

# 6. Tiempos de espera entre solicitudes
REQUEST_DELAY = 2  # Segundos de espera entre solicitudes a la API

# 7. Parámetros relacionados a fechas
SEARCH_SINCE = "today"  # Publicaciones desde hoy

# 8. Nivel de logs
LOG_LEVEL = "INFO"  # Nivel de logueo de la aplicación (DEBUG, INFO, WARNING, ERROR)
