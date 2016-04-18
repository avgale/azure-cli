from __future__ import print_function
import argparse
import inspect
import sys
import textwrap
import yaml

from ._locale import L
from ._help_files import _load_help_file

__all__ = ['print_detailed_help', 'print_welcome_message', 'GroupHelpFile', 'CommandHelpFile']

_out = sys.stdout

def show_help(nouns, parser, is_group):
    delimiters = ' '.join(nouns)
    help_file = CommandHelpFile(delimiters, parser) \
        if not is_group \
        else GroupHelpFile(delimiters, parser)

    help_file.load(parser)

    if len(nouns) == 0:
        print('\nSpecial intro help for az')
        help_file.command = 'az'

    print_detailed_help(help_file)

def show_welcome(parser):
    print_welcome_message()

    help_file = GroupHelpFile('', parser)
    print_description_list(help_file.children)

def print_welcome_message():
    _print_indent(L(r"""
     /\                        
    /  \    _____   _ _ __ ___ 
   / /\ \  |_  / | | | \'__/ _ \
  / ____ \  / /| |_| | | |  __/
 /_/    \_\/___|\__,_|_|  \___|
"""))
    _print_indent(L('\nWelcome to the cool new Azure CLI!\n\nHere are the base commands:\n'))

def print_detailed_help(help_file, out=sys.stdout): #pylint: disable=unused-argument
    global _out #pylint: disable=global-statement
    _out = out
    _print_header(help_file)

    _print_indent(L('Arguments') if help_file.type == 'command' else L('Sub-Commands'))

    if help_file.type == 'command':
        print_arguments(help_file)
    elif help_file.type == 'group':
        _print_groups(help_file)

    if len(help_file.examples) > 0:
        _print_examples(help_file)

def print_description_list(help_files, out=sys.stdout):
    global _out #pylint: disable=global-statement
    _out = out

    indent = 1
    max_name_length = max(len(f.name) for f in help_files) if help_files else 0
    for help_file in sorted(help_files, key=lambda h: h.name):
        _print_indent('{0}{1}{2}'.format(help_file.name,
                                         _get_column_indent(help_file.name, max_name_length),
                                         ': ' + help_file.short_summary \
                                             if help_file.short_summary \
                                             else ''),
                      indent)

def print_arguments(help_file):
    indent = 1
    if not help_file.parameters:
        _print_indent('None', indent)
        _print_indent('')
        return

    if len(help_file.parameters) == 0:
        _print_indent('none', indent)
    required_tag = L(' [Required]')
    max_name_length = max(len(p.name) + (len(required_tag) if p.required else 0)
                          for p in help_file.parameters)
    for p in sorted(help_file.parameters, key=lambda p: str(not p.required) + p.name):
        indent = 1
        required_text = required_tag if p.required else ''
        _print_indent('{0}{1}{2}{3}'.format(p.name,
                                            _get_column_indent(p.name + required_text,
                                                               max_name_length),
                                            required_text,
                                            ': ' + p.short_summary if p.short_summary else ''),
                      indent,
                      max_name_length + indent*4 + 2)

        indent = 2
        if p.long_summary:
            _print_indent('{0}'.format(p.long_summary.rstrip()), indent)

        if p.value_sources:
            _print_indent('')
            _print_indent(L("Values from: {0}").format(', '.join(p.value_sources)), indent)
    return indent

def _print_header(help_file):
    indent = 0
    _print_indent('')
    _print_indent(L('Command') if help_file.type == 'command' else L('Group'), indent)

    indent += 1
    _print_indent('{0}{1}'.format(help_file.command,
                                  ': ' + help_file.short_summary
                                  if help_file.short_summary
                                  else ''),
                  indent)

    indent += 1
    if help_file.long_summary:
        _print_indent('{0}'.format(help_file.long_summary.rstrip()), indent)
    _print_indent('')

def _print_groups(help_file):
    indent = 1
    max_name_length = max(len(c.name) for c in help_file.children) \
        if len(help_file.children) > 0 \
        else 0
    for c in sorted(help_file.children, key=lambda h: h.name):
        _print_indent('{0}{1}{2}'.format(c.name,
                                         _get_column_indent(c.name, max_name_length),
                                         ': ' + c.short_summary if c.short_summary else ''),
                      indent)
    _print_indent('')

def _print_examples(help_file):
    indent = 0
    _print_indent(L('Examples'), indent)

    for e in help_file.examples:
        indent = 1
        _print_indent('{0}'.format(e.name), indent)

        indent = 2
        _print_indent('{0}'.format(e.text), indent)


class HelpFile(object): #pylint: disable=too-few-public-methods
    def __init__(self, delimiters):
        self.delimiters = delimiters
        self.name = delimiters.split()[-1] if len(delimiters) > 0 else delimiters
        self.command = delimiters
        self.type = ''
        self.short_summary = ''
        self.long_summary = ''
        self.examples = ''

    def load(self, options):
        self.short_summary = getattr(options, 'description', None)
        file_data = (_load_help_file_from_string(inspect.getdoc(options._defaults.get('func'))) # pylint: disable=protected-access
                     if hasattr(options, '_defaults')
                     else None)

        if file_data:
            self._load_from_data(file_data)
        else:
            self._load_from_file()

    def _load_from_file(self):
        file_data = _load_help_file(self.delimiters)
        if file_data:
            self._load_from_data(file_data)

    def _load_from_data(self, data):
        if not data:
            return

        if isinstance(data, str):
            self.long_summary = data
            return

        if 'type' in data:
            self.type = data['type']

        if 'short-summary' in data:
            self.short_summary = data['short-summary']

        self.long_summary = data.get('long-summary')

        if 'examples' in data:
            self.examples = [HelpExample(d) for d in data['examples']]


class GroupHelpFile(HelpFile): #pylint: disable=too-few-public-methods
    def __init__(self, delimiters, parser):
        super(GroupHelpFile, self).__init__(delimiters)
        self.type = 'group'

        self.children = []
        for options in parser.choices.values():
            delimiters = ' '.join(options.prog.split()[1:])
            child = HelpFile(delimiters)
            child.load(options)
            self.children.append(child)

class CommandHelpFile(HelpFile): #pylint: disable=too-few-public-methods
    def __init__(self, delimiters, parser):
        super(CommandHelpFile, self).__init__(delimiters)
        self.type = 'command'

        self.parameters = []

        for action in [a for a in parser._actions if a.help != argparse.SUPPRESS]: # pylint: disable=protected-access
            self.parameters.append(HelpParameter('/'.join(sorted(action.option_strings)),
                                                 action.help,
                                                 required=action.required))

    def _load_from_data(self, data):
        super(CommandHelpFile, self)._load_from_data(data)

        if isinstance(data, str) or not self.parameters or not data.get('parameters'):
            return

        loaded_params = []
        loaded_param = {}
        for param in self.parameters:
            loaded_param = next((n for n in data['parameters'] if n['name'] == param.name), None)
            if loaded_param:
                param.update_from_data(loaded_param)
            loaded_params.append(param)

        extra_param = next((p for p in data['parameters']
                            if p['name'] not in [lp.name for lp in loaded_params]),
                           None)
        if extra_param:
            raise HelpAuthoringException('Extra help param {0}'.format(extra_param['name']))
        self.parameters = loaded_params


class HelpParameter(object): #pylint: disable=too-few-public-methods
    def __init__(self, param_name, description, required):
        self.name = param_name
        self.required = required
        self.type = 'string'
        self.short_summary = description
        self.long_summary = ''
        self.value_sources = []

    def update_from_data(self, data):
        if self.name != data.get('name'):
            raise HelpAuthoringException("mismatched name {0} vs. {1}"
                                         .format(self.name,
                                                 data.get('name')))

        if self.required != data.get('required', False):
            raise HelpAuthoringException("mismatched required {0} vs. {1}, {2}"
                                         .format(self.required,
                                                 data.get('required'),
                                                 data.get('name')))

        self.type = data.get('type')
        self.short_summary = data.get('short-summary')
        self.long_summary = data.get('long-summary')
        self.value_sources = data.get('populator-commands')


class HelpExample(object): #pylint: disable=too-few-public-methods
    def __init__(self, _data):
        self.name = _data['name']
        self.text = _data['text']

def _print_indent(s, indent=0, subsequent_spaces=-1):
    tw = textwrap.TextWrapper(initial_indent='    '*indent,
                              subsequent_indent=('    '*indent
                                                 if subsequent_spaces == -1
                                                 else ' '*subsequent_spaces),
                              replace_whitespace=False,
                              width=100)
    paragraphs = s.split('\n')
    for p in paragraphs:
        print(tw.fill(p), file=_out)

def _get_column_indent(text, max_name_length):
    return ' '*(max_name_length - len(text))

def _load_help_file_from_string(text):
    try:
        return yaml.load(text) if text else None
    except Exception: #pylint: disable=broad-except
        return text

def _get_single_metadata(cmd_table):
    assert len(cmd_table) == 1
    return next(metadata for _, metadata in cmd_table.items())

class HelpAuthoringException(Exception):
    pass
