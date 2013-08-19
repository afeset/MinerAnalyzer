#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file contains definition of lexer and parser for miner language
#

from expressions import *
import commands
import io_command
import statements
import common
import loggers
import miner_globals
import os.path
import re

#####################
# Syntax token definitions
#####################

tokens = [
    'INTEGER', 'HEXINTEGER', 'OCTINTEGER', 'BININTEGER',
    'FLOAT',
    'STRING',
    'ID',
    'GE', 'LE', 'EQ', 'NEQ', 'POW',
    'MATCH_EQ', 'MATCH_NEQ',
    'INCR', 'DECR',
    'FILENAME', 'STREAMTYPE', 'STREAMVAR',
    'ALIAS_ID',
    'SHIFT_LEFT', 'SHIFT_RIGHT',
    'FLOORDIV', 'BINARY_OR',
    'RAWSTRING',
    ]

states = (
    ('files', 'inclusive'),
    ('raw', 'inclusive'),
)

reserved = {
    'not'   : 'NOT',
    'or'    : 'OR',
    'and'   : 'AND',
    'in'    : 'IN',
    'is'    : 'IS',
    'True'  : 'TRUE',
    'False' : 'FALSE',
    'None'  : 'NONE',
    'as'    : 'AS',
    'ASC'   : 'ASC',
    'DESC'  : 'DESC',
    'FROM'  : 'FROM',
    'for'   : 'LC_FOR',
    'IN'    : 'UC_IN',
    'BY'    : 'BY',
    }

for c in commands.NAMES + statements.NAMES + io_command.SOURCE_COMMAND_NAMES + io_command.DESTINATION_COMMAND_NAMES:
    reserved[c] = c

tokens.extend(list(reserved.values()))

literals = [',', '.', '+', '-', '*', '%', '/', '=', '<', '>', '?', '(', ')', '|', '[', ']', ':', '&', '^', '@', ';']

t_raw_RAWSTRING = r'.+'
t_STRING = r'\"([^\\"]|(\\.))*\"'
t_INTEGER    = r'[1-9]\d*[lL]?|0'
t_HEXINTEGER = r'0[xX][0-9a-fA-F]+[lL]?'
t_OCTINTEGER = r'0[oO]?[0-7]+[lL]?'
t_BININTEGER = r'0[bB][0-1]+[lL]?'
t_GE  = r'>='
t_LE  = r'<='
t_EQ  = r'=='
t_NEQ = r'!='
t_MATCH_EQ  = r'=~'
t_MATCH_NEQ = r'!~'
t_POW  = r'\*\*'
t_INCR = r'\+\+'
t_DECR = r'--'
t_SHIFT_LEFT  = r'\<\<'
t_SHIFT_RIGHT = r'\>\>'
t_FLOORDIV    = r'//'
t_BINARY_OR   = r'\|\|'

t_ignore  = ' \t'
t_files_ignore  = ' \t'

tpart_exponent      =  r"[eE][-+]?\d+"
tpart_fraction      =  r"\.\d+"
tpart_pointfloat    =  r"(\d+)?(%s)|(\d+)\." % tpart_fraction
tpart_exponentfloat =  r"(\d+|%s)%s" % (tpart_pointfloat, tpart_exponent)

t_FLOAT = "%s|%s" % (tpart_pointfloat, tpart_exponentfloat)

def t_NUMBERBYTES(t):
    r"\d+[TGMK]B"
    number = int(t.value[:-2])
    prefix = t.value[-2]
    if prefix=="T":
        number *= 1024 * 1024 * 1024 * 1024
    elif prefix=="G":
        number *= 1024 * 1024 * 1024
    elif prefix == "M":
        number *= 1024 * 1024
    elif prefix == "K":
        number *= 1024
    t.value = str(number)
    t.type = "INTEGER"
    return t

def t_NUMBERSUFFIX(t):
    r"\d+(T|G|M|K|d|h|m)"
    number = int(t.value[:-1])
    suffix = t.value[-1]
    if suffix=="T":
        number *= 1000*1000*1000*1000
    elif suffix=="G":
        number *= 1000000000
    elif suffix == "M":
        number *= 1000000
    elif suffix == "K":
        number *= 1000
    elif suffix == "d":
        number *= 24*3600
    elif suffix == "h":
        number *= 3600
    elif suffix == "m":
        number *= 60
    t.value = str(number)
    t.type = "INTEGER"
    return t

def t_files_STREAMTYPE(t):
    r'\<[a-zA-Z0-9]+\>'
    t.value = t.value[1:-1]
    return t

def t_files_STREAMVAR(t):
    r"""[a-zA-Z]\w*=([^ \t]*|"[^"]*"|'[^']*')"""
    equal = t.value.index('=')
    t.value = (t.value[:equal], t.value[equal+1:])
    return t

# This token is used to specify filenames or filename patterns
# it is active only in the <files> state (after READ and WRITE)
def t_files_FILENAME(t):
    r'[^ \t\n\",|\<\>=]+'
    return t

def t_rSTRING(t):
    r"""r?\"([^\\"]|(\\.))*\"|r?'([^\\']|(\\.))*'"""
    t.type = 'STRING'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type in ['READ', 'WRITE', 'SOURCE', 'HELP']:
        # we need to switch to the special lexing state which accepts only files
        t.lexer.begin('files')
    elif t.type == 'PARAM':
        t.lexer.begin('raw')
    elif statements.aliasCommands.get(t.value, None):
        t.type = 'ALIAS_ID'

    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def t_files_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# parsing rules
precedence = (
    ('right', '?', 'CONDITIONAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'UNARY_NOT'),
    ('left', '<', '>', 'LE', 'GE', 'EQ', 'NEQ', 'IN', 'IS'),
    ('nonassoc', 'MATCH_EQ', 'MATCH_NEQ' ),
    ('left', '|'),
    ('left', '^'),
    ('left', '&'),
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
    ('right', 'UNARY'),
    ('right', 'POW'),
    ('left', '.', '(', '[', 'POSTFIX')
)

#########
# Define parsing rules
#########

# Miner accept different type of statements:
def p_statement(p):
    '''statement : mining_command
                | set_statement
                | show_statement
                | show_all_statement
                | alias_statement
                | import_statement
                | source_statement
                | help_statement
                | eval_statement
                | history_statement
                | usage_statement
                | doc_statement
                | exit_statement'''
    p[0] = p[1]

def p_mining_command(p):
    '''mining_command : source '|' command_chain '|' destination'''
    p[0] = statements.MiningCommand(p[1], p[3], p[5])

def p_set_statement(p):
    '''set_statement : SET ID '=' expression '''
    statements.Set.setValue(p[2], p[4])

def p_set_show_statement(p):
    '''show_statement : SET ID'''
    statements.Set.show(p[2])

def p_set_show_all_statement(p):
    '''show_all_statement : SET'''
    statements.Set.showAll()

def p_set_remove_statement(p):
    '''show_all_statement : SET '-'  ID'''
    statements.Set.remove(p[3])

def p_alias_statement(p):
    '''alias_statement : ALIAS ID '=' command_chain
                       | ALIAS ALIAS_ID '=' command_chain'''
    statements.Alias.add(p[2], p[4])

def p_alias_statement_described(p):
    '''alias_statement : ALIAS STRING ID '=' command_chain
                       | ALIAS STRING ALIAS_ID '=' command_chain'''
    statements.Alias.add(p[3], p[5], p[2][1:-1])

def p_alias_show(p):
    '''alias_statement : ALIAS'''
    statements.Alias.show()

def p_alias_remove(p):
    '''alias_statement : ALIAS '-' ALIAS_ID'''
    statements.Alias.remove(p[3])

def p_import_statement(p):
    '''import_statement : IMPORT import_name'''
    statements.Import.add(p[2])

def p_import_show(p):
    '''import_statement : IMPORT'''
    statements.Import.show()

def p_import_remove(p):
    '''import_statement : IMPORT '-' import_name'''
    statements.Import.remove(p[3])

def p_source_statement(p):
    '''source_statement : SOURCE FILENAME'''
    p.lexer.begin("INITIAL")
    statements.SourceStatement.execute(p[2])

# Generic help
def p_help_statement(p):
    '''help_statement : HELP'''
    statements.Help.printHelp()

# Get help with single keyword (use filename as HACK to skip specifying all keywords explicitly)
def p_help_statement_ID(p):
    '''help_statement : HELP FILENAME'''
    statements.Help.printHelp(p[2])

# Get help for 2 part keyword (e.g. "FOR DISTINCT")
def p_help_statement_ID_ID(p):
    '''help_statement : HELP FILENAME FILENAME'''
    statements.Help.printHelp("%s %s" % (p[2], p[3]))

def p_eval_statement(p):
    '''eval_statement : EVAL expression'''
    p[0] = statements.EvalStatement(p[2])

def p_history_statement(p):
    '''history_statement : HISTORY'''
    statements.History.execute()

def p_history_statement_limit(p):
    '''history_statement : HISTORY integer'''
    statements.History.execute(int(p[2]))

def p_usage_statement(p):
    '''usage_statement : USAGE STRING usage_params'''
    statements.Usage.execute(p[2][1:-1], p[3])

def p_doc_statement(p):
    '''doc_statement : DOC import_name'''
    p[0] = statements.DocStatement(p[2])

def p_exit_statement(p):
    '''exit_statement : EXIT'''
    statements.ExitStatement.execute()

def p_exit_statement_with_code(p):
    '''exit_statement : EXIT integer'''
    statements.ExitStatement.execute(int(p[2]))

def p_param_statement(p):
    '''statement : PARAM RAWSTRING'''
    nameValue = p[2]
    nameValue.lstrip()
    pos = nameValue.find('=')
    if pos<=0:
        raise common.CompilerSyntaxError(p.lexpos(2))
    if pos>1 and nameValue[pos-1]=='?':
        isConditional = True
        name = nameValue[:pos-1]
    else:
        isConditional = False
        name = nameValue[:pos]
    name = name.rstrip()
    value = nameValue[pos+1:]
    if not re.match("^[_a-zA-Z][_a-zA-Z0-9]*$", name):
        raise common.CompilerSyntaxError(p.lexpos(2))
    if isConditional:
        statements.ParamStatement.setValueIfNotDefined(name, value)
    else:
        statements.ParamStatement.setValue(name, value)
    
########################
# Sub rules
########################

# Import statement
def p_import_name(p):
    '''import_name : ID'''
    p[0] = p[1]

def p_import_name_ID(p):
    '''import_name : import_name '.' ID'''
    p[0] = p[1] + '.' + p[3]

# usage statement

def p_usage_params(p):
    '''usage_params : usage_param'''
    p[0] = [ p[1] ]

def p_usage_params_param(p):
    '''usage_params :  usage_params usage_param'''
    p[0] = p[1]
    p[0].append(p[2])

def p_usage_param(p):
    '''usage_param : ID  '=' STRING
                   | '*' '=' STRING
                   | '>' '=' STRING
                   | INTEGER '=' STRING'''
    p[0] = { 'name': p[1], 'description': p[3][1:-1] }

def p_usage_param_GE(p):
    '''usage_param : GE STRING'''
    p[0] = { 'name': '>', 'description': p[2][1:-1] }

def p_usage_param_optional(p):
    '''usage_param : '[' usage_param ']' '''
    p[0] = p[2]
    p[0]['isOptional'] = 1

#####################
# Mining statement
#####################
def p_destination(p):
    '''destination : WRITE streamvar_list FILENAME'''
    p[0] = io_command.Destination(p[3], streamVars = p[2])
    # we are now in file state so pop back
    p.lexer.begin("INITIAL")

def p_typed_destination(p):
    '''destination : WRITE STREAMTYPE streamvar_list FILENAME'''
    p[0] = io_command.Destination(p[4], destinationType=p[2], streamVars=p[3])
    # we are now in file state so pop back
    p.lexer.begin("INITIAL")

def p_destination_stdout(p):
    '''destination : STDOUT'''
    p[0] = io_command.Destination("stdout", "stdout")

def p_source(p):
    '''source : READ streamvar_list filename_list'''
    p[0] = io_command.Source(p[3], streamVars=p[2])
    p.lexer.begin('INITIAL')

def p_typed_source(p):
    '''source : READ STREAMTYPE streamvar_list filename_list'''
    p[0] = io_command.Source(p[4], sourceType=p[2], streamVars=p[3])
    p.lexer.begin('INITIAL')

def p_iterator_source(p):
    '''source : ITERATE ID IN expression'''
    p[0] = io_command.IteratorStream([p[2]], p[4].getValue())

def p_iterator_source_dictionary(p):
    '''source : ITERATE ID ',' ID IN expression'''
    p[0] = io_command.IteratorStream([p[2], p[4]], p[6].getValue())

def p_command_chain_command(p):
    '''command_chain : command'''
    if isinstance(p[1], list):
        p[0] = list(p[1])
    else:
        p[0] = [p[1]]

def p_command_chain_add_command(p):
    '''command_chain : command_chain '|' command'''
    p[0] = p[1]
    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].append(p[3])

# Filename list
# used in "source"
def p_filename_list(p):
    '''filename_list : FILENAME '''
    p[0] = [ p[1] ]

def p_filename_list_FILENAME(p):
    '''filename_list : filename_list FILENAME '''
    p[0] = p[1]
    p[0].append(p[2])

# Stream variables used in source and destination
def p_streamvar_list(p):
    '''streamvar_list : '''
    p[0] = {}

def p_streamvar_list_streamvar(p):
    '''streamvar_list : streamvar_list STREAMVAR'''
    p[0] = p[1]
    p[0][p[2][0]] = p[2][1]

# Mining command definitions
def p_command(p):
    '''command : accumulate_command
               | select_command
               | if_command
               | limit_command
               | parse_command
               | sortby_command
               | top_command
               | bottom_command
               | alias_command
               | expand_command
               | for_command
               | match_command
               | pass_command'''
    p[0] = p[1]

def p_accumulate_coals(p):
    '''accumulate_command :
                          | ACCUMULATE'''
    p[0] = commands.AccumulateCoals()

def p_accumulate_command(p):
    '''accumulate_command : ACCUMULATE ID BY import_name'''
    p[0] = commands.AccumulateCommand(p[2], p[4])

def p_select_command(p):
    '''select_command : SELECT named_expression
                      | DISTINCT named_expression'''
    if p[1] == 'SELECT':
        p[0] = commands.SelectCommand()
    elif p[1] == 'DISTINCT':
        p[0] = commands.DistinctCommand()
    p[0].add(p[2])

def p_select_command_expression(p):
    '''select_command : select_command ',' named_expression'''
    p[0] = p[1]
    p[0].add(p[3])

def p_select_command_all(p):
    '''select_command : SELECT '*' '''
    p[0] = commands.SelectCommand()
    p[0].add('*')

def p_select_command_add_all(p):
    '''select_command : select_command ',' '*' '''
    p[0] = p[1]
    p[0].add('*')

def p_select_command_prepare_list(p):
    '''select_command : SELECT '[' named_parameter_list ']' named_expression
                      | DISTINCT '[' named_parameter_list ']'  named_expression'''
    if p[1] == 'SELECT':
        p[0] = commands.SelectCommand(p[3])
    elif p[1] == 'DISTINCT':
        p[0] = commands.DistinctCommand(p[3])
    p[0].add(p[5])

def p_if_command(p):
    '''if_command : IF expression'''
    p[0] = commands.IfCommand(p[2])

def p_if_command_prepare_list(p):
    '''if_command : IF '[' named_parameter_list ']' expression'''
    p[0] = commands.IfCommand(p[3], p[5])

def p_limit_command(p):
    '''limit_command : LIMIT integer'''
    p[0] = commands.LimitCommand(int(p[2]))

def p_parse_command(p):
    '''parse_command : PARSE ID'''
    if p[2] == "request":
        p[0] = commands.ParseRequestCommand()
    elif p[2] == "response":
        p[0] = commands.ParseResponseCommand()
    else:
        raise common.CompilerSyntaxError(p.lexpos(2)+len(p[2]))

def p_parse_from_command(p):
    '''parse_command : PARSE ID FROM expression'''
    if p[2] == "request":
        p[0] = commands.ParseRequestCommand(p[4])
    elif p[2] == "response":
        p[0] = commands.ParseResponseCommand(p[4])
    elif p[2] == "uri":
        p[0] = commands.ParseUriCommand(p[4])
    else:
        raise common.CompilerSyntaxError(p.lexpos(2)+len(p[2]))

def p_match_command(p):
    '''match_command : MATCH expression MATCH_EQ STRING'''
    p[0] = commands.MatchCommand(p[2], p[4])

def p_for_select_command(p):
    '''for_command : FOR SELECT aggregated_named_expression_list'''
    p[0] = commands.ForSelectCommand(p[3])

def p_for_dinstinct_select_command(p):
    '''for_command : FOR DISTINCT named_expression_list SELECT aggregated_named_expression_list'''
    p[0] = commands.ForDistinctSelectCommand(p[3], p[5])

def p_for_in_select_command(p):
    '''for_command : FOR named_expression UC_IN expression SELECT aggregated_named_expression_list'''
    p[0] = commands.ForInSelectCommand(p[2], p[4], p[6])

def p_sortby_command(p):
    '''sortby_command : SORTBY expression'''
    p[0] = commands.SortbyCommand(p[2], True)

def p_sortby_direction_command(p):
    '''sortby_command : SORTBY expression ASC
                      | SORTBY expression DESC'''
    p[0] = commands.SortbyCommand(p[2], (p[3] == 'ASC'))

def p_top_command(p):
    '''top_command : TOP integer expression'''
    p[0] = commands.TopCommand(p[2], p[3])

def p_bottom_command(p):
    '''bottom_command : BOTTOM integer expression'''
    p[0] = commands.BottomCommand(p[2], p[3])

def p_alias_command(p):
    '''alias_command : ALIAS_ID'''
    commandList = statements.aliasCommands.get(p[1], None)
    p[0] = commandList

def p_expand_command(p):
    '''expand_command : EXPAND expression AS id_list'''
    p[0] = commands.ExpandCommand(p[2], p[4])

def p_expand_command_select(p):
    '''expand_command : EXPAND expression AS id_list SELECT named_expression_list'''
    p[0] = commands.ExpandCommand(p[2], p[4], p[6])

def p_pass_command(p):
    '''pass_command : PASS expression
                    | PASS assign_expression'''
    p[0] = commands.PassCommand()
    p[0].add(p[2])

def p_pass_command_expression(p):
    '''pass_command : pass_command ';' expression
                    | pass_command ';' assign_expression'''
    p[0] = p[1]
    p[0].add(p[3])

#####################
# Expression rules
#####################
def p_expression(p):
    '''expression : ID'''
    p[0] = Expression()
    p[0].setId(p[1])

def p_expression_constant(p):
    '''expression : constant '''
    p[0] = Expression()
    p[0].setValue(p[1])

def p_integer(p):
    '''integer : INTEGER
                | HEXINTEGER
                | OCTINTEGER
                | BININTEGER'''
    p[0] = p[1]

def p_constant(p):
    '''constant : integer
                | FLOAT
                | STRING
                | TRUE
                | FALSE
                | NONE '''
    p[0] = p[1]
def p_expression_deref(p):
    '''expression : expression '.' ID'''
    p[0] = Expression()
    p[0].setDeref(p[1], p[3])

def p_expression_index(p):
    '''expression : expression '[' expression ']' %prec POSTFIX'''
    p[0] = Expression()
    p[0].setListAccess(p[1], p[3])

def p_expression_range_from_to(p):
    '''expression : expression '[' expression ':' expression ']' %prec POSTFIX'''
    p[0] = Expression()
    p[0].setListRange(p[1], p[3], p[5])

def p_expression_range_from(p):
    '''expression : expression '[' expression ':' ']' %prec POSTFIX'''
    p[0] = Expression()
    p[0].setListRange(p[1], p[3], None)

def p_expression_range_to(p):
    '''expression : expression '[' ':' expression ']' %prec POSTFIX'''
    p[0] = Expression()
    p[0].setListRange(p[1], None, p[4])

def p_expression_range_whole(p):
    '''expression : expression '[' ':' ']' %prec POSTFIX'''
    p[0] = Expression()
    p[0].setListRange(p[1], None, None)

def p_named_expression_list(p):
    '''named_expression_list : named_expression'''
    p[0] = [ p[1] ]

def p_named_expression_list_named_expression(p):
    '''named_expression_list : named_expression_list ',' named_expression'''
    p[0] = p[1]
    p[0].append(p[3])

def p_aggregated_named_expression_list(p):
    '''aggregated_named_expression_list : aggregated_named_expression'''
    p[0] = [ p[1] ]

def p_aggregated_named_expression_list_named_expression(p):
    '''aggregated_named_expression_list : aggregated_named_expression_list ',' aggregated_named_expression'''
    p[0] = p[1]
    p[0].append(p[3])

def p_aggregated_named_expression(p):
    '''aggregated_named_expression : import_name named_expression'''
    p[0] = (p[1], p[2])

def p_named_expression(p):
    '''named_expression : expression'''
    p[0] = p[1]

def p_named_expression_as(p):
    '''named_expression : expression AS ID'''
    p[0] = p[1]
    p[0].setName(p[3])

def p_id_list(p):
    '''id_list : ID'''
    p[0] = [ p[1] ]

def p_id_list_id(p):
    '''id_list : id_list ',' ID'''
    p[0] = p[1]
    p[0].append(p[3])

#################
# Arithmetical expressions
#################
def p_exp_binary_exp(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '%' expression
                  | expression POW expression
                  | expression '<' expression
                  | expression '>' expression
                  | expression LE   expression
                  | expression GE   expression
                  | expression EQ   expression
                  | expression NEQ  expression
                  | expression OR   expression
                  | expression AND  expression
                  | expression IN   expression
                  | expression IS   expression
                  | expression '&'  expression
                  | expression '^'  expression
                  | expression SHIFT_LEFT  expression
                  | expression SHIFT_RIGHT expression
                  | expression FLOORDIV    expression'''
    p[0] = Expression()
    p[0].setBinary(p[1], p[2], p[3])

def p_assign_expression(p):
    '''assign_expression : expression '=' expression'''
    p[0] = Expression()
    p[0].setBinary(p[1], p[2], p[3])

def p_exp_not_in_exp(p):
    '''expression : expression NOT IN expression %prec IN'''
    p[0] = Expression()
    p[0].setBinary(p[1], "not in", p[4])

def p_exp_is_not_exp(p):
    '''expression : expression IS NOT expression %prec IS'''
    p[0] = Expression()
    p[0].setBinary(p[1], "is not", p[4])

def p_expression_binary_or(p):
    '''expression : expression BINARY_OR expression '''
    p[0] = Expression()
    p[0].setBinary(p[1], '|', p[3])

def p_unary_exp(p):
    '''expression : '-' expression %prec UNARY
                  | '+' expression %prec UNARY
                  | '~' expression %prec UNARY
                  | NOT expression %prec UNARY_NOT'''
    p[0] = Expression()
    p[0].setUnary(p[1], p[2])

def p_expression_brackets(p):
    "expression : '(' expression ')'"
    p[0] = Expression()
    p[0].setBracketExpression(p[2])

def p_expression_match(p):
    "expression : expression MATCH_EQ expression"
    p[0] = MatchExpression(p[1], p[3])

def p_expression_nmatch(p):
    "expression : expression MATCH_NEQ expression"
    p[0] = MatchExpression(p[1], p[3], negate=True)

def p_function_call(p):
    "expression : expression '(' expression_list ')' %prec POSTFIX"
    p[0] = Expression()
    p[0].setFunctionCall(p[1], p[3], None)

def p_function_call_named_parameters(p):
    "expression : expression '(' named_parameter_list ')' %prec POSTFIX"
    p[0] = Expression()
    p[0].setFunctionCall(p[1], None, p[3])

def p_function_call_both_types_of_parameters(p):
    "expression : expression '(' not_empty_expression_list ',' named_parameter_list ')' %prec POSTFIX"
    p[0] = Expression()
    p[0].setFunctionCall(p[1], p[3], p[5])

def p_expression_list(p):
    "expression_list : "
    p[0] = []

def p_expression_list_not_empty_expression_list(p):
    "expression_list : not_empty_expression_list"
    p[0] = p[1]

def p_not_empty_expression_list(p):
    "not_empty_expression_list : expression"
    p[0] = [ p[1] ]

def p_not_empty_expression_list_expression(p):
    "not_empty_expression_list : not_empty_expression_list ',' expression"
    p[0] = p[1]
    p[0].append(p[3])

def p_named_parameter_list(p):
    '''named_parameter_list : ID '=' expression'''
    exp = Expression()
    exp.setAssignment(p[1], p[3])
    p[0] = [ exp ]

def p_named_parameter_list_named_parameter(p):
    '''named_parameter_list : named_parameter_list ',' ID '=' expression'''
    p[0] = p[1]
    newExp = Expression()
    newExp.setAssignment(p[3], p[5])
    p[0].append(newExp)

def p_list_expression(p):
    '''expression : '[' expression_list ']' '''
    p[0] = Expression()
    p[0].setList(p[2])

def p_conditional_expression(p):
    '''expression : expression '?' expression ':' expression %prec CONDITIONAL'''
    p[0] = Expression()
    p[0].setConditional(p[1], p[3], p[5])

# Tuples
def p_expression_tuple_with_coma(p):
    '''expression : '(' tuple_with_coma ')' '''
    p[0] = Expression()
    p[0].setTupleWithComa(p[2])

def p_expression_tuple_without_coma(p):
    '''expression : '(' tuple_without_coma ')' '''
    p[0] = Expression()
    p[0].setTupleWithoutComa(p[2])

def p_tuple_with_coma(p):
    '''tuple_with_coma : expression ',' '''
    p[0] = [p[1]]

def p_tuple_without_coma(p):
    '''tuple_without_coma : tuple_with_coma expression '''
    p[0] = p[1]
    p[0].append(p[2])

def p_tuple_with_coma_without(p):
    '''tuple_with_coma : tuple_without_coma ',' '''
    p[0] = p[1]

# Counter expressions
def p_expression_counter_expression(p):
    '''expression : counter_expression '''
    p[0] = p[1]

def p_counter_expression(p):
    '''counter_expression : '@' ID '''
    p[0] = CounterExpression(p[2])

def p_counter_expression_preIncr(p):
    '''counter_expression : INCR counter_expression '''
    p[0] = p[2]
    p[0].preIncr()

def p_counter_expression_postIncr(p):
    '''counter_expression : counter_expression INCR '''
    p[0] = p[1]
    p[0].postIncr()

def p_counter_expression_preDecr(p):
    '''counter_expression : DECR counter_expression '''
    p[0] = p[2]
    p[0].preDecr()

def p_counter_expression_postDecr(p):
    '''counter_expression : counter_expression DECR '''
    p[0] = p[1]
    p[0].postDecr()

def p_counter_expression_add(p):
    '''counter_expression : counter_expression '+' '=' expression'''
    p[0] = p[1]
    p[0].add(p[4])

def p_counter_expression_sub(p):
    '''counter_expression : counter_expression '-' '=' expression'''
    p[0] = p[1]
    p[0].sub(p[4])

def p_list_comprehension(p):
    '''expression : expression LC_FOR ID IN expression'''
    p[0] = Expression()
    p[0].setListComprehension(p[1], p[3], p[5])

# Error rule for syntax errors
def p_error(t):
    raise common.CompilerSyntaxError(t.lexpos if t else -1)


import ply.yacc as yacc
#lexer = lex.lex(debug=True,debuglog=log)

# If write_tables=0 is not specified
# yacc parser will write down parsing table file to decrease startup
# times next time miner loads
#parser = yacc.yacc(debug=0, write_tables=0)
minerTablesFileName = os.path.join("~", ".minerparsetables")
if miner_globals.runsUnderPypy:
    minerTablesFileName += "_pypy"
minerTablesFileName = os.path.expanduser(minerTablesFileName)
parser = yacc.yacc(debug=0, errorlog=loggers.compileLog, picklefile=minerTablesFileName)
 
def parseCommand(command):
    if miner_globals.debugMode:
        loggers.compileLog.info("Compiling %s" % command)
    lexer.begin('INITIAL')
    if miner_globals.debugMode:
        debug = loggers.basicLog
    else:
        debug = 0
    result = parser.parse(command, debug=debug)
    if result and miner_globals.debugMode:
        loggers.compileLog.info("Dumping command to execute\n%s" % result.getCommand())
    return result

