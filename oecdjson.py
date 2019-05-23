# -*- coding: utf-8 -*-

import json
import requests
from pyloco import Task

default_dataset = "QNA"
default_filter = "USA+KOR+CHN.GDP+B1_GE.CUR+VOBARSA.Q"
default_agency = "all"

class OECDJson(Task):
    """collects OECD statistics in JSON format

'oecdjson' task downloads OECD statistics from OECD web-site in JSON format
and optionally save the collected in a file for later use.
To access OECD data, the task internally use the following URL syntax:
'http://stats.oecd.org/SDMX-JSON/data/<dataset>/<filter>/<agency>[?<parameters>]'
You can specify your own data query using command-line options. Please run 
'pyloco oecejson -h' after installation of this task.

Example(s)
----------

Following command collect OECD stats of dataset='%s', filter='%s',
agency='%s', and save the collected data to 'oecd.json'.
>>> pyloco oecejson -o oecd.json
""" % (default_dataset, default_filter, default_agency)

    _name_ = "oecdjson"
    _version_ = "0.1.0"

    def __init__(self, parent):

        self.add_option_argument("-d", "--dataset", metavar="dataset",
                default=default_dataset, help="Dataset code (default='%s')"
                % default_dataset) 

        self.add_option_argument("-f", "--filter", metavar="filter",
                default=default_filter, help="Query filter(default='%s')"
                % default_filter)

        self.add_option_argument("-a", "--agency", metavar="agency",
                default=default_agency, help="Agency code. (default='%s')"
                % default_agency) 

        self.add_option_argument("-p", "--params", metavar="params",
                help="Additional parameters") 

        self.add_option_argument("-o", "--outfile", metavar="outfile",
                help="Save OECD data in a file") 

        self.register_forward("data", help="OECD stats in JSON format ")

    def perform(self, targs):

        if targs.params:
            params = "?" + targs.params

        else:
            params = ""

        url = ("https://stats.oecd.org/SDMX-JSON/data/%s/%s/%s%s" %
               (targs.dataset, targs.filter, targs.agency, params))

        r = requests.get(url)

        data = None

        if r.status_code == 200:
            data = r.json()

        if data is not None and targs.outfile:
            with open(targs.outfile, "w") as f:
                json.dump(data, f, indent=2)

        self.add_forward(data=data)
