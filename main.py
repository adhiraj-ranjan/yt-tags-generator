import requests
import re

headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"126.0.6478.127"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'Referer': 'https://www.youtube.com/',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'client': 'youtube',
    'hl': 'en-gb',
    'gl': 'in',
    'sugexp': 'ytwzsh_h,maxz=10,starz.maxq=10,starz.mxs=10,ytpo.mzp=15,cfro=1',
    'gs_rn': '64',
    'gs_ri': 'youtube',
    'tok': '7RtEoPn6gN5h08WP_ZC7mw',
    'ds': 'yt',
    'cp': '8',
    'gs_id': 'v',
    'callback': 'google.sbox.p50',
    'gs_gbg': 'p3LdDizBMfbO',
}

query = input("Enter Query (one word to four words) : ")

params['q'] = query
response = requests.get('https://suggestqueries-clients6.youtube.com/complete/search', params=params, headers=headers)

# print(response.text)
req_tags = re.findall(f'{query}\s?[^"]*', response.text)
print("\n")
print(", ".join(req_tags))