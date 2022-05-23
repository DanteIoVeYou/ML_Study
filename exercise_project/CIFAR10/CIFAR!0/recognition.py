import torch
import torchvision
from PIL import Image
from torch import nn

image_path = "D:\\codehub\\ML_Study\\exercise_project\\CIFAR10\\CIFAR!0\\recognition_imgs\\claisen.PNG"
image = Image.open(image_path)
print(image)
image = image.convert("RGB")
transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])
image = transform(image)
print(image.shape)

class CIFAR10_NeuralNetwork(nn.Module):
    def __init__(self):
        super(CIFAR10_NeuralNetwork, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4, 64),
            nn.Linear(64, 10)
        )
    def forward(self, x):
        x = self.model(x)
        return x

model = torch.load("D:\\codehub\\ML_Study\\exercise_project\\CIFAR10\\CIFAR!0\\model\\CIFAR10_88.pth", map_location=torch.device('cpu'))

image = torch.reshape(image, (1, 3, 32, 32))
model.eval()
with torch.no_grad():
    output = model(image)
print(output)
print(output.argmax(1))

total_success = 0
for i in range(200):
    model = torch.load("D:\\codehub\\ML_Study\\exercise_project\\CIFAR10\\CIFAR!0\\model\\CIFAR10_{}.pth".format(i),
                       map_location=torch.device('cpu'))
    image = torch.reshape(image, (1, 3, 32, 32))
    model.eval()
    with torch.no_grad():
        output = model(image)
    if output.argmax(1).item() == 5:
        total_success += 1
print(total_success)
