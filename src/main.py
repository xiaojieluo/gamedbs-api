from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text, json
from web import route


def make_app(name=__name__, route=route):
    app = Sanic(name)
    # 循环导入 route
    for url, view in route:
        app.add_route(view.as_view(), url)

    return app


if __name__ == '__main__':
    app = make_app(__name__)
    app.run(host='0.0.0.0', port=8888, workers=4, debug=True)
