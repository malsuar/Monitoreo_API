from fastapi import APIRouter
from config.db import conn
from schemas.monitoreo import monitoreoEntity, muchosmonitoreosEntity
from models.monitoreo import Monitoreo

monitoreo = APIRouter()
@monitoreo.get('/monitoreo') 

def find_all_monitoreo():
    print('Hola pichurria\n')
    return  muchosmonitoreosEntity(conn.monitoreo.dato.find()) # 'Llamado a la función find_all_monitoreo'

@monitoreo.get('/monitoreo/temperatura')
def find_monitoreo_temperatura():
    return monitoreoEntity(conn.monitoreo.dato.find({'temperatura':{'$gt':30}}))

@monitoreo.post('/monitoreo')
def save_monitoreo(mon: Monitoreo):
    new_mon=dict(mon)
    conn.monitoreo.dato.insert_one(new_mon)
    return 'Dato almacenado'


@monitoreo.put('./monitoreo')
def update_monitoreo():
       return 'actualización de datos monitoreo'

@monitoreo.delete('./monitoreo')
def delete_monitoreo():
     return 'Se borró esa mondá'
