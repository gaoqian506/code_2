
'''
这个文件相当于是总的文件, 有着接受参数和整体控制的作用
'''


def train():
    '''
    训练函数, 创建数据和重建器, 然后让重建器去学习
    :return:无
    '''

    dataset = create_dataset(config)
    constructor = create_constructor(config)

    for epoch in config.epochs:
        for data in dataset:
            constructor.learn(data)


if __name__ == '__main__':
    train()
