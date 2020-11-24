from nameko.rpc import rpc
from time import sleep

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)