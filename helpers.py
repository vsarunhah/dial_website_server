import os

import pymongo

db = pymongo.MongoClient(os.getenv("CONN"))["company_organizations"]
crunchbase_db = db["crunchbase"]