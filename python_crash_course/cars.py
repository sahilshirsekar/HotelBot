def car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name
    return car_info

car_profile = car('subaru', 'outback', color = 'blue', tow_package=True)
print(car_profile)
    