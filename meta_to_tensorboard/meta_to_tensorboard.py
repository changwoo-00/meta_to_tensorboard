
import argparse
import tensorflow as tf
import os
from tensorflow.summary import FileWriter

args_list = []
parser = argparse.ArgumentParser()

def add_arg_group(name):
    """
    :param name: argument group, str
    :return: list (argument)
    """
    arg = parser.add_argument_group(name)
    args_list.append(arg)
    return arg

def get_config():
    cfg, un_parsed = parser.parse_known_args()
    return cfg, un_parsed

def main():
    print('--------------------------------')
    print('ARGUMENTS : ')
    print('--meta : input meta file')
    print('--savedir : save directory name')
    print('--------------------------------')
    config, _ = get_config()

    if config.meta == None:
        print('meta file path : ')
        config.meta = input()

    if config.savedir == None:
        print('save directory name')
        config.savedir = input()

    sess = tf.Session()
    tf.train.import_meta_graph(config.meta)
    FileWriter("savedir/"+config.savedir, sess.graph)

    print('Open tensorboard?(y/n)')
    ans = input()
    if ans == 'y':
        os.system('cmd /k "tensorboard --logdir savedir\%s"'%config.savedir)


mode_arg = add_arg_group('mode')
mode_arg.add_argument('--meta', type=str, default=None)
mode_arg.add_argument('--savedir', type=str, default=None)

if __name__ == "__main__":
    main()
