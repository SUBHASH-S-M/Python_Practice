use assigmnet;


create table occupations (name varchar(30), occupation varchar(50));

insert into occupations values ('Samantha', 'Doctor');  

insert into occupations values ('Julia', 'Actor');

insert into occupations values ('Maria', 'Actor');

insert into occupations values ('Meera', 'Singer');

insert into occupations values ('Ashley', 'Professor');

insert into occupations values ('Ketty', 'Professor');

insert into occupations values ('Christeen', 'Professor');

insert into occupations values ('Jane', 'Actor');

insert into occupations values ('Jenny', 'Doctor');

insert into occupations values ('Priya', 'Singer');


create temporary table temp as (select row_number() over(partition by occupation) rnk,
case when occupation='Actor' then name end as Actor,
case when occupation='Doctor' then name end as Doctor,
case when occupation='Professor' then name end as Professor,
case when occupation='Singer' then name end as Singer
 from occupations);
 
 select rnk,max(Actor),max(Professor),max(Singer),max(Doctor) from temp
 group by rnk;
 
 drop table assignment_1;
 Create table assignment_1(ID varchar(10) ,DATE varchar(20));
 
 insert into assignment_1 values(
"A1","20-APR-1985"),	
("A2","20-APR-1985"),	
("A1","25-APR-1985"),
("A3","25-MAY-1985"),
("A1","30-APR-1985"),
("A2","05-MAY-1985");



select ID,DATE AS START_DATE,lead(DATE) over(partition by ID) AS END_DATE From assignment_1;

use assigmnet;
truncate table  unpivot;
create table unpivot( id varchar(10));
insert into unpivot values(1),("ABC"),(1000),("SALES"),(2),("XYZ"),(2000),("PROD");

set @countv=round((select count(*) from unpivot)/4);
select @countv;
select min(ID) as ID,min(Name) as ENAME,min(Occu) as SAL,min(post) as DEPT from
(select grp,row_number() over() as rn,case when rnum=1 then id end as ID,
case when rnum=2 then id end as Name,case when rnum=3 then id end as Occu,
case when rnum=4 then id end as post
from(select id,grp,row_number() over(partition by grp) as rnum 
from(select id,ntile(2) over() as grp from unpivot) t1)t2)t3
group by grp;

create database prac;
use prac;
create table employee
( emp_ID int primary key
, emp_NAME varchar(50) not null
, DEPT_NAME varchar(50)
, SALARY int);

insert into employee values(101, 'Mohan', 'Admin', 4000);
insert into employee values(102, 'Rajkumar', 'HR', 3000);
insert into employee values(103, 'Akbar', 'IT', 4000);
insert into employee values(104, 'Dorvin', 'Finance', 6500);
insert into employee values(105, 'Rohit', 'HR', 3000);
insert into employee values(106, 'Rajesh',  'Finance', 5000);
insert into employee values(107, 'Preet', 'HR', 7000);
insert into employee values(108, 'Maryam', 'Admin', 4000);
insert into employee values(109, 'Sanjay', 'IT', 6500);
insert into employee values(110, 'Vasudha', 'IT', 7000);
insert into employee values(111, 'Melinda', 'IT', 8000);
insert into employee values(112, 'Komal', 'IT', 10000);
insert into employee values(113, 'Gautham', 'Admin', 2000);
insert into employee values(114, 'Manisha', 'HR', 3000);
insert into employee values(115, 'Chandni', 'IT', 4500);
insert into employee values(116, 'Satya', 'Finance', 6500);
insert into employee values(117, 'Adarsh', 'HR', 3500);
insert into employee values(118, 'Tejaswi', 'Finance', 5500);
insert into employee values(119, 'Cory', 'HR', 8000);
insert into employee values(120, 'Monica', 'Admin', 5000);
insert into employee values(121, 'Rosalin', 'IT', 6000);
insert into employee values(122, 'Ibrahim', 'IT', 8000);
insert into employee values(123, 'Vikram', 'IT', 8000);
insert into employee values(124, 'Dheeraj', 'IT', 11000);

select * from employee;


select x.*
from employee e
join (select *,
max(salary) over (partition by dept_name) as max_salary,
min(salary) over (partition by dept_name) as min_salary
from employee) x
on e.emp_id = x.emp_id
and (e.salary = x.max_salary or e.salary = x.min_salary)
order by x.dept_name, x.salary;

select min(salary) from employee where dept_name='admin' group by DEPT_NAME;
select * from employee e1
where e1.salary=(select min(e2.salary) from employee e2 where e1.dept_name=e2.dept_name group by e1.dept_name)
union 
select * from employee e1
where e1.salary=(select max(e2.salary) from employee e2 where e1.dept_name=e2.dept_name group by e1.dept_name);



create table login_details(
login_id int primary key,
user_name varchar(50) not null,
login_date date);


insert into login_details values
(101, 'Michael', current_date),
(102, 'James', current_date),
(103, 'Stewart', current_date+1),
(104, 'Stewart', current_date+1),
(105, 'Stewart', current_date+1),
(106, 'Michael', current_date+2),
(107, 'Michael', current_date+2),
(108, 'Stewart', current_date+3),
(109, 'Stewart', current_date+3),
(110, 'James', current_date+4),
(111, 'James', current_date+4),
(112, 'James', current_date+5),
(113, 'James', current_date+6);

