import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

#load the image and preprocess the image
img = Image.open("../images/1.jpg").convert('RGB')
img_preprocessed = preprocess(img)
batch_img_tensor = torch.unsqueeze(img_preprocessed, 0)

#make the prediction
model = models.resnet18(pretrained=True)
model.eval()
# out = model(batch_img_tensor)
#get the machine learning model

traced = torch.jit.trace(model, batch_img_tensor)
traced.save('model.pt')
