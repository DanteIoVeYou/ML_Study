from time import time
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torch
from torch import nn

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

if __name__ == '__main__':
    NeuralNetwork = CIFAR10_NeuralNetwork()
    input = torch.ones((64, 3, 32, 32))
    output = NeuralNetwork(input)
    print(output.shape)
# 准备数据集
from torch.utils.tensorboard import SummaryWriter

train_dataset = torchvision.datasets.CIFAR10(root="./data", train=True, transform=torchvision.transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.CIFAR10(root="./data", train=False, transform=torchvision.transforms.ToTensor(), download=True)

# 数据集大小
len_train_dataset = len(train_dataset)
len_test_dataset = len(test_dataset)
print("训练数据集大小：{}".format(len_train_dataset))
print("测试数据集大小：{}".format(len_test_dataset))

# 加载数据集
train_dataloader = DataLoader(train_dataset, batch_size=64)
test_dataloader = DataLoader(test_dataset, batch_size=64)

# 创建神经网络
neural_network = CIFAR10_NeuralNetwork()
if torch.cuda.is_available():
    neural_network = neural_network.cuda() #gpu

# 损失函数
loss_function = nn.CrossEntropyLoss()
if torch.cuda.is_available():
    loss_function = loss_function.cuda() #gpu
# 优化器
learning_rate = 1e-2
optimizer = torch.optim.SGD(neural_network.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
#记录训练的次数
total_train = 0
#记录测试的次数
total_test = 0
#记录训练的轮数
epoch = 200

# 添加Tensorboard
writer = SummaryWriter("./logs")
time_start = time()
for i in range(epoch):
    print("------第 {} 轮训练开始------".format(i+1))

    # 训练步骤
    neural_network.train()
    for data in train_dataloader:
        imgs, targets = data
        if torch.cuda.is_available():
            imgs = imgs.cuda()
            targets = targets.cuda()
        outputs = neural_network(imgs)
        loss = loss_function(outputs ,targets)


        optimizer.zero_grad() #优化器梯度清零
        loss.backward() #反向传播
        optimizer.step()
        total_train += 1
        if total_train % 100 == 0:
            print("训练次数: {}, Loss: {}".format(total_train, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train)

# 测试步骤
    neural_network.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            if torch.cuda.is_available():
                imgs = imgs.cuda()
                targets = targets.cuda()
            outputs = neural_network(imgs)
            accuracy = (outputs.argmax(1)==targets).sum()
            total_accuracy += accuracy
            loss = loss_function(outputs, targets)
            total_test_loss += loss.item()
    print("整体测试集上的Loss: {}".format(total_test_loss))
    print("整体测试集上的正确率: {}".format(total_accuracy/len_test_dataset))
    writer.add_scalar("test_loss", total_test_loss, total_test)
    writer.add_scalar("accuracy", total_accuracy/len_test_dataset, total_test)
    total_test += 1

    torch.save(neural_network, "model/CIFAR10_{}.pth".format(i))
    print("模型已保存")
    time_end = time()
    time_consume = time_end - time_start
    time_consume = ('%.2f' % time_consume)
    print("耗时: {}s".format(time_consume))
writer.close()


