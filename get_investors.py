import requests
import json

url = "https://www.crunchbase.com/v4/data/searches/principal.investors?source=slug_advanced_search"
json_payload = {
    "field_ids": [
        "identifier",
        "num_investments_funding_rounds",
        "num_exits",
        "investor_type",
        "investor_stage",
        "categories",
        "rank_principal_investor",
        "description"
    ],
    "order": [
        {
            "field_id": "num_investments_funding_rounds",
            "sort": "desc"
        }
    ],
    "query": [
        {
            "type": "sub_query",
            "collection_id": "funding_round.participated_in.forward",
            "query": [
                {
                    "type": "predicate",
                    "field_id": "funded_organization_categories",
                    "operator_id": "includes",
                    "include_nulls": False,
                    "values": [
                        "6a733ac8-b79c-e2d2-55b9-cc3d66435eb6",
                        "fa736a2c-3108-8e06-9adf-fb7a75744f5b",
                        "ccb73ca1-4648-8df2-22ae-029e3500f4c1",
                        "9ee51d4b-2d79-a32c-479f-668767ad6898",
                        "5330335e-33c9-5613-67d8-cac000930acf",
                        "e303e839-52d3-f2f0-b87d-757ee8b86b48",
                        "9c5dc6d5-70fc-b0b1-106c-42d0326e8a37",
                        "5ecb5545-454b-9dca-6eb3-1ea48692c3c4",
                        "ba32af71-dbca-ceba-814e-5a3947c4ea31",
                        "9f701861-d7ed-8dba-de9b-25c2ce5018cf",
                        "ac057a31-756a-62be-1677-0fee94b6aeca",
                        "8fae7891-8002-aee2-311a-92b253c892d8",
                        "16ad1d6c-c7ee-b6b5-701d-32c79a19dfae",
                        "58842728-7ab9-5bd1-bb67-e8e55f6520a0",
                        "47b7f337-c81c-bb9e-e4d2-08022a0dd60f",
                        "9b58eb8a-89e7-b238-a1eb-5b9766cc4b3a",
                        "e37ada49-ab15-5e46-0a49-f0ce1a3c9128",
                        "4b5272c7-6e2e-cba3-5b37-e35dcb737344",
                        "e611283c-e2f1-4f80-3650-4ced61374404",
                        "ea9c541f-e059-4e9a-4aaa-c445a2a0570b",
                        "d9ee2821-9f88-c0cf-e775-a34db739e9ec",
                        "03ef4ce7-c2ac-aa82-a8f4-d97ab53cd085",
                        "d6c66c61-1af2-b02f-cb28-a1cdae75b125",
                        "e4f60985-e604-9faa-3226-2df779f0d198",
                        "bad7067e-b24d-5c63-a2e9-54a9e059d7cb",
                        "b5cdd7ca-83f5-f44a-ee85-955a43b74d0a",
                        "e5dbd6bd-bc84-dc1d-ebac-595549a4319d",
                        "3d91b7f7-78f6-2c44-e6ea-9a5e3e392f06",
                        "a5194b80-118a-af3e-db95-665fd12f2474",
                        "3343a371-2b37-8490-7f75-9b6545d445c4",
                        "8a3ae13e-ac51-4759-31a5-c578e6c1e31c",
                        "14364faa-63f9-0d45-7b6a-7378113364a2",
                        "62bac433-ee68-7075-c47e-c9efc0d3c0aa",
                        "97e0bac2-7d87-173a-47b3-366f201da451",
                        "1680f5c4-9050-f7bf-0a37-4b929f68bd75",
                        "21b207a5-9f0b-b037-9ee9-d9d9ed7c3fa9",
                        "eca36366-3502-acb7-f7a4-03d35360ddbd",
                        "654b60a6-b105-fc40-2295-88a9a7dab2f5",
                        "5e863b20-28f6-a760-89c7-005249ab4a70",
                        "8e46de21-5561-0114-eacc-cae29ea61767",
                        "51385655-f802-346b-045d-f44f461989fc",
                        "301b97f0-6284-b2f2-6457-848b4e10828d",
                        "6ea20ef4-dd12-8a46-3565-22dab9c8a7d4",
                        "91d07503-1e4b-bec1-6115-6df19b26be3c",
                        "2643338a-b464-bb84-8a4e-2a1f0e8a9958",
                        "cbc36b3c-09fd-1e1f-7ac8-400a546de247",
                        "4acdae6a-217f-be4d-5f3d-6955756b92d5"
                    ]
                }
            ]
        }
    ],
    "field_aggregators": [],
    "collection_id": "principal.investors",
    "limit": 1000
}
payload = json.dumps(json_payload)
headers = {
    'authority': 'www.crunchbase.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'cid=CihuYmI4upVgbwAvzJOaAg==; _pxvid=3630474a-a93f-11ec-b380-716b63595454; _ga=GA1.2.806936003.1649138604; drift_aid=40fd4e45-ffd2-4ba0-843e-7c3717cc347b; driftt_aid=40fd4e45-ffd2-4ba0-843e-7c3717cc347b; xsrf_token=5hMld/6JjE0O668Zg3GbQOLyLWXEeEbp6NXSAY7LkGM; pxcts=b5d4ec52-b6aa-11ec-ac6e-524b4648786b; drift_eid=3dfaba2d-6c61-492e-ad0a-b019476811f7; __cflb=02DiuJLCopmWEhtqNz5aroddpPeSHCJLwWopkweFVnFhv; drift_campaign_refresh=1e07569a-9069-4382-b458-01dfb4a6b708; _gid=GA1.2.1469073197.1649380893; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI2ZGI4OWUyMC05OTU2LTQ3MWQtOGEyZS01YWQ1MGYzYTY0YzkiLCJpc3MiOiJ1c2Vyc2VydmljZV85ZWQ0NjczOF82MDQiLCJzdWIiOiIzZGZhYmEyZC02YzYxLTQ5MmUtYWQwYS1iMDE5NDc2ODExZjciLCJleHAiOjE2NDkzODEyNTYsImlhdCI6MTY0OTM4MDk1NiwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVDOWJKK2RtN2RlY252TG1DRFRjQVZkU3RFeDh2d2t0YjlqVzVQMXI4U1VwM01oVGtWV0swUkRzQmdTcVI0WG9ZOFpxRzY4RlZLYUJIQ2hNWGZSMjlBcHN2SFJCaW5ncnhjLzlvVFdRZjhJVFIzV2dNektLM3l1WlpGNWpSZ0RRUjNSNGxpenE1c1lvSGRmelNvWjVvUnQxZ2tNYXpMZDdVSkRhTHIwdDFJTVpzSnUzV0FHbmxKN29CUUZYdDk2UjhHdXhld3dLUlh0WHBrUjNIN3J5NmFuazA3aVpoV2tCdERKelBVazZWRDZBYk1aMlcxSlZndHpvcVFDci9KOGJJZXBqSXRGY3ZSMFZ6K29UbFFKNHZIMnFTQzRpbmVjYnZjNTBtTVpSZURFUlVPdWk3WWE1eDNPWWxqd05GSTdVNVNLL2srMFRsaytGMm9HZm1ETFdqSVJYTlo2amFLd09GckFQMUVFOEJWTHRoTXUvcms0SXVISGhwSTUzY3AzVlhvS25PdElmRU5GbG5wUnVUUGxnTllHd2hRN21HUnJqblYydDV5WmFOWGEzWXhUMUo0bmRyeGErdGROT0xMaXI4Nm1GdWtNYWJGNDN1N2hVdVRFY2lzUzA0NDBXRXEyZGtiVUdGWGVnQ1NqakFvTDE1QnZBdjJHQUNkL0JSbTVNSHdvRzVBaWFhdmE1RUsyUWJXazY3ZzZpbUt5cVFTRXJ2R3lFcW9Fa3ZvamJhREdkRy9MTVN3MjRwbkxXcUc5K1RSc3Roank0dXhoYjQza1hlZmNOak94QndXOGVXQXI5UnZjVEk4RzFuVWh0MWM4VS9LdStIOTJveWdRZU1Eb0lzczlOMWZRWlBHcWxoc3BuQlIwbld5TUZFNmRYWWFVYjdrRFVBRk9NUTRCalRkZUhLSStHaGRDYlJUa2c2TFZTSDdBYlpDM0RIVHFEdGFCUGQzSkY5SFRGd2ozc2dBaTZ4K014aW5OTlU3c1l5RzVTUDRTcWJFWXZIOWtEajNnTmp2SmlKNVdGbFBnRlE5ejlyU055OXltRDlVZVBwWS9DbW1mZjRHUUxUYnlHVHRwNnU3eWFmKzBsMGpwR2VqckhKQzJDY21qcmNSZGJ1UWxNUXc4d3BpdlJ0L1dyQVY3RXBBSzZJeVF3NDZ0TWFqa2w0UUwrV0hXTktxU1R0alVEUlRadjJDZWJjbkFzR2pjUVM4MUhHRjBWZFRNcFMxRk1jcXBaNTBSbjdDNTBOby9jZW0yYTl1dk5MRDJScVo1dFRuUDQ2aXQ0b1p2Ny81Zy9tTkVVZEEwN01rVjNRVkdQL09JTjRKdVE5VC9lZTZwQ0ZJZ0p1RmNCTFYvbjIvQ1EyREc2ZmZHeDZPV3dtZTZEMHp2amRadlQ5OTh5NXNMQzN2N3VYZ3FMMldvZEhyWjhHYXoxdHhIRlVPQ0dLalllRE14V2NoQ2Nvbk5DOXpzeVFrdGxKMHFqQkUzVUI5aXlyMit0cHpqOHZ6MkdFTFNkQTlPWFZoTUlEZHFDd2YvZDkiLCJwdWJsaWMiOnsic2Vzc2lvbl9oYXNoIjoiMzY2MTczOTgyIn19.d7SNG9Us0MmAEzMpAh2iTdnp6i8QhMxxsBc9VEY2AKBtLeBlQwhKLs8-xcAP07zeWcuaIxpmxXKYRDJ_kU22dw; _pxhd=73tKSKAYr4aHikJxbiQc0/ggCwJWGysE-B5RpLmSvw/7mmTl6oWi9T-uqiGTzvBcpNKDjin8z239KJfWeN2HgA; _px3=21afea1ba4021134baf08269d25ab8afd5455b68a7f347052b7223d6de34aa55:2OKHcYRlfNzES+blAIi6YVH4zQ8YZuCYnM/h4hPFn81C9SgPbSga1TdobM98X3ps3tKgeEwjfu/B76Yc9Qq5sw==:1000:Jb+xGvEQ8g7e91jJ958XFoWJSJfWDbtnZRcANaWXwW0pLtTd5AdUdYp5deF0y5ryjI0OxESBH7/151U5aFGnWJ4xA/sBzLHLKPYnak2mUT19W7x3QoX3aICthACHGB4vfpAOsSpK24mxdxlw7EFk7uvuqD4NdcR7GGztNOaS6o0LI2WCP+xpsDr/RUV1qMe/QKY38WxopbD4iWDjUT5zIw==; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Apr+07+2022+21%3A22%3A38+GMT-0400+(Eastern+Daylight+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=a3a47f9b-fb78-471f-842a-73f0134c8d1e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CSPD_BG%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false; _pxhd=o-KBiJaN3NoOnzyMK-q4jvsqMr65o8uuI3mAogQrSdJwu43Id8ra0VoFgS2hqY0vwJ81mRSnuyqRk04Tl2eXRQ; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI2ZGI4OWUyMC05OTU2LTQ3MWQtOGEyZS01YWQ1MGYzYTY0YzkiLCJpc3MiOiJ1c2Vyc2VydmljZV85ZWQ0NjczOF82MDQiLCJzdWIiOiIzZGZhYmEyZC02YzYxLTQ5MmUtYWQwYS1iMDE5NDc2ODExZjciLCJleHAiOjE2NDkzODE5MzIsImlhdCI6MTY0OTM4MTYzMiwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVDOWJKK2RtN2RlY252TG1DRFRjQVZkU3RFeDh2d2t0YjlqVzVQMXI4U1VwM01oVGtWV0swUkRzQmdTcVI0WG9ZOFpxRzY4RlZLYUJIQ2hNWGZSMjlBcHN2SFJCaW5ncnhjLzlvVFdRZjhJVFIzV2dNektLM3l1WlpGNWpSZ0RRUjNSNGxpenE1c1lvSGRmelNvWjVvUnQxZ2tNYXpMZDdVSkRhTHIwdDFJTVpzSnUzV0FHbmxKN29CUUZYdDk2UjhHdXhld3dLUlh0WHBrUjNIN3J5NmFuazA3aVpoV2tCdERKelBVazZWRDZBYk1aMlcxSlZndHpvcVFDci9KOGJJZXBqSXRGY3ZSMFZ6K29UbFFKNHZIMnFTQzRpbmVjYnZjNTBtTVpSZURFUlVPdWk3WWE1eDNPWWxqd05GSTdVNVNLL2srMFRsaytGMm9HZm1ETFdqSVJYTlo2amFLd09GckFQMUVFOEJWTHRoTXUvcms0SXVISGhwSTUzY3AzVlhvS25PdElmRU5GbG5wUnVUUGxnTllHd2hRN21HUnJqblYydDV5WmFOWGEzWXhUMUo0bmRyeGErdGROT0xMaXI4Nm1GdWtNYWJGNDN1N2hVdVRFY2lzUzA0NDBXRXEyZGtiVUdGWGVnQ1NqakFvTDE1QnZBdjJHQUNkL0JSbTVNSHdvRzVBaWFhdmE1RUsyUWJXazY3ZzZpbUt5cVFTRXJ2R3lFcW9Fa3ZvamJhREdkRy9MTVN3MjRwbkxXcUc5K1RSc3Roank0dXhoYjQza1hlZmNOak94QndXOGVXQXI5UnZjVEk4RzFuVWh0MWM4VS9LdStIOTJveWdRZU1Eb0lzczlOMWZRWlBHcWxoc3BuQlIwbld5TUZFNmRYWWFVYjdrRFVBRk9NUTRCalRkZUhLSStHaGRDYlJUa2c2TFZTSDdBYlpDM0RIVHFEdGFCUGQzSkY5SFRGd2ozc2dBaTZ4K014aW5OTlU3c1l5RzVTUDRTcWJFWXZIOWtEajNnTmp2SmlKNVdGbFBnRlE5ejlyU055OXltRDlVZVBwWS9DbW1mZjRHUUxUYnlHVHRwNnU3eWFmKzBsMGpwR2VqckhKQzJDY21qcmNSZGJ1UWxNUXc4d3BpdlJ0L1dyQVY3RXBBSzZJeVF3NDZ0TWFqa2w0UUwrV0hXTktxU1R0alVEUlRadjJDZWJjbkFzR2pjUVM4MUhHRjBWZFRNcFMxRk1jcXBaNTBSbjdDNTBOby9jZW0yYTl1dk5MRDJScVo1dFRuUDQ2aXQ0b1p2Ny81Zy9tTkVVZEEwN01rVjNRVkdQL09JTjRKdVE5VC9lZTZwQ0ZJZ0p1RmNCTFYvbjIvQ1EyREc2ZmZHeDZPV3dtZTZEMHp2amRadlQ5OTh5NXNMQzN2N3VYZ3FMMldvZEhyWjhHYXoxdHhIRlVPQ0dLalllRE14V2NoQ2Nvbk5DOXpzeVFrdGxKMHFqQkUzVUI5aXlyMit0cHpqOHZ6MkdFTFNkQTlPWFZoTUlEZHFDd2YvZDkiLCJwdWJsaWMiOnsic2Vzc2lvbl9oYXNoIjoiMzY2MTczOTgyIn19.yb9iV2IVacxRgIbRbexh7trNQ2YbvkBYxeokbwnc1uS35ToxcrtwxUkFUcVurs1WoVdiPedQSmfWF-5sqSdnVw',
    'dnt': '1',
    'origin': 'https://www.crunchbase.com',
    'pragma': 'no-cache',
    'referer': 'https://www.crunchbase.com/discover/principal.investors/746013c4b25ef8cb8860665102902dc3?pageId=2_a_26bcf130-4aa8-a3b3-3571-1b8f13143370',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': '5hMld/6JjE0O668Zg3GbQOLyLWXEeEbp6NXSAY7LkGM'
}
counter = 0
ids = set()
while counter <= 26800:
    response = requests.request("POST", url, headers=headers, data=payload)
    file = open(f"data_{counter}.json", "w")
    file.write(response.text)
    json_payload["after_id"] = json.loads(response.text)["entities"][-1]["uuid"]
    payload = json.dumps(json_payload)
    print(len(json.loads(response.text)["entities"]))
    for entit in json.loads(response.text)["entities"]:
        ids.add(entit["uuid"])
    counter += 1000
    print(counter)
print(len(ids))
