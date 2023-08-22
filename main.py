import requests
import random

if __name__ == '__main__':
    number = random.randrange(1, 50)
    numtype = 'trivia'
    url = 'http://numbersapi.com'
    req = requests.get(f"{url}/{number}/{numtype}?json")
    rep_text = req.text
    rep_json =req.json()
    if req.status_code == 200:
        print(rep_json)
    else:
        print("Erreur pour l'entier " + str(number) + " avec le code " + str(req.status_code))



