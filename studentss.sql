use python_db;
create table studentss(
STUDENTID   integer auto_increment primary key ,
NAM  varchar(50),
AGE   integer,
CITY  varchar(50),
MARKS  integer
);

select * from studentss;

insert into studentss(NAM, AGE, CITY, MARKS) values('Ram', 23 ,'Selam' , 499);