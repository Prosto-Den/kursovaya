import ctypes

lib = ctypes.CDLL('./dll/kursovaya.dll')

# func for connection to database
connectToDB =  lib.startConnection

# func for inserting into materials table
insertIntoMaterials = lib.insertIntoMaterials

# func for receiving data from materials table
selectAllMaterials = lib.selectAllMaterials

# func for disconnection from database
disconnectFromDB = lib.endConnection