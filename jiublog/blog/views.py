from flask import Blueprint
from flask.views import MethodView

blog = Blueprint('blog', __name__)


class HomeView(MethodView):
    """
    主页视图
    """
    def get(self):
        return 'hi jiublog'

    def post(self):
        pass
