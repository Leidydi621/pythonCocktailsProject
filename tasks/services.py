import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    
def get_username(params={}):
    response = generate_request('https://www.thecocktaildb.com/api/json/v1/1/random.php', params)
    if response:
       user = response.get('drinks')[0]
       data = {
           'id': user.get('idDrink'),
           'name': user.get('strDrink'),
           'img': user.get('strDrinkThumb'),
           'categoryName': user.get('strCategory'),
           'glass': user.get('strGlass'),
           'instructions': user.get('strInstructions'),
           'ingredients': [
               user.get('strIngredient1'),
               user.get('strIngredient2'),
               user.get('strIngredient3'), 
               user.get('strIngredient4'), 
               user.get('strIngredient5'),
               user.get('strIngredient6')
               ]
       }
       
       return data

    return ''