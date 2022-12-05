#!/usr/bin/env python3
import urllib
import json
import argparse
import pprint

import requests
import bs4


def get_content(url, cookies_string):
    return requests.get(url=url, headers={
        'Cookie': cookies_string
    }).content

def extract_render_data(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    return soup.find(id='RENDER_DATA').contents[0]

def video_bit_rate_list_from_render_data_object(render_data_object):
    video_bit_rate_list = render_data_object['1']['videoDetail']['video']['bitRateList']
    return video_bit_rate_list

def url_cookies_to_video_bit_rate_list(url, cookies_string):
    content = get_content(url, cookies_string=cookies_string)
    render_data = extract_render_data(content)
    render_data = urllib.parse.unquote(render_data)
    render_data_object = json.loads(render_data)
    video_bit_rate_list = video_bit_rate_list_from_render_data_object(render_data_object)
    return video_bit_rate_list

def add_arguments(parser):
    parser.add_argument('--url', 
        required=True, 
        type=str, 
        help='URL to douyin.com video page',
    )
    parser.add_argument('--cookies-string',
        required=True,
        type=str,
        help='A workable cookie string (pass captcha)',
    )

if __name__ == '__main__':
    # cookies_string = '__ac_nonce=0638e18b700c4ad5cd39f; __ac_signature=_02B4Z6wo00f01a-SZDQAAIDCDKCUz5ad1HWvsmCAAAhrb7; ttwid=1%7CbIKjOiBYYE3NLr-FDD6dp4hkcx1sqcgLBqlQrKdCbjk%7C1670256823%7C8dba0d8cc3e4091f9fbd9b26aad760c2e3cf2aba619fcf5a6a4239220764bf92; douyin.com; s_v_web_id=verify_lbazsdt1_XguhkqQE_n3N1_4VT1_Bh0s_whUStCjHT7yR; passport_csrf_token=4a418fd9d60cefc8b5e244d5b7e70d04; passport_csrf_token_default=4a418fd9d60cefc8b5e244d5b7e70d04; csrf_session_id=9d06fbfb708c19655c2d993f82c1d0cf; ttcid=c4ce1148707e4ab48b2ed22eea60cfca94; download_guide=%221%2F20221206%22; strategyABtestKey=%221670257052.003%22; msToken=tJUgxn051HRJu9TWoYSVbHZnmjHipFm0wJvQ4Sg4eIZiLRu3ciLbkvBb5_Td4pAZRAiQL02Kz7tQGFu0X2WZK62vw9ZPywqtTMXvvRwWA2IDQowjfYS2iKiju9Y2Rg==; msToken=cbXZLNmamqDF00_D8K84e7LbQz0AN4Pe5aci81JEcL1rKq1jMVBcbv-i6stok7PKb4tBKLRGwDAeZ5jQglDA_9hkAkAIYjQ9lBqKBWcdy55KphGZvCAR37O_XUHv2w==; home_can_add_dy_2_desktop=%221%22; tt_scid=Px3YU4kZUhSaxDspIcTqkYiicQ-RIT2NSP4NYfMhPYeMiRVhPcNqG9lbYi-mLVxZ1afd'
    # url = 'https://www.douyin.com/discover?modal_id=6933932356776627470'

    parser = argparse.ArgumentParser(prog='steal-douyin-video-content-url')
    add_arguments(parser)
    args = parser.parse_args()

    cookies_string = args.cookies_string
    url = args.url

    video_bit_rate_list = url_cookies_to_video_bit_rate_list(url, cookies_string)    
    pprint.pprint(video_bit_rate_list)