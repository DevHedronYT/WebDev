import requests

city_to_search_for = 'q=' + str(input())
url = ''.join(['https://api.openweathermap.org/data/2.5/weather?', str(city_to_search_for), '&appid=404b51a2b0365e05382a9c72d4848868', '&units=metric'])
page = requests.get(url)
main_data = page.json()

print(main_data['name'], ':', '\n', 'The Coordinates of the location are', '\n', 'Longitude is: ', main_data['coord']['lon'], '\n', 'Latitude is: ', main_data['coord']['lat'], '\n', 'The description of the sky is: ', main_data['weather'][0]['description'], '\n', 'The temperature is: ', main_data['main']['temp'], 'Celsius', '\n', 'The humidity is: ', main_data['main']['humidity'], '%', '\n', 'The wind speed is ', main_data['wind']['speed'], 'meter/sec', 'and the wind direction is ', main_data['wind']['deg'], 'degrees')
