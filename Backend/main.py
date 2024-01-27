from flask import Flask, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model (only once at startup)
model = None
model_path = 'Backend/best_model.h5'

if os.path.exists(model_path):
    from keras.models import load_model
    model = load_model(model_path)
else:
    print(f"Model file '{model_path}' not found!")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected image'})

    try:
        # Convert the FileStorage object to a BytesIO object
        image_data = io.BytesIO(image.read())

        # Load the uploaded image
        img = load_img(image_data, target_size=(128, 128))
        img_array = img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make a prediction using the cached model
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        confidence = np.max(prediction, axis=1)  # Get the maximum probability score

        # Assuming a categorical model, the prediction will be an array with probabilities for each class.
        # You can convert this to a class label if needed.
        return jsonify({
            'predicted_class': int(predicted_class[0]),
            'confidence': float(confidence[0])  # Convert numpy float to Python native float for JSON serialization
        })

    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)