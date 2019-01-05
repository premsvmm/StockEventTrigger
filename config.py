import os

class Config():
        DATABASE_URL= os.environ.get('DATABASE_URL', '')
        EMAIL_ID= os.environ.get('EMAIL_ID', '')
        EMAIL_PASSWORD= os.environ.get('EMAIL_PASSWORD', '')




if __name__ == '__main__':
    print(Config.DATABASE_URL)
    print(Config.EMAIL_ID)
    print(Config.EMAIL_PASSWORD)