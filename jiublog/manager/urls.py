from jiublog.manager import manager
from jiublog.manager.views import HomeView, NewBlogView, BlogsView, BlogTypeView, NewPhotoView, PhotosView

manager.add_url_rule('/manager', view_func=HomeView.as_view('home'))
manager.add_url_rule('/m/blog_new', view_func=NewBlogView.as_view('blog_new'))
manager.add_url_rule('/m/blogs', view_func=BlogsView.as_view('blogs'))
manager.add_url_rule('/m/blog_type', view_func=BlogTypeView.as_view('blog_type'))
manager.add_url_rule('/m/photo_new', view_func=NewPhotoView.as_view('photo_new'))
manager.add_url_rule('/m/photos', view_func=PhotosView.as_view('photos'))
