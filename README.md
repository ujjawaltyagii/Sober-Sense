## Sober-Sense

### What does it do?
Sober-Sense is a solution that combines both facial recognition and audio recognition technology to determine an individual's level of sobriety. This allows us to check if they are fit to drive a car. If they are not fit to drive it will redirect the user to Uber app or Ola app.

### Features

Sober-Sense is a fully responsive web-app with two tests to detect sobriety:

- First is a face test, we trained this fully from scratch on a dataset of both drunk and sober people.
- Second we analyzed spectrograms & used an algorithm called levenshtein distance to be able to detect whether a user is slurring.
- It used flask which is a a web application framework written in python, Flask helps in implementing a Machine Learning app in python that can be easily plugged, extended and deployed as a web application.
- It uses several modules like `os`, `Torchvision`, `numpy`, `pydub`, `torch.nn.module`, `PIL>IMAGE`, `Shutil`, `torch.optim` 

### Tech Stack 
- Python
- Pytorch
- JavaScript
- Bootstrap
- HTML
- CSS
