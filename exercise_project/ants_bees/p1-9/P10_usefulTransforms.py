from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img = Image.open("dataset/train/ants/0013035.jpg")
print(img)

# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
print(img_tensor)
writer.add_image("test",img_tensor,0)
writer.close()

# Normalize 归一化
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
print(img_norm)
writer.add_image("Normalize",img_norm,1)
writer.close()

# resize
trans_resize = transforms.Resize((512,512))
img_resize = trans_resize(img)
img_resize = trans_totensor(img_resize)
print(img_resize)
writer.add_image("Resize",img_resize,1)
writer.close()

# Compose
trans_resize2 = transforms.Resize(512)
trans_compose = transforms.Compose([trans_resize2, trans_totensor])
img_resize_2 = trans_compose(img)
writer.add_image("Resize",img_resize_2,2)
writer.close()

# RandomCrop

trans_random = transforms.RandomCrop(500)
trans_compose2 = transforms.Compose([trans_random, trans_totensor])
for i in range(10):
    img_random = trans_compose2(img)
    writer.add_image("Random", img_random, i)
    writer.close()