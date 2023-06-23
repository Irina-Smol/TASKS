 create table dataset (name varchar(250) not null, age integer not null, grade varchar(250) not null);

 \COPY dataset FROM 'C:\Users\IASmolenskaya\Desktop\Excel3.csv' DELIMITER ‘;’ CSV HEADER;
COPY 5
postgres=# select * from dataset;
 name  | age | grade
-------+-----+-------
 Ira   |  26 | C
 Raisa |  25 | B
 Vova  |  23 | A
 Misha |  28 | A
 Ashan |  30 | B
(5 ёЄЁюъ)


postgres=#

