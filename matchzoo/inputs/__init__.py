# note
from __future__ import absolute_import
import six
from keras.utils.generic_utils import deserialize_keras_object

from .point_generator import PointGenerator
from .point_generator import Triletter_PointGenerator
from .point_generator import DRMM_PointGenerator

from .pair_generator import PairGenerator
from .pair_generator import Triletter_PairGenerator
from .pair_generator import DRMM_PairGenerator
from .pair_generator import PairGenerator_Feats
from .list_generator import ListGenerator
from .list_generator import Triletter_ListGenerator
from .list_generator import DRMM_ListGenerator
from .list_generator import ListGenerator_Feats

def serialize(generator):
    return generator.__name__

def deserialize(name, custom_objects=None):
    return deserialize_keras_object(name,
                                    module_objects=globals(),#会以字典类型返回当前位置的全部全局变量
                                    custom_objects=custom_objects,
                                    printable_module_name='loss function')

def get(identifier):
    if identifier is None:
        return None
    if isinstance(identifier, six.string_types):#six专门用来兼容 Python 2 和 Python 3 的库,解决了诸如 urllib 的部分方法不兼容， str 和 bytes 类型不兼容等“知名”问题
        identifier = str(identifier)
        return deserialize(identifier)
    elif callable(identifier):
        return identifier
    else:
        raise ValueError('Could not interpret '
                         'loss function identifier:', identifier)

