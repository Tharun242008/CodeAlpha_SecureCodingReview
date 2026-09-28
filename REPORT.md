# CodeAlpha Cyber Security Internship
## Task 3 - Secure Coding Review

### Introduction
This project reviews a simple Python login application, identifies security weaknesses, and demonstrates improvements.

### Application Selected
- Programming Language: Python
- Application: Simple Login System
- Review Method: Manual Code Review

### Vulnerabilities Identified
1. Hardcoded password
2. Weak password
3. No password hashing
4. No login-attempt protection
5. Basic authentication design

### Remediation
The improved version demonstrates password hashing with PBKDF2-HMAC-SHA256, random salt generation, limited login attempts, hidden password input, and generic authentication errors.

### Conclusion
Even a small login application can contain security weaknesses. Secure coding practices should be considered during development.

**Note:** This is an educational demonstration, not a production authentication system.
