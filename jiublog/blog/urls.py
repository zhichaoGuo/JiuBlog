from jiublog.blog import blog
from jiublog.blog.views import HomeView

blog.add_url_rule('/', view_func=HomeView.as_view('home'))