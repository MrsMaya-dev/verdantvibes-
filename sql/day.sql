-- create database practice;
-- use practice;
-- CREATE TABLE employees (
--     emp_id INT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     dept_id INT,
--     salary INT
-- );
-- INSERT INTO employees VALUES
-- (1, 'Amit', 101, 30000),
-- (2, 'Neha', 102, 40000),
-- (3, 'Rahul', 101, 35000),
-- (4, 'Pooja', 103, 45000),
-- (5, 'Ankit', NULL, 28000);

-- CREATE TABLE departments (
--     dept_id INT PRIMARY KEY,
--     dept_name VARCHAR(50),
--     location VARCHAR(50)
-- );
-- INSERT INTO departments VALUES
-- (101, 'HR', 'Delhi'),
-- (102, 'IT', 'Bangalore'),
-- (104, 'Finance', 'Mumbai');
-- select*from employees

-- SELECT e.emp_name, d.dept_name
-- FROM employees e
-- LEFT JOIN departments d
-- ON e.dept_id = d.dept_id;

-- SELECT e.emp_name, d.dept_name
-- FROM employees e
-- RIGHT JOIN departments d
-- ON e.dept_id = d.dept_id;

-- SELECT e.emp_name, e.dept_id, d.dept_name
-- FROM employees e
-- LEFT JOIN departments d
-- ON e.dept_id = d.dept_id
-- UNION
-- SELECT e.emp_name, e.dept_id, d.dept_name
-- FROM employees e
-- RIGHT JOIN departments d
-- ON e.dept_id = d.dept_id;

-- SELECT e.emp_name, d.dept_name
-- FROM employees e
-- JOIN departments d
-- ON e.dept_id = d.dept_id;

-- use practice;









