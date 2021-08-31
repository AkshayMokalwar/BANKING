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
