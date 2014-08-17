# -*- coding: utf-8 -*-

# Copyright © 2014  Kushal Das <kushaldas@gmail.com>
# Copyright © 2014  Ratnadeep Debnath <rtnpro@gmail.com>
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU General Public License v.2, or (at your option) any later
# version.  This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.  You
# should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

import logging
import logging.handlers
import os
import sys

import flask
from flask import request
from flask import send_from_directory
from functools import wraps

__version__ = '0.1'

app = flask.Flask(__name__)
app.config.from_object('ownstorage.default_config')

# Log to stderr as well
STDERR_LOG = logging.StreamHandler(sys.stderr)
STDERR_LOG.setLevel(logging.INFO)
app.logger.addHandler(STDERR_LOG)

LOG = app.logger

@app.route('/')
def index():
    """ Displays the index page.
    """
    return 'Hello World!'


