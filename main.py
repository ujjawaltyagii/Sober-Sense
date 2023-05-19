from flask import Flask, render_template, request
import os
import face_model
import voice_model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  print("here")
  return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
  return render_template('test.html')

@app.route('/upload_image', methods=['GET'])
def upload_image_get():
   return render_template('submit_image.html')

@app.route('/upload_video', methods=['GET'])
def upload_video_get():
   return render_template('submit_video.html')


@app.route('/upload_image', methods=['POST'])
def upload_image():
    print("recieved")
    photo = request.files['image']
    return render_template('upload_video.html')
    if photo:
        filename = photo.filename
        # Set the destination directory where the photo will be saved
        os.makedirs('drunkImages', exist_ok=True)
        destination = os.path.join(os.getcwd(), 'drunkImages', filename)
        photo.save(destination)

        val = face_model.check_intoxicated(photo.filename)
        with open('val.txt', 'w') as f:
         f.write(str(val))


# @app.route('/upload_video', methods=['POST'])
# def upload_video():
#     video = request.files['video']
#     if video:
#         filename = video.filename
#         # Set the destination directory where the video will be saved
#         destination = os.path.join(os.getcwd(), 'uploads', filename)
#         video.save(destination)
@app.route('/upload_video', methods=['POST'])
def upload_video():
    video = request.files['video']
    print(video)
    video_path = os.path.join(os.getcwd(), video.filename)  # Get the absolute file path

    video.save(video_path)

    phrase = 'energetic happiness'

    with open('phrase.txt', 'w') as f:
         f.write(phrase)

    voice_model.get_wav_file(video.filename)

    val2 = voice_model.check_slurring('test.wav', phrase)

    r = open('val.txt', 'r')
    val = r.read()
    val = float(val)
    res = val+val2

    print(res/2)

    if res/2 >= 0.6:
      return render_template('drunk.html')
    else:
      return render_template('sober.html')

app.run(host='0.0.0.0', port=18)
