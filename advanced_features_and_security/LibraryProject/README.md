echo "# Advanced Features and Security Django Project

This project demonstrates:

- Custom User model with extra fields (date_of_birth, profile_photo)
- Custom User Manager
- Permissions and Groups:
    - Groups: Viewers, Editors, Admins
    - Permissions: can_view, can_create, can_edit, can_delete
- Enforcement of permissions in views using @permission_required decorator
- Admin panel integration for CustomUser and Book models
" > README.md




## Security Measures

1. DEBUG set to False in production.
2. CSRF and session cookies are secure (HTTPS only).
3. Browser protections:
   - SECURE_BROWSER_XSS_FILTER
   - X_FRAME_OPTIONS='DENY'
   - SECURE_CONTENT_TYPE_NOSNIFF
4. All forms include {% csrf_token %} for CSRF protection.
5. ORM queries used to prevent SQL injection.
6. Content Security Policy configured via django-csp middleware.
7. HSTS enabled for HTTPS.
