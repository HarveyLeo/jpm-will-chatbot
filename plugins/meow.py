from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class MeowPlugin(WillPlugin):

    @hear("^~meow")
    def meow(self, message):
        self.reply(message, "meow meow meow!")


