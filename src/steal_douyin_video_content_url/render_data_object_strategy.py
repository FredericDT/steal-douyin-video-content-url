import logging
__logging = logging.getLogger(__name__)

from .exception import RenderDataObjectStrategyNotDefinedException

def _render_data_rate_list_map_aweme(name='41'):
    return {
        'extract': lambda render_data_object: render_data_object[name]['aweme']['detail']['video']['bitRateList'],
        'criteria': lambda render_data_object: render_data_object[name],
    }

# TODO: Refactor with Strategy Pattern
_render_data_rate_list_map = {
    '1': {
        'extract': lambda render_data_object: render_data_object['1']['videoDetail']['video']['bitRateList'],
        'criteria': lambda render_data_object: render_data_object['1']['videoDetail'],
    },
    '41': _render_data_rate_list_map_aweme('41'),
    '42': _render_data_rate_list_map_aweme('42'),
    '43': _render_data_rate_list_map_aweme('43'),
}

def video_bit_rate_list_from_render_data_object(render_data_object: dict) -> list:
    """Try to extract video bit rate list from render_data_object with pre-defined strategies.

    Args:
        render_data_object (dict): render_data_object json object loaded from tag body whose id is 'RENDER_DATA'

    Raises:
        RenderDataObjectStrategyNotDefinedException: raised when all strategy failed to extract renderDataObject

    Returns:
        list: bitRateList from render_data_object
    """    
    video_bit_rate_list = []
    for k, v in _render_data_rate_list_map.items():
        try:
            if v['criteria'](render_data_object):
                video_bit_rate_list = v['extract'](render_data_object)
                return video_bit_rate_list
        except TypeError as e:
            __logging.debug('TypeError on render_data_object: {}'.format(render_data_object))
        except KeyError as e:
            __logging.debug('KeyError on render_data_object: {}'.format(render_data_object))
    raise RenderDataObjectStrategyNotDefinedException()