from datetime import date
import yfinance as yf
import pickle
d = date.today().strftime("%d%b%y")
for i in ["VIXY","SPXL"]:
    s = yf.Ticker(i)
    pickle.dump(s, open(i.lower()+'.'+d+'.p','wb'))
