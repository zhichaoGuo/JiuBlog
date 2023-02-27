from jiublog.manager import manager
from jiublog.manager.views import HomeView

manager.add_url_rule('/manager', view_func=HomeView.as_view('home'))
