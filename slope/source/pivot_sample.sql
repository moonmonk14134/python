CREATE TABLE yourtable
	(`Name` varchar(4), `kode` varchar(5), `jum` int)
;
	
INSERT INTO yourtable
	(`Name`, `kode`, `jum`)
VALUES
	('aman', 'kode1', 2),
	('aman', 'kode2', 1),
	('jhon', 'kode1', 4),
	('amir', 'kode2', 4)
;



SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT(
      'max(case when kode = ''',
      kode,
      ''' then jum else 0 end) AS ',
      kode
    )
  ) INTO @sql
FROM yourtable;


SET @sql = CONCAT('SELECT name, ', @sql, ', sum(jum) as `count`
                  FROM yourtable 
                  GROUP BY name');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

