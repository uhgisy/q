import random
# 生成 0.0 到 1.0 之间的随机浮点数
print(random.random()) # 输出示例: 0.7597072251250637
# 生成指定范围内的随机整数
print(random.randint(1, 10)) # 输出示例: 7
# 从列表中随机选择一个元素
choices = [1, 2, 3, 4, 5]
print(random.choice(choices)) # 输出示例: 3
# 将列表中的元素随机打乱
random.shuffle(choices)
print(choices) # 输出示例: [4, 1, 5, 3, 2]
