import requests
import json
import os

def reqAs():
    uri = "http://localhost:5000/"
    with open(os.path.join("./data_dir/variable_misuse_datasets","eval.jsontxt-00000-of-00004"),"r") as f:
    #with open(os.path.join("./data_dir/pred_exception_datasets","eval.jsontxt-0"),"r") as f:
        inp = f.readlines()[44]
        js = json.loads(inp)
    code = js["function"]
    reqData = {"source" : code, "otherData" : 42}
    resp = requests.post(uri, json=reqData)
    print(resp)
    resp = resp.json()
    print(resp)



if __name__ == '__main__':
    reqAs()
