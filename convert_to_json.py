from json.encoder import encode_basestring

def to_json(title: str, type: str, amount: int, price: float, fine: float, **kwargs) -> dict:
    data = {
        "title": title,
        "type": type,
        "info": None,
        "amount": amount,
        "price": price,
        "fine": fine
    }

    if type == 'Книга':
        info = {
            "authors": kwargs["authors"],
            "publisher": kwargs["publisher"],
            "publish_year": kwargs["publish_year"]
        }

    elif type == 'Газета':
        info = {
            "number": kwargs["number"],
            "date": kwargs["date"]
        }

    elif type == 'Журнал':
        info = {
            "number": kwargs["number"],
            "date": kwargs["date"],
            "publisher": kwargs["publisher"]
        }

    data['info'] = info

    return data