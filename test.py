import httplib
import json
import os
import pandas as pd
import time
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation
from sklearn.metrics import classification_report
import numpy as np
from sklearn.metrics import accuracy_score
import textblob as TextBlob
from sklearn.utils import resample

os.getcwd()

api_key = "g82m86t7tdzw2mau9qvtud9b"

#category id
opt = "/v1/categories"
query ="?format=json"
c = httplib.HTTPConnection("api.remix.bestbuy.com")
c.request('GET','%s%s&apiKey=%s&show=id,name' %(opt,query,api_key))
r = c.getresponse()
data = r.read()

print data

jdata = json.loads(data)['categories']

#category Id TVs
for d in jdata:
    if dict.values(d)[1] == 'TVs':
        tv_id = dict.values(d)[0]