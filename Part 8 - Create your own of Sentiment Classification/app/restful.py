from flask import Flask
from flask_restful import Resource, Api, reqparse
import pickle

app = Flask(__name__)
api = Api(app)

with open('model.pkl', 'rb') as file_model:
    model = pickle.load(file_model)


class SentimentAnalysis(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('kalimat',
                        type=str,
                        required=True,
                        help="Masukkan kalimat yang akan dicek")

    def get(self):
        kal = SentimentAnalysis.parser.parse_args()
        pred = model.predict([str(kal['kalimat'])])
        return {"sentimen": str(pred[0])}


api.add_resource(SentimentAnalysis, '/')

if __name__ == "__main__":
    app.debug = True
    app.run()
