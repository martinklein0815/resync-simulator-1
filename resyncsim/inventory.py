#!/usr/bin/env python
# encoding: utf-8
"""
inventory.py: A collection of inventory implementations.

Created by Bernhard Haslhofer on 2012-04-26.
Copyright 2012, ResourceSync.org. All rights reserved.
"""

import tornado.web

class Inventory(object):
    """An inventory knows about a source and produces info about it contents"""
    
    def __init__(self, source):
        self.source = source


class DynamicSiteMap(Inventory):
    """A dynamic sitemap is generated on the fly"""

    def __init__(self, source, config):
        super(DynamicSiteMap, self).__init__(source)
        print "\n*** Instantiated Dynamic SiteMap Generator ***"
        
    @property
    def handlers(self):
        return [(r"/sitemap.xml", 
                DynamicSiteMapHandler,
                dict(source = self.source)),
                (r"/inventory", 
                DynamicSiteMapHandler,
                dict(source = self.source)),
        ]


class DynamicSiteMapHandler(tornado.web.RequestHandler):
    """The HTTP request handler for the DynamicSiteMapInventory"""

    def initialize(self, source):
        self.source = source
    
    def get(self):
        self.set_header("Content-Type", "application/xml")
        self.render("sitemap.xml",
                    resources = self.source.resources.values())
    