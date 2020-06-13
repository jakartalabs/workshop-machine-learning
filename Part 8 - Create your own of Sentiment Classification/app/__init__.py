from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as file_model:
    model = pickle.load(file_model)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        kalimat = str(request.form['kalimat'])
        pred = model.predict([kalimat])
        if pred[0] == -1:
            sentiment = 'negatif'
        elif pred[0] == 0:
            sentiment = 'netral'
        elif pred[0] == 1:
            sentiment = 'positif'
        else:
            sentiment = 'undefined'
        return render_template("index.html", hasil_sentimen=sentiment)
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
