# -*- coding=utf-8 -*-
import os
import sys
import traceback
import psutil


def show_layer_info(layer_name, layer_out):
    print('[layer]: %s\t[shape]: %s \n%s' % (layer_name,str(layer_out.get_shape().as_list()), show_memory_use()))


def show_memory_use():
    used_memory_percent = psutil.virtual_memory().percent
    strinfo = '{}% memory has been used'.format(used_memory_percent)
    return strinfo


def import_class(import_str):
    mod_str, _sep, class_str = import_str.rpartition('.')
    __import__(mod_str)
    try:
        return getattr(sys.modules[mod_str], class_str)#Python中所有加载到内存的模块都放在sys.modules。当import一个模块时首先会在这个列表中查找是否已经加载了此模块，如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。如果没有加载则从sys.path目录中按照模块名称查找模块文件，模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，并将名称导入到当前的Local名字空间
    except AttributeError:
        raise ImportError('Class %s cannot be found (%s)' %
                (class_str,
                    traceback.format_exception(*sys.exc_info())))


def import_object(import_str, *args, **kwargs):
    return import_class(import_str)(*args, **kwargs)


def import_module(import_str):
    __import__(import_str)
    return sys.modules[import_str]
