import requests

def get_weather_desc_and_temp():
    api_key = "7eac94a4e39bcfe4a8610d1fe9acba07"
    city = "Orlando"
    url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=imperial".format(city_name = city, API = api_key)

    request = requests.get(url)
    json = request.json()


    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description,
        "temp_min": temp_min,
        "temp_max": temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    print("todays forecast is", weather_dict.get("description"))
    print("the minimum temp is", weather_dict.get("temp_min"), "degrees.")
    print("the maximum temp is", weather_dict.get("temp_max"), "degrees.")

main()
