import torch
from torchvision import transforms, datasets
from __paths import TRAINING_DATA

image_transforms = transforms.Compose([
    transforms.Resize((50, 50)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

training = datasets.ImageFolder(TRAINING_DATA, transform=image_transforms)
train_loader = torch.utils.data.DataLoader(
    training, batch_size=3, shuffle=True)


def getTrainLoader():
    return train_loader
