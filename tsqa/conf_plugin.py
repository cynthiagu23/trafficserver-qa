import logging
import os

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.ConfPlugin')

class ConfPlugin(Plugin):

    name = 'conf-plugin'
    def options(self, parser, env=os.environ):
        """Register commandline options.
        """
        Plugin.options(self, parser, env)
        parser.add_option('--keep-tmp', action='store_true', dest='keep_tmp',
                          help="Keep tmp files after running successfully")
        parser.add_option('--sleep-in-sec', type='int',
                          dest='sleep_in_sec',
                          help='Sleep time before ATS start and after ATS stop to allow enough time for async tests')
        parser.add_option('--standalone-ats-port', type='int',
                          dest='stand_alone',
                          help="Allow standalone test with pre-deployed ATS port")


