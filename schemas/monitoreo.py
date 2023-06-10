def monitoreoEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'lugar':str(item['lugar']),
        'autor':  str(item['autor']),
        'temperatura':item['temperatura'],
        'humedad':item['humedad'],
        'createdAT':item['createdAT'],
        'updatedAT':item['updatedAT'],
    }


def muchosmonitoreosEntity(entity) -> list:
    return [monitoreoEntity(item) for item in entity]