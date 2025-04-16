import requests
import chardet
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
    'https://clearbluesky72.wiki/_v7/c04229b4d9709ff6927306689f15e92d7d6dc41cdf7a9aaef60c1a0dc9abbe5d5d2878ed43af5fefbe9713e711acf3fbf0c71bbb8e7cf15ff1ff92e65306d81ba59f1cb45e4f223698940d0d6e5c86f79276b112fbd59d89ae355b97cc63e183c9917c9850ac82a193920e0c9be84811916f7d0b50dd1e42c0c62c7263a14ef6/seg-131-f2-v1-a1.txt',
    headers=headers,
)
print(response.text)
print(response.status_code)

with open('a1.ts', 'wb') as f:
    f.write(response.content)