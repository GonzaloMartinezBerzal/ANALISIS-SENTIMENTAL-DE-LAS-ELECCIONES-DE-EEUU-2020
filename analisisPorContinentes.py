# -- coding: utf-8 --
import sys
import pandas as pd
import numpy as np
from textblob import TextBlob
from pandarallel import pandarallel

#ARGUMENTO 1= CSV A USAR(biden,trump,both, ARGUMENTO 2 = n_workers(tantos como cores), ARGUMENTO 3 = progressbar(True-False)

#from translate import Translator
#CONTINENTS: Africa, Asia, Europe, North America
	#South America, Antarctica, Oceania

nworkers =int(sys.argv[2])

if sys.argv[3].lower() == 'true':
    pb = True
else:
    pb = False

pandarallel.initialize(progress_bar=pb,nb_workers = nworkers)


#translator = Translator(to_lang="en")
def myfunc(x, y, z):
    try:
        #tradu=translator.translate(x)
        blob=TextBlob(x)     
        return blob.sentiment.polarity + 1
    except Exception:
        return 1
        

def apply_myfunc_to_DF(df): return df.parallel_apply((lambda row: myfunc(*row)), axis=1)
def pandas_apply(df): return apply_myfunc_to_DF(df)

if str(sys.argv[1]).lower()=='trump' or str(sys.argv[1]).lower()=='both':
	dataTrump=pd.read_csv('trump.csv',lineterminator='\n')
	dataTrump=dataTrump[['tweet','country','continent']]
	dataTrump=dataTrump.dropna(subset=['country','continent'])
	dataTrump=dataTrump.sort_values(by='continent')
	africa=dataTrump[dataTrump["continent"]=="Africa"]
	asia=dataTrump[dataTrump["continent"]=="Asia"]
	europe=dataTrump[dataTrump["continent"]=="Europe"]
	na=dataTrump[dataTrump["continent"]=="North America"]
	sa=dataTrump[dataTrump["continent"]=="South America"]
	oceania=dataTrump[dataTrump["continent"]=="Oceania"]

	#Africa Trump
	africaSent = pandas_apply(africa)
	sumaSerie=africaSent.sum()
	TrumpPonderacionAfrica = sumaSerie/africaSent.count()
	print("Trump's weighting in Africa is " )
	print(TrumpPonderacionAfrica)

	#Asia Trump
	asiaSent = pandas_apply(asia)
	sumaSerie=asiaSent.sum()
	TrumpPonderacionAsia = sumaSerie/asiaSent.count()
	print("Trump's weighting in Asia is " )
	print(TrumpPonderacionAsia)

	#Europe Trump
	
	europeSent = pandas_apply(europe)
	sumaSerie=europeSent.sum()
	TrumpPonderacionEurope = sumaSerie/europeSent.count()
	print("Trump's weighting in Europe is " )
	print(TrumpPonderacionEurope)

	#North America Trump

	naSent = pandas_apply(na)
	sumaSerie=naSent.sum()
	TrumpPonderacionNA = sumaSerie/naSent.count()
	print("Trump's weighting in North_America is " )
	print(TrumpPonderacionNA)

	#South America Trump
	saSent = pandas_apply(sa)
	sumaSerie=saSent.sum()
	TrumpPonderacionSA = sumaSerie/saSent.count()
	print("Trump's weighting in South America is " )
	print(TrumpPonderacionSA)

	#Oceania Trump

	oceaniaSent = pandas_apply(oceania)
	sumaSerie=oceaniaSent.sum()
	TrumpPonderacionOceania = sumaSerie/oceaniaSent.count()
	print("Trump's weighting in Oceania is " )
	print(TrumpPonderacionOceania)
    
if str(sys.argv[1]).lower()=='biden' or str(sys.argv[1]).lower()=='both':
	dataBiden=pd.read_csv('biden.csv',lineterminator='\n')
	dataBiden=dataBiden[['tweet','country','continent']]
	dataBiden=dataBiden.dropna(subset=['country','continent'])
	dataBiden=dataBiden.sort_values(by='continent')
	africaB=dataBiden[dataBiden["continent"]=="Africa"]
	asiaB=dataBiden[dataBiden["continent"]=="Asia"]
	europeB=dataBiden[dataBiden["continent"]=="Europe"]
	naB=dataBiden[dataBiden["continent"]=="North America"]
	saB=dataBiden[dataBiden["continent"]=="South America"]
	oceaniaB=dataBiden[dataBiden["continent"]=="Oceania"]


	#Africa Biden


	africaSent = pandas_apply(africaB)
	sumaSerie=africaSent.sum()
	BidenPonderacionAfrica = sumaSerie/africaSent.count()
	print("Biden's weighting in Africa is ")
	print(BidenPonderacionAfrica)


	#Asia Biden


	asiaSent = pandas_apply(asiaB)
	sumaSerie=asiaSent.sum()
	BidenPonderacionAsia = sumaSerie/asiaSent.count()
	print("Biden's weighting in Asia is ")
	print(BidenPonderacionAsia)


	#Europe Biden


	europeSent = pandas_apply(europeB)
	sumaSerie=europeSent.sum()
	BidenPonderacionEurope = sumaSerie/europeSent.count()
	print("Biden's weighting in Europa is " )
	print(BidenPonderacionEurope)


	#North America Biden


	naSent = pandas_apply(naB)
	sumaSerie=naSent.sum()
	BidenPonderacionNA = sumaSerie/naSent.count()
	print("Biden's weighting in North America is ")
	print(BidenPonderacionNA)


	#South America Biden


	saSent = pandas_apply(saB)
	sumaSerie=saSent.sum()
	BidenPonderacionSA = sumaSerie/saSent.count()
	print("Biden's weighting in South America is " )
	print(BidenPonderacionSA)


	#Oceania Biden


	oceaniaSent = pandas_apply(oceaniaB)
	sumaSerie=oceaniaSent.sum()
	BidenPonderacionOceania = sumaSerie/oceaniaSent.count()
	print("Biden's weighting in Oceania is ")
	print(BidenPonderacionOceania)








#Comparison Africa
if str(sys.argv[1]).lower() == 'both':
	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("Africa prefers Joe Biden")
	else: print("Africa prefers Donald Trump")

	#Comparison Asia
	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("Asia prefers Joe Biden")
	else: print("Asia prefers Donald Trump")

	#Comparison Europe

	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("Europe prefers Joe Biden")
	else: print("Europe prefers Donald Trump")

	#Comparison North America

	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("North America prefers Joe Biden")
	else: print("North America prefers Donald Trump")

	#Comparison South America

	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("South America prefers Joe Biden")
	else: print("South America prefers Donald Trump")

	#Comparison Oceania

	if TrumpPonderacionAfrica < BidenPonderacionAfrica:
		print("Oceania prefers Joe Biden")
	else: print("Oceania prefers Donald Trump")

