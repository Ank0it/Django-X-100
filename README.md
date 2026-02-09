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

# DAY 3
- Topic: Models, migrations, and the Django admin
- Methods learned: defining a `models.Model`, running `makemigrations` and `migrate`
- Methods learned: registering models in `admin.py` and creating a superuser
- Built pages: model-driven list view
- Note: Run migrations after model changes to update the database schema.

# DAY 4
- Topic: Detail pages and dynamic URLs
- Methods learned: `get_object_or_404()` for safe lookups
- Added route with `path('<int:app_id>/')` and template link using `{% url %}`
- Built pages: app_details
- Updated model: added `description` field and ran migrations
- Note: Keep URL name consistency to avoid `NoReverseMatch` errors.
