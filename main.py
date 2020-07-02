from flask import Flask, render_template, url_for, request, jsonify
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/character/search')
def character_search():
    phrase = request.args.get('phrase', None)
    if phrase:
        characters = queries.search_characters(phrase)
        return jsonify(characters)

    return render_template('character-search.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
