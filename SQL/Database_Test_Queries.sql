-- TC-SQL-001
-- Verify that patient records exist in the database.
-- Expected Result: Patient records are returned.
-- Actual Result: Patient record for Jordan Smith was returned successfully.
-- Status: PASS

SELECT *
FROM patients;



-- TC-SQL-002
-- Verify patient can be retrieved by Patient ID.

SELECT *
FROM patients
WHERE id = 1;



-- TC-SQL-003
-- Verify patient can be retrieved by first name.
-- Test Data: Jordan
-- Expected Result: Jordan Smith's patient record is returned.
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE first_name = 'Jordan';




-- TC-SQL-004
-- Verify patient can be retrieved using first and last name.
-- Test Data: Jordan Smith
-- Expected Result: Jordan Smith's patient record is returned.
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE first_name = 'Jordan'
AND last_name = 'Smith';




-- TC-SQL-005
-- Verify required patient fields do not contain NULL values.
-- Fields Tested: first_name, last_name, date_of_birth, phone, email
-- Expected Result: Zero records are returned.
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE first_name IS NULL
   OR last_name IS NULL
   OR date_of_birth IS NULL
   OR phone IS NULL
   OR email IS NULL;




   -- TC-SQL-006
-- Verify there are no duplicate Patient IDs.
-- Expected Result: Zero records are returned.
-- A Patient ID should uniquely identify one patient.
-- Status: PASS after execution and verification.

SELECT id, COUNT(*)
FROM patients
GROUP BY id
HAVING COUNT(*) > 1;



-- TC-SQL-007
-- Verify the total number of patient records.
-- Expected Result: The database count matches the number
-- of patient records expected/displayed by the application.
-- Status: PASS after execution and verification.

SELECT COUNT(*)
FROM patients;



-- TC-SQL-008
-- Verify patient search works regardless of capitalization.
-- Test Data: jordan
-- Expected Result: Jordan Smith's patient record is returned.
-- Related Defect: BUG-001
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE LOWER(first_name) = LOWER('jordan');




-- TC-SQL-009
-- Verify a search for a nonexistent patient returns no records.
-- Test Data: NotARealPatient
-- Expected Result: Zero patient records are returned.
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE first_name = 'NotARealPatient';




-- TC-SQL-010
-- Verify a patient registered through the website
-- is successfully stored in the database.
-- Test Data: Taylor Brown
-- Expected Result: Taylor Brown's patient record is returned.
-- Status: PASS after execution and verification.

SELECT *
FROM patients
WHERE first_name = 'Taylor'
AND last_name = 'Brown';

