from server.__server import start_server
from __setup import setup
from models.face.transform_and_train import getTrainLoader
from models.face.train import train_model
from models.face.pieces import pieces
from __utils import get_model

setup()
pieces()
model = get_model()
# train_model(model, getTrainLoader())

start_server()
