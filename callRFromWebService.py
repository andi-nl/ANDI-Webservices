#import rpy2
from flask import Flask
from flask import request
import json 
from numpy import *
#from rpy2.robjects.numpy2ri import numpy2ri
import scipy as sp
from pandas import *
import pickle
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
#from rpy2.robjects.packages import importr
#import rpy2.robjects as ro
#import rpy2.rinterface as rinterface
#import pandas.rpy.common as com
#from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
import subprocess
import sys
#from rpy2.robjects import pandas2ri
#pandas2ri.activate()


app = Flask(__name__)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
def run_script():
    ro.r('x=c()')
    ro.r('x[1]=22')
    ro.r('x[2]=44')
    s = str(ro.r['x'])
    return s

@app.route('/demoTestScores',methods=['GET','POST'])
def api_demoTestScores():
    if request.headers['Content-Type']=='application/json':
        return "JSON Object: " + json.dumps(request.json)


"""
@app.route('/formTestScores',methods=['GET','POST'])
def api_formTestScores():
    if request.headers['Content-Type']=='application/json':
        #jsonlite=importr('jsonlite')
        myPyJSON= request.data
        ro.r('myJSON <- fromJSON({})'.format(repr(myPyJSON)))
        ro.r('source("/home/anandgavai/ANDI/flask/functionforandi.R")')
        t = json.dumps(ro.r('myFunc({})'.format(repr(myPyJSON))))
        #return ro.r('whichtestindexes')
        print t
        return t
"""

@app.route('/formTestScores',methods=['GET','POST','OPTIONS'])
@crossdomain(origin='*',headers='Content-type')
def api_formTestScores():
    #if request.headers['Content-Type']=='application/json':
        #jsonlite=importr('jsonlite')
	print "-->"+request.data+"<--"
        myPyJSON=request.data
        #print myPyJSON
        p = subprocess.Popen(["Rscript", "functionforandi.R"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        t = p.communicate(myPyJSON)
        #print t
        return t


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
