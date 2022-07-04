"""main module of audifi flask application"""

from flask import Flask
from .views import views
app = Flask('audifi')
app.register_blueprint(views, url_prefix="/")
