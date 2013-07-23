import ConfigParser
import base64
import getpass

config = ConfigParser.RawConfigParser()

huid = base64.b64encode(str(input("Enter your HUID: ")))
pin = base64.b64encode(str(getpass.getpass("Enter your PIN: ")))

config.add_section("setup")
config.set("setup", "a", huid)
config.set("setup", "b", pin)

with open('config.ini', 'wb') as configfile:
    config.write(configfile)
