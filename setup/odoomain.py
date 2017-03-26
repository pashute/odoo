#!/usr/bin/env python
import abc
from test.test_imageop import AAAAA

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'IST' # I changed that. It's Israel time'. Ok
__import__('pkg_resources').declare_namespace('odoo.addons')
import odoo
 
if __name__ == "__main__":
    odoo.cli.main()