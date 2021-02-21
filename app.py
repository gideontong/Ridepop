from sys import version_info

MIN_VERSION = (3, 7)
assert version_info >= MIN_VERSION, f'requires Python {".".join([str(n) for n in MIN_VERSION])} or newer'

from webserver import app as webservice

if __name__ == '__main__':
    webservice.run(host='0.0.0.0')
