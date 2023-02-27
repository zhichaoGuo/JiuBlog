from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask.views import MethodView
from flask_login import logout_user, current_user, login_user
from sqlalchemy import or_

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
        if current_user.is_authenticated:
            return redirect(url_for('blog.home'))
        form = LoginForm()
        return render_template('blog/signin.html', form=form)

    def post(self):
        _form = request.form
        usr = _form.get('usr_email')
        pwd = _form.get('password')
        user = User.query.filter(or_(User.username == usr, User.email == usr.lower())).first()
        if user is None:
            flash('无效的邮箱或用户名.', 'danger')
        elif user.is_ban():
            flash('您的账号处于封禁状态,禁止登陆！联系管理员解除封禁!', 'danger')
            return redirect(url_for('blog.signin'))
        elif user.is_log_off():
            flash('您的账号已被注销！', 'danger')
        elif user.check_password(pwd):
            login_user(user)
            flash('登录成功!', 'success')
            if request.args.get('next'):
                return redirect(url_for(request.args.get('next')))
            return redirect(url_for('blog.home'))
        else:
            flash('用户名或密码错误!', 'danger')
            return redirect(url_for('blog.signin'))






class RegisterView(MethodView):
    """
    注册视图
    """

    def get(self):
        form = RegisterForm()

        return render_template('blog/signup.html', form=form)

    def post(self):
        _form = request.form
        user_name = _form.get('user_name')
        pwd = _form.get('confirm_pwd')
        email = _form.get('user_email')
        if User.name_is_exist(user_name):
            flash('用户名已存在', 'warning')
            return render_template('blog/signup.html', form=RegisterForm())
        if User.email_is_exist(user_name):
            flash('邮箱已注册', 'warning')
            return render_template('blog/signup.html', form=RegisterForm())
        user = User(username=user_name, email=email, password=pwd)
        user.set_password(pwd)
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
