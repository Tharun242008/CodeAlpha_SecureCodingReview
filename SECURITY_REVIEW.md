# Security Review

## Application
- Language: Python
- Application: Simple Login System
- Method: Manual Code Review

## Findings

### 1. Hardcoded Password
The original code stores `12345` directly in source code.
**Risk:** Anyone who can read the code can obtain the credential.
**Fix:** Never store plaintext secrets in source code. Use secure credential storage.

### 2. Weak Password
`12345` is very easy to guess.
**Risk:** Weak passwords are vulnerable to guessing attacks.
**Fix:** Use strong, unique passwords and appropriate password policies.

### 3. No Password Hashing
The original code compares a plaintext password.
**Risk:** Plaintext password handling increases exposure if code or data is leaked.
**Fix:** Use a password-hashing method. The demo uses PBKDF2-HMAC-SHA256 with a random salt.

### 4. No Login Attempt Protection
The original code allows unlimited attempts.
**Risk:** Repeated guessing is possible.
**Fix:** Add rate limiting, attempt limits, or temporary lockout.

### 5. Basic Authentication Design
The original program has almost no protection around authentication.
**Fix:** Use secure credential storage, MFA where appropriate, HTTPS, logging/monitoring, and safe authentication flows.

## Testing
1. Correct demo credentials -> login succeeds.
2. Wrong password -> generic error.
3. Repeated wrong passwords -> attempts are limited.
4. Password input is hidden while typing.
