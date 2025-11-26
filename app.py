from flask import Flask, render_template

# On dit à Flask où trouver les fichiers HTML (le dossier qu'on vient de créer)
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
