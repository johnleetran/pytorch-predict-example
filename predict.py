import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image

#get the machine learning model
model = models.resnet18(pretrained=True)

#we need to pre-process image before making the inference
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

#load the image and preprocess the image
img = Image.open("./images/1.jpg").convert('RGB')
img_preprocessed = preprocess(img)
batch_img_tensor = torch.unsqueeze(img_preprocessed, 0)

#make the prediction
model.eval()
out = model(batch_img_tensor)

# out has information on what the prediction is and now we need to decodeit
#
# Load the file containing the 1,000 labels for the ImageNet dataset classes
#
with open('./imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]
#
# Find the index (tensor) corresponding to the maximum score in the out tensor.
# Torch.max function can be used to find the information
#
_, index = torch.max(out, 1)
#
# Find the score in terms of percentage by using torch.nn.functional.softmax function
# which normalizes the output to range [0,1] and multiplying by 100
#
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
#
# Print the name along with score of the object identified by the model
#
print(labels[index[0]], percentage[index[0]].item())
#
# Print the top 5 scores along with the image label. Sort function is invoked on the torch to sort the scores.
#
_, indices = torch.sort(out, descending=True)
[(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]
