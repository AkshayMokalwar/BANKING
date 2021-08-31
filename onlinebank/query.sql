use dbstudent ;
create table tbl_customer(ID int not null auto_increment, 
firstname varchar(15),lastname varchar(15),birthdate date,address varchar(25),
pincode int ,city varchar(10),primary key(ID));

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Akshay','Mokalwar',"2000-09-07",'Nandanwan',440009,'Nagpur');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Mohan','Gawarle',"1982-04-21",'Wathoda',490012,'Nashik');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Sanskruti','Rane',"2002-06-08",'Sadar',440009,'Nagpur');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Badal','Banait',"1990-12-26",'Lokmanya Nagar',410019,'Amaravati');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Prashant','Kale',"1986-02-18",'Ganesh Peth',390019,'Pune');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Indrajit','Kukade',"2001-05-28",'Dharam Peth',420019,'Amaravati');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Harshal','Chichghare',"2004-02-18",'Ganesh Peth',390021,'Pune');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Gaurav','Yelker',"1985-10-30",'Babul Peth',490025,'Nashik');


insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Mohit','Nindeker',"2001-06-18",'Ganesh Peth',390019,'Pune');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Google','Pandey',"1998-07-04",'Chandan Nagar',480059,'Nashik');

insert into tbl_customer (firstname,lastname,birthdate,address,pincode,city) 
values('Facebook','Sharma',"2004-02-04",'Ghokuldham',480059,'Amaravati');



-- Q1) print the detail of customer born after 01 jan 20000 from table tbl_customer
select * from tbl_customer where birthdate >"2000-01-01";

-- Q2)print the detail  of customer and calculate age and name column as "AGE" from table tbl_customer
select * ,year(current_date())-year(birthdate) as age from tbl_customer;

-- Q3) print the detail of customer born before 01 jan 2000 from table tbl_customer
select * from tbl_customer where birthdate <"2000-01-01";

-- Q4)print the detail  of customer and "AGE"  from table tbl_customer whoose Age is greater than 21
select * ,year(current_date())-year(birthdate) as age from tbl_customer
 where (year(current_date())-year(birthdate) )>21;

-- Q5) print the detail of customer born After 01 jan 1990 and 
-- before 01 jan 2002  from table tbl_customer
select * from tbl_customer where birthdate >="1990-01-01" and birthdate<="2002-01-01";

-- Q6) print the unique cities from table tbl_customer
select distinct city from tbl_customer ;

-- Q7) print the unique cities and total number of custmer from each unique 
-- city from table tbl_customer
select count(*) as 'No. Customer' ,city city from tbl_customer  group by city;

-- Q8) print the detail of customer in ascending order firstname  who lives in same city 
select * from tbl_customer order by city , firstname;

-- Q9) print the detail of customer in descending order of their firstname  who lives in same city 
select * from tbl_customer order by city , firstname desc;

-- Q10)print the detail of customer in  ascending by their pincode
select * from tbl_customer order by pincode;

-- Q11)print total unique pincode in ascending by their pincode with same city
select * from tbl_customer order by city ,pincode ;