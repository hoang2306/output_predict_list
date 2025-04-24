Once the training process is complete, three files — user_list.pt, bundle_list.pt, and score_list.pt — will be saved to the directory specified by log_path = "./log/%s/%s" % (conf["dataset"], conf["model"]).

Next, use the script get_user_bundle_predict_list.py to generate a .csv file containing three columns: user, bundle, and score.

⚠️ Note: Make sure to correctly configure the paths to the three .pt files in the script.

