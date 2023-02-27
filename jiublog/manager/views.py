from flask import Blueprint, render_template
from flask.views import MethodView

from jiublog.forms import PostForm

manager = Blueprint('manager', __name__)


class HomeView(MethodView):
    """
    后台主页视图
    """

    def get(self):
        return render_template('manager/index.html')

    def post(self):
        pass


class NewBlogView(MethodView):
    """
    新增博客视图
    """

    def get(self):
        form = PostForm()
        return render_template('manager/blog.html',form=form)

    def post(self):
        pass


class BlogsView(MethodView):
    """
    管理博客视图
    """

    def get(self):
        form = PostForm()
        return render_template('manager/blog.html',form=form)

    def post(self):
        pass


class BlogTypeView(MethodView):
    """
    管理博客分类视图
    """

    def get(self):
        pass

    def post(self):
        pass


class NewPhotoView(MethodView):
    """
    新增图片视图
    """

    def get(self):
        pass

    def post(self):
        pass


class PhotosView(MethodView):
    """
    管理图片视图
    """

    def get(self):
        pass

    def post(self):
        pass
