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

# func for deleting the client
deleteClient = lib.deleteClient

# func for receiving data from clients
selectAllClients = lib.selectAllClients

# func for inserting data in material_client table
insertBorrowBook = lib.insertBorrowBook

# func for receiving all data from material_client table
selectAllClientMaterial = lib.selectAllClientMaterial

# func for deleting data from ckient_material
deleteBorrow = lib.deleteBorrow

# func for receiving all data from debtors
selectAllDebtors = lib.selectAllDebtors

insertIntoDebtors = lib.insertIntoDebtors

