import ConfigParser
import base64
import getpass

config = ConfigParser.RawConfigParser()

huid = base64.b64encode(str(input("Enter your HUID: ")))
pin = base64.b64encode(str(getpass.getpass("Enter your PIN: ")))
db_user = base64.b64encode(str(input("Enter your database user: ")))
db_pass = base64.b64encode(str(getpass.getpass("Enter your database password: ")))

config.add_section("setup")
config.set("setup", "a", huid)
config.set("setup", "b", pin)
config.set("setup", "c", db_user)
config.set("setup", "d", db_pass)

with open('config.ini', 'wb') as configfile:
    config.write(configfile)
