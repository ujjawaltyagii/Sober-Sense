import torch
import torch.optim as optim
import torch.nn as NeuralNetwork


def train_model(model, train_loader):

    opt = optim.Adam(model.parameters(), lr=0.0001)
    loss_fn = NeuralNetwork.CrossEntropyLoss()

    for epoch in range(20):
        for batch in train_loader:
            X, y = batch
            output = model(X)

            loss = loss_fn(output, y)
            opt.zero_grad()
            loss.backward()
            opt.step()

        print(f'LOSS: {loss}')
        torch.save(model.state_dict(), 'model.pth')
