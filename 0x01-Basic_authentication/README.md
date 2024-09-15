# 0x01. Basic authentication

| Project Name | Description |
| --- | --- |
| `api/v1/app.py` | Entry point of the API, handles authentication for protected routes |
| `api/v1/views/index.py` | Implements basic endpoints of the API: `/status` and `/stats` |
| `api/v1/auth/__init__.py` | Initializes the auth package |
| `api/v1/auth/auth.py` | Implements the Auth class for handling authentication |
| `api/v1/auth/basic_auth.py` | Implements the BasicAuth class, extending Auth for Basic Authentication |
| `api/v1/views/users.py` | Implements all user-related endpoints of the API |
