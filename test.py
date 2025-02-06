import ConfigParser

config = ConfigParser.ConfigParser()
config.read('configuration.conf')

print("Sections:", config.sections())
if config.has_section('ldap'):
	print("password:", config['ldap'].get('password'))