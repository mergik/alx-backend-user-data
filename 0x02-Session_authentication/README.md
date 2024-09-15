# 0x02. Session authentication

| Project Name | Description |
| --- | --- |
| `api/v1/app.py` | Entry point of the API, handles authentication for protected routes and session management |
| `api/v1/views/index.py` | Implements basic endpoints of the API: `/status`, `/stats`, and `/unauthorized` |
| `api/v1/views/users.py` | Implements all user-related endpoints of the API, including session-based operations |
| `api/v1/auth/__init__.py` | Initializes the auth package |
| `api/v1/auth/basic_auth.py` | Implements the BasicAuth class for Basic Authentication |
| `api/v1/auth/session_auth.py` | Implements the SessionAuth class for Session Authentication |
| `api/v1/auth/auth.py` | Implements the base Auth class for handling authentication |
| `api/v1/views/session_auth.py` | Implements session-specific views for login, logout, and session management |
| `api/v1/views/__init__.py` | Initializes the views package and registers blueprints |
