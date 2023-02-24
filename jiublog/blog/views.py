from flask import Blueprint, render_template
from flask.views import MethodView

blog = Blueprint('blog', __name__)


class HomeView(MethodView):
    """
    主页视图
    """
    def get(self):
        return render_template('index.html')

    def post(self):
        pass
