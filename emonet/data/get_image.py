from PIL import Image
from os import listdir
from torch.utils.data import Dataset
from pathlib import Path

import os

class Images(Dataset):
    def __init__(self, folder_name, transformations, downsample=10, path= '/emonet/data/videos/'):

        self.path = os.getcwd() + path + folder_name + '/'
        files = [f for f in listdir(self.path)]
        self.down_selected = []
        for i in range(0, len(files), downsample):
            self.down_selected.append(self.path + files[i])

        self.transforms = transformations

    def __len__(self):
        return len(self.down_selected)

    def __getitem__(self, index):
        filepath = self.down_selected[index]
        im = Image.open(filepath)
        im = self.transforms(im)
        return im

# im = Image.open()
# # print(im.shape)
# # print(im.dtype)
# #transform_image = transforms.Compose([transforms.ToTensor(), transforms.Resize((256, 256))])
# transform_image = transforms.Compose([transforms.ToTensor(), transforms.Resize(256), transforms.CenterCrop(256)])
# im = transform_image(im)
#
# print(im.shape)
# print(im.dtype)
#
# im1 = io.imread("./videos/big_short/ezgif-frame-001.jpg")
# print(im1.shape)
# print(im1.dtype)
# im1 = transform_image(im1)
# print(im1.shape)
# print(im1.dtype)
# plt.imshow(im1.permute(1, 2, 0))
# plt.show()
