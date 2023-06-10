import requests 

dato = {'lugar':'Medellin', 'temperatura':45, 'humedad':70}

res = requests.post('http://localhost:8000/monitoreo', json=dato)
print(res.text)