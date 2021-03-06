# -*- coding: utf-8 -*-

"""{{ cookiecutter.site_name }} base Invenio configuration."""

from __future__ import absolute_import, print_function

from flask_celeryext import create_celery_app

from .factory import create_app

celery = create_celery_app(create_app())
