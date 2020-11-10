SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT(
      'max(case when T_date = ''',
      T_date,
      ''' then day20_slp_ema20 else 0 end) AS ',
      T_date  
    )
  ) INTO @sql
FROM v_slp_ema20_01;


SET @sql = CONCAT('SELECT symbol, ', @sql, ', sum(day20_slp_ema20) as `count`
                  FROM v_slp_ema20_01 
                  GROUP BY symbol');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

