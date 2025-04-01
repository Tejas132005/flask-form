from flask import Flask, render_template, request
from markupsafe import escape
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')

        return render_template('form_result.html',
                               username=escape(username),
                               city=escape(city),
                               state=escape(state),
                               country=escape(country))

    return render_template('form.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)