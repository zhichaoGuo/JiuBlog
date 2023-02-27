from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

from jiublog.models import BlogType


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

class PostForm(FlaskForm):
    title = StringField(u'博客标题', validators=[Length(min=3, max=50, message='用户名长度必须在3到20位之间')],
                        render_kw={'class': '', 'rows': 50, 'placeholder': '输入您的博客标题'})
    blog_type = SelectField(label=u'博客类型',
                            default=0,
                            coerce=int)
    blog_level = SelectField(label=u'博客权限', choices=[(1, '公开'), (2, '私有')], validators=[DataRequired()],
                             default=1, coerce=int)
    brief_content = TextAreaField(u'博客简介', validators=[DataRequired()])
    blog_img_file = FileField(label=u'博客示例图',
                              validators=[DataRequired(), FileAllowed(['png', 'jpg'], '只接收png和jpg图片')],
                              render_kw={'value': "上传", 'class': 'btn btn-default'})
    body = CKEditorField('Body', validators=[DataRequired(message='请输入博客内容')])
    save = SubmitField(u'保存草稿')
    submit = SubmitField(u'发布博客')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        categories = BlogType.query.all()
        self.blog_type.choices = [(cate.id, cate.name) for cate in categories]