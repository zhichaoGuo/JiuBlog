from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo


class LoginForm(FlaskForm):
    usr_email = StringField(u'邮箱/用户名', validators=[DataRequired(message='用户名或邮箱不能为空')],
                            render_kw={'placeholder': '请输入邮箱或用户名'})
    password = StringField(u'登录密码',
                           validators=[DataRequired(message='登录密码不能为空'),
                                       Length(min=8, max=40, message='登录密码必须在8-40位之间')],
                           render_kw={'type': 'password', 'placeholder': '请输入用户密码'})
    remember_me = BooleanField('记住我')
    submit = SubmitField(u'登录', render_kw={'class': 'btn btn-secondary'})


class RegisterForm(FlaskForm):
    user_name = StringField(u'用户名',
                            validators=[DataRequired(message='用户名不能为空'),
                                        Length(min=1, max=16, message='用户名长度限定在1-16位之间'),
                                        Regexp('^[a-zA-Z0-9_]*$',
                                               message='用户名只能包含数字、字母以及下划线.')],
                            render_kw={'placeholder': '请输入用户名长度1-8之间'})
    user_email = StringField(u'注册邮箱',
                             validators=[DataRequired(message='注册邮箱不能为空'),
                                         Length(min=4, message='注册邮箱长度必须大于4')],
                             render_kw={'placeholder': '请输入注册邮箱', 'type': 'email'})
    password = StringField(u'密码',
                           validators=[DataRequired(message='用户密码不能为空'),
                                       Length(min=8, max=40, message='用户密码长度限定在8-40位之间'),
                                       EqualTo('confirm_pwd', message='两次密码不一致')],
                           render_kw={'placeholder': '请输入密码', 'type': 'password'})
    confirm_pwd = StringField(u'确认密码',
                              validators=[DataRequired(message='用户密码不能为空'),
                                          Length(min=8, max=40, message='用户密码长度限定在8-40位之间')],
                              render_kw={'placeholder': '请确认密码', 'type': 'password'})
    submit = SubmitField(u'创建', render_kw={'class': 'btn btn-secondary'})
