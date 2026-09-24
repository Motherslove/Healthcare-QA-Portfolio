Healthcare QA Portfolio

A hands-on software quality assurance portfolio project demonstrating the full QA lifecycle across a Flask healthcare application: test planning, manual functional testing, defect reporting, regression testing, SQL/database validation, REST API testing with Postman, and API test automation with Pytest.

Project Highlights

Built and tested a patient management web application using Python, Flask, HTML/CSS, and SQLite.

Created and executed 10 manual patient-search test cases.

Identified, documented, fixed, and retested search defects involving lowercase and full-name searches.

Completed regression testing with 10/10 tests passing.

Created and executed 10 SQL/database validation tests.

Created and executed 10 REST API tests in Postman covering positive and negative scenarios.

Added Pytest automation for core API workflows, including GET, POST, 404, and required-field validation.

Used Git and GitHub for version control and portfolio documentation.

Technologies & Tools

Application: Python, Flask, HTML, CSS, SQLite
QA / Testing: Manual Testing, Regression Testing, SQL, Postman, REST APIs, Pytest
Workflow: Git, GitHub, Visual Studio, Chrome

Application Features

The application supports:

Patient registration

SQLite patient storage

Patient record display

Search by patient ID

Search by first or last name

Partial and case-insensitive search

Full-name search

REST API endpoints for retrieving and creating patient records

QA Workflow

1. Manual Functional Testing

Created structured test cases for patient-search functionality, including valid and invalid searches, partial names, lowercase input, empty searches, special characters, and full-name searches.

Regression result: 10 executed, 10 passed, 0 failed.

2. Defect Reporting

Two search defects were identified during testing:

BUG-001 - Lowercase Search
Lowercase search text initially failed to return the expected patient. The SQL search logic was updated to perform case-insensitive comparisons, followed by successful retesting.

BUG-002 - Full-Name Search
Searching for a full name such as Jordan Smith initially returned no result even though first-name and last-name searches worked independently. The query was updated to support combined first- and last-name matching, followed by successful retesting.

3. SQL / Database Testing

Created a 10-test SQL validation suite covering:

Patient retrieval

Search by patient ID

Search by first name

Full-name validation

NULL checks on required fields

Duplicate patient ID checks

Record-count validation

Case-insensitive search

Nonexistent-patient searches

UI-to-database persistence validation

Result: 10 executed, 10 passed, 0 failed.

4. REST API Testing with Postman

Tested Flask API endpoints with positive and negative scenarios, including:

GET /api/patients

GET /api/patients/<id>

POST /api/patients

200 OK

201 Created

400 Bad Request

404 Not Found

JSON response validation

Missing and empty required fields

Malformed JSON

Persistence of newly created patients

Result: 10 executed, 10 passed, 0 failed.

5. Pytest Automation

Automated core REST API checks using Flask's test client and Pytest. Automated coverage includes:

GET all patients

GET patient by ID

404 handling for nonexistent patients

POST patient creation

Missing required-field validation

Empty required-field validation

Repository Structure

Healthcare-QA-Portfolio/
├── API-Testing/
│   ├── API_Test_Cases.md
│   └── Healthcare_QA_API_Tests.postman_collection.json
├── Bug-Reports/
│   └── Bug_Report.xlsx
├── SQL/
│   └── Database_Test_Queries.sql
├── Test-Cases/
│   └── Healthcare_Test_Cases.xlsx
├── tests/
│   └── test_api.py
├── static/
├── templates/
├── app.py
├── healthcare.db
└── README.md

Skills Demonstrated

Manual testing • Functional testing • Regression testing • Test case design • Defect lifecycle • Bug reporting • SQL validation • Database testing • REST API testing • Postman • Pytest • Test automation • JSON validation • HTTP status-code validation • Python • Flask • SQLite • Git • GitHub

Portfolio Value

This project demonstrates an end-to-end QA workflow rather than isolated test artifacts: application behavior was tested at the UI, database, and API layers; defects were documented and retested; regression coverage was completed; and repeatable API checks were automated with Pytest.

Author

Asha Johnson
GitHub: https://github.com/Motherslove