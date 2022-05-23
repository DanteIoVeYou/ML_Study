from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy


writer = SummaryWriter("logs")
img_path = "dataset/train/bees/16838648_415acd9e3f.jpg"
img_PIL = Image.open(img_path)
img_numpy = numpy.array(img_PIL)
writer.add_image("test",img_numpy, 3, dataformats="HWC")
writer.close()