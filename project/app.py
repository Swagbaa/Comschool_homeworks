from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

NAV_LINKS = [
    {"name": "მთავარი", "endpoint": "home"},
    {"name": "ჩვენს შესახებ", "endpoint": "about"},
    {"name": "კონტაქტი", "endpoint": "contact"},
]

CURRENT_YEAR = datetime.now().year


@app.context_processor
def inject_globals():
    return {
        "nav_links": NAV_LINKS,
        "current_year": CURRENT_YEAR,
        "site_name": "MySite",
    }


@app.route("/")
def home():
    features = [
        "სწრაფი და მარტივი გვერდები",
        "Jinja შაბლონების გამოყენება",
        "სრულად რესპონსიული დიზაინი",
        "მარტივად გასაფართოებელი სტრუქტურა",
    ]
    return render_template("home.html", active_page="home", features=features)


@app.route("/about")
def about():
    team = [
        {"name": "john doe", "role": "Backend დეველოპერი"},
        {"name": "jane doe", "role": "Frontend დეველოპერი"},
        {"name": "Saba", "role": "UI/UX დიზაინერი"},
    ]
    return render_template("about.html", active_page="about", team=team)


@app.route("/contact")
def contact():
    contact_info_available = True
    email = "info@mysite.ge"
    phone = "+995 555 123 456"
    return render_template(
        "contact.html",
        active_page="contact",
        contact_info_available=contact_info_available,
        email=email,
        phone=phone,
    )


if __name__ == "__main__":
    app.run(debug=True)
