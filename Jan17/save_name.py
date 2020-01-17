import os


def save_name(path, suffix):
    base_dir = os.path.dirname(path)
    file_name = os.path.basename(path).split('.')
    # print(file_name)
    save_name_str = '{}_{}.{}'.format(file_name[0], suffix, file_name[1])
    # print(save_name_str)
    return os.path.join(base_dir, save_name_str)


if __name__ == "__main__":
    print(save_name('IMAGE/iu1.jpg', 'test'))
