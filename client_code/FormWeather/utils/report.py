def format_weather_report(report_json) -> str:
    current_condition = report_json['current_condition'][0]
    location = report_json['nearest_area'][0]
    weather = report_json['weather'][0]

    weather_emoji = {
        'rain': '☔',
        'sunny': '☀️',
        'cloudy': '☁️',
        'snow': '❄️',
        'drizzle': '🌧️',
        'default': '🌦️'
    }
    description = current_condition['weatherDesc'][0]['value'].lower()
    emoji = weather_emoji.get(description, weather_emoji['default'])

    report = f"<b style='color: blue;'>--- Weather Report for {location['areaName'][0]['value']}, {location['country'][0]['value']} ---</b><br>"
    report += f"<b>Date:</b> {weather['date']}<br>"
    report += f"<b>Temperature:</b> <span style='color: red;'>{current_condition['temp_C']}°C ({current_condition['temp_F']}°F)</span><br>"
    report += f"<b>Feels Like:</b> <span style='color: red;'>{current_condition['FeelsLikeC']}°C ({current_condition['FeelsLikeF']}°F)</span><br>"
    report += f"<b>Cloud Cover:</b> {current_condition['cloudcover']}%<br>"
    report += f"<b>Humidity:</b> {current_condition['humidity']}%<br>"
    report += f"<b>Weather Description:</b> {emoji} {current_condition['weatherDesc'][0]['value']}<br>"
    report += f"<b>Wind Direction:</b> {current_condition['winddir16Point']} ({current_condition['winddirDegree']}°)<br>"
    report += f"<b>Wind Speed:</b> {current_condition['windspeedKmph']} Kmph ({current_condition['windspeedMiles']} Miles)<br>"
    report += f"<b>Sunrise:</b> {weather['astronomy'][0]['sunrise']}<br>"
    report += f"<b>Sunset:</b> {weather['astronomy'][0]['sunset']}<br>"
    report += f"<b>UV Index:</b> {weather['uvIndex']}<br>"

    return report
