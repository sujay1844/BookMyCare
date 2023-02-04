from book import book_appointment
from db_helpers import get_all_doctors
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()
    book_appointment(data)
    return "Success"

@app.route("/", methods=["GET"])
def get_doctors():
    print(get_all_doctors())
    return jsonify({"data": get_all_doctors() })

if __name__ == "__main__":
    app.run()
