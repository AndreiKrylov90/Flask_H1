from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    news = [{'title': 'The biggest spider was born in Sidney',
             'context': 'This spider was born last month. Two hundred people decided to relocate to another city',
             'date': '2023-11-12'},
            {'title': 'First koala was born in Zoo',
             'context': 'Scientists of Wuhan helped this lazy animal to born a child',
             'date': '2019-10-2'}]
    return render_template('news.html', news = news)


if __name__ == "__main__":
    app.run(debug=True)

