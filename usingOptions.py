import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-n", "--name", dest="name", help="Provide your name")

(options, arguments) = parser.parse_args()

name = options.name

print("Welcome to my program " + name)
