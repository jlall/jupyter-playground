import sys, re
import requests
import pylab
from pprint import *

def _fetch(ticker, year, month):
	root = 'http://finance.yahoo.com/q/op?s=%s&m=%s-%s'
	uri = root%(ticker, year, month)
	req = requests.get(uri)
	if req.status_code == requests.codes.ok:
		return req.text
	return None

def _clean(nt):
	vals = []
	for t in nt:
		if t[0] == '': vals.append(0.0)
		else: vals.append(float(t[0].replace(",", "")))
	return vals

if __name__ == '__main__':

	# usage: python yahoo-options.py SPY 2014 1
	ticker = sys.argv[1]
	year = sys.argv[2]
	month = sys.argv[3]

	txt = _fetch(ticker, year, month)
	options = re.findall('<tr>(.*)</tr>', txt)[2].split('</tr><tr>')
	pprint(options)
	for o in options:
		strike = re.findall('k=([0-9]*.[0-9]*)', o)
		if len(strike) == 0: continue
		strike = strike[0]
		symbol, option_type = re.findall('>([A-Z0-9]*(C|P)[0-9]*)<', o)[0]
		numbers = _clean(
			re.findall('(?:>([0-9]{1,}(?:[0-9]*|.[0-9]*))|(N/A))<', o))
		lst = numbers[1]
		bid = numbers[3]
		ask = numbers[4]
		print (symbol, option_type, strike, lst, bid, ask)
