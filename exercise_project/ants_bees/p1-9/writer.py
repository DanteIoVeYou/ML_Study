from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("logs")
for i in range(1,100):
    writer.add_scalar("y=3x",3*i,i)
writer.close()