import datetime
from . import models

def update_sale_data(sale:models.Sale, data:dict) -> None:
    if 'name' in data.keys():
        sale.name = data['name']
    if 'value' in data.keys():
        sale.value = data['value']
    if 'preview' in data.keys():
        sale.preview = data['preview']
    if 'start_date' in data.keys():
        sale.start_date = datetime.datetime.strptime(data['start_date'], '%H:%M:%S %d-%m-%Y')
    if 'end_date' in data.keys():
        sale.end_date = datetime.datetime.strptime(data['end_date'], '%H:%M:%S %d-%m-%Y')
    sale.save()