import pytest

class Bot:
    def __init__(self, name):
        self.name = name
        self.commands = {'help': 'Показать список команд', 'start': 'Запустить бота', 'hi': 'Привет'}

    def greeting(self):
        return self.commands['hi']

@pytest.fixture(scope='module')
def bot():
    return Bot('TestBot')

@pytest.mark.bot
def test_greeting_bot(bot):
    assert bot.greeting() == "Привет"

@pytest.mark.bot
def test_commands_bot(bot):
    assert bot.commands['help']
    assert bot.commands['start']

@pytest.mark.bot_2
def test_greeting_bot2(bot):
    assert bot.greeting() == "Привет"

@pytest.mark.bot_2
def test_commands_bot2(bot):
    assert bot.commands['help']
    assert bot.commands['start']