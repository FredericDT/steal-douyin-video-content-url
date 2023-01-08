#!/usr/bin/env python3
import urllib
import json
import argparse
import pprint
import logging

import requests
import bs4

from .render_data_object_strategy import video_bit_rate_list_from_render_data_object
from .exception import RenderDataTagNotFoundException, RenderDataObjectStrategyNotDefinedException

__logging = logging.getLogger(__name__)


def get_content(url: str, cookies_string: str, headers={}) -> bytes:
    """Fetch content from the given url with cookies and optional headers.

    Args:
        url (str): URL to douyin.com video page, i.g. https://www.douyin.com/discover?modal_id={model_id} or https://www.douyin.com/video/{id}.
        cookies_string (str): A workable cookie string (pass captcha).
        headers (dict, optional): HTTP request headers, not overriding Cookie header. Defaults to {}.

    Returns:
        bytes: requests.content object corresponding to the content of url
    """    
    _headers = {}
    _headers.update(headers)
    _headers['Cookie'] = cookies_string

    return requests.get(url=url, headers=_headers).content

def extract_render_data(content: bytes) -> str:
    """Extract tag body whose id is 'RENDER_DATA'.

    Args:
        content (bytes): page content, supposed to be requests' content attribute.

    Raises:
        RenderDataTagNotFoundException: raise when the given content contains no RENDER_DATA tag

    Returns:
        str: 'RENDER_DATA' tag's body 
    """    
    soup = bs4.BeautifulSoup(content, 'html.parser')
    soup_finding_render_data = soup.find(id='RENDER_DATA')
    if soup_finding_render_data is None:
        raise RenderDataTagNotFoundException()
    return soup_finding_render_data.contents[0]


def url_cookies_to_video_bit_rate_list(url: str, cookies_string: str, headers={}) -> list:
    """Extract video bit rate list from give url.

    Args:
        url (str): URL to douyin.com video page, i.g. https://www.douyin.com/discover?modal_id={model_id} or https://www.douyin.com/video/{id}.
        cookies_string (str): A workable cookie string (pass captcha).
        headers (dict, optional): HTTP request headers, not overriding Cookie header. Defaults to {}.

    Raises:
        RenderDataTagNotFoundException: raise when the given content contains no RENDER_DATA tag
        RenderDataObjectStrategyNotDefinedException: raised when all strategy failed to extract renderDataObject

    Returns:
        list: bitRateList from 'RENDER_DATA' tag body
    """    
    content = get_content(url, cookies_string=cookies_string, headers=headers)
    __logging.debug('content: {}'.format(content))
    render_data = extract_render_data(content)
    render_data = urllib.parse.unquote(render_data)
    render_data_object = json.loads(render_data)
    __logging.debug('render_data_object: {}'.format(render_data_object))
    video_bit_rate_list = video_bit_rate_list_from_render_data_object(render_data_object)
    return video_bit_rate_list

def add_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add arguemnts to argparse parser.

    Args:
        parser (argparse.ArgumentParser): argparse parser

    Returns:
        argparse.ArgumentParser: argparse parser
    """    
    parser.add_argument('--url', 
        required=True, 
        type=str, 
        help='URL to douyin.com video page, i.g. https://www.douyin.com/discover?modal_id={model_id} or https://www.douyin.com/video/{id}',
    )
    parser.add_argument('--cookies-string',
        required=True,
        type=str,
        help='A workable cookie string (pass captcha)',
    )

def main():
    parser = argparse.ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()

    cookies_string = args.cookies_string
    url = args.url

    try:
        video_bit_rate_list = url_cookies_to_video_bit_rate_list(url, cookies_string)
        pprint.pprint(video_bit_rate_list)
    except RenderDataTagNotFoundException as e:
        logging.error("RENDER_DATA tag not found")
    except RenderDataObjectStrategyNotDefinedException as e:
        logging.error("No any strategy can be used to extract video bit rate list from RENDER_DATA")

if __name__ == '__main__':
    main()