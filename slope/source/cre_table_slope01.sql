
CREATE TABLE `slope01` (
  `symbol` char(8) DEFAULT NULL,
  `Td_date` date DEFAULT NULL,
  `slp_lvl` int(11) DEFAULT NULL COMMENT '3: ema20,12 slp 1.5 cnt13, 2: ema20,12 slp1.0 cnt13, 1: ema20,12 slp10 cnt7 ',
  `close` decimal(10,2) DEFAULT NULL,
  `d_chg_pct` decimal(10,2) DEFAULT NULL,
  `vol` decimal(10,2) DEFAULT NULL,
  `ema7` decimal(10,2) DEFAULT NULL,
  `ema12` decimal(10,2) DEFAULT NULL,
  `ema20` decimal(10,2) DEFAULT NULL,
  `ema60` decimal(10,2) DEFAULT NULL,
  `ema120` decimal(10,2) DEFAULT NULL,
  `ema144` decimal(10,2) DEFAULT NULL,
  `ema169` decimal(10,2) DEFAULT NULL,
  `ma20` decimal(10,2) DEFAULT NULL,
  `ma60` decimal(10,2) DEFAULT NULL,
  `ma120` decimal(10,2) DEFAULT NULL,
  `no_slp_12` int(11) DEFAULT NULL,
  `no_slp_20` int(11) DEFAULT NULL,
  `day20_slp_ema12` decimal(10,2) DEFAULT NULL,
  `day20_slp_ema20` decimal(10,2) DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

alter table slope01 add primary key (symbol,Td_date) ;
