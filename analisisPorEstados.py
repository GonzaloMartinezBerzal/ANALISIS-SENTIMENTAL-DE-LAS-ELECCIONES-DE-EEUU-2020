#-*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
from textblob import TextBlob
from pandarallel import pandarallel

#ARGUMENTO 1 = n_workers(tantos como cores), ARGUMENTO 2 = progressbar(True-False)

if (len(sys.argv) != 3):
	sys.exit("Usage: " + sys.argv[0] + " <n_workers> <progressBar>")

nworkers =int(sys.argv[1])
pb = True if sys.argv[2].lower() == 'true' else False

pandarallel.initialize(progress_bar=pb,nb_workers = nworkers)


# We store the name of every state and who won
states = {"Alabama":"Trump", "Alaska":"Trump", "Arizona":"Biden", "Arkansas":"Trump", "California":"Biden", "Colorado":"Biden", "Connecticut":"Biden", "Delaware":"Biden",
"District of Columbia": "Biden", "Florida":"Trump", "Georgia":"Biden", "Hawaii":"Biden", "Idaho":"Trump", "Illinois":"Biden", "Indiana":"Trump", "Iowa":"Trump",
"Kansas":"Trump", "Kentucky":"Trump", "Louisiana":"Trump", "Maine":"Biden", "Maryland":"Biden", "Massachusetts":"Biden", "Michigan":"Biden", "Minnesota":"Biden",
"Mississippi":"Trump", "Missouri":"Trump", "Montana":"Trump", "Nebraska":"Trump","Nevada":"Biden", "New Hampshire":"Biden", "New Jersey":"Biden", "New Mexico":"Biden",
"New York":"Biden", "North Carolina":"Trump", "North Dakota":"Trump", "Ohio":"Trump", "Oklahoma":"Trump", "Oregon":"Biden", "Pennsylvania":"Biden", "Rhode Island":"Biden",
"South Carolina":"Trump", "South Dakota":"Trump", "Tennessee":"Trump", "Texas":"Trump", "Utah":"Trump", "Vermont":"Biden","Virginia":"Biden", "Washington":"Biden",
"West Virginia":"Trump", "Wisconsin":"Biden", "Wyoming":"Trump"}

matches = 0

def myfunc(x, y):
    try:
        blob=TextBlob(x)     
        return blob.sentiment.polarity + 1
    except Exception:
        return 1
        

def apply_myfunc_to_DF(df): return df.parallel_apply((lambda row: myfunc(*row)), axis=1)
def pandas_apply(df): return apply_myfunc_to_DF(df)

def loadDataframe(csv):
	if csv == "Trump":
		data=pd.read_csv('trump.csv',lineterminator='\n')
	else:
		data=pd.read_csv('biden.csv',lineterminator='\n')
	data=data[['tweet','state']]
	data=data.dropna(subset=['state'])
	data=data.sort_values(by='state')
	return data

def tweetEstimation(df):
	result = pandas_apply(df)
	sumaSerie=result.sum()
	return sumaSerie/result.count()

def checkIfMatches(trump, biden):
	preferred = "Trump" if TrumpPonderacionState > BidenPonderacionState else "Biden"
	if preferred == winner:
		print("Tweets prediction matches with the election results in " + stateName)
		return True
	else:
		print("Tweets prediction does not match with the election results in " + stateName)
		return False


dataTrump = loadDataframe("Trump")
dataBiden = loadDataframe("Biden")
for stateName, winner in states.items():
	trumpState=dataTrump[dataTrump["state"]==stateName]
	bidenState=dataBiden[dataBiden["state"]==stateName]

	TrumpPonderacionState = tweetEstimation(trumpState)
	print("Trump's weighting in " + stateName + " is")
	print(TrumpPonderacionState)

	BidenPonderacionState = tweetEstimation(bidenState)
	print("Biden's weighting in " + stateName + " is")
	print(BidenPonderacionState)

	if (checkIfMatches(TrumpPonderacionState, BidenPonderacionState)):
		matches = matches + 1

print("There are " + str(matches) + " matches out of 51, which means an average prediction of " + str(round(((matches/51.0) * 100),3)) + "%")