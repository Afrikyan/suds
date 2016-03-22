gunicorn -D -b '0.0.0.0:8000' ask.wsgi --access-logfile access.log --error-logfile error.log --log-level info
