# 专业选修课 <Web开发技术> 大作业

## 开发及测试环境

- 操作系统: `Arch Linux`
- 运行环境: `Python 3.8.3`
- 兼容性测试平台: `Windows 10`

## 前端方案

- CSS框架：`Bulma` v0.9.0 (纯CSS框架，无需配套的js文件) ([官网地址](https://bulma.io/))
- 图标库：`Font Awesome` v5.13.0 ([官网地址](https://fontawesome.com/))
- JavaScript: 全面脱离jQuery, 回归原生js

## 后端方案

- `Python Flask` v1.1.2
- 数据库：`SQLite3` 
- ORM支持: `flask-sqlalchemy` v2.4.3

## 网站内容简介

- 用户注册/登录/注销(配合session实现)
- 在线云笔记(不支持Markdown)
- 在线图床(可一次上传多张, 支持上传前预览)
- 留言板
- 项目介绍页面
- 对移动端进行了响应式适配

> [/screenshots](./screenshots) 文件中存放有截图

## 项目目录结构介绍

> 自定义了类似于Django的项目结构, 便于大型项目的维护、开发和拓展

- `/app/`: 类似于Django的app文件夹
  - `__init__.py`: 声明这个文件夹是一个 python package
  - `views.py`: 提供渲染网页模板的蓝图
  - `api.py`: 提供后端API的蓝图, 使用 Ajax POST 方式访问
  - `models.py`: 提供可操作的数据库ORM对象和定义数据模型
  - `decorators.py`: 提供装饰器, 例如: 要求用户必须登录的视图装饰器
  - `utils.py`: 提供一些自定义函数
- `/conf/`: 项目的配置文件夹
  - `__init__.py`: 声明这个文件夹是一个 python package
  - `app.py`: 提供创建 Flask App 对象的函数
  - `config.py`: 将Flask需要的配置打包成一个Class
  - `settings.py`: 提供一些目录的绝对路径和其他杂项
- `/db/`: 存放数据库相关文件
  - `models.db`: SQLite3本地文件
- `/migrations/`: Flask Migrate的生成文件夹
- `/static/`: 存放网站所需的静态文件
  - `/upload/`: 存放用户上传的文件
- `/templates/`: 存放 Jinja2 网页模板
- `manage.py`: 用于启动服务端, 进行数据库的初始化、迁移、升级等
- `requirements.txt`: pipreqs生成的引入的第三方库清单, 配合 `pip -r` 命令使用

## 项目运行

- 首先安装好 `Python` (建议64位), 在 Windows 环境下确保 `pip` 在终端中可用
- 执行 `pip -r requirements.txt` 安装好运行所必需的第三方库 *(如果pip下载速度慢, 可换清华源)*
- 执行 `python manage.py runserver` 以启动服务端, 附带的数据库文件已经包含有测试数据, 可以展示所有测试数据的账号为: 用户名: `测试账号`, 密码: `123`

### 如果附带的数据库文件出现异常, 请删除原数据库文件, 并执行如下命令

- `python manage.py db init`
- `python manage.py db migrate`
- `python manage.py db upgrade`

> 执行以上三条命令后, 数据库重建完成, 请自行填充数据
