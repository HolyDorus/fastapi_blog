from starlette.config import Config


config = Config('.env')


API_VERSION = 'v1'

SECRET_KEY = config('SECRET_KEY', cast=str)

# Application configuration
APP_HOST = config('APP_HOST', cast=str, default='127.0.0.1')
APP_PORT = config('APP_PORT', cast=int, default=5000)
APP_AUTORELOAD = config('APP_AUTORELOAD', cast=bool, default=True)

# Database URL
SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL', cast=str)

LOGN_URL = f'/api/{API_VERSION}/auth/login'

# Token 60 minutes * 24 hours * 7 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# Sub for access token
ACCESS_TOKEN_SUB = 'access_token'

# List of all tracked models by alembic
INSTALLED_MODELS = [
    'src.blogs.models',
    'src.users.models'
]
