from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SWYNEX Python API is running",
        "status": "success"
    })


@app.route("/add", methods=["POST"])
def add_numbers():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        if "a" not in data or "b" not in data:
            return jsonify({
                "error": "Both 'a' and 'b' are required"
            }), 400

        if not isinstance(data["a"], (int, float)) or not isinstance(data["b"], (int, float)):
            return jsonify({
                "error": "a and b must be numbers"
            }), 400

        result = data["a"] + data["b"]

        return jsonify({
            "a": data["a"],
            "b": data["b"],
            "result": result
        }), 200

    except Exception:
        return jsonify({
            "error": "Invalid request"
        }), 400


if __name__ == "__main__":
    app.run(debug=True)