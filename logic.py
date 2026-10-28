games = [
    {
    "id": 1,
    "title": "Hollow Knight",
    "normalPrice": 14.99,
    "salePrice": 7.49,
    "store": "Steam"
  },
  {
    "id": 2,
    "title": "Stardew Valley",
    "normalPrice": 13.99,
    "salePrice": 13.99,
    "store": "GOG"
  },
  {
    "id": 3,
    "title": "Celeste",
    "normalPrice": 19.99,
    "salePrice": 4.99,
    "store": "Steam"
  },
  {
    "id": 4,
    "title": "Hades",
    "normalPrice": 24.99,
    "salePrice": 12.49,
    "store": "Epic Games"
  },
  {
    "id": 5,
    "title": "Portal 2",
    "normalPrice": 9.99,
    "salePrice": 0.99,
    "store": "Steam"
  },
  {
    "id": 6,
    "title": "Terraria",
    "normalPrice": 9.99,
    "salePrice": 9.99,
    "store": "GOG"
  },
  {
    "id": 7,
    "title": "Disco Elysium",
    "normalPrice": 39.99,
    "salePrice": 9.99,
    "store": "GOG"
  },
  {
    "id": 8,
    "title": "Cuphead",
    "normalPrice": 19.99,
    "salePrice": 14.99,
    "store": "Steam"
  }
]

def get_games_on_sale(games):
    sale_games = []

    for game in games:
        if game["salePrice"] < game["normalPrice"]:
            sale_games.append(game)

    return sale_games

def calculate_discount(game):
    normal_price = game["normalPrice"]
    sale_price = game["salePrice"]

    if sale_price >= normal_price:
        return 0

    discount = ((normal_price - sale_price) / normal_price) * 100

    return round(discount)


def get_cheapest_game(games):
    if not games:
        return None

    cheapest_game = games[0]

    for game in games:
        if game["salePrice"] < game["normalPrice"]:
            current_price = game["salePrice"]
        else:
            current_price = game["normalPrice"]

        if current_price < get_current_price(cheapest_game):
            cheapest_game = game

    return cheapest_game


def get_current_price(game):
    if game["salePrice"] < game["normalPrice"]:
        return game["salePrice"]

    return game["normalPrice"]


def search_games(games, search_word):
    matching_games = []

    search_word = search_word.lower()

    for game in games:
        title = game["title"].lower()

        if search_word in title:
            matching_games.append(game)

    return matching_games