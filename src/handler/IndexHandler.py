from handler.APIHandler import APIHandler
from sanic.response import json

class index(APIHandler):

    async def get(self, request):
        return json({'index':'indexs'})
