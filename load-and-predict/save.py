import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image

#get the machine learning model
model = models.resnet18(pretrained=True)
model.eval()
torch.save(model.state_dict(), "model.pt")
