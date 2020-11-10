import csv
import mysql.connector
import sys

try:
    v_Td_date = sys.argv[1]
except IndexError:
    print("**The Scrpt: " ,sys.argv[0])
    print("**    usage: python "+sys.argv[0]+ " YYYY-MM-DD")
    print("**    For level 1 :slope 1.0 count 7 file")
    print(" ")
    sys.exit() 
         
mydb = mysql.connector.connect(host='127.0.0.1',user='stocks',password='Welcome123',port='3307',database='lei')
mycursor = mydb.cursor()

fname = 'slp10_7_'+ v_Td_date +'.csv'
print('Input file:'+ fname)
Fulname = '/Users/jchang/stockfetcher/slope/data/' + fname

v_slp_lvl = 0
if fname.startswith('slp15_13'):
   v_slp_lvl = 3
if fname.startswith('slp10_13'):
   v_slp_lvl = 2
if fname.startswith('slp10_7'):
   v_slp_lvl = 1
if (v_slp_lvl == 0 ):
   sys.exit('File not found')

#v_Td_date =(fname.split('_')[2]).split('.')[0]
print( "Slope level: {0:5d}".format(v_slp_lvl))

with open(Fulname, 'r') as csvfile:
    dataframe = csv.DictReader(csvfile )
    print(dataframe)

    for row in dataframe:
        v_symbol = row['Symbol']
        v_close = float(row['Last'])
        v_d_chg_pct = float(row['Chg(%)'])
        v_vol = int(row['Vol'])
        v_ema7 = float(row['ema7'])
        v_ema12 = float(row['ema12'])
        v_ema20 = float(row['ema20'])
        v_ema60 = float(row['ema60'])
        v_ema120 = float(row['ema120'])
        v_ema144 = float(row['ema144'])
        v_ema169 = float(row['ema169'])
        v_ma20 = float(row['ma20'])
        v_ma60 = float(row['ma60'])
        v_ma120 = float(row['ma120'])
        v_no_slp_12 = int(row['slopeema12'])
        v_no_slp_20 = int(row['slopeema20'])
        v_day20_slp_ema12 = float(row['d20_slp_of_ema12'])
        v_day20_slp_ema20 = float(row['d20_slp_of_ema20'])
      
        data_query01 = (v_symbol, v_Td_date, v_slp_lvl, v_close, v_d_chg_pct, v_vol,v_ema7,v_ema12,v_ema20,v_ema60,v_ema120,v_ema144,v_ema169,
                        v_ma20,v_ma60,v_ma120,v_no_slp_12,v_no_slp_20,v_day20_slp_ema12,v_day20_slp_ema20,'') 
        query01 = ("INSERT INTO slope01 ( symbol, Td_date, slp_lvl, close, d_chg_pct, vol," 
 	            "ema7, ema12, ema20, ema60, ema120, ema144, ema169, ma20, ma60, ma120, " 
 	            "no_slp_12, no_slp_20, day20_slp_ema12, day20_slp_ema20, memo) " 
                    "VALUES( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)" ) 
        ## for Debug purpose
        ##data_query02 = (v_symbol, v_Td_date, v_slp_lvl, v_close, v_no_slp_12, '')
        ##query02 = ("INSERT INTO slope01 ( symbol, Td_date, slp_lvl, close, no_slp_12, memo)" 
        ##           "VALUES( %s, %s, %s, %s, %s, %s) " )  

        print(data_query01)
        mycursor.execute(query01, data_query01) 

mycursor.close()
mydb.commit()
mydb.close()
