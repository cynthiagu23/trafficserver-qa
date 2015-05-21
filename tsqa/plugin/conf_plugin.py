import logging
import os
import traceback

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.ConfPlugin')

class ConfPlugin(Plugin):

    name = 'conf-plugin'
    def options(self, parser, env=os.environ):
        """Register commandline options.
        """
        Plugin.options(self, parser, env)
        parser.add_option('--keep-env', action='store_true', dest='keep_env', default=True,
                          help="Keep env files after running successfully")
        parser.add_option('--sleep-in-sec', type='int', default=0,
                          dest='sleep_in_sec',
                          help='Sleep time before ATS start and after ATS stop to allow enough time for async tests')
        parser.add_option('--standalone-ats-port', type='int', default=-1,
                          dest='standalone_ats_port',
                          help="Allow standalone test with pre-deployed ATS port")

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        global args
        args = options
