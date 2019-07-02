import matplotlib as mpl
import matplotlib.pyplot as plt
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# fig_size = (14, 6)

# mpl.rcParams['figure.figsize'] = fig_size
# name_list = [
#     '美国', '中国', '日本', '德国', '法国', '英国', '韩国', '荷兰', '瑞士', '加拿大', '西班牙', '印度',
#     '巴西', '澳大利亚', '意大利', '俄罗斯', '爱尔兰', '墨西哥', '新加坡', '瑞典', '其他'
# ]
# num_list = [
#     126, 120, 52, 32, 28, 20, 16, 14, 14, 12, 9, 7, 7, 7, 6, 4, 4, 4, 3, 2, 13
# ]

# rects = plt.bar(range(len(num_list)), num_list, color='rgby')
# # X轴标题
# index = [
#     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# ]
# # index=[float(c)+0.1 for c in index]
# plt.ylim(ymax=200, ymin=0)
# plt.xticks(index, name_list)
# plt.ylabel("各国拥有五百强企业个数(按数量排序 暂只统计拥有两个及以上的国家)")  #Y轴标签
# for rect in rects:
#     height = rect.get_height()
#     plt.text(
#         rect.get_x() + rect.get_width() / 2,
#         height,
#         str(height),
#         ha='center',
#         va='bottom')
# plt.title('Top 500(1)')
# plt.show()

mpl.rcParams['font.sans-serif'] = ['SimHei']
fig_size = (14, 6)

mpl.rcParams['figure.figsize'] = fig_size
name_list = [
    '美国', '中国', '日本', '德国', '法国', '英国', '印度', '巴西', '意大利', '加拿大', '韩国', '俄罗斯',
    '澳大利亚', '西班牙', '墨西哥', '荷兰', '瑞士', '瑞典', '爱尔兰', '新加坡', '其他'
]
num_list = [
    126, 120, 52, 32, 28, 20, 7, 7, 6, 12, 16, 4, 7, 9, 4, 14, 14, 2, 4, 3, 13
]

rects = plt.bar(range(len(num_list)), num_list, color='rgby')
# X轴标题
index = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]
# index=[float(c)+0.1 for c in index]
plt.ylim(ymax=200, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("各国拥有五百强企业个数(按gdp排序 暂只统计拥有两个及以上的国家)")  #Y轴标签
for rect in rects:
    height = rect.get_height()
    plt.text(
        rect.get_x() + rect.get_width() / 2,
        height,
        str(height),
        ha='center',
        va='bottom')
plt.title('Top 500(2)')
plt.show()