from jiublog.blog import blog
from jiublog.blog.views import HomeView, LoginView, RegisterView, BlogView, PhotoView, TimeView, ToolView, OtherView, \
    ForgotPwdView, LogoutView

blog.add_url_rule('/', view_func=HomeView.as_view('home'))
blog.add_url_rule('/signin', view_func=LoginView.as_view('signin'))
blog.add_url_rule('/signup', view_func=RegisterView.as_view('signup'))
blog.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
blog.add_url_rule('/forgot_pwd', view_func=ForgotPwdView.as_view('forgot_pwd'))
blog.add_url_rule('/blog', view_func=BlogView.as_view('blog'))
blog.add_url_rule('/photo', view_func=PhotoView.as_view('photo'))
blog.add_url_rule('/time', view_func=TimeView.as_view('time'))
blog.add_url_rule('/tool', view_func=ToolView.as_view('tool'))
blog.add_url_rule('/other', view_func=OtherView.as_view('other'))