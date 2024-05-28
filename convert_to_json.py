def material_to_json(title: str, type: str, amount: int, 
            fine: float, image_path: str, room: int = 0, rack: int = 0, shelf: int = 0,
            id: int = None, **kwargs) -> dict:
    data = {
        "title": title,
        "type": type,
        "info": kwargs,
        "amount": amount,
        "fine": fine,
        "image_path": image_path,
        "room_id": room,
        "rack_id": rack,
        "shelf_id": shelf
    }

    if id is not None:
        data['id'] = id

    return data

def client_to_json(name: str, birthday: str, passport: str) -> dict:
    data = {
        "name": name,
        "birthday": birthday,
        "passport": passport
    }

    return data