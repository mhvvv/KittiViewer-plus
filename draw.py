import numpy as np
import open3d as o3d
import struct
import matplotlib.pyplot as plt
from pandas import DataFrame
from pyntcloud import PyntCloud
import math
import random
#import Spectral as sp
from collections import defaultdict
 
# 功能：从kitti的.bin格式点云文件中读取点云
# 输入：
#     path: 文件路径
# 输出：
#     点云数组
def read_velodyne_bin(path):
    '''
    :param path:
    :return: homography matrix of the point cloud, N*3
    '''
    pc_list = []
    with open(path, 'rb') as f:
        content = f.read()
        pc_iter = struct.iter_unpack('ffff', content)
        for idx, point in enumerate(pc_iter):
            pc_list.append([point[0], point[1], point[2]])
    return np.asarray(pc_list, dtype=np.float32)
 
 
def main():
    iteration_num = 1  # 文件数
 
    # for i in range(iteration_num):
    filename = '/data/sets/kitti_second/training/velodyne/000002.bin'  # 数据集路径
    print('clustering pointcloud file:', filename)
 
    origin_points = read_velodyne_bin(filename)  # 读取数据点
    origin_points_df = DataFrame(origin_points, columns=['x', 'y', 'z'])  # 选取每一列 的 第0个元素到第二个元素   [0,3)
    point_cloud_pynt = PyntCloud(origin_points_df)  # 将points的数据 存到结构体中
    point_cloud_o3d = point_cloud_pynt.to_instance("open3d", mesh=False)  # 实例化
    #
    o3d.visualization.draw_geometries([point_cloud_o3d])  # 显示原始点云
 
 
if __name__ == '__main__':
    main()
