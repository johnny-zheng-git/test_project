######################################
# Time:2020/02/07
# writer: ZWQ
######################################

from ADAM.user.urls import user_mold
from common import create_app

app = create_app()
app.register_blueprint(user_mold, url_prefix='/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)