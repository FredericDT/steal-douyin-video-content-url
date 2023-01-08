# Steal douyin.com Video Content URL

## Mission

### Goals

- To steal a video content URL from douyin.com pages like `https://www.douyin.com/discover?modal_id={model_id}` or `https://www.douyin.com/video/{id}`, in which `{model_id}` or `{id}` is an unsigned long integer

### Challenges

- Implement the procedure of parsing the video content URL from page script tag.
- Understading how the data was organized via basic MISC knowledge.

## Common Use Cases

Parameters:
- url: URL to douyin.com video page, i.g. https://www.douyin.com/discover?modal_id={model_id} or https://www.douyin.com/video/{id}. See also in references 1.
- cookies_string: A workable cookie string (pass captcha).  See also in references 2.

### Programatically

```python3
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

```

Or see example.py

### Command Line

```
$ douyin-get --url 'https://www.douyin.com/discover?modal_id=6933932356776627470' --cookies-string '__ac_nonce=0638e18b700c4ad5cd39f; __ac_signature=_02B4Z6wo00f01a-SZDQAAIDCDKCUz5ad1HWvsmCAAAhrb7; ttwid=1%7CbIKjOiBYYE3NLr-FDD6dp4hkcx1sqcgLBqlQrKdCbjk%7C1670256823%7C8dba0d8cc3e4091f9fbd9b26aad760c2e3cf2aba619fcf5a6a4239220764bf92; douyin.com; s_v_web_id=verify_lbazsdt1_XguhkqQE_n3N1_4VT1_Bh0s_whUStCjHT7yR; passport_csrf_token=4a418fd9d60cefc8b5e244d5b7e70d04; passport_csrf_token_default=4a418fd9d60cefc8b5e244d5b7e70d04; csrf_session_id=9d06fbfb708c19655c2d993f82c1d0cf; ttcid=c4ce1148707e4ab48b2ed22eea60cfca94; download_guide=%221%2F20221206%22; strategyABtestKey=%221670257052.003%22; msToken=tJUgxn051HRJu9TWoYSVbHZnmjHipFm0wJvQ4Sg4eIZiLRu3ciLbkvBb5_Td4pAZRAiQL02Kz7tQGFu0X2WZK62vw9ZPywqtTMXvvRwWA2IDQowjfYS2iKiju9Y2Rg==; msToken=cbXZLNmamqDF00_D8K84e7LbQz0AN4Pe5aci81JEcL1rKq1jMVBcbv-i6stok7PKb4tBKLRGwDAeZ5jQglDA_9hkAkAIYjQ9lBqKBWcdy55KphGZvCAR37O_XUHv2w==; home_can_add_dy_2_desktop=%221%22; tt_scid=Px3YU4kZUhSaxDspIcTqkYiicQ-RIT2NSP4NYfMhPYeMiRVhPcNqG9lbYi-mLVxZ1afd'
[{'bitRate': 1601791,
  'gearName': 'normal_1080_0',
  'height': 1080,
  'isH265': 0,
  'playAddr': [{'src': '//v26-web.douyinvod.com/6dee45a98440c6027f4914b17d084b77/638ee2e3/video/tos/cn/tos-cn-ve-15c001-alinc2/091adbeb4c00419794f8ba92ac962b9b/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1564&bt=1564&cs=0&ds=4&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=0&rc=aWZpOztnNWU7OTY0Zzs5Z0Bpams5OmU1NDw3MzMzaWkzM0BiLi4uY182NjQxNGNfMWNjYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/3daf7f881c33e6c0bd3c2e6721d788bd/638ee2e3/video/tos/cn/tos-cn-ve-15c001-alinc2/091adbeb4c00419794f8ba92ac962b9b/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1564&bt=1564&cs=0&ds=4&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=0&rc=aWZpOztnNWU7OTY0Zzs5Z0Bpams5OmU1NDw3MzMzaWkzM0BiLi4uY182NjQxNGNfMWNjYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=fdf648bdf17346789b92bdf8181f1cef&sign=ecf45da02397461bd295ef82d2c1f5bb&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 1,
  'videoFormat': 'mp4',
  'width': 1920},
 {'bitRate': 950131,
  'gearName': 'normal_720_0',
  'height': 720,
  'isH265': 0,
  'playAddr': [{'src': '//v26-web.douyinvod.com/913fdb716fc4caddcf076cbd0cee1d0c/638ee2e3/video/tos/cn/tos-cn-ve-15/79d41e71bd5149c188d74776b074a486/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=927&bt=927&cs=0&ds=3&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=0&rc=PGY4OGQ1M2Y4ZjdkZDNkOkBpams5OmU1NDw3MzMzaWkzM0A2NTAyXmMvXjIxXzFeNi9hYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/77c9311a11945047f5532e62f021c63f/638ee2e3/video/tos/cn/tos-cn-ve-15/79d41e71bd5149c188d74776b074a486/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=927&bt=927&cs=0&ds=3&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=0&rc=PGY4OGQ1M2Y4ZjdkZDNkOkBpams5OmU1NDw3MzMzaWkzM0A2NTAyXmMvXjIxXzFeNi9hYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=d72a90aa4ab44c55ac20f2aa55358c99&sign=7fd350d937353872a4273eb1caca3742&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 10,
  'videoFormat': 'mp4',
  'width': 1280},
 {'bitRate': 649532,
  'gearName': 'adapt_lowest_720_1',
  'height': 720,
  'isH265': 1,
  'playAddr': [{'src': '//v26-web.douyinvod.com/8c71402b9d5c32f9faf7dcd83a0fb40a/638ee2e3/video/tos/cn/tos-cn-ve-15/401c9c33fcc246d69b533a5a13160196/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=634&bt=634&cs=2&ds=3&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=15&rc=NjNmaTNlPDo5Ozs2ZTNoNUBpams5OmU1NDw3MzMzaWkzM0AzLjEwMF8vNjMxXjJfNDMyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/c47f749c0e6fce6d89b03b41dbf31427/638ee2e3/video/tos/cn/tos-cn-ve-15/401c9c33fcc246d69b533a5a13160196/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=634&bt=634&cs=2&ds=3&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=15&rc=NjNmaTNlPDo5Ozs2ZTNoNUBpams5OmU1NDw3MzMzaWkzM0AzLjEwMF8vNjMxXjJfNDMyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=526e70bb53a848669729bb303f4c1063&sign=0bba3209da9bbf4d0937069f27d38de0&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 15,
  'videoFormat': 'mp4',
  'width': 1280},
 {'bitRate': 562092,
  'gearName': 'lower_540_0',
  'height': 576,
  'isH265': 0,
  'playAddr': [{'src': '//v26-web.douyinvod.com/37a3b9883078179b46180e994bfefb4d/638ee2e3/video/tos/cn/tos-cn-ve-15/b1a76e79c9994e09a3ee89ceb6a9f9bf/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=548&bt=548&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=4&rc=ZjU0ZWY0OGU5PDNkOjhkO0Bpams5OmU1NDw3MzMzaWkzM0AxXjVeNjRiNjExNS9eNDIyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/21e7d3d65649e8805deb3cab33248d65/638ee2e3/video/tos/cn/tos-cn-ve-15/b1a76e79c9994e09a3ee89ceb6a9f9bf/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=548&bt=548&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=4&rc=ZjU0ZWY0OGU5PDNkOjhkO0Bpams5OmU1NDw3MzMzaWkzM0AxXjVeNjRiNjExNS9eNDIyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=585a75a72a8049469be5719cab81a24c&sign=1d595dd610fb8840bc2a592b7a1dea3b&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 24,
  'videoFormat': 'mp4',
  'width': 1024},
 {'bitRate': 551064,
  'gearName': 'adapt_540_1',
  'height': 576,
  'isH265': 1,
  'playAddr': [{'src': '//v26-web.douyinvod.com/a51ef8773bdb8dac0561ba348a843c68/638ee2e3/video/tos/cn/tos-cn-ve-15/5fe6d0c585954bbdb3acc4aad892989f/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=538&bt=538&cs=2&ds=6&eid=258&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=11&rc=N2U8ZTo3ZTg4aGc3M2c6ZEBpams5OmU1NDw3MzMzaWkzM0BfNF5fYWMtXzYxMi8uLTIyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/dc9cf9b79187918f8720f44b047da197/638ee2e3/video/tos/cn/tos-cn-ve-15/5fe6d0c585954bbdb3acc4aad892989f/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=538&bt=538&cs=2&ds=6&eid=258&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=11&rc=N2U8ZTo3ZTg4aGc3M2c6ZEBpams5OmU1NDw3MzMzaWkzM0BfNF5fYWMtXzYxMi8uLTIyYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=5a570d10245d4e95b50bf4d7bba97bb4&sign=9199d0c78c586a085d203b9b3172a56b&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 28,
  'videoFormat': 'mp4',
  'width': 1024},
 {'bitRate': 413595,
  'gearName': 'adapt_lower_540_1',
  'height': 576,
  'isH265': 1,
  'playAddr': [{'src': '//v26-web.douyinvod.com/d5452e5e05c1e49442aae0ba8d25fd10/638ee2e3/video/tos/cn/tos-cn-ve-15/e6af7d5df6294e3d87c2b0c4937370f9/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=403&bt=403&cs=2&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=14&rc=ZTw1ODU0ZTo5NWhpaTM2OkBpams5OmU1NDw3MzMzaWkzM0A2LjMtXy1eNjIxLy40X2JeYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'},
               {'src': '//v3-web.douyinvod.com/6ee0538b93c0841ff5f92f33aab25cdf/638ee2e3/video/tos/cn/tos-cn-ve-15/e6af7d5df6294e3d87c2b0c4937370f9/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=403&bt=403&cs=2&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi-GkC~jKJIc5bAG0P3-A&mime_type=video_mp4&qs=14&rc=ZTw1ODU0ZTo5NWhpaTM2OkBpams5OmU1NDw3MzMzaWkzM0A2LjMtXy1eNjIxLy40X2JeYSNebTRhNDIuNnFgLS0zLS9zcw%3D%3D&l=20221206133048010141130035000BCCED&btag=30000'}],
  'playApi': '//www.douyin.com/aweme/v1/play/?video_id=v0200f6f0000c0t49911527bd776phag&line=0&file_id=a7e3b07f1f2e425697ab01b20562199b&sign=8a44a4bb0eb5c357c8df93c13da0c585&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383',
  'qualityType': 21,
  'videoFormat': 'mp4',
  'width': 1024}]

```

## Installation

```
$ python setup.py sdist
$ pip install dist/steal_douyin_video_content_url-{VERSION}.tar.gz
```

## Contributors

Great thanks to all contributors.

## Contributing 

Pull requests are welcome.

## References

1. Uniform Resource Locator (URL). https://en.wikipedia.org/wiki/URL
2. HTTP cookies. https://en.wikipedia.org/wiki/HTTP_cookie

## License

[GPLv3](./LICENSE)

Copyright (c) 2022-present, Weihan (fdt) Tian