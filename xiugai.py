
import torch
model = torch.load('model_x4_2.pt')
# model['epoch']= 0
y=model['stat_dict']
# y['epochs']=0
# y['losses']=[]
y['set5']['best_psnr']['value']=0
y['set5']['best_ssim']['value']=0

y['set14']['best_psnr']['value']=0
y['set14']['best_ssim']['value']=0

y['b100']['best_psnr']['value']=0
y['b100']['best_ssim']['value']=0

y['u100']['best_psnr']['value']=0
y['u100']['best_ssim']['value']=0

y['manga109']['best_psnr']['value']=0
y['manga109']['best_ssim']['value']=0
print(model['model_state_dict'])

# torch.save(model,'model_x45.pt')