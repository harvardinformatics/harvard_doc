import os

ROOT_PATH =  os.path.dirname(os.path.abspath(__file__))

configs = {
  '/Users/ericmattison/code/dokken': 'dev_settings',
  '/var/www/docs': 'prod_settings',
}

#print ROOT_PATH
#print configs

config_module = __import__("config.%s" % configs[ROOT_PATH], globals(), locals(), 'dokken')

for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)
        #print locals()


