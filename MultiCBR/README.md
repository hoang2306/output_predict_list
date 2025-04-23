# How output rec list 
cách output ra predict list cho mỗi user theo topk (multiCBR: https://github.com/HappyPointer/MultiCBR.git)

* tải datasets từ repo của multiCBR
* train models như trong repo
* sau khi train xong -> vào folder log sẽ thấy 3 file bundle_list.pt, score_list.pt, users_list.pt
* dùng file get_user_bundle_predict_list.py trong folder test_toolkit để output ra file .csv 3 cột user, bundle, score (chú ý chỉnh lại path)
* để check xem file có output đúng hay không, ta check recall thông qua file test_toolkit/test_read.ipynb
