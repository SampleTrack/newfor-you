import importlib
import os

PLUGIN_PATH = 'bot/plugins'

for file in os.listdir(PLUGIN_PATH):
    if file.endswith('.py') and not file.startswith('_'):
        importlib.import_module(f'bot.plugins.{file[:-3]}')
