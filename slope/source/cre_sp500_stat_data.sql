CREATE TABLE sp500_stat_data (
  symbol char(8) DEFAULT NULL,
  Td_date date DEFAULT NULL,
  close decimal(10,2) DEFAULT NULL,
  d_chg_pct decimal(10,2) DEFAULT NULL,
  vol decimal(10,2) DEFAULT NULL,
  ema7 decimal(10,2) DEFAULT NULL,
  ema12 decimal(10,2) DEFAULT NULL,
  ema20 decimal(10,2) DEFAULT NULL,
  ema60 decimal(10,2) DEFAULT NULL,
  ema120 decimal(10,2) DEFAULT NULL,
  ema144 decimal(10,2) DEFAULT NULL,
  ema169 decimal(10,2) DEFAULT NULL,
  ma20 decimal(10,2) DEFAULT NULL,
  ma60 decimal(10,2) DEFAULT NULL,
  ma120 decimal(10,2) DEFAULT NULL,
  no_slp_12 int(11) DEFAULT NULL,
  no_slp_20 int(11) DEFAULT NULL,
  day20_slp_ema12 decimal(10,2) DEFAULT NULL,
  day20_slp_ema20 decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

alter table sp500_stat_data add primary key (Td_date,symbol) ;
alter table sp500_stat_data add column memo varchar(255) ;
alter table sp500_stat_data add column ded20 decimal(10,2) DEFAULT NULL;
alter table sp500_stat_data add column ded60 decimal(10,2) DEFAULT NULL;
alter table sp500_stat_data add column ded120 decimal(10,2) DEFAULT NULL;
