import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="postgress1server.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="abinm670@postgress1server" #TODO: Update value
    POSTGRES_PW="Ahmed1934$"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://techconf.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=BwcoSp8acVkYHMUpZ3QY2f+hO44rI3c6uKfDTeYD0QY=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='techconfque'
    ADMIN_EMAIL_ADDRESS:'jeddah_nona_1980@hotmail.com'
    SENDGRID_API_KEY = 'Local Env Only' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
