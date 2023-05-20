import torch
from PIL import Image
from .transform_and_train import image_transforms
from __utils import get_model

model = get_model()


def check_inebriated(path):

    model.load_state_dict(torch.load(path))
    img = Image.open('IMAGES/sober/piece72.jpg')
    img_transformed = image_transforms(img)
    img_batch = img_transformed.unsqueeze(0)

    output = model(img_batch)
    predicted_class = torch.argmax(output)
    print("Predicted class:", predicted_class.item())
    return predicted_class.item() == 0
