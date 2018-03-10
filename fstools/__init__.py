import os


def list_path(path, filter=None, recursive=True):
    """
    列出目录下的文件
    :param path: 路径，绝对或相对路径
    :param filter: 过滤函数，结果为True时返回，默认不做过滤
    :param recursive: 是否递归调用
    :return: 文件名列表
    """
    res = []
    if not os.path.isdir(path):
        return []
    files = os.listdir(path)
    for e_file in files:
        e_file = os.path.join(path, e_file)
        if os.path.isdir(e_file):
            if recursive:
                res.extend(list_path(e_file, filter, True))
        if not callable(filter) or filter(e_file):
            res.append(e_file)
    return res


def list_large_files(path, min_size):
    """
    列出目录下的大文件
    :param path: 绝对/相对路径
    :param min_size: 大文件的标准
    """
    for e_file in list_path(path):
        file_size = os.stat(e_file).st_size
        if file_size >= min_size:
            print("%s,%d"%(e_file, file_size))