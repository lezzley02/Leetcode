/* Write your PL/SQL query statement below */
SELECT c.name as customers FROM
customers C LEFT JOIN orders O
ON C.id = O.customerid
WHERE O.id IS NULL