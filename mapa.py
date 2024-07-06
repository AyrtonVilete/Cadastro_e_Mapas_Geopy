import folium

min_lon, max_lon = -45, -42
min_lat, max_lat = -23, -20

m = folium.Map(
    max_bounds=True,     # Limites máximo ativado
    location=[-22.75684850991244, -43.45169152484088],  # Localização do usuário
    zoom_start=15,
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
)

# Número de vagas

v = 14
x = 12
y = 9
z = 18



# Adição das coordenadas dos Estacionamentos

## As coordenadas geográficas foram obtidas no Google Maps selecionando alguns estacionamentos em Nova Iguaçu.

## Os nomes apresentados pelos estacionamentos no Google Maps foram ocultados neste código, sendo que cada um deles recebeu
## o nome "Estacionamento" acrescido de uma letra maiúscula. ex: "Estacionamento A"

folium.Marker([-22.75442521336245, -43.44922357077658], tooltip=f'Estacionameno A. Vagas:{v}').add_to(m)
folium.Marker([-22.75711765995792, -43.44748362773216], tooltip=f'Estacionamento B. Vagas: {x}').add_to(m)
folium.Marker([-22.75724221667799, -43.45252604690573], tooltip=f'Estacionamento C. Vagas: {y} ').add_to(m)
folium.Marker([-22.75780191142348, -43.451811395930385], tooltip=f'Estacionamento D. Vagas: {z}').add_to(m)

m