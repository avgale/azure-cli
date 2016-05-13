from __future__ import print_function

import argparse
import json
import re
import sys

from azure.cli.application import Configuration

PRIMITIVES = (str, int, bool, float)

class Exporter(json.JSONEncoder):

    def default(self, o):#pylint: disable=method-hidden
        try:
            return super(Exporter, self).default(o)
        except TypeError:
            return str(o)

def _extract_non_callable(obj):
    if isinstance(obj, PRIMITIVES):
        return obj
    elif callable(obj):
        return 'function <{}>'.format(obj.__name__)
    elif isinstance(obj, dict):
        new_dict = {key: _extract_non_callable(obj[key]) for key in obj.keys()}
        return new_dict
    elif isinstance(obj, list):
        new_list = [_extract_non_callable(x) for x in obj]
        return new_list

def _extract_command_table_entry(name):
    return next(x for x in cmd_table.values() if name == x['name'])

parser = argparse.ArgumentParser(description='Command Table Parser')
parser.add_argument('--commands', metavar='N', nargs='+', help='Filter by first level command (OR)')
parser.add_argument('--params', metavar='N', nargs='+', help='Filter by parameters (OR)')
args = parser.parse_args()
cmd_set_names = args.commands
param_names = args.params

config = Configuration([])
cmd_table = config.get_command_table()
cmd_list = []
if cmd_set_names is None :
    # if no command prefix specified, use all command table entries
    cmd_list = [x['name'] for x in cmd_table.values()]
else:
    # if the command name matches a prefix, add it to the output list
    for val in cmd_table.values():
        cmd_name = val['name']
        for prefix in cmd_set_names:
            if cmd_name.startswith(prefix):
                cmd_list.append(cmd_name)
                break

results = []
if param_names:
    for name in cmd_list:
        cmd_args = _extract_command_table_entry(name)['arguments']
        match = False
        for arg in cmd_args:
            if match:
                break
            arg_name = re.sub('--','', arg['name']).split(' ')[0]
            if arg_name in param_names:
                results.append(name)
                match = True
else:
    results = cmd_list

heading = '=== COMMANDS IN {} PACKAGE(S) WITH {} PARAMETERS ==='.format(
    cmd_set_names or 'ANY', param_names or 'ANY')
print('\n{}\n'.format(heading))

for cmd_name in results:
    print('== {} =='.format(cmd_name))
    table_entry = _extract_command_table_entry(cmd_name)
    # keep only the JSON Serializable keys
    json_entry = {}
    for key in table_entry.keys():
        json_entry[key] = _extract_non_callable(table_entry[key])
    print(json.dumps(json_entry, indent=2, sort_keys=True), end='\n\n')
    