import json
import os

import pymongo
from pymongo.errors import DuplicateKeyError, BulkWriteError

db = pymongo.MongoClient(os.getenv("CONN"))["company_organizations"]
crunchbase_db = db["crunchbase"]
ERROR_FILE = "currData/duplicateKey.txt"
broken_file = open(ERROR_FILE, "w+")
IMAGE_LINK = 'https://res.cloudinary.com/crunchbase-production/image/upload/'
defaultImage = "https://svgshare.com/i/g64.svg"
for i in range(0, 27000, 1000):
    f = open(f"currData/data_{i}.json", "r")
    entities = json.load(f)["entities"]
    counter = 0
    companies = []
    for entity in entities:
        counter += 1
        uuid = entity["uuid"]
        properties = entity["properties"]
        numInvestments = properties["num_investments_funding_rounds"]  # num investments
        name = properties["identifier"]["value"]  # name
        image = properties["identifier"].get("image_id")
        if image is None:
            image = defaultImage
        image = IMAGE_LINK + image  # logo
        description = properties.get("description")  # about
        investorStage = properties.get("investor_stage")  #
        investorType = properties.get("investor_type")  # funding type
        numExits = properties.get("num_exits")  # numExits
        companyInfo = {
            "_id": uuid,
            "numInvestments": numInvestments,
            "name": name,
            "logo": image,
            "about": description,
            "fundingType": investorType,
            "stages": investorStage,
            "numExits": numExits,
        }
        companies.append(companyInfo)
    try:
        crunchbase_db.insert_many(companies)
    except BulkWriteError:
        for company in companies:
            try:
                crunchbase_db.insert_one(company)
            except DuplicateKeyError:
                broken_file.write(company["_id"] + ": " + company["name"])
    print(i)

