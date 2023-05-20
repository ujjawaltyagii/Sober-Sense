import torch.nn as NeuralNetwork


class Model(NeuralNetwork.Module):
    def __init__(self):

        super().__init__()

        self.convolution = NeuralNetwork.Sequential(
            NeuralNetwork.Conv2d(1, 32, (5, 5)),
            NeuralNetwork.ReLU(),
            NeuralNetwork.Conv2d(32, 64, (5, 5)),
            NeuralNetwork.ReLU(),
            NeuralNetwork.Flatten(),
            NeuralNetwork.Linear(112896, 2)
        )

    def forward(self, x):
        return self.convolution(x)
