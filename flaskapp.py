import os
import uuid
from io import BytesIO
from Histogram import get_histogram_by_nlp_data
from flask import Flask, render_template, request, send_file
from TextTransfromer import get_nlp_data_from_text, make_nlp_img_from_text
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<uid>', methods=['GET'])
def get_file(uid):
    filepath = f'{current_path}/uploads/{uid}.svg'
    if os.path.isfile(filepath):
        file = open(filepath, 'rb')
        data = file.read()
        os.remove(filepath)
        return send_file(BytesIO(data), download_name=f'{uid}.svg', as_attachment=True)
    else:
        return 'такого файлу немає'

@app.route('/post', methods=['POST'])
def post():
    text_data = request.form.get('text', None)
    file = request.files.get('file', None)
    if not text_data and not file:
        return "ви нічого не ввели"
    if file:
        text_data = file.stream.read().decode('utf-8')

    nlp_data = get_nlp_data_from_text(text_data)
    svg = make_nlp_img_from_text(text_data)
    new_hex = uuid.uuid4().hex
    file = open(f'{current_path}/uploads/{new_hex}.svg', 'w')
    file.write(svg)
    histogram = get_histogram_by_nlp_data(nlp_data)
    return render_template('result.html', data_len=len(list(nlp_data.keys())), keys=list(nlp_data.keys()),
                               nlp_data=nlp_data, uid = new_hex, histogram=histogram)
        # return render_template('result.html', nlp_data=nlp_data, uid = new_hex)


if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5500)))