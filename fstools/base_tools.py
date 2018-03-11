import os


def list_path(path, filter=None, recursive=True):
    """
    列出目录下的文件
    :param path: 路径，绝对或相对路径
    :param filter: 过滤函数，结果为True时返回，默认不做过滤
    :param recursive: 是否递归调用
    :return: 文件名列表
    """

    if not os.path.isdir(path):
        return []
    files = os.listdir(path)
    for e_file in files:
        e_file = os.path.join(path, e_file)
        if os.path.isdir(e_file):
            if recursive:
                try:
                    for e_s_file in list_path(e_file, filter, True):
                        yield  e_s_file
                except:
                    pass
        if not callable(filter) or filter(e_file):
            yield e_file


def list_large_files(path, min_size, recursive):
    """
    列出目录下的大文件
    :param path: 绝对/相对路径
    :param min_size: 大文件的标准
    :param recursive: 是否递归检查
    """
    for e_file in list_path(path, recursive=recursive):
        file_size = os.stat(e_file).st_size
        if file_size >= min_size:
            print("%s,%d"%(e_file, file_size))