select *,lead(login_date) over(partition by user_name order by login_date) as nxt_1,
lead(login_date,2) over(partition by user_name order by login_date) as nxt_2
from login_details;

select distinct user_name from(select *, case when lead(user_name) over() = user_name 
 and lead(user_name,2) over() = user_name 
 then 1 else 0 end ch from login_details) x where ch=1;

drop table students;
create table students
(
id int primary key,
student_name varchar(50) not null
);
insert into students values
(1, 'James'),
(2, 'Michael'),
(3, 'George'),
(4, 'Stewart'),
(5, 'Robin');

select id,student_name,case when id%2=0 then lag(student_name) over() 
else lead(student_name,1,student_name)over()  end as next_name
from students;

create table weather
(
id int,
city varchar(50),
temperature int,
day date
);
truncate table weather;
delete from weather;
insert into weather values
(1, 'London', -1, str_to_date('2021-01-01',"%Y-%m-%d")),
(2, 'London', -2, str_to_date('2021-01-02',"%Y-%m-%d")),
(3, 'London', 4, str_to_date('2021-01-03',"%Y-%m-%d")),
(4, 'London', 1, str_to_date('2021-01-04',"%Y-%m-%d")),
(5, 'London', -2, str_to_date('2021-01-05',"%Y-%m-%d")),
(6, 'London', -5, str_to_date('2021-01-06',"%Y-%m-%d")),
(7, 'London', -7, str_to_date('2021-01-07',"%Y-%m-%d")),
(8, 'London', 5, str_to_date('2021-01-08',"%Y-%m-%d"));

select * from weather;
select id,city,temperature,day from (
select *,case when temperature<0 and lead(temperature) over(order by day) <0 
and lead(temperature,2) over(order by day)<0 then 'Y'
when  temperature<0 and lag(temperature) over(order by day)<0 and lag(temperature,2) over(order by day)<0 then 'Y'
when temperature<0 and lag(temperature) over(order by day)<0 and lead(temperature) over(order by day)<0 then 'Y' end as Status
from weather)temp
where Status='Y';


drop table event_category;
create table event_category
(
  event_name varchar(50),
  category varchar(100)
);

drop table physician_speciality;
create table physician_speciality
(
  physician_id int,
  speciality varchar(50)
);

drop table patient_treatment;
create table patient_treatment
(
  patient_id int,
  event_name varchar(50),
  physician_id int
);


insert into event_category values ('Chemotherapy','Procedure');
insert into event_category values ('Radiation','Procedure');
insert into event_category values ('Immunosuppressants','Prescription');
insert into event_category values ('BTKI','Prescription');
insert into event_category values ('Biopsy','Test');


insert into physician_speciality values (1000,'Radiologist');
insert into physician_speciality values (2000,'Oncologist');
insert into physician_speciality values (3000,'Hermatologist');
insert into physician_speciality values (4000,'Oncologist');
insert into physician_speciality values (5000,'Pathologist');
insert into physician_speciality values (6000,'Oncologist');


insert into patient_treatment values (1,'Radiation', 1000);
insert into patient_treatment values (2,'Chemotherapy', 2000);
insert into patient_treatment values (1,'Biopsy', 1000);
insert into patient_treatment values (3,'Immunosuppressants', 2000);
insert into patient_treatment values (4,'BTKI', 3000);
insert into patient_treatment values (5,'Radiation', 4000);
insert into patient_treatment values (4,'Chemotherapy', 2000);
insert into patient_treatment values (1,'Biopsy', 5000);
insert into patient_treatment values (6,'Chemotherapy', 6000);


select * from patient_treatment;
select * from event_category;
select * from physician_speciality;

select * from patient_treatment e1
where exists(select event_name from event_category ct where ct.event_name=e1.event_name 
and ct.category='Procedure');
create table patient_logs
(
  account_id int,
  date date,
  patient_id int
);

insert into patient_logs values (1, str_to_date('02-01-2020',"%d-%m-%Y"), 100);
insert into patient_logs values (1, str_to_date('27-01-2020',"%d-%m-%Y"), 200);
insert into patient_logs values (2, str_to_date('01-01-2020',"%d-%m-%Y"), 300);
insert into patient_logs values (2, str_to_date('21-01-2020',"%d-%m-%Y"), 400);
insert into patient_logs values (2, str_to_date('21-01-2020',"%d-%m-%Y"), 300);
insert into patient_logs values (2, str_to_date('01-01-2020',"%d-%m-%Y"), 500);
insert into patient_logs values (3, str_to_date('20-01-2020',"%d-%m-%Y"), 400);
insert into patient_logs values (1, str_to_date('04-03-2020',"%d-%m-%Y"), 500);
insert into patient_logs values (3, str_to_date('20-01-2020',"%d-%m-%Y"), 450);


select * from patient_logs;

select account_id,month,count from (select account_id,monthname(date) as month,count(distinct patient_id) as count,
row_number() over(partition by monthname(date),count(distinct patient_id)) as  rnk from patient_logs
group by account_id,monthname(date)
order by 3 desc)t1
where rnk=1;








 