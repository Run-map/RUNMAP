#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass
