import torch
from torchvision import transforms, datasets
import torch.nn as nn
import torch.optim as optim
from PIL import Image
import os
import os
import shutil

directory_path = 'pieces'

even_folder_path = 'sober'
odd_folder_path = 'drunk'

os.makedirs(even_folder_path, exist_ok=True)
os.makedirs(odd_folder_path, exist_ok=True)

for filename in os.listdir(directory_path):
    if filename.endswith('.jpg'):
        number = int(filename.replace('piece', '').replace('.jpg', ''))
        
        if number % 2 == 0:
            shutil.move(os.path.join(directory_path, filename), os.path.join(even_folder_path, filename))
        else:
            shutil.move(os.path.join(directory_path, filename), os.path.join(odd_folder_path, filename))


img_transforms = transforms.Compose([
    transforms.Resize((50, 50)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

training = datasets.ImageFolder('IMAGES', transform=img_transforms)
train_loader = torch.utils.data.DataLoader(training, batch_size=3, shuffle=True)
#torch.utils.data.DataLoader. The DataLoader is responsible for loading the data from the dataset in batches
class Model(nn.Module):
    def __init__(self):

        super().__init__()

        self.convolution = nn.Sequential(      # sequential container for the model's layers.
            nn.Conv2d(1, 32, (5, 5)),        #Applies a 2D convolutional layer with 1 input channel, 32 output channels, and a kernel size of 5x5.
            nn.ReLU(),
            nn.Conv2d(32, 64, (5, 5)),
            nn.ReLU(),                           #Applies the rectified linear unit activation function
            nn.Flatten(),                     # Flattens the input tensor into a 1D vector.
            nn.Linear(112896, 2)         #Applies a linear transformation to the input tensor, mapping it to a 2-dimensional output tensor.
        )

    def forward(self, x):                   #x is the input tensor.
        return self.convolution(x)            #x is passed above

def train_model():
    model = Model()                 #creating instance of model class

    opt = optim.Adam(model.parameters(), lr = 0.0001)      # update the model's parameters during training.
    loss_fn = nn.CrossEntropyLoss()            #to compute the loss between the model's output and the target labels.

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

#train_model()

def check_intoxicated(path):

    model = Model()
    model.load_state_dict(torch.load(path))
    img = Image.open('IMAGES/sober/piece72.jpg')
    img_transformed = img_transforms(img)
    img_batch = img_transformed.unsqueeze(0)  # Add a batch dimension to the tensor img

    output = model(img_batch)
    predicted_class = torch.argmax(output)
    print("Predicted class:", predicted_class.item())
