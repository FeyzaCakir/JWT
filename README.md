# JWT Authentication Mini Project (Python)

## Overview

This project is a **minimal implementation of JSON Web Token (JWT) based authentication** written in Python.
The goal of the project is to demonstrate the internal mechanics of an authentication system including:

* User registration
* User login
* Token generation
* Token verification
* Route protection using decorators

The project is intentionally designed with **clear separation of concerns** to simulate a simplified backend architecture.

---

# Architecture

The project follows a layered structure:

```
Data Layer → Service Layer → Security Layer → Application Layer
```

Each layer has a distinct responsibility, which improves maintainability and readability.

---

# Project Structure

```
jwt-auth-mini/

app.py

auth/
    routes.py
    service.py

core/
    jwt_utils.py
    decorators.py

data/
    users.py

config.py
requirements.txt
```

---

# Module Responsibilities

## 1. `config.py`

Contains application configuration values.

Typical configuration values include:

* `SECRET_KEY` used for signing JWT tokens
* Token expiration settings
* Debug configurations

This module centralizes configuration to avoid hardcoding sensitive values.

---

## 2. `data/users.py`

Acts as a **mock database layer**.

Responsibilities:

* Define the `User` model
* Store users in an in-memory list
* Provide helper functions to access user data

Key operations:

* Add a new user
* Find user by email
* Find user by ID

This module simulates persistence without requiring a real database.

---

## 3. `core/jwt_utils.py`

Handles **JWT token creation and verification**.

Responsibilities:

* Encode payloads into JWT tokens
* Decode and validate incoming tokens
* Handle token-related errors

Typical operations include:

* Token signing using `HS256`
* Expiration validation
* Signature verification

---

## 4. `auth/service.py`

Implements the **authentication business logic**.

Responsibilities:

* Register new users
* Authenticate users during login
* Generate JWT tokens
* Validate tokens and retrieve associated users

Main operations:

### Register

Creates a new user after verifying that the email does not already exist.

### Login

Validates user credentials and generates a JWT token containing:

* `user_id`
* expiration timestamp (`exp`)

### Token Verification

Decodes a token and retrieves the corresponding user from the data layer.

---

## 5. `core/decorators.py`

Implements **authorization logic** using decorators.

Decorators are used to protect functions or routes that require authentication.

Responsibilities:

* Extract token from function arguments
* Decode the token
* Verify user identity
* Allow or deny access to the protected function

This approach simulates middleware behavior used in real backend frameworks.

---

## 6. `auth/routes.py`

Defines application endpoints or logical entry points for authentication actions.

Typical endpoints include:

* `register`
* `login`
* `protected`

Routes delegate business logic to the **service layer**, ensuring clean separation between request handling and application logic.

---

## 7. `app.py`

The application entry point.

Responsibilities:

* Initialize the application
* Register routes
* Start the program or testing workflow

---

# Authentication Flow

## Registration Flow

```
Client → register
        ↓
routes.py
        ↓
service.py
        ↓
users.py
        ↓
User stored in fake database
```

---

## Login Flow

```
Client → login
        ↓
routes.py
        ↓
service.py
        ↓
users.py (user lookup)
        ↓
jwt_utils.encode()
        ↓
JWT token returned
```

---

## Protected Access Flow

```
Client → protected function
        ↓
decorator
        ↓
jwt_utils.decode()
        ↓
verify_token()
        ↓
User validated
        ↓
Protected logic executed
```

---

# JWT Structure Used

The project uses the standard JWT structure:

```
Header.Payload.Signature
```

Example payload:

```
{
  "user_id": 1,
  "exp": <expiration timestamp>
}
```

The token is signed using:

```
HS256 (HMAC + SHA256)
```

---

# Dependencies

Install dependencies using:

```
pip install -r requirements.txt
```

Typical dependencies:

```
PyJWT
python-dotenv
```

---

# Security Notes

This project is intended for **educational purposes**.
In production systems additional security practices are required:

* Password hashing (bcrypt / argon2)
* Secure token storage
* Refresh tokens
* Rate limiting
* Proper database persistence
* HTTPS enforcement

---

# Learning Objectives

This project demonstrates:

* How JWT authentication works internally
* Separation of concerns in backend architecture
* Service-layer based authentication logic
* Token-based authorization using decorators

---

# Future Improvements

Possible enhancements:

* Integrate a real database (PostgreSQL / SQLite)
* Implement password hashing
* Add refresh tokens
* Add role-based access control (RBAC)
* Integrate with a web framework such as Flask or FastAPI

---

# License

This project is intended for educational and learning purposes.
