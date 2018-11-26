import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o@r0^%_&sd6vtrmeek@54*uh#_ih6j#1ftl*l*psi%qb0a7p8k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# 系统的apps
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 第三方的apps
EXT_APPS = []

# 自定义apps
CUSTOM_APPS = [
    'apps.account',
    'apps.cate',
    'apps.detail',
    'apps.main',
    'apps.home',
    'apps.search',

]
# Application definition

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopping91.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 启动应用程序的配置
WSGI_APPLICATION = 'shopping91.wsgi.application'

# 数据库的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopping',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 语言配置(开发中设置为中文)
LANGUAGE_CODE = 'zh-hans'
# 时区设置,设置成中国时区
TIME_ZONE = 'Asia/Shanghai'
# 国际化配置,自动转化多国语言
USE_I18N = True

USE_L10N = True
# 开启django时区,如果不需要django时区可以设置为False(建议False/)
USE_TZ = False

# ============================ 静态文件================
# 访问静态文件的路径配置   命令collectstatic
STATIC_URL = '/static/'
# 配置静态文件整理的根目录,配合命令
STATIC_ROOT = ''
# 配置静态文件的目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

# ======================== 缓存======================
# pip install djanog-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            'MAX_ENTRIES': 2000,
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 缓存地址
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            'MAX_ENTRIES': 2000,
            # 使用线程池管理连接
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
}

# ================== SESSION 缓存配置 ==================
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# session 失效时间,7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60

# ===================== 邮件配置 ====================
# 邮箱stmp端口
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'yinyaowhy@163.com'
EMAIL_HOST_PASSWORD = 'py1805'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL
# EMAIL_TIMEOUT
# EMAIL_SSL_KEYFILE
# EMAIL_SSL_CERTFILE


# ======================= 日志配置================
