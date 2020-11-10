use lei ;
create view v_slp_ema20_01 as select symbol, concat('D',replace( convert(Td_date,char(12)) ,'-','') ) as T_date, day20_slp_ema20 from slope01 ;
