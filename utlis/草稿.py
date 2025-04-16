import requests

headers = {
    'User-Agent': 'Microsoft BITS/7.8',
    # 'Accept-Encoding': 'identity',
    'If-Unmodified-Since': 'Thu, 10 Apr 2025 20:01:24 GMT',
    'Range': 'bytes=298154-940493',
}

params = {
    'P1': '1745357440',
    'P2': '404',
    'P3': '2',
    'P4': 'jhbyUWdsRcEFVwM895yHtMReWNpLflSE439beovkyQWxn9THn4astzOyd88z5Ak0GkWnhISPL3tzqhxDasfSdQ==',
}

response = requests.get(
    'http://msedge.b.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/ce08bfa8-7506-4fb6-99a9-fc68424c1df4',
    params=params,
    headers=headers,
)
print(response.text)
print(response.status_code)  # 206

with open('video.ts', 'wb') as f:
    f.write(response.content)