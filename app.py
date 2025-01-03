from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Set environment variables (optional, depending on your needs)
# os.putenv("LANG", "en_US.UTF-8")
# os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)  # No need to specify template_folder explicitly if it's 'templates'
CORS(app)  # Enable CORS for the entire app

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")  # Corrected path

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    try:
        # Import and run the training function directly rather than using os.system
        import main  # Assuming main.py has a function to handle the training
        main.train()  # Replace with the actual function call to train your model
        return "Training done successfully!"
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    try:
        image = request.json["image"]
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except KeyError:
        return jsonify({"error": "No image data found in request"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    clApp = ClientApp()  # Initialize ClientApp
    app.run(host="0.0.0.0", port=8080)






