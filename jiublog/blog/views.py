from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask.views import MethodView
from flask_login import logout_user

from jiublog.extension import db
from jiublog.forms import LoginForm, RegisterForm
from jiublog.models import User

blog = Blueprint('blog', __name__)


class HomeView(MethodView):
    """
    主页视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass


class LoginView(MethodView):
    """
    登录视图
    """

    def get(self):
        form = LoginForm()
        return render_template('blog/signin.html', form=form)

    def post(self):
        pass


class RegisterView(MethodView):
    """
    注册视图
    """

    def get(self):
        form = RegisterForm()

        return render_template('blog/signup.html', form=form)

    def post(self):
        form = request.form
        user_name = form.get('user_name')
        pwd = form.get('confirm_pwd')
        email = form.get('user_email')
        if User.is_exist(user_name):
            flash('用户名已存在')
            return None
        user = User(username=user_name, email=email, password=pwd)
        db.session.add(user)
        db.session.commit()
        flash('注册成功,欢迎加入Blogin.', 'success')
        return redirect(url_for('blog.signin'))


class ForgotPwdView(MethodView):
    """
    忘记密码视图
    """

    def get(self):
        form = RegisterForm()
        return render_template('blog/forgot_pwd.html', form=form)

    def post(self):
        flash('注册成功,欢迎加入Blogin.', 'success')
        return redirect(url_for('blog.signin'))


class LogoutView(MethodView):
    """
    退出登录视图
    """

    def get(self):
        logout_user()
        flash('退出成功!', 'success')
        return redirect(url_for('blog.home'))


class BlogView(MethodView):
    """
    博客视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass


class PhotoView(MethodView):
    """
    相册视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass


class TimeView(MethodView):
    """
    归档视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass


class ToolView(MethodView):
    """
    工具视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass


class OtherView(MethodView):
    """
    其他视图
    """

    def get(self):
        return render_template('blog/index.html')

    def post(self):
        pass
