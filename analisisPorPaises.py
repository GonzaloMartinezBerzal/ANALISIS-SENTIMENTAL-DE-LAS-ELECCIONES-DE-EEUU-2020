#-*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
from textblob import TextBlob
from pandarallel import pandarallel

#ARGUMENTO 1 = country_code, n_workers(tantos como cores), ARGUMENTO 2 = progressbar(True-False)

if (len(sys.argv) != 4):
	sys.exit("Usage: " + sys.argv[0] + "<country_code> <n_workers> <progressBar>")

nworkers =int(sys.argv[2])
pb = True if sys.argv[3].lower() == 'true' else False

pandarallel.initialize(progress_bar=pb,nb_workers = nworkers)

# We store the code and name of every country
countries = {'ABW':'Aruba','AFG':'Afghanistan','AGO':'Angola','AIA':'Anguilla','ALA':'Åland Islands','ALB':'Albania','AND':'Andorra','ARE':'United Arab Emirates','ARG':'Argentina',
'ARM':'Armenia','ASM':'American Samoa','ATA':'Antarctica','ATF':'French Southern Territories','ATG':'Antigua and Barbuda','AUS':'Australia','AUT':'Austria','AZE':'Azerbaijan',
'BDI':'Burundi','BEL':'Belgium','BEN':'Benin','BES':'Bonaire, Sint Eustatius and Saba','BFA':'Burkina Faso','BGD':'Bangladesh','BGR':'Bulgaria','BHR':'Bahrain','BHS':'Bahamas',
'BIH':'Bosnia and Herzegovina','BLM':'Saint Barthélemy','BLR':'Belarus','BLZ':'Belize','BMU':'Bermuda','BOL':'Bolivia','BRA':'Brazil','BRB':'Barbados','BRN':'Brunei Darussalam',
'BTN':'Bhutan','BVT':'Bouvet Island','BWA':'Botswana','CAF':'Central African Republic','CAN':'Canada','CCK':'Cocos (Keeling) Islands','CHE':'Switzerland','CHL':'Chile','CHN':'China',
'CIV':'''Côte d'Ivoire''','CMR':'Cameroon','COD':'Democratic Republic of the Congo','COG':'Congo','COK':'Cook Islands','COL':'Colombia','COM':'Comoros','CPV':'Cabo Verde',
'CRI':'Costa Rica','CUB':'Cuba','CUW':'Curaçao','CXR':'Christmas Island','CYM':'Cayman Islands','CYP':'Cyprus','CZE':'Czechia','DEU':'Germany','DJI':'Djibouti','DMA':'Dominica',
'DNK':'Denmark','DOM':'Dominican Republic','DZA':'Algeria','ECU':'Ecuador','EGY':'Egypt','ERI':'Eritrea','ESH':'Western Sahara','ESP':'Spain','EST':'Estonia','ETH':'Ethiopia',
'FIN':'Finland','FJI':'Fiji','FLK':'Falkland Islands','FRA':'France','FRO':'Faroe Islands','FSM':'Federated States of Micronesia','GAB':'Gabon','GBR': 'United Kingdom', 'GEO':'Georgia',
'GGY':'Guernsey','GHA':'Ghana','GIB':'Gibraltar','GIN':'Guinea','GLP':'Guadeloupe','GMB':'Gambia','GNB':'Guinea-Bissau','GNQ':'Equatorial Guinea','GRC':'Greece','GRD':'Grenada',
'GRL':'Greenland','GTM':'Guatemala','GUF':'French Guiana','GUM':'Guam','GUY':'Guyana','HKG':'Hong Kong','HMD':'Heard Island and McDonald Islands','HND':'Honduras','HRV':'Croatia',
'HTI':'Haiti','HUN':'Hungary','IDN':'Indonesia','IMN':'Isle of Man','IND':'India','IOT':'British Indian Ocean Territory','IRL':'Ireland','IRN':'Iran','IRQ':'Iraq','ISL':'Iceland',
'ISR':'Israel','ITA':'Italy','JAM':'Jamaica','JEY':'Jersey','JOR':'Jordan','JPN':'Japan','KAZ':'Kazakhstan','KEN':'Kenya','KGZ':'Kyrgyzstan','KHM':'Cambodia','KIR':'Kiribati',
'KNA':'Saint Kitts and Nevis','KOR': 'South Korea', 'KWT':'Kuwait','LAO':'''Lao People's Democratic Republic''', 'LBN':'Lebanon', 'LBR':'Liberia', 'LBY':'Libya','LCA':'Saint Lucia',
'LIE':'Liechtenstein','LKA':'Sri Lanka','LSO':'Lesotho','LTU':'Lithuania','LUX':'Luxembourg','LVA':'Latvia','MAC':'Macao','MAF':'Saint Martin','MAR':'Morocco','MCO':'Monaco',
'MDA':'Moldova','MDG':'Madagascar','MDV':'Maldives','MEX':'Mexico','MHL':'Marshall Islands','MKD':'Macedonia','MLI':'Mali','MLT':'Malta','MMR':'Myanmar','MNE':'Montenegro',
'MNG':'Mongolia','MNP':'Northern Mariana Islands','MOZ':'Mozambique','MRT':'Mauritania','MSR':'Montserrat','MTQ':'Martinique','MUS':'Mauritius','MWI':'Malawi','MYS':'Malaysia',
'MYT':'Mayotte','NAM':'Namibia','NCL':'New Caledonia','NER':'Niger','NFK':'Norfolk Island','NGA':'Nigeria','NIC':'Nicaragua','NIU':'Niue','NLD':'Netherlands','NOR':'Norway',
'NPL':'Nepal','NRU':'Nauru','NZL':'New Zealand','OMN':'Oman','PAK':'Pakistan','PAN':'Panama','PCN':'Pitcairn','PER':'Peru','PHL':'Philippines','PLW':'Palau','PNG':'Papua New Guinea',
'POL':'Poland','PRI':'Puerto Rico', 'PRK':'North Korea','PRT':'Portugal','PRY':'Paraguay','PSE':'Palestine','PYF':'French Polynesia','QAT':'Qatar','REU':'Réunion','ROU':'Romania',
'RUS':'Russian Federation','RWA':'Rwanda','SAU':'Saudi Arabia','SDN':'Sudan','SEN':'Senegal','SGP':'Singapore','SGS':'South Georgia and the South Sandwich Islands',
'SHN':'Saint Helena, Ascension and Tristan da Cunha','SJM':'Svalbard and Jan Mayen','SLB':'Solomon Islands','SLE':'Sierra Leone','SLV':'El Salvador','SMR':'San Marino',
'SOM':'Somalia','SPM':'Saint Pierre and Miquelon','SRB':'Serbia','SSD':'South Sudan','STP':'Sao Tome and Principe','SUR':'Suriname','SVK':'Slovakia','SVN':'Slovenia',
'SWE':'Sweden','SWZ':'Eswatini','SXM':'Sint Maarten (Dutch part)','SYC':'Seychelles','SYR':'Syrian Arab Republic','TCA':'Turks and Caicos Islands','TCD':'Chad','TGO':'Togo',
'THA':'Thailand','TJK':'Tajikistan','TKL':'Tokelau','TKM':'Turkmenistan','TLS':'Timor-Leste','TON':'Tonga','TTO':'Trinidad and Tobago','TUN':'Tunisia','TUR':'Turkey',
'TUV':'Tuvalu','TWN':'Taiwan','TZA':'Tanzania','UGA':'Uganda','UKR':'Ukraine','UMI':'United States Minor Outlying Islands','URY':'Uruguay','USA':'United States','UZB':'Uzbekistan',
'VAT':'Holy See','VCT':'Saint Vincent and the Grenadines','VEN':'Venezuela','VGB':'Virgin Islands (British)','VIR':'Virgin Islands (U.S.)','VNM':'Viet Nam','VUT':'Vanuatu',
'WLF':'Wallis and Futuna','WSM':'Samoa','YEM':'Yemen','ZAF':'South Africa','ZMB':'Zambia','ZWE':'Zimbabwe'}

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
	data=data[['tweet','country']]
	data=data.dropna(subset=['country'])
	return data

