create database car_vehicle;

use car_vehicle;
show tables;

select * from vehicle_info;

#1 Show all vehicles that use Diesel fuel.
select * from vehicle_info where fuel ="Diesel";

#2  Display vehicle name, year, and brand for all vehicles.
select name,year,brand from vehicle_info;

#3  Find all sales where selling price is below 5,00,000.
select *from vehicle_sales where selling_price <500000;

#4  Find fuel types where average selling price is greater than 6,00,000.
select i.fuel , avg(s.selling_price) avg_price
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
group by i.fuel
having avg(s.selling_price) > 600000;

#5  Find brands that have more than 50 vehicles listed.
select i.brand , count(*) as total_vehicles
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
group by i.brand
having count(*) > 50;

#6  Show transmission types where the average selling price is greater than 7,00,000 AND 
#the total number of vehicles is at least 30.
select i.transmission, avg(s.selling_price) as avg_price, count(*) as total_vehicels
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
group by i.transmission
having avg(s.selling_price) > 700000 and count(*) >= 30;

#7 Find price categories where the average km driven is above 75,000, 
#but only include categories that have more than 20 vehicles AND only 
#count Diesel vehicles.

select s.price_category, avg(s.km_driven) as avg_km, count(*) as total_vehicle
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
where i.fuel = 'Diesel'
group by s.price_category
having avg(s.km_driven) > 75000 and count(*) >20;

#8 Find vehicles whose selling price is higher than the overall average selling price.

select i.name, s.selling_price
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
where s.selling_price > (select avg(selling_price )from vehicle_sales);

#9  Find brands whose average selling price is greater than the average 
#selling price of Toyota vehicles.

select  i.brand , avg(s.selling_price) as avg_brand_price 
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
group by i.brand
having avg(s.selling_price)>
       (select avg(s.selling_price)
        from vehicle_info i
        join vehicle_sales s
        on i.vehicle_uid = s.vehicle_uid
        where i.brand = 'Toyota');

#10 Find fuel types where total selling price is higher than total selling price of Petrol vehicles.

select i.fuel , sum(s.selling_price) as toatl_sales
from vehicle_info i
join vehicle_sales s
on i.vehicle_uid = s.vehicle_uid
group by i.fuel
having sum(s.selling_price) >
        (select sum(s.selling_price)
         from vehicle_info i
         join vehicle_sales s
         on i.vehicle_uid = s.vehicle_uid
         where i.fuel = 'Petrol');


