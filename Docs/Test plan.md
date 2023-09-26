# Swagger Petstore Test Plan
*Prepared by: Durin Evgenii*

## 1. Introduction
The Swagger Petstore Test Plan serves as a baseline to identify scope, available resources, establish timelines, and outline associated risks and assumptions for automated test coverage.

## 2. Resource
- Tester: Durin Evgenii
- Test dates: September 21, 2023 – September 27, 2023

## 3. In Scope
The following functionality described in [https://petstore.swagger.io/](https://petstore.swagger.io/) is in scope:

## 4. Out of Scope
- Orthography
- Performance testing
- Security testing (SQL Injection) is not included since this is a third-party project, and any potential security intrusion would be a violation.

## 5. Quality and Acceptance Criteria
- Full set of tests passed after code freeze.
- There are no open bugs with Priority Blocker and High.

## 6. Assumptions
Swagger Petstore is aimed at showcasing the Swagger UI product and does not contain complete documentation or full functionality.

## 7. Risks
Some of the functionality cannot be covered by automated tests due to the fact that related functionality is not functioning.

## 8. Test Types
The following test types will be conducted:
- Test cases for creating, reading, updating, and deleting records.

## 9. Testing Tools
- Language: Python
- Test Framework: Pytest
- HTTP Requests: Requests
- Reporting: Allure
- Containerization: Docker

## 10. Completion Criteria
Testing will be considered successful when:
- All specified test cases have passed.
- There are no open bugs with Priority Blocker and High.
