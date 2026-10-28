# 🎮 PC Game Deals

Hi there! 👋 Welcome to my **PC Game Deals** web application project!

I built this project to create a clean, responsive, and easy-to-use web app that helps gamers browse PC video game deals across different stores (like Steam, GOG, and Epic Games) and find the best discounts available in South African Rands (ZAR).

---

## 💡 Project Overview

The goal of this project was to build a full-stack web application using **Python** and **Flask**, focusing on clean code structure, separation of concerns, and an intuitive user interface. 

Rather than cramming everything into one file, I separated the routing logic (`app.py`) from the core business logic (`logic.py`), making the codebase easier to read, maintain, and test.

---

## ✨ Features

- 🔍 **Title Search:** Instant case-insensitive search by game name (e.g., searching "hol", "celeste", etc.).
- 🏷️ **Sale Filter:** A toggle checkbox to quickly filter out full-price titles and only view games currently discounted.
- 💰 **Cheapest Game Highlight:** Dynamically identifies and highlights the lowest-priced title among the currently displayed results.
- 📊 **Discount Percentage Calculator:** Automatically calculates the discount percentage (`((normal - sale) / normal) * 100`) and displays eye-catching badges for deals.
- 🛒 **Store Attribution:** Displays which storefront offers the deal (Steam, GOG, Epic Games).
- 📱 **Clean & Responsive UI:** Built with custom modern CSS grid cards, subtle shadows, and mobile-friendly styling.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask (lightweight and great for learning how request routing and templating work!)
- **Templating:** Jinja2 (used for dynamic HTML rendering, currency formatting, and passing helper functions)
- **Frontend:** HTML5 & Vanilla CSS3 (CSS Grid, Flexbox, custom badges, responsive design)
- **Data Source:** In-memory Python data structures (simulating a database of game catalog items)

---

## 📂 Project Structure

```text
PC-Game-Deals/
│
├── app.py              # Flask server setup, URL routing, and request handling
├── logic.py            # Core business logic, mock dataset, and helper functions
├── templates/
│   └── index.html      # Main page template rendered with Jinja2
├── static/
│   └── styles.css      # Custom styling, grid layout, and UI components
├── README.md           # Project documentation (you are here!)
└── .venv/              # Virtual environment (dependencies)
```

### Why I split `app.py` and `logic.py`:
As a junior dev, one of the biggest lessons I've learned is the importance of **Separation of Concerns**:
- `logic.py` contains the mock data and pure helper functions (`get_games_on_sale`, `calculate_discount`, `get_cheapest_game`, `get_current_price`, `search_games`). Because these functions don't touch Flask or the web directly, they could easily be unit tested with `pytest`!
- `app.py` stays slim and focuses purely on handling GET request query parameters (`search`, `sale_only`), coordinating which functions to run, and rendering the view.

---

## 🚀 Getting Started

Follow these steps to run the application locally on your machine:

### 1. Prerequisites
Make sure you have **Python 3.10+** installed on your system. You can check by running:
```bash
python3 --version
```

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd PC-Game-Deals
```

### 3. Set Up a Virtual Environment
It's always best practice to create a virtual environment to isolate project dependencies:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate it (macOS / Linux)
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

### 4. Install Dependencies
Install Flask:
```bash
pip install Flask
```

### 5. Run the Application
```bash
python3 app.py
```

### 6. View in Your Browser
Open your browser and navigate to:
```
http://127.0.0.1:5000
```
*(Debug mode is enabled by default for development).*

---

## 🧠 Key Learnings & Challenges

- **Query Parameters in Flask:** Learning how to read and combine multiple GET request parameters (`request.args.get("search")` and `request.args.get("sale_only")`) while preserving form states in the template.
- **Handling Edge Cases:**
  - Handling discounts gracefully when `salePrice >= normalPrice` to avoid negative or misleading discount percentages.
  - Ensuring searching is resilient by trimming whitespace and converting strings with `.lower()`.
  - Handling scenarios where a search returns no matching games (preventing `IndexError` when finding the cheapest game).
- **Jinja2 Filters & Helpers:** Formatting numbers cleanly to two decimal places (`R{{ "%.2f"|format(...) }}`) and conditionally rendering elements like sale badges only when applicable.

---

## 🔮 Future Improvements / Next Steps

Given more time, here are the top things I would love to add next:
- [ ] **Unit Tests:** Add a test suite with `pytest` or `unittest` to achieve high test coverage on `logic.py`.
- [ ] **Real Database:** Replace the in-memory dictionary list with SQLite or PostgreSQL using SQLAlchemy.
- [ ] **Live Deals API:** Integrate a public video game deal API (such as the [CheapShark API](https://apidocs.cheapshark.com/)) to fetch live prices and actual game box-art images!
- [ ] **Sorting Options:** Add a dropdown to sort results by title (A-Z), price (low to high), or discount percentage (highest savings first).
- [ ] **Requirements File:** Add a `requirements.txt` file for one-command installation.

---

## 👨‍💻 Author

Created with enthusiasm by a junior software engineer eager to learn, build, and receive constructive feedback. If you have any suggestions or feedback, feel free to reach out or submit a pull request!
