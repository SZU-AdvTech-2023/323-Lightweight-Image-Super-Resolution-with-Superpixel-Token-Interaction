import matplotlib.pyplot as plt
import numpy as np
import yaml
with open('stat_dict.yml') as file1:
    data = yaml.load(file1,Loader=yaml.FullLoader)

y=data['losses']
x=range(len(y))
# list=['set5','set14','b100','u100','manga109']
# for i in list:
#     # print(data[i]['best_psnr']['value'])
#     print(str(data[i]['best_psnr']['value'])+'/'+str(data[i]['best_ssim']['value']),end='  ')

# y_train_loss = data_read(train_loss_path)  # loss值，即y轴
# x_train_loss = range(len(y_train_loss))  # loss的数量，即x轴

plt.figure()

# 去除顶部和右边框框
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel('iters')  # x轴标签
plt.ylabel('loss')  # y轴标签

# 以x_train_loss为横坐标，y_train_loss为纵坐标，曲线宽度为1，实线，增加标签，训练损失，
# 默认颜色，如果想更改颜色，可以增加参数color='red',这是红色。
plt.plot(x, y, linewidth=1, linestyle="solid", label="train loss")
plt.legend()
plt.title('Loss curve')
# plt.show()
plt.savefig("loss.png")