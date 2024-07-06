from geopy.geocoders import Nominatim

def obter_coordenadas(endereco):
    localizador = Nominatim(user_agent="geoapiTeste")
    localizacao = localizador.geocode(endereco)
    if localizacao:
        return localizacao.latitude, localizacao.longitude
    return None, None