import csv
import mysql.connector
import sys
import os
import pathlib


def arch_files(patfile):
  p = pathlib.Path(__file__)
  ppath = p.absolute().parent
  pppath = str(ppath)
  mv_spath = pppath +  "/../data/"
  mv_dpath = pppath +  "/../arch/"
  cmd_mv = "mv "+ mv_spath + patfile +" "+ mv_dpath
  os.system(cmd_mv)
  print(cmd_mv)


def load_sp500_stats(fnamepreL): 
  for Fulname in fnamepreL:
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
            v_ded20 = float(row['ded20'])
            v_ded60 = float(row['ded60'])
            v_ded120 = float(row['ded120'])
      
            data_query01 = (v_symbol, v_Td_date, v_close, v_d_chg_pct, v_vol,v_ema7,v_ema12,v_ema20,v_ema60,v_ema120,v_ema144,v_ema169,
                        v_ma20,v_ma60,v_ma120,v_no_slp_12,v_no_slp_20,v_day20_slp_ema12,v_day20_slp_ema20,v_ded20,v_ded60,v_ded120,'' ) 
            query01 = ("INSERT INTO sp500_stat_data ( symbol, Td_date, close, d_chg_pct, vol," 
 	            "ema7, ema12, ema20, ema60, ema120, ema144, ema169, ma20, ma60, ma120, " 
 	            "no_slp_12, no_slp_20, day20_slp_ema12, day20_slp_ema20, ded20, ded60, ded120) " 
                    "VALUES( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
                    "ON DUPLICATE KEY UPDATE sp500_stat_data.memo = %s" ) 
            ## for Debug purpose
            ##data_query02 = (v_symbol, v_Td_date, v_slp_lvl, v_close, v_no_slp_12, '')
            ##query02 = ("INSERT INTO slope01 ( symbol, Td_date, slp_lvl, close, no_slp_12, memo)" 
            ##           "VALUES( %s, %s, %s, %s, %s, %s) " )  

            print(data_query01)
            mycursor.execute(query01, data_query01) 
  
  return 'load_sp500_stats completed '


def load_target_stats(fnamepreL): 
  for Fulname in fnamepreL:
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
            v_ded20 = float(row['ded20'])
            v_ded60 = float(row['ded60'])
            v_ded120 = float(row['ded120'])
      
            data_query01 = (v_symbol, v_Td_date, v_close, v_d_chg_pct, v_vol,v_ema7,v_ema12,v_ema20,v_ema60,v_ema120,v_ema144,v_ema169,
                        v_ma20,v_ma60,v_ma120,v_no_slp_12,v_no_slp_20,v_day20_slp_ema12,v_day20_slp_ema20,v_ded20,v_ded60,v_ded120, '' ) 
            query01 = ("INSERT INTO target01_stat_data ( symbol, Td_date, close, d_chg_pct, vol," 
 	            "ema7, ema12, ema20, ema60, ema120, ema144, ema169, ma20, ma60, ma120, " 
 	            "no_slp_12, no_slp_20, day20_slp_ema12, day20_slp_ema20, ded20, ded60, ded120) " 
                    "VALUES( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
                    "ON DUPLICATE KEY UPDATE target01_stat_data.memo = %s" ) 
            ## for Debug purpose
            ##data_query02 = (v_symbol, v_Td_date, v_slp_lvl, v_close, v_no_slp_12, '')
            ##query02 = ("INSERT INTO slope01 ( symbol, Td_date, slp_lvl, close, no_slp_12, memo)" 
            ##           "VALUES( %s, %s, %s, %s, %s, %s) " )  

            print(data_query01)
            mycursor.execute(query01, data_query01) 
  
  return 'load_target_stats completed '

def main():
    global v_Td_date,mydb, mycursor
    try:
        v_Td_date = sys.argv[1]
    except IndexError:
        print("**The Scrpt: " ,sys.argv[0])
        print("**    usage: python "+sys.argv[0]+ " YYYY-MM-DD")
        print(" ")
        sys.exit() 
         
    mydb = mysql.connector.connect(host='127.0.0.1',user='stocks',password='Welcome123',port='3307',database='lei')
    mycursor = mydb.cursor()

    f_pattern01 = 'sp500_stat_data*'+ v_Td_date +'.csv'
    f_pattern02 = 'target01_stat_data*'+ v_Td_date +'.csv'
    path = pathlib.Path('/Users/jchang/stockfetcher/slope/data/')
    filesL1 = path.rglob(f_pattern01)
    filesL2 = path.rglob(f_pattern02)

    load_sp500_stats(filesL1) 
    load_target_stats(filesL2) 

    mycursor.close()
    mydb.commit()
    mydb.close()

    arch_files(f_pattern01)
    arch_files(f_pattern02)

if __name__ == "__main__" :
    main()
