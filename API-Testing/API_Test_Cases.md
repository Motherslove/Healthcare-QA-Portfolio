# Healthcare API Test Cases

## Test Summary

- Total Test Cases: 10
- Passed: 10
- Failed: 0
- Pass Rate: 100%
- Tool: Postman
- API Framework: Flask
- Database: SQLite

---

## TC-API-001 — Get All Patients

**Method:** GET  
**Endpoint:** /api/patients

**Expected Result:**
- HTTP 200 OK
- Patient records returned in JSON format

**Actual Result:**
- HTTP 200 OK
- Patient records returned successfully

**Status:** PASS

---

## TC-API-002 — Get Patient by ID

**Method:** GET  
**Endpoint:** /api/patients/1

**Expected Result:**
- HTTP 200 OK
- Correct patient record returned

**Actual Result:**
- HTTP 200 OK
- Jordan Smith returned successfully

**Status:** PASS

---

## TC-API-003 — Patient Not Found

**Method:** GET  
**Endpoint:** /api/patients/999

**Expected Result:**
- HTTP 404 Not Found
- Error message returned

**Actual Result:**
- HTTP 404 Not Found
- "Patient not found" returned

**Status:** PASS

---

## TC-API-004 — Create New Patient

**Method:** POST  
**Endpoint:** /api/patients

**Test Data:** Morgan Davis

**Expected Result:**
- HTTP 201 Created
- New patient record created

**Actual Result:**
- HTTP 201 Created
- Morgan Davis created successfully

**Status:** PASS

---

## TC-API-005 — Missing Required Field

**Method:** POST  
**Endpoint:** /api/patients

**Test Condition:**
Email field omitted from request

**Expected Result:**
- HTTP 400 Bad Request
- Validation error returned

**Actual Result:**
- HTTP 400 Bad Request
- "All patient fields are required" returned

**Status:** PASS

---

## TC-API-006 — Verify Created Patient

**Method:** GET  
**Endpoint:** /api/patients

**Expected Result:**
- HTTP 200 OK
- Morgan Davis appears in patient records

**Actual Result:**
- HTTP 200 OK
- Morgan Davis returned successfully

**Status:** PASS

---

## TC-API-007 — Empty Required Field

**Method:** POST  
**Endpoint:** /api/patients

**Test Condition:**
Email field submitted with an empty value

**Expected Result:**
- HTTP 400 Bad Request
- Validation error returned

**Actual Result:**
- HTTP 400 Bad Request
- "All patient fields are required" returned

**Status:** PASS

---

## TC-API-008 — Invalid JSON

**Method:** POST  
**Endpoint:** /api/patients

**Test Condition:**
Malformed JSON request body submitted

**Expected Result:**
- HTTP 400 Bad Request
- Invalid request rejected

**Actual Result:**
- HTTP 400 Bad Request
- Malformed request rejected

**Status:** PASS

---

## TC-API-009 — Multiple Missing Required Fields

**Method:** POST  
**Endpoint:** /api/patients

**Test Condition:**
Date of birth, phone, and email omitted

**Expected Result:**
- HTTP 400 Bad Request
- Validation error returned

**Actual Result:**
- HTTP 400 Bad Request
- "All patient fields are required" returned

**Status:** PASS

---

## TC-API-010 — Get Created Patient by ID

**Method:** GET  
**Endpoint:** /api/patients/3

**Expected Result:**
- HTTP 200 OK
- Morgan Davis returned using patient ID

**Actual Result:**
- HTTP 200 OK
- Created patient returned successfully

**Status:** PASS

---

# API Testing Skills Demonstrated

- REST API testing
- Postman
- GET requests
- POST requests
- JSON request and response validation
- HTTP status code validation
- Positive testing
- Negative testing
- Required-field validation
- Invalid JSON testing
- Database persistence validation
- API-to-database verification