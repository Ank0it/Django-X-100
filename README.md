# DAY 1
- Topic: Django basics (views, URL routing, templates, static files)
- Methods learned: `HttpResponse()` for simple responses
- Methods learned: `render()` to return templates
- Built pages: home, about, contact
- Linked CSS via `{% static %}`
- Note: Restart the dev server after changing settings or installed apps.
- Note: Keep templates and static files in their proper folders.

# DAY 2
- Topic: App creation and app-level URL routing
- Methods learned: `path()` in app `urls.py` and `render()` in app views
- Added app to `INSTALLED_APPS` and enabled app templates
- Used template inheritance with `{% extends %}` and `{% block %}`
- Built an app page: all_app
- Note: Include the app's `urls.py` in the project `urls.py` for routing.
