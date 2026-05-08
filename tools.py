def get_weather(city):
    weather_data = {
        "北京": "晴天 25°C",
        "上海": "多云 28°C",
        "三亚": "暴雨 30°C"
    }

    return weather_data.get(city, "暂无天气数据")