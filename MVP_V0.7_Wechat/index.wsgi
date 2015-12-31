# coding=utf-8
# Author: shawn0lee0
# Mail: run-map@googlegroups.com
import sae
import sys
reload(sys)
import os

sae.add_vendor_dir('site-packages')
#basedir = os.path.abspath(os.path.dirname(__file__))
#sys.path.insert(0, os.path.join(basedir, 'site-packages'))

sys.setdefaultencoding('utf-8')


from myapp import app

application = sae.create_wsgi_app(app)