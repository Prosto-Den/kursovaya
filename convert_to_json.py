def material_to_json(title: str, type: str, amount: int, 
            fine: float, image_path: str, 
            id: int = None, **kwargs) -> dict:
    data = {
        "title": title,
        "type": type,
        "info": kwargs,
        "amount": amount,
        "fine": fine,
        "image_path": image_path
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