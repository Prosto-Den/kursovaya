def to_json(title: str, type: str, amount: int, price: float, fine: float, image_path: str, **kwargs) -> dict:
    data = {
        "title": title,
        "type": type,
        "info": kwargs,
        "amount": amount,
        "price": price,
        "fine": fine,
        "image_path": image_path
    }

    return data