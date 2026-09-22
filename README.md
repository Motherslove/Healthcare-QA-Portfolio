# Healthcare QA Portfolio Project

## Project Overview

This project is a healthcare patient management web application that I created to demonstrate both software development and Quality Assurance (QA) testing skills.

I first built the application using Python, Flask, HTML, CSS, and SQLite. After the core functionality was working, I tested the application manually, documented test cases, identified defects, implemented fixes, retested the defects, and completed regression testing.

All patient information used in this project is synthetic test data.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Visual Studio Code
- Git
- GitHub

## Application Features

The application currently supports:

- Patient registration
- Patient record storage using SQLite
- Patient record display
- Search by Patient ID
- Search by first name
- Search by last name
- Partial-name search
- Case-insensitive search
- Full-name search

## How I Built the Application

I created the project in Visual Studio Code and used Python with Flask for the backend.

SQLite was used as the database for storing patient records.

The frontend was created with HTML and CSS.

The patient registration form collects:

- First name
- Last name
- Date of birth
- Phone number
- Email address

After registration, Flask processes the form data and stores the patient information in the SQLite database.

I then added patient search functionality so records could be located using Patient ID or patient names.

## QA Testing Process

After building the application, I created manual test cases for the patient search functionality.

My testing process included:

1. Creating test scenarios and test cases.
2. Defining test data and expected results.
3. Executing the test cases manually.
4. Comparing expected results with actual results.
5. Identifying defects.
6. Documenting defects in a bug report.
7. Updating the application to resolve the defects.
8. Retesting the fixes.
9. Performing regression testing.

## Test Coverage

I created 10 manual test cases covering:

- Valid first-name search
- Valid last-name search
- Patient ID search
- Nonexistent patient search
- Partial-name search
- Lowercase search
- Empty/cleared search
- Special-character input
- Full-name search
- Lowercase full-name search

The completed regression test cycle resulted in:

**10 Passed / 10 Executed**

**Regression Status: PASS**

The detailed test cases are available in:

`Test-Cases/Healthcare_Test_Cases.xlsx`

## Defects Found

### BUG-001 — Case-Insensitive Patient Search

During testing, I discovered that searching for an existing patient using lowercase text did not return the patient.

Example:

Patient record:

`Jordan Smith`

Search:

`jordan`

**Expected Result:**  
Jordan Smith should appear regardless of capitalization.

**Actual Result:**  
The patient was not returned.

**Resolution:**  
The SQL search logic was updated to perform case-insensitive comparisons.

**Retest Result:** PASS

---

### BUG-002 — Full-Name Patient Search

During additional testing, I discovered that searching by first name or last name worked individually, but searching by the patient's complete name did not.

For example:

`Jordan` → PASS

`Smith` → PASS

`Jordan Smith` → FAIL

**Expected Result:**  
Jordan Smith should appear when the complete patient name is entered.

**Actual Result:**  
No matching patient appeared.

**Root Cause:**  
The search query checked the first and last name separately but did not search the combined full name.

**Resolution:**  
The SQL query was updated to support combined first-name and last-name searches while maintaining case-insensitive searching.

**Retest Result:** PASS

The detailed defect documentation is available in:

`Bug-Reports/Bug_Report.xlsx`

## Regression Testing

After fixing the identified defects, I reran the patient search test suite.

Regression testing confirmed that the fixes did not negatively affect the existing search functionality.

Final result:

**10 Test Cases Executed**  
**10 Test Cases Passed**  
**0 Test Cases Failed**

## QA Skills Demonstrated

This project demonstrates experience with:

- Manual Testing
- Functional Testing
- Regression Testing
- Test Case Design
- Test Execution
- Defect Identification
- Bug Reporting
- Severity and Priority Classification
- Retesting
- Negative Testing
- Web Application Testing
- SQL/Database Validation
- Test Documentation
- Git and GitHub

## QA Defect Lifecycle Demonstrated

Build Application  
↓  
Create Test Cases  
↓  
Execute Tests  
↓  
Identify Defects  
↓  
Document Bugs  
↓  
Implement Fixes  
↓  
Retest  
↓  
Regression Testing  
↓  
Document Results

## Future Enhancements

Future additions to this QA portfolio may include:

- REST API testing with Postman
- SQL database test queries
- Automated testing with Pytest
- UI automation with Playwright or Selenium
- GitHub Actions for automated test execution
- Appointment management
- Medication management
- Laboratory results

## Author

**Asha Johnson**

Healthcare QA Portfolio Project