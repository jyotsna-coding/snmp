"""
This file loads all constants in yaml config file into a variable conf
"""

import sys
import os
import yaml

def load_config(file):
    try:
        with open(file) as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            for doc in docs:
                if 'staging' in doc:
                    return doc['staging']
                else:
                    sys.exit()
    except Exception as e:
        print(e)


file_path = os.path.dirname(os.path.realpath(__file__))
# print("The file path is",file_path)
conf_dir = os.path.join(file_path,'conf')
# print("The conf dir is in",conf_dir)
conf_file = os.path.join(conf_dir,'config.yaml')
conf = load_config(conf_file)
# print("Conf file has",conf['log_dir'])