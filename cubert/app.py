from flask import Flask
from flask import request, jsonify
import os
import tempfile
import json
import subprocess

app = Flask(__name__)

def _run_exception_analyser(src):
    jsonstr = json.dumps({"function": src, "label":"None"})+"\n"
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        with open(os.path.join(tmpdirname, "eval.jsontxt-0"),"w") as fsrc:
            fsrc.write(jsonstr)
        subprocess.call(["./predict_except.sh", tmpdirname, tmpdirname])
        with open(os.path.join(tmpdirname,"predictions.txt"),"r") as fpred:
            res = fpred.readlines()[0].replace("\n","")
    return res
def _run_varmisuse_analyser(src):
    jsonstr = json.dumps({"function": src, "label":"Correct"})+"\n"
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        with open(os.path.join(tmpdirname, "eval.jsontxt-0"),"w") as fsrc:
            fsrc.write(jsonstr)
        subprocess.call(["./predict_varmisuse.sh", tmpdirname, tmpdirname])
        with open(os.path.join(tmpdirname,"predictions.txt"),"r") as fpred:
            res = fpred.readlines()[0].replace("\n","")
    return res
def _run_swappedop_analyser(src):
    jsonstr = json.dumps({"function": src, "label":"Correct"})+"\n"
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        with open(os.path.join(tmpdirname, "eval.jsontxt-0"),"w") as fsrc:
            fsrc.write(jsonstr)
        subprocess.call(["./predict_swappedop.sh", tmpdirname, tmpdirname])
        with open(os.path.join(tmpdirname,"predictions.txt"),"r") as fpred:
            res = fpred.readlines()[0].replace("\n","")
    return res
def _run_wrongop_analyser(src):
    jsonstr = json.dumps({"function": src, "label":"Correct"})+"\n"
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        with open(os.path.join(tmpdirname, "eval.jsontxt-0"),"w") as fsrc:
            fsrc.write(jsonstr)
        subprocess.call(["./predict_wrongop.sh", tmpdirname, tmpdirname])
        with open(os.path.join(tmpdirname,"predictions.txt"),"r") as fpred:
            res = fpred.readlines()[0].replace("\n","")
    return res


@app.route('/', methods=["POST"])
def hello_world():  # put application's code here
    content = request.get_json(force=True)
    print(content)
    reqsrc = content["source"]

    exception =_run_exception_analyser(reqsrc)
    svar = _run_varmisuse_analyser(reqsrc)
    swappedop = _run_swappedop_analyser(reqsrc)
    wrongop = _run_wrongop_analyser(reqsrc)

    return jsonify(varmisuse=svar, swappedop=swappedop, wrongop=wrongop, exception=exception)


if __name__ == '__main__':
    app.run()


