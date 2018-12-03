# -*- coding: utf-8 -*-
from marvinbot.plugins import Plugin
import logging

log = logging.getLogger(__name__)


class BroadcastPlugin(Plugin):
    def __init__(self):
        super(BroadcastPlugin, self).__init__('broadcast_plugin')

    def get_default_config(self):
        return {
            'short_name': self.name,
            'enabled': True,
        }

    def configure(self, config):
        pass

    def setup_handlers(self, adapter):
        pass

    def setup_schedules(self, adapter):
        pass

    def provide_blueprint(self, config):
        pass
