SELECT * FROM myTable 
-- Selects all fields from table specified

SELECT UName, Age, DOB FROM myTable 
WHERE UName = 'John' OR UName = 'William' 
-- Selects records from the 3 fields specified in myTable
-- if the records have a matching name specified in the where block

SELECT UName, Age, DOB FROM myTable 
WHERE UName = 'John' OR UName = 'William' 
ORDER BY ASC -- (Or DESC)
-- Selects records from the 3 fields specified in myTable
-- if the records have a matching name specified in the where block,
-- but put it in ascending/descending order

