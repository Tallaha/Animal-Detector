from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
import base64
import io
import os
import predict
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']

        filename = secure_filename(img.filename)

        pathUpload = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        img.save(pathUpload)

        prediction = predict.predict(pathUpload)

        im = Image.open(pathUpload)
        data = io.BytesIO()
        im.save(data, "JPEG")
        #Then encode the saved image file.
        encoded_img_data = base64.b64encode(data.getvalue())
        return render_template('prediction.html', prediction=prediction, img_data=encoded_img_data.decode('utf-8'))

    return render_template('index.html')

app.run()
