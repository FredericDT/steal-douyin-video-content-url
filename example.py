import argparse
import pprint

import steal_douyin_video_content_url 

def main():
    parser = argparse.ArgumentParser()
    steal_douyin_video_content_url.add_arguments(parser)
    args = parser.parse_args()

    cookies_string = args.cookies_string
    url = args.url

    video_bit_rate_list = steal_douyin_video_content_url.url_cookies_to_video_bit_rate_list(url, cookies_string)    
    pprint.pprint(video_bit_rate_list)

if __name__ == '__main__':
    main()
