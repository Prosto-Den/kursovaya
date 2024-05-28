import ctypes

lib = ctypes.CDLL('./dll/kursovaya.dll')

# func for connection to database
connectToDB =  lib.startConnection

# func for disconnection from database
disconnectFromDB = lib.endConnection

# func for inserting into materials table
insertIntoMaterials = lib.insertIntoMaterials

# func for receiving data from materials table
selectAllMaterials = lib.selectAllMaterials

# func for updating material data
updateMaterial = lib.updateMaterial

# func for deleting material data
deleteMaterial = lib.deleteMaterial

# func for inserting into clients table
insertClient = lib.insertIntoClients

updateClient = lib.updateClient

deleteClient = lib.deleteClient

# func for receiving data from clients
selectAllClients = lib.selectAllClients