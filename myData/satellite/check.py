from PIL import Image
import os

file_path = "train/img000005.png"

if os.path.exists(file_path):
    try:
        img = Image.open(file_path)
        # img.show()
    except Exception as e:
        print(f"错误: {e}")
else:
    print("文件不存在！")