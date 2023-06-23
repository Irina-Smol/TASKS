create table dataset (name varchar(250) not null, age integer not null, grade varchar(250) not null);

\COPY dataset FROM 'C:\Users\IASmolenskaya\Desktop\Excel3.csv' DELIMITER ‘;’ CSV HEADER;
COPY 5
select * from dataset;
 name  | age | grade
-------+-----+-------
 Ira   |  26 | C
 Raisa |  25 | B
 Vova  |  23 | A
 Misha |  28 | A
 Ashan |  30 | B
(5 ёЄЁюъ)



\h explain

Команда:     EXPLAIN
Описание:    показать план выполнения оператора
Синтаксис:
EXPLAIN [ ( параметр [, ...] ) ] оператор
EXPLAIN [ ANALYZE ] [ VERBOSE ] оператор

где допустимый параметр:

    ANALYZE [ логическое_значение ]
    VERBOSE [ логическое_значение ]
    COSTS [ логическое_значение ]
    SETTINGS [ логическое_значение ]
    BUFFERS [ логическое_значение ]
    WAL [ логическое_значение ]
    TIMING [ логическое_значение ]
    SUMMARY [ логическое_значение ]
    FORMAT { TEXT | XML | JSON | YAML }

URL: https://www.postgresql.org/docs/15/sql-explain.html

EXPLAIN select * from aircrafts;

                        QUERY PLAN
----------------------------------------------------------
 Seq Scan on aircrafts  (cost=0.00..1.09 rows=9 width=52)
(1 строка)
