from flask import Flask, render_template, request, make_response
from __utils import get_phrase
from .__server_utils import save_video
from models.face.check_inebriated import check_inebriated
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/taketest')
def taketest():
    return render_template('test.html')


@app.route('/drunk')
def drunk():
    return render_template('drunk.html')


@app.route('/sober')
def sober():
    return render_template('sober.html')


@app.route('/submit_image', methods=['GET'])
def submit_image_get():
    return render_template('submit_image.html')


@app.route('/submit', methods=['GET'])
def submit():
    phrase = get_phrase()
    return render_template('submit.html', phrase=phrase)


@app.route('/submit_image', methods=['POST'])
def submit_image():
    image = request.files['image']
    if image:
        filename = image.filename
        os.makedirs('userImages', exist_ok=True)
        dest = os.path.join(os.getcwd(), 'userImages', filename)
        image.save(dest)
    res = make_response('submit')
    res.headers['Content-Type'] = 'text/plain'
    return res


@app.route('/submit', methods=['POST'])
def submit_post():

    video = request.files['video']
    # phrase = request.form.get('phrase')
    save_video(video)

    res = make_response('drunk')
    # res = make_response('sober')

    res.headers['Content-Type'] = 'text/plain'
    return res

    # predicted = check_inebriated(video_location)
    # print(predicted)


def start_server():
    debug = False
    app.run(host='0.0.0.0', port=8080, debug=debug)
