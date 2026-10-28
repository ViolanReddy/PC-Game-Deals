from flask import Flask, render_template, request
from logic import (
    games,
    get_games_on_sale,
    calculate_discount,
    get_cheapest_game,
    get_current_price,
    search_games,

)

app = Flask(__name__)

@app.route("/")
def home():
    
    search_word = request.args.get("search", "").strip()
    sale_only = request.args.get("sale_only") == "true"

    displayed_games = games

    if search_word:
        displayed_games = search_games(displayed_games, search_word)

    if sale_only:
        displayed_games = get_games_on_sale(displayed_games)

    cheapest_game = get_cheapest_game(displayed_games)

    
    return render_template(
        "index.html",
        games=displayed_games,
        search_word=search_word,
        sale_only=sale_only,
        get_current_price=get_current_price,
        calculate_discount=calculate_discount
    )

if __name__ == "__main__":
    app.run(debug=True)