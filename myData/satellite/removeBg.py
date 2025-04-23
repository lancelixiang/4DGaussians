from rembg import remove
import os

# 去除背景
def remove_bg(input_path, output_path):
    with open(input_path, "rb") as f_in:
        with open(output_path, "wb") as f_out:
            input_img = f_in.read()
            output_img = remove(input_img)  # 自动返回透明背景的PNG
            f_out.write(output_img)

remove_bg('train/img003182.jpg','train/img003182.png')
remove_bg('test/img003182.jpg','test/img003182.png')

# folder = "./train"
# files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
# # print(files)
# for file in files:
#     # print(fruit)
#     if not os.path.exists(os.path.join(folder, file.replace('jpg', 'png'))):
#         print(file)
#         remove_bg(os.path.join(folder, file), os.path.join(folder, file.replace('jpg', 'png')))
