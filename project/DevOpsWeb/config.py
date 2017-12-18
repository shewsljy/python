import os

''' 文件所在目录的绝对路径 '''
basedir = os.path.abspath(os.path.dirname(__file__))

''' config配置类 '''
class Config(object):
    # 设置安全密钥，首先取环境变量的值，没有则取默认值
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devopsweb'
    # 每次请求结束后都会自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 静态方法 当前环境的配置初始化
    @staticmethod
    def init_app(app):
        pass

''' 开发配置类继承Config类 '''
class DevelopmentConfig(Config):
    # 开启DEBUG模式
    DEBUG = True
    # 数据库连接方式 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

''' 测试配置类继承Config类 '''
class TestingConfig(Config):
    # 开启测试模式
    TESTING = True
    # 数据库连接方式 
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

''' 生产配置类继承Config类 '''
class ProductionConfig(Config):
    # 数据库连接方式 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

''' 配置字典，默认为开发配置 '''
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}