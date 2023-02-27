from flask import Blueprint, render_template
from flask.views import MethodView

manager = Blueprint('manager', __name__)

class HomeView(MethodView):
    """
    后台主页视图
    """

    def get(self):
        return render_template('manager/index.html')

    def post(self):
        pass