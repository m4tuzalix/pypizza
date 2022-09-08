import requests

data = {
    "name": "Mateusz",
    "surname": "Wolowicz",
    "email": "adasjdjiasd@wp.pl",
    "phone": "111222333",
    "postal_code": "56-200",
    "address": "huj 11",
    "pizzas":[
        {
            "pizza":{
                "name": "salama",
                "price": 12.30,
                "ingredients": ["cheese", "onion", "salami"]
            },
            "size": "big",
            "amount": 3
        }
    ]
}
r = requests.post("http://127.0.0.1:8000/order/create_order/", data=data)
print(r.json())