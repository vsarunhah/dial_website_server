import json
import os

import pymongo
import requests

# To run this file:
# Go to https://www.crunchbase.com/search/funding_rounds/field/organizations/num_investments/y-combinator?pageId=2_a_1f35a896-5a38-4598-a10f-f415a6fb028a
# Open up developer tools (inspect element) and go to network. In network, look for the funding_rounds? request
# Copy as curl, copy into Postman and get the Python headers. Basically you just want the headers from the request.
# Copy it into the headers variable.
# Profit until it breaks
# Repeat this until you get everything you want


db = pymongo.MongoClient(os.getenv("CONN"))[
    "company_organizations"]
crunchbase_db = db["crunchbase"]


# Gets the uuids that haven't been scraped yet
def get_uuids(crunchbase_db=crunchbase_db):
    all_ids = []
    uuids = crunchbase_db.find(filter={}, projection={"_id": 1})
    for uuid in uuids:
        if os.path.exists(f"investees/{uuid['_id']}_0.json"):
            continue
        else:
            all_ids.append(uuid["_id"])
    return all_ids


# Gets the investees of all the companies that haven't been scraped yet. Redoes the last one in case
# we missed any investees.
def get_investees():
    for uuid in get_uuids():
        url = "https://www.crunchbase.com/v4/data/searches/funding_rounds?source=drill_in_other"
        json_payload = {
            "field_ids": [
                "identifier",
                "funded_organization_identifier",
                "investment_type",
                "money_raised",
                "announced_on",
                "funded_organization_description",
                "funded_organization_website",
            ],
            "order": [],
            "query": [
                {
                    "type": "sub_query",
                    "collection_id": "principal.participated_in.reverse",
                    "query": [
                        {
                            "type": "predicate",
                            "field_id": "identifier",
                            "operator_id": "includes",
                            "include_nulls": False,
                            "values": [
                                uuid
                            ]
                        }
                    ]
                }
            ],
            "field_aggregators": [],
            "collection_id": "funding_rounds",
            "limit": 1000
        }
        payload = json.dumps(json_payload)
        headers = {
            'authority': 'www.crunchbase.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': 'cid=CihuYmI4upVgbwAvzJOaAg==; _pxvid=3630474a-a93f-11ec-b380-716b63595454; _ga=GA1.2.806936003.1649138604; drift_aid=40fd4e45-ffd2-4ba0-843e-7c3717cc347b; driftt_aid=40fd4e45-ffd2-4ba0-843e-7c3717cc347b; _gcl_au=1.1.762873709.1649382509; _biz_uid=c3b8409ab1d64986aeb20b368f0b4414; _mkto_trk=id:976-JJA-800&token:_mch-crunchbase.com-1649382509218-72492; __qca=P0-1504926169-1649382509287; _hjSessionUser_977177=eyJpZCI6ImRiZjJjODg1LTg3MDQtNWM3OS05N2E2LWU3YjJkNGFiOTRhZSIsImNyZWF0ZWQiOjE2NDkzODI1MDkwOTgsImV4aXN0aW5nIjp0cnVlfQ==; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Mkto%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _gid=GA1.2.1899221148.1649810243; _gaexp=GAX1.2.z8yW7HaCQS2rbajfgJdtPg.19180.1!mFKegBbiQaO6B1xO3qUNGw.19180.0; _gcl_aw=GCL.1649880728.CjwKCAjw6dmSBhBkEiwA_W-EoNTCOtSTcP4k7A4nItws8gFxSVvJPCXICzL4HHtONulqwaQwJ3xHehoCDm0QAvD_BwE; _biz_nA=18; _gac_UA-60854465-1=1.1649880728.CjwKCAjw6dmSBhBkEiwA_W-EoNTCOtSTcP4k7A4nItws8gFxSVvJPCXICzL4HHtONulqwaQwJ3xHehoCDm0QAvD_BwE; _biz_pendingA=%5B%5D; _hp2_id.973801186=%7B%22userId%22%3A%22460197339759958%22%2C%22pageviewId%22%3A%228780544367371541%22%2C%22sessionId%22%3A%228339027358649265%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __cflb=02DiuJLCopmWEhtqNz5aroddpPeSHCJLvdFBY2h7MDXsS; xsrf_token=5hMld/6JjE0O668Zg3GbQOLyLWXEeEbp6NXSAY7LkGM=; pxcts=cd949773-bb82-11ec-b3e6-676876695051; drift_eid=3dfaba2d-6c61-492e-ad0a-b019476811f7; drift_campaign_refresh=e83ff071-1b1e-425c-a69a-eaedebcbe159; _pxff_bsco=1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Apr+14+2022+00%3A01%3A38+GMT-0400+(Eastern+Daylight+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=a3a47f9b-fb78-471f-842a-73f0134c8d1e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CSPD_BG%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIwYWI1ZGE3OC1lM2Y4LTQ2NGQtODY2Yi0wZjhlMWVjMGFmM2MiLCJpc3MiOiJ1c2Vyc2VydmljZV82ODFiNDMxNV82MDQiLCJzdWIiOiIzZGZhYmEyZC02YzYxLTQ5MmUtYWQwYS1iMDE5NDc2ODExZjciLCJleHAiOjE2NDk5MDkyMDIsImlhdCI6MTY0OTkwODkwMiwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVDOWJKK2RtN2RlY252TG1DRFRjQVZkU3RFeDh2d2t0YjlqVzVQMXI4U1VwM01oVGtWV0swUkRzQmdTcVI0WG9ZOFpxRzY4RlZLYUJIQ2hNWGZSMjlBcHN2SFJCaW5ncnhjLzlvVFdRZjhJVFIzV2dNektLM3l1WlpGNWpSZ0RRUjNSNGxpenE1c1lvSGRmelNvWjVvUnQxZ2tNYXpMZDdVSkRhTHIwdDFJTVpzSnUzV0FHbmxKN29CUUZYdDk2UjhHdXhld3dLUlh0WHBrUjNIN3J5NmFuazA3aVpoV2tCdERKelBVazZWRDZBYk1aMlcxSlZndHpvcVFDci9KOGJJZXBqSXRGY3ZSMFZ6K29UbFFKNHZIMnFTQzRpbmVjYnZjNTBtTVpSZURFUlVPdWk3WWE1eDNPWWxqd05GSTdVNVNLL2srMFRsaytGMm9HZm1ETFdqSVJYTlo2amFLd09GckFQMUVFOEJWTHRoTXUvcms0SXVISGhwSTUzY3AzVlhvS25PdElmRU5GbG5wUnVUUGxnTllHd2hRN21HUnJqblYydDV5WmFOWGEzWXhUMUo0bmRyeGErdGROT0xMaXI4Nm1GdWtNYWJGNDN1N2hVdVRFY2lzUzA0NDBXRXEyZGtiVUdGWGVnQ1NqakFvTDE1QnZBdjJHQUNkL0JSbTVNSHdvRzVBaWFhdmE1RUsyUWJXazY3ZzZpbUt5cVFTRXJ2R3lFcW9Fa3ZvamJhREdkRy9MTVN3MjRwbkxXcUc5K1RSc3Roank0dXhoYjQza1hlZmNOak94QndXOGVXQXI5UnZjVEk4RzFuVWh0MWM4VS9LdStIOTJveWdRZU1Eb0lzczlOMWZRWlBHcWxoc3BuQlIwbld5TUZFNmRYWWFVYjdrRFVBRk9NUTRCalRkZUhLSStHaGRDYlJUa2c2TFZTSDdBYlpDM0RIVHFEdGFCUGQzSkY5SFRGd2ozc2dBaTZ4K014aW5OTlU3c1l5RzVTUDRTcWJFWXZIOWtEajNnTmp2SmlKNVdGbFBnRlE5ejlyU055OXltRDlVZVBwWS9DbW1mZjRHUUxUYnlHVHRwNnU3eWFmKzBsMGpwR2VqckhKQzJDY21qcmNSZGJ1UWxNUXc4d3BpdlJ0L1dyQVY3RXBBSzZJeVF3NDZ0TWFqa2w0UUwrV0hXTktxU1R0alVEUlRadjJDZWJjbkFzR2pjUVM4MUhHRjBWZFRNcFMxRk1jcXBaNTBSbjdDNTBOby9jZW0yYTl1dk5MRDJScVo1dFRuUDQ2aXQ0b1p2Ny81Zy9tTkVVZEEwN01rVjNRVkdQL09JTjRKdVE5VC9lZTZwQ0ZJZ0p1RmNCTFYvbjIvQ1EyREc2ZmZHeDZPV3dtZTZEMHp2amRadlQ5OTh5NXNMQzN2N3VYZ3FMMldvZEhyWjhHYXoxdHhIRlVPQ0dLalllRE14V2NoQ2Nvbk5DOXpzeVFrdGxKMHFqQkUzVUI5aXlyMit0cHpqOHZ6MkdFTFNkQTlPWFZoTUlEZHFDd2YvZDkiLCJwdWJsaWMiOnsic2Vzc2lvbl9oYXNoIjoiMzY2MTczOTgyIn19.Y6oTWJclyiOaPO3sZi1DXTMhsZORMDb4dOf6S_VfuOocJqx9vz05WMBvC5XvdrUBU5hq-1yDuLjcuyiWn6C3RA; _pxhd=IRfi-gTA89/zjD60CCyOt5ojxknwXPQTKqCUboJR6buorEa4jGSJwy9JZRXciSgabNpuFKVspgFV2k7wBFE/pg; _pxhd=ymflp/QDG1m-7KYj2LuVpAaaPNjonKD9d3Gub00z2ARvvLpJSDJkiK5VatZk2H1CrJMy971E22QZaIroGjpOqQ; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI2ZGI4OWUyMC05OTU2LTQ3MWQtOGEyZS01YWQ1MGYzYTY0YzkiLCJpc3MiOiJ1c2Vyc2VydmljZV8wYzMzYWVkMV82MDQiLCJzdWIiOiIzZGZhYmEyZC02YzYxLTQ5MmUtYWQwYS1iMDE5NDc2ODExZjciLCJleHAiOjE2NDk4MTAwOTMsImlhdCI6MTY0OTgwOTc5MywicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVDOWJKK2RtN2RlY252TG1DRFRjQVZkU3RFeDh2d2t0YjlqVzVQMXI4U1VwM01oVGtWV0swUkRzQmdTcVI0WG9ZOFpxRzY4RlZLYUJIQ2hNWGZSMjlBcHN2SFJCaW5ncnhjLzlvVFdRZjhJVFIzV2dNektLM3l1WlpGNWpSZ0RRUjNSNGxpenE1c1lvSGRmelNvWjVvUnQxZ2tNYXpMZDdVSkRhTHIwdDFJTVpzSnUzV0FHbmxKN29CUUZYdDk2UjhHdXhld3dLUlh0WHBrUjNIN3J5NmFuazA3aVpoV2tCdERKelBVazZWRDZBYk1aMlcxSlZndHpvcVFDci9KOGJJZXBqSXRGY3ZSMFZ6K29UbFFKNHZIMnFTQzRpbmVjYnZjNTBtTVpSZURFUlVPdWk3WWE1eDNPWWxqd05GSTdVNVNLL2srMFRsaytGMm9HZm1ETFdqSVJYTlo2amFLd09GckFQMUVFOEJWTHRoTXUvcms0SXVISGhwSTUzY3AzVlhvS25PdElmRU5GbG5wUnVUUGxnTllHd2hRN21HUnJqblYydDV5WmFOWGEzWXhUMUo0bmRyeGErdGROT0xMaXI4Nm1GdWtNYWJGNDN1N2hVdVRFY2lzUzA0NDBXRXEyZGtiVUdGWGVnQ1NqakFvTDE1QnZBdjJHQUNkL0JSbTVNSHdvRzVBaWFhdmE1RUsyUWJXazY3ZzZpbUt5cVFTRXJ2R3lFcW9Fa3ZvamJhREdkRy9MTVN3MjRwbkxXcUc5K1RSc3Roank0dXhoYjQza1hlZmNOak94QndXOGVXQXI5UnZjVEk4RzFuVWh0MWM4VS9LdStIOTJveWdRZU1Eb0lzczlOMWZRWlBHcWxoc3BuQlIwbld5TUZFNmRYWWFVYjdrRFVBRk9NUTRCalRkZUhLSStHaGRDYlJUa2c2TFZTSDdBYlpDM0RIVHFEdGFCUGQzSkY5SFRGd2ozc2dBaTZ4K014aW5OTlU3c1l5RzVTUDRTcWJFWXZIOWtEajNnTmp2SmlKNVdGbFBnRlE5ejlyU055OXltRDlVZVBwWS9DbW1mZjRHUUxUYnlHVHRwNnU3eWFmKzBsMGpwR2VqckhKQzJDY21qcmNSZGJ1UWxNUXc4d3BpdlJ0L1dyQVY3RXBBSzZJeVF3NDZ0TWFqa2w0UUwrV0hXTktxU1R0alVEUlRadjJDZWJjbkFzR2pjUVM4MUhHRjBWZFRNcFMxRk1jcXBaNTBSbjdDNTBOby9jZW0yYTl1dk5MRDJScVo1dFRuUDQ2aXQ0b1p2Ny81Zy9tTkVVZEEwN01rVjNRVkdQL09JTjRKdVE5VC9lZTZwQ0ZJZ0p1RmNCTFYvbjIvQ1EyREc2ZmZHeDZPV3dtZTZEMHp2amRadlQ5OTh5NXNMQzN2N3VYZ3FMMldvZEhyWjhHYXoxdHhIRlVPQ0dLalllRE14V2NoQ2Nvbk5DOXpzeVFrdGxKMHFqQkUzVUI5aXlyMit0cHpqOHZ6MkdFTFNkQTlPWFZoTUlEZHFDd2YvZDkiLCJwdWJsaWMiOnsic2Vzc2lvbl9oYXNoIjoiMzY2MTczOTgyIn19.bhqjrQ25j-GT5DqxXO_Bg0xwN3mq1Wz_OBq7MAWuk340lDI1fBdBoUMyVJKm0z1-3j6d7rVGykT8WhcMCRsv3g',
            'dnt': '1',
            'origin': 'https://www.crunchbase.com',
            'pragma': 'no-cache',
            'referer': 'https://www.crunchbase.com/search/funding_rounds/field/organizations/num_investments/y-combinator',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': '5hMld/6JjE0O668Zg3GbQOLyLWXEeEbp6NXSAY7LkGM='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_resp = response.json()
        # print(json_resp)
        entities = json_resp["entities"]
        with open(f"investees/{uuid}_0.json", "w+") as f:  # write the first 1000 results
            f.write(json.dumps(json_resp))
        counter = 1000
        while len(entities) > 0:
            after_id = entities[-1]["uuid"]
            json_payload["after_id"] = after_id  # get the next 1000 results
            payload = json.dumps(json_payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            json_resp = response.json()
            entities = json_resp["entities"]  # update entities
            if len(entities) > 0:
                with open(f"investees/{uuid}_{counter}.json", "w+") as f:  # write the new data
                    f.write(json.dumps(json_resp))
            counter += 1000


# Counts the number of investment rounds collected till now
def count_rounds():
    directory = input("Enter folder name: ")
    total_count = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if ".json" in f and os.path.isfile(f):
            with open(f, "r+") as file:
                total_count += json.load(file)["count"]
    return total_count


# get_investees()
# print(len(get_uuids()))
if __name__ == "__main__":
    print(count_rounds())