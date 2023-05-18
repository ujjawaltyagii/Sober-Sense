from flask import Flask, render_template, request
import os
import face_model
import voice_model

app = Flask(__name__)


@app.route('/')
def camera():
  return render_template('camera.html')


@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    photo = request.files['photo']
    if photo:
        filename = photo.filename
        # Set the destination directory where the photo will be saved
        destination = os.path.join(os.getcwd(), 'drunkImages', filename)
        photo.save(destination)

        val = face_model.check_intoxicated(photo.filename)
        with open('val.txt', 'w') as f:
         f.write(str(val))

    return render_template('voice_model.html')

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
      return render_template('intoxicated.html')
    else:
      return render_template('not_intoxicated.html')

app.run(host='0.0.0.0', port=18)
