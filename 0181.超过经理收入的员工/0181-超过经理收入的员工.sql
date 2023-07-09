# Write your MySQL query statement below
select ee.name as Employee
from Employee as ee
where ee.salary > (select mg.salary from Employee as mg where mg.id = ee.managerId)