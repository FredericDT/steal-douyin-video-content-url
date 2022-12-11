#!/usr/bin/env python3
import urllib
import json
import argparse
import pprint
import logging

import requests
import bs4

__logging = logging.getLogger(__name__)


def get_content(url, cookies_string):
    return requests.get(url=url, headers={
        'Cookie': cookies_string
    }).content

def extract_render_data(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    soup_finding_render_data = soup.find(id='RENDER_DATA')
    return soup_finding_render_data.contents[0]

def video_bit_rate_list_from_render_data_object(render_data_object):
    video_bit_rate_list = []
    if render_data_object['1']['videoDetail']:
        video_bit_rate_list = render_data_object['1']['videoDetail']['video']['bitRateList']
    elif render_data_object['41']:
        video_bit_rate_list = render_data_object['41']['aweme']['detail']['video']['bitRateList']
    return video_bit_rate_list

def url_cookies_to_video_bit_rate_list(url, cookies_string):
    content = get_content(url, cookies_string=cookies_string)
    __logging.debug('content: {}'.format(content))
    render_data = extract_render_data(content)
    render_data = urllib.parse.unquote(render_data)
    render_data_object = json.loads(render_data)
    __logging.debug('render_data_object: {}'.format(render_data_object))
    video_bit_rate_list = video_bit_rate_list_from_render_data_object(render_data_object)
    return video_bit_rate_list

def add_arguments(parser):
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

    video_bit_rate_list = url_cookies_to_video_bit_rate_list(url, cookies_string)    
    pprint.pprint(video_bit_rate_list)

if __name__ == '__main__':
    main()