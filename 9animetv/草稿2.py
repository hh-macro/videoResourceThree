import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://rapid-cloud.co',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://rapid-cloud.co/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://lightningflash39.live/_v7/cfe37ebac83426d59305fe2f2461e86b88e39951b0eb951b0587bc4f5e6f489069baf258fcf84a9dc9b4ba81941f425ed5b1f79c51c6980afec23eedc578219672e24f659510e859c7a9dff7b324e78fd5e1da241c2cb2a5556ba34fd8ae5b44d5579f85cdba3e0d807f8db8118f544937fbe2b1325f10f0bda0da5489c125e1/index-f2-v1-a1.m3u8',
    headers=headers,
)
print(response.text)
print(response.status_code)
with open('playlist.m3u8', 'w') as f:
    f.write(response.text)


"""
93ad968a98b2e0714b39a0153ee3322292df16759978f1a08c7f455ea86ba5c882fcca20db96269febf509eb45fa5b57f799d28e4e8bb10a8ff9e1118655ae9b70f6dcae4077cb2e873260303d050fb14cf2fca33880c00ef06ce41acd6939e3d85e2411f726c3b4d1711a418ef87209c2ae100384f9989b59fe720bda3d0926
c04229b4d9709ff6927306689f15e92d7d6dc41cdf7a9aaef60c1a0dc9abbe5d5d2878ed43af5fefbe9713e711acf3fbf0c71bbb8e7cf15ff1ff92e65306d81ba59f1cb45e4f223698940d0d6e5c86f79276b112fbd59d89ae355b97cc63e183c9917c9850ac82a193920e0c9be84811916f7d0b50dd1e42c0c62c7263a14ef6


9animetv: 目前已解决监视器控制台无限debug, 且找到视频使用视频加载方式m3u8, 已经可获取下来。目前问题,发现视频m3u8中的流媒体形式并不是正常的.ts, 而是以html css js txt jpg ico,这些组成,极为怪异。在视频播放时,也是随着加载出上面那些异常流媒体。现在,在分析这些异常的流媒体中,是否是将标准的ts隐藏加密在这里面。
"""