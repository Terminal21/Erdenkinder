from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from kotti.fanstatic import base_css

library = Library("erdenkinder", "static")
erdenkinder_css = Resource(library, "style.css", depends=[base_css])
erdenkinder_group = Group([erdenkinder_css])
