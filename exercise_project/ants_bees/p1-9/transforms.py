from PIL import Image
from torchvision import transforms

img_path = "dataset/train/ants/0013035.jpg"
img_jpeg = Image.open(img_path)
tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img_jpeg)