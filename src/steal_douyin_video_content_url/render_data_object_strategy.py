import logging
__logging = logging.getLogger(__name__)

from .exception import RenderDataObjectStrategyNotDefinedException

# TODO: Refactor with Strategy Pattern
_render_data_rate_list_map = {
    '1001': {
        'criteria': lambda x: x['videoDetail'],
        'extract': lambda x: x['videoDetail']['video']['bitRateList'],
    },
    '1041': {
        'criteria': lambda x: x['aweme'],
        'extract': lambda x: x['aweme']['detail']['video']['bitRateList'],
    },
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
    for i, x in render_data_object.items():
        video_bit_rate_list = []
        for k, v in _render_data_rate_list_map.items():
            try:
                if v['criteria'](x):
                    video_bit_rate_list = v['extract'](x)
                    return video_bit_rate_list
            except TypeError as e:
                __logging.debug('TypeError on k={} render_data_object: {}'.format(k, x))
            except KeyError as e:
                __logging.debug('KeyError on k={} render_data_object: {}'.format(k, x))
    raise RenderDataObjectStrategyNotDefinedException()