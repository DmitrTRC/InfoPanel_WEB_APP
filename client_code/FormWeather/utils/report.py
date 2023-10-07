def format_weather_report(report_json) -> str:
    current_condition = report_json['current_condition'][0]
    location = report_json['nearest_area'][0]
    weather = report_json['weather'][0]

    report = f"--- Weather Report for {location['areaName'][0]['value']}, {location['country'][0]['value']} ---\n"
    report += f"Date: {weather['date']}\n"
    report += f"Temperature: {current_condition['temp_C']}°C ({current_condition['temp_F']}°F)\n"
    report += f"Feels Like: {current_condition['FeelsLikeC']}°C ({current_condition['FeelsLikeF']}°F)\n"
    report += f"Cloud Cover: {current_condition['cloudcover']}%\n"
    report += f"Humidity: {current_condition['humidity']}%\n"
    report += f"Weather Description: {current_condition['weatherDesc'][0]['value']}\n"
    report += f"Wind Direction: {current_condition['winddir16Point']} ({current_condition['winddirDegree']}°)\n"
    report += f"Wind Speed: {current_condition['windspeedKmph']} Kmph ({current_condition['windspeedMiles']} Miles)\n"
    report += f"Sunrise: {weather['astronomy'][0]['sunrise']}\n"
    report += f"Sunset: {weather['astronomy'][0]['sunset']}\n"
    report += f"UV Index: {weather['uvIndex']}\n"

    return report