def tweetEstimation(df):
	result = pandas_apply(df)
	sumaSerie=result.sum()
	return sumaSerie/result.count()

def tweetProcess(country):
	trumpCountry=dataTrump[dataTrump["country"]==country]
	bidenCountry=dataBiden[dataBiden["country"]==country]

	TrumpPonderacionState = 0
	if not trumpCountry.empty:
		TrumpPonderacionState = tweetEstimation(trumpCountry)

	BidenPonderacionState = 0
	if not bidenCountry.empty:
		BidenPonderacionState = tweetEstimation(bidenCountry)
	
	if (TrumpPonderacionState == 0 and BidenPonderacionState == 0) or (TrumpPonderacionState == BidenPonderacionState): # There are countries where perhaps there are no tweets regarding neither of the candidates
		return "None"
	else:
		if TrumpPonderacionState > BidenPonderacionState:
			print("Trump (" + str(TrumpPonderacionState) + ") has a higher polarity in " + country + " than Biden (" + str(BidenPonderacionState) + ")")
			return "Trump"
		else:
			print("Biden (" + str(BidenPonderacionState) + ") has a higher polarity in " + country + " than Trump (" + str(TrumpPonderacionState) + ")")
			return "Biden"

dataTrump = loadDataframe("Trump")
dataBiden = loadDataframe("Biden")

country = countries.get(sys.argv[1].upper())
trumpCountries = 0
bidenCountries = 0

if sys.argv[1].upper() != "ALL":
	tweetProcess(country)
else:
	country_list = countries.values()
	for x in country_list:
		winner = tweetProcess(x)
		if winner == "Trump":
			trumpCountries = trumpCountries + 1
		elif winner == "Biden":
			bidenCountries = bidenCountries + 1
	print("Trump has a higher polarity in " + str(trumpCountries) + " countries")
	print("Biden has a higher polarity in " + str(bidenCountries) + " countries")