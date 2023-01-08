import argparse
import pprint

import steal_douyin_video_content_url 

import logging

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    steal_douyin_video_content_url.add_arguments(parser)
    args = parser.parse_args()

    cookies_string = args.cookies_string
    url = args.url
    try:
        video_bit_rate_list = steal_douyin_video_content_url.url_cookies_to_video_bit_rate_list(url, cookies_string)
        pprint.pprint(video_bit_rate_list)
    except steal_douyin_video_content_url.RenderDataTagNotFoundException as e:
        logging.error("RENDER_DATA tag not found")
    except steal_douyin_video_content_url.RenderDataObjectStrategyNotDefinedException as e:
        logging.error("No any strategy can be used to extract video bit rate list from RENDER_DATA")


if __name__ == '__main__':
    main()
