import json
import os
import numpy as np
from scipy.spatial.transform import Rotation
import pandas as pd

# source_file = 'train.json'
# target_file = 'transforms_train.json'
source_file = 'validation.json'
target_file = './transforms_test.json'

# 读取 JSON 文件

with open(source_file, "r") as f:
    trainData = json.load(f)
    
print('total', len(trainData))
   
arr = []
for i in range(len(trainData)):
    data = trainData[i]
    path = data["filename"]
    
    file_path = './train/' + path
    if os.path.exists(file_path):
        # print(data)
        
        # 输入数据
        t = data['r_Vo2To_vbs_true']  # 平移 (x, y, z)
        q = data['q_vbs2tango_true']  # 四元数 (x, y, z, w)

        # 四元数 → 旋转矩阵
        rotation = Rotation.from_quat(q)
        R = rotation.as_matrix()

        # 构建 4x4 位姿矩阵
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = t

        # print("旋转矩阵 R:\n", R)
        # print("\n位姿变换矩阵 T:\n", T)
        
        arr.append({
            "file_path": file_path,
            "rotation": 0.041887902047863905,
            "time": len(arr)*0.006711409395973154,
            "transform_matrix": T
        })

print('left', len(arr))
# print(arr[0], arr[1], arr[3])


# 修改并保存
# df = pd.DataFrame(arr)
# json_str = df.to_json()
# print(json_str)
print(arr)
obj = {
    "camera_angle_x": 0.6911112070083618,
    "frames": []
}
with open(target_file, "w") as f:
    json.dump(obj, f, indent=4)