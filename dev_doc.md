## 目录结构设计

```
JiuBlog
  | jiublog
  |   | 
```
## 数据库设计
### 用户表 user

|  id  |  account  |  email  |  password  |  group  |  signup_time  |  code  |  ban  |  login_time  |  log_off  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |

- id:编号
- account:账号 唯一 字符确认
- email：邮箱 邮箱确认
- password:密码 hash加密
- group:权限组 分割用户
- signup_time：注册时间
- code:邮件验证码
- ban:拉黑
- login_time:登录时间
- log_off：注销

### 博文表 blog

|  id |  title |  type_id |  img |  introduce |  content |  creat_time |  update_time |  read_times |  is_hide |  is_top  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |

- id:编号
- title:标题
- type_id:类别编号
- img:主图位置名称
- introduce:简介
- content:正文
- creat_time:创建时间
- update_time:更新时间
- read_times:阅读次数
- is_hide:是否隐藏
- is_top:是否置顶

### 草稿表 draft

|  id |  title |  type_id |  img |  introduce |  content |  time  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  |
| ----  | ----  | ----  | ----  | ----  | ----  | ----  |

- id:
- title:
- type_id:
- img:
- introduce:
- content:
- time:

### 博文类型表 blog_type

|  id |  name |  counts |  introduce |  create_time  |
|   ----  | ----  | ----  | ----  | ----  |
|   ----  | ----  | ----  | ----  | ----  |

- id：编号
- name：类别名称
- counts：本类文章数量
- introduce：类别简介
- create_time：类别创建时间

### 友情链接表 friend_link 

|  id |  title |  link |  desc  |
|   ----  | ----  | ----  | ----  |
|   ----  | ----  | ----  | ----  |

- id:编号
- title:友链名称
- link:链接
- desc:简介

### 相册表 photo 

|  id |  title |  introduce |  save_path |  create_time |  is_hide  |
|   ----  | ----  | ----  |   ----  | ----  | ----  |
|   ----  | ----  | ----  |   ----  | ----  | ----  |

- id:编号
- title:标题
- introduce:简介
- save_path:保存路径
- create_time:创建时间
- is_hide:是否隐藏
