import json
import os

import pymongo


db = pymongo.MongoClient(os.getenv("CONN"))
crunchbase_db = db["crunchbase"]


def data_for_one_investor(investor_id: str) -> (list, list, list):
    search_terms = []
    notable_investments = []
    notable_names = set()
    directory = "investees"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if ".json" in f and investor_id in f and os.path.isfile(f):  # if the file is json
            with open(f, "r+") as file:  # open it
                json_data = json.load(file)  # load it as a dictionary
                entities = json_data["entities"]  # get all the entities
                for investing_round in entities:  # loop over all the funding rounds (each entry in entities)
                    info = investing_round["properties"]
                    description = info["funded_organization_description"]  # description of investee
                    search_terms.append(description)
                    if info.get("money_raised"):
                        money_invested = info["money_raised"]["value_usd"]
                    else:
                        money_invested = -1
                    company_name = info["funded_organization_identifier"][
                        "value"]  # build notable investments based on money invested
                    if info.get("funded_organization_website"):
                        company_website = info["funded_organization_website"]["value"]
                    else:
                        company_website = None
                    prior_len = len(notable_names)
                    notable_names.add(company_name)
                    if len(notable_names) != prior_len:
                        notable_investments.append((money_invested, company_name, company_website))
                    else:
                        index = [x for x, y in enumerate(notable_investments) if y[1] == company_name][0]  # index of first occurrence of company (there should only be one)
                        if notable_investments[index][0] < money_invested:
                            notable_investments[index] = (money_invested, company_name, company_website)
    notable_investments = sorted(notable_investments, key=lambda tup: tup[0], reverse=True)
    max_index = 10 if len(notable_investments) > 10 else len(notable_investments)
    notable_investments = notable_investments[:max_index]  # only want top 10 max
    notable_websites = []
    notable_names = []
    for i in range(len(notable_investments)):
        notable_names.append(notable_investments[i][1])
        notable_websites.append(notable_investments[i][2])
    return search_terms, notable_names, notable_websites


def upload_data(investor_id: str, search_terms: list, notable_names: list, notable_website: list):
    crunchbase_db.update_one({"_id": investor_id},
                             {"$set":
                             {"search_terms": search_terms,
                              "notable_website": notable_website,
                              "notable_names": notable_names
                              }
                              }
                             )


def get_uuids() -> list:
    mongo_data = crunchbase_db.find(filter={}, projection={"_id": 1})
    uuids = []
    for _id in mongo_data:
        uuids.append(_id["_id"])
    return uuids


def upload_all_data():
    uuids = get_uuids()
    counter = 0
    for uuid in uuids:
        search_terms, notable_names, notable_website = data_for_one_investor(uuid)
        upload_data(uuid, search_terms, notable_names, notable_website)
        counter += 1
        if counter % 1000 == 0:
            print(counter)


if __name__ == "__main__":
    t = ["Crowdfunding", "Venture"]
    for a in t:
        s = a.lower().replace(" ", "_").replace("-", "_")
        crunchbase_db.update_many({"stage": s}, {"$set": {"fundingType.$": a}})
    s = set()
    f = set()
    for obj in crunchbase_db.find():
        for t in obj["fundingType"]:
            f.add(t)
        for t in obj["stages"]:
            s.add(t)
    print(f)
    print("DONE")
    print(s)
