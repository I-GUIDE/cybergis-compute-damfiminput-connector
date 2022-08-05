#!/bin/env python3

import yaml
import os

connector_dict = {'$1': {'Input': {'DamFIMInput': {'dam_id':os.environ['param_dam_id'],'scenarios':os.environ['param_scenarios']}}}}

with open('/job/data/damfiminput.yml','w') as damfile:
    yaml.dump(connector_dict,damfile)
