import torch
from tqdm import tqdm 
import pandas as pd 

users_list = torch.load('users_list.pt')
bundle_list = torch.load('bundle_list.pt')
score_list = torch.load('score_list.pt')


data = []
for user, bundles, scores in tqdm(zip(users_list, bundle_list, score_list)):
    for bundle, score in zip(bundles, scores):
        data.append({'user': user.item(), 'bundle': bundle.cpu().item(), 'score': "{:.4f}".format(score.cpu().item())})

df = pd.DataFrame(data)
# log_path = "./log/%s/%s" % (conf["dataset"], conf["model"]) + '/user_bundle_predict_list.csv'
log_path = 'user_bundle_predict_list.csv'
df.to_csv(log_path, index=False)
print('------------------user-bundle list predict has write---------------------')