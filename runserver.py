#!/usr/bin/env python

# These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

from ownstorage import app
app.debug = True
app.run()
