from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils import predict_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Predict Route
@app.route('/predict', methods=['POST'])
def upload_and_predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    label, confidence = predict_image(filepath)
    return render_template('index.html', prediction=label, confidence=confidence, image_url=filepath)

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)
