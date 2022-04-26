import os
import time

import pymongo

from helpers import crunchbase_db


def all_investors() -> list:
    mongo_results = crunchbase_db.find()
    # print(mongo_results.insert_one({"_id": "VARUN"}).inserted_id)
    results = []
    for result in mongo_results:
        # print(result)
        results.append(result)
    return results


def text_search(body) -> list:
    start = time.time()
    text = body["text"]
    mongo_results = crunchbase_db.aggregate([{
        '$search': {
            'index': 'searchIndex',
            'text': {
                'query': f'{text}',
                'path': {
                    'wildcard': '*'
                }
            }
        }
    }])
    results = []
    for result in mongo_results:
        result.pop("search_terms")
        results.append(result)
    # results = list(mongo_results)
    # print(time.time() - start)
    return results


def get_company_info(company: str):
    return crunchbase_db.find_one({"name": company})
