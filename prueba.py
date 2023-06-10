import requests 

dato = {'lugar':'Medellin','autor':'Mario','temperatura':45, 'humedad':70}

#res = requests.post('http://localhost:8000/monitoreo', json=dato)
res = requests.post('https://diplomadoiot-mariosucerquia.b4a.run/monitoreo', json=dato)
print(res.text)