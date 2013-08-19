#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file contains definition of different commands used in mining statement
# Each command is responsible to create code text for its generator function
#

from common import *
from expressions import *
import aggregate
import runtime

# First name of commands:
# Multiple commands may share the same first name.
# This list is used for syntax tokens specifications and for completion
NAMES = [ 'SELECT', 'DISTINCT', 'IF', 'LIMIT', 'PARSE', 'SORTBY', 'FOR', 'ACCUMULATE', 'EXPAND', 'MATCH', 'TOP', 'BOTTOM', 'PASS' ]

def createTupleString(listValues):
    if len(listValues) == 1:
        return "( %s, )" % listValues[0]
    else:
        return "( " + ", ".join(listValues) + " )"

def createNamedParameters(listValues):
    return ", ".join("%s = %s" % (e,e) for e in listValues)

class CommandBase(GeneratorBase):
    '''
    Base class for all commands
    '''
    def __init__(self):
        GeneratorBase.__init__(self)
    def createGenerator(self, name, parentGeneratorName):
        '''
        Main logic of a command
        It is responsible to generate code which performs command logic: yield records
          parentGeneratorName - name of parent generator function
          returns - string containing implementation of command logic
        '''
        raise NotImplementedError
    def getVariableNames(self):
        '''
        Returns record variables of the command
        '''
        raise NotImplementedError
    def getRequiredVars(self):
        '''
        Returns list of variables used in command for some minimal validation
        '''
        return []

class TypicalCommand(CommandBase):
    '''
    Typical command consists of main loop over parent generator
    with hook places for start section before loop, loop body and end section after loop
    '''
    def __init__(self, preparationList = None):
        '''
        preparationList - specifies list of expressions that should be evaluated before actual command execution
        '''
        CommandBase.__init__(self)
        self.myPreparationList = preparationList
    def createGenerator(self, name, parentGeneratorName):
        return """
def %s():
%s
    for %s in %s():
%s
%s
%s
""" %   (name, self.getStart(), createTupleString(self.myParent.getVariableNames()), parentGeneratorName, self.getPreparationList(), self.getBody(), self.getEnd())

    def getBody(self):
        '''Returns loop body - alignment 8 spaces'''
        raise NotImplementedError
    def getEnd(self):
        '''Returns section after loop - alignment 4 spaces'''
        return ""
    def getStart(self):
        '''Returns section before loop - alignment 4 spaces'''
        # create global explessions
        globalExps = self.getGlobalExpressions()
        s = ""
        for g in globalExps:
            s += g.getGlobalSection()
        return s
    def getGlobalExpressions(self):
        globalExps = []
        if self.myPreparationList:
            for exp in self.myPreparationList:
                globalExps.extend(exp.getGlobalExpressions() )
        return globalExps
    def getPreparationList(self):
        s = ""
        if self.myPreparationList:
            for exp in self.myPreparationList:
                s += """        %s""" % exp.getValue()
        return s


class AccumulateCommand(TypicalCommand):
    NAME = "ACCUMULATE"
    SHORT_HELP = "ACCUMULATE|<empty> - accumulates coal records"
    LONG_HELP = """ACCUMULATE
<empty>
    Accumulates coal records according to the sysId, vaId, flowId and transactionId
    coal record is released when decoding information becomes available
"""
    def __init__(self, accumulatorVariable, accumulatorClass):
        TypicalCommand.__init__(self)
        self.myAccumulatorVariable = accumulatorVariable
        self.myAccumulatorClass = accumulatorClass
    def getStart(self):
        return """    accumulator = %s()\n""" % self.myAccumulatorClass
    def getBody(self):
        return """
        %s = accumulator.accumulate(%s)
        if %s:
            yield %s
        
""" % (self.myAccumulatorVariable, self.myAccumulatorVariable, self.myAccumulatorVariable, createTupleString(self.getVariableNames()) )

    def getEnd(self):
        return """
    %s = accumulator.final()
    if %s:
        yield %s
""" % (self.myAccumulatorVariable, self.myAccumulatorVariable, createTupleString(self.getVariableNames()) )
    def getRequiredVariables(self):
        return [self.myAccumulatorVariable]

    def getVariableNames(self):
        return self.myParent.getVariableNames()

class AccumulateCoals(TypicalCommand):
    NAME = "ACCUMULATE"
    SHORT_HELP = "ACCUMULATE|<empty> - accumulates coal records"
    LONG_HELP = """ACCUMULATE
<empty>
    Accumulates coal records according to the sysId, vaId, flowId and transactionId
    coal record is released when decoding information becomes available
"""
    def getStart(self):
        return """    accumulator = accumulate.AccumulateCoals()\n"""
    def getBody(self):
        return """
        accumulated = accumulator.accumulate(coal=coal)
        if accumulated:
            yield (accumulated, )
"""

    def getRequiredVariables(self):
        return ["coal"]

    def getVariableNames(self):
        return ["coal"]


class SelectCommand(TypicalCommand):
    NAME = "SELECT"
    SHORT_HELP = "SELECT exp1 [as name1], exp2 [as name2] ... - generates records using the specified expressions"
    LONG_HELP = """SELECT exp1 [as name1], exp2 [as name2]
SELECT '[' name = expression, ... ']' exp1 [as name1], exp2 [as name2]
    SELECT command generates record according to the expressions provided.
    The values from the chains above becomes no longe available, for example:
      SELECT coal.flowId, coal.transactionId as TID
        will generate records with two variable flowId and TID and you will not be able to refer to coal itself anymore
"""
    def __init__(self, preparationList=None):
        TypicalCommand.__init__(self, preparationList)
        self.expressions = []
    def add(self, exp):
        if exp == '*':
            pass
        elif not exp.getName():
            name = "_%d" % (len(self.expressions)+1)
            exp.setName(name)
        self.expressions.append( exp )
    def setParent(self, parent):
        GeneratorBase.setParent(self, parent)
        try:
            pos = self.expressions.index('*')
            del self.expressions[pos]
            for var in self.myParent.getVariableNames():
                exp = Expression()
                exp.setId(var)
                self.expressions.insert(pos, exp)
                pos += 1
        except:
            pass
    def getVariableNames(self):
        return [e.getName() for e in self.expressions]
    def getReturnValues(self):
        return [e.getValue() for e in self.expressions]
    def getReturn(self):
        tupleStr = createTupleString( self.getReturnValues() )
        return tupleStr
    def getBody(self):
        return """        yield %s
""" % self.getReturn()

    def getGlobalExpressions(self):
        globalExps = TypicalCommand.getGlobalExpressions(self)
        for e in self.expressions:
            globalExps.extend(e.getGlobalExpressions())
        return globalExps

class IfCommand(TypicalCommand):
    NAME = "IF"
    SHORT_HELP = "IF expression - applies filter to recors"
    LONG_HELP = """IF expression
    Passes only records which eveluate expression to True.
    Record itself is not changed
"""
    def __init__(self, expression, preparationList=None):
        TypicalCommand.__init__(self, preparationList)
        self.myExpression = expression
    def getBody(self):
        return """
        if %s:
            yield %s
""" % (self.myExpression.getValue(), createTupleString(self.getVariableNames()))

    def getRequiredVariables(self):
        return []

    def getVariableNames(self):
        return self.myParent.getVariableNames()

    def getGlobalExpressions(self):
        globalExps = TypicalCommand.getGlobalExpressions(self)
        return globalExps + self.myExpression.getGlobalExpressions()

class LimitCommand(TypicalCommand):
    NAME = "LIMIT"
    SHORT_HELP = "LIMIT <number> - limits number of records passed through this chain"
    LONG_HELP = """LIMIT <number>
    Only specified will pass further.
    Reading of additional records will be stopped, but in most cases more then specified number of records will be
    processed in the chains before the limit chain
"""
    def __init__(self, limit):
        TypicalCommand.__init__(self)
        self.myLimit = limit
    def getStart(self):
        return "    current = 0\n"
    def getBody(self):
        return """
        if current == %d:
            break
        else:
            yield %s
        current += 1
""" % (self.myLimit, createTupleString(self.getVariableNames()))

    def getVariableNames(self):
        return self.myParent.getVariableNames()

class ParseRequestCommand(TypicalCommand):
    NAME = "PARSE request"
    SHORT_HELP = "PARSE request [FROM <expression>]"
    LONG_HELP  = """PARSE request
PARSE request FROM <expression>
    Parses HTTP request headers from the coal object (by default) or provided expression (string).
    "request" object is added to the current record
"""
    def __init__(self, requestExpression = None):
        TypicalCommand.__init__(self)
        self.nonDefaultExpression = requestExpression
    def getBody(self):
        if self.nonDefaultExpression:
            s = """
        request = http.HttpRequest(%s)
""" % self.nonDefaultExpression.getValue()
        else:
            s = """
        if coal.HasField("request"):
            request = http.HttpRequest(coal.request.body)
        else:
            request = None
"""
        s += "        yield %s\n" % createTupleString(self.getVariableNames())
        return s

    def getVariableNames(self):
        return self.myParent.getVariableNames() + ["request"]
    def getGlobalExpressions(self):
        if self.nonDefaultExpression:
            return self.nonDefaultExpression.getGlobalExpressions()
        else:
            return []

class ParseResponseCommand(TypicalCommand):
    NAME = "PARSE response"
    SHORT_HELP = "PARSE response [FROM <expression>]"
    LONG_HELP  = """PARSE response
PARSE response FROM <expression>
    Parses HTTP response headersfrom the coal object (by default) or provided expression (string).
    "request" object is added to the current record
"""
    def __init__(self, responseExpression = None):
        TypicalCommand.__init__(self)
        self.nonDefaultExpression = responseExpression
    def getBody(self):
        if self.nonDefaultExpression:
            s = """
        response = HttpResponse(%s)
""" % self.nonDefaultExpression.getValue()
        else:
            s = """
        if coal.HasField("response"):
            response = http.HttpResponse(coal.response.body)
        else:
            response = None
"""
        s += "        yield %s\n" % createTupleString(self.getVariableNames())
        return s

    def getVariableNames(self):
        return self.myParent.getVariableNames() + ["response"]
    def getGlobalExpressions(self):
        if self.nonDefaultExpression:
            return self.nonDefaultExpression.getGlobalExpressions()
        else:
            return []

class ParseUriCommand(TypicalCommand):
    NAME = "PARSE uri"
    SHORT_HELP = "PARSE uri FROM <expression>"
    LONG_HELP  = """PARSE request FROM <expression>
    Parses uri from the in the string provided
    "uri" object is added to the current record
"""
    def __init__(self, expression):
        TypicalCommand.__init__(self)
        self.myExpression = expression
    def getBody(self):
        s = """
        uri = http.Uri(%s)
        yield %s
""" % (self.myExpression.getValue(), createTupleString(self.getVariableNames()))
        return s

    def getVariableNames(self):
        return self.myParent.getVariableNames() + ["uri"]
    def getGlobalExpressions(self):
        return self.myExpression.getGlobalExpressions()

class DistinctCommand(SelectCommand):
    NAME = "DISTINCT"
    SHORT_HELP = "DISTINCT exp1 [as name1], exp2 [as name2] ... - generates distinct set of records"
    LONG_HELP = """DISTINCT exp1 [as name1], exp2 [as name2]
DISTINCT '[' name = expression, ... ']' exp1 [as name1], exp2 [as name2]
    This command generates only distinct records out of all produced by previous chains
    Record is consider distinct if at lieast one of its variables is different.
    Space complexity of the chain command is the size of the distinct set of recors
    Second form allows to use some precalculated expressions
"""
    def __init__(self, preparationList=None):
        SelectCommand.__init__(self, preparationList)
    def getStart(self):
        return """
    distincts = set()
"""
    def getBody(self):
        return """
        t = %s
        if not t in distincts:
            distincts.add(t)
            yield t
""" % self.getReturn()

class MatchCommand(TypicalCommand):
    NAME = "MATCH"
    SHORT_HELP = "MATCH <expression> =~ <regexp>"
    LONG_HELP = """MATCH <expression> =~ <regexp>
    MATCH commands filters records that match specified regular expression (string) and extract named groups from it:
      MATCH request.path =~ r"video/(?P<start>\d+)-(?P<end>\d+)"
    After this command string variables 'start' and 'end' will be added to existing record
    You can use int(start) and int(end) to convert them to integer 
"""
    def __init__(self, expression, regExp):
        TypicalCommand.__init__(self)
        matchRegExp = runtime.Matcher(regExp)
        self.groupNames = matchRegExp.getGroupNames()
        self.myExpression = expression
        self.myRegExp = regExp

    def getVariableNames(self):
        return self.myParent.getVariableNames() + self.groupNames

    def getBody(self):
        return """
        if _matcher_.match(%s):
            yield %s
""" % (self.myExpression.getValue(), createTupleString(self.getReturnValues()))

    def getStart(self):
        return """
    _matcher_ = runtime.Matcher(%s)
""" % self.myRegExp

    def getGlobalExpressions(self):
        globalExps = TypicalCommand.getGlobalExpressions(self)
        return globalExps + self.myExpression.getGlobalExpressions()

    def getReturnValues(self):
        returnValues = [("_matcher_['%s']" % group) for group in self.groupNames]
        return self.myParent.getVariableNames() + returnValues

class ForSelectCommand(TypicalCommand):
    NAME = "FOR SELECT"
    SHORT_HELP = "FOR SELECT <agg> exp1 [as name1], <agg> exp2 [as name2] ... - generates aggregated records"
    LONG_HELP = """FOR SELECT SELECT <agg> exp1 [as name1], <agg> exp2 [as name2]
    FOR SELECT command performs aggregation query on the generated record set.
""" + aggregate.LONG_HELP

    def __init__(self, aggregatedExpressions, aggregatedExpressionsOffset=0, preparationList=None):
        TypicalCommand.__init__(self, preparationList)
        self.myAggregatedExpressions = aggregatedExpressions
        i = aggregatedExpressionsOffset
        for agg, exp in self.myAggregatedExpressions:
            if not exp.getName():
                name = "_%d" % (i+1)
                exp.setName(name)
            i += 1

    def getVariableNames(self):
        return [e[1].getName() for e in self.myAggregatedExpressions]

    def getAggregateDictionary(self):
        entries = []
        for aggregated in self.myAggregatedExpressions:
            if aggregated[0].find('.') == -1:
                constructor = "aggregate.%s%s()" % (aggregated[0][0].upper(), aggregated[0][1:])
            else:
                constructor = "%s()" % aggregated[0]
            entries.append("'%s': %s" %(aggregated[1].getName(), constructor))
        return "{ %s }" %  ", ".join(entries)

    def getAddValuesSection(self, dictionaryName):
        s = ""
        for aggregated in self.myAggregatedExpressions:
            s += "        %s['%s'].add(%s)\n" % (dictionaryName, aggregated[1].getName(), aggregated[1].getValue())
        return s
    def getDictionaryValues(self):
        return "".join(("d['%s'].getValue(),"%aggregated[1].getName()) for aggregated in self.myAggregatedExpressions)
    def getStart(self):
        s = TypicalCommand.getStart(self)
        return s+"    d = %s\n" % self.getAggregateDictionary()
    def getBody(self):
        return self.getAddValuesSection("d")
    def getEnd(self):
        return "    yield (%s)" % self.getDictionaryValues()
    def getGlobalExpressions(self):
        globalExps = TypicalCommand.getGlobalExpressions(self)
        for aggregated in self.myAggregatedExpressions:
            globalExps.extend(aggregated[1].getGlobalExpressions())
        return globalExps


class ForDistinctSelectCommand(ForSelectCommand):
    NAME = "FOR DISTINCT"
    SHORT_HELP = "FOR DISTINCT expr1, ... SELECT <agg> exp1 [as name1], ... - generates aggregated records for distinct sets"
    LONG_HELP = """FOR DISTINCT expr1 [as name1], ... SELECT <agg> expN [as nameN], ...
    FOR DISTINCT command performs selective aggregation on the distinct set of records.
    For example count traffic generated to distinct hosts:
      FOR DISTINCT request.hosts SELECT sum response.length
""" + aggregate.LONG_HELP

    def __init__(self, distinctExpressions, aggregatedExpressions, preparationList=None):
        ForSelectCommand.__init__(self, aggregatedExpressions, len(distinctExpressions), preparationList)
        self.myDistinctExpressions = distinctExpressions
        i = 0
        for exp in self.myDistinctExpressions:
            if not exp.getName():
                name = "_%d" % (i+1)
                exp.setName(name)
            i += 1
    def getVariableNames(self):
        return [e.getName() for e in self.myDistinctExpressions] + ForSelectCommand.getVariableNames(self)
    def getStart(self):
        s = ForSelectCommand.getStart(self)
        return s+"    distincts = {}\n"
    def getDistinctTuple(self):
        tupleStr = createTupleString( [e.getValue() for e in self.myDistinctExpressions] )
        return tupleStr
    def getBody(self):
        s = """
        t = %s
        if not t in distincts:
            distincts[t] = %s
        d = distincts[t]
%s
""" % ( self.getDistinctTuple(), self.getAggregateDictionary(), self.getAddValuesSection("d"))
        return s
    def getEnd(self):
        dictValues = self.getDictionaryValues()
        return """
    for t, d in distincts.iteritems():
        yield t + (%s)
""" % dictValues

class ForInSelectCommand(ForSelectCommand):
    NAME = "FOR IN"
    SHORT_HELP = "FOR expr [as name] IN sequenceExpr SELECT <agg> exp1 [as name1], ... - FOR IN - generates aggregated records for predefined sequence of values"
    LONG_HELP = """FOR expr [as name] IN sequenceExpr SELECT <agg> exp1 [as name1], ...
    FOR IN command performs selective aggregation on the predefined sequence of values:
    For example to count requests to hosts youtube.com and xvideos.com:
      FOR request.host.split(".")[-2] as name in ["youtube", "xvideos"] SELECT count True as numRecords
""" + aggregate.LONG_HELP

    def __init__(self, forExpression, sequenceExpression, aggregatedExpressions):
        ForSelectCommand.__init__(self, aggregatedExpressions, 1)
        self.myForExpression = forExpression
        if not self.myForExpression.getName():
            self.myForExpression.setName("_1")
        self.mySequenceExpression = sequenceExpression
    def getVariableNames(self):
        return [self.myForExpression.getName()] + ForSelectCommand.getVariableNames(self)
    def getStart(self):
        s = ForSelectCommand.getStart(self)
        return s+"""    distincts = {}
    keys = [ k for k in %s ]
    for k in keys:
        distincts[k] = %s
""" % (self.mySequenceExpression.getValue(), self.getAggregateDictionary())
    def getBody(self):
        s = """
        key = %s
        if not key in distincts:
            continue
        d = distincts[key]
%s
""" % ( self.myForExpression.getValue(), self.getAddValuesSection("d"))
        return s
    def getEnd(self):
        dictValues = self.getDictionaryValues()
        return """
    for key in keys:
        d = distincts[key]
        yield (key, %s)
""" % dictValues

class SortbyCommand(CommandBase):
    NAME = "SORTBY"
    SHORT_HELP = "SORTBY expression [ASC|DESC] - sorts records by expression"
    LONG_HELP = """SORTBY expression [ASC|DESC]
    Sorts recors according to the expression. Default order is ascending. 
    As usual algorith is O(N) in space and O(N*logN) in time
    Although it is stable meaning that the order of records with the same key remains uncanged
"""
    def __init__(self, exp, ascending):
        CommandBase.__init__(self)
        self.myExpression = exp
        self.myAscending = ascending
    def getVariableNames(self):
        return self.myParent.getVariableNames()
    def createGenerator(self, name, parentGeneratorName):
        s = """
def %s():
    def getkey( record ):
        %s = record
        return %s
    allData = sorted(%s(), key=getkey %s)
    return allData

""" % (name, createTupleString(self.getVariableNames()), self.myExpression.getValue(), parentGeneratorName, "" if self.myAscending else ", reverse=True")
        return s

class TopCommand(CommandBase):
    NAME = "TOP"
    SHORT_HELP = "TOP <number> expression - Returns at most <number> of top records ordered by expression"
    LONG_HELP = """TOP <number> expression
    Returns <number> of records with maximum values of expression in decreasing order
    Heap sorting is used. O(n*log(number))
"""
    def __init__(self, number, exp, ascending=False):
        CommandBase.__init__(self)
        self.myNumber = number
        self.myExpression = exp
        self.myAscending = ascending
    def getVariableNames(self):
        return self.myParent.getVariableNames()
    def createGenerator(self, name, parentGeneratorName):
        op = "heapq.nsmallest" if self.myAscending else "heapq.nlargest"
        s = """
def %s():
    import heapq
    def getkey( record ):
        %s = record
        return %s
    allData = %s(%s, %s(), key=getkey)
    return allData

""" % (name, createTupleString(self.getVariableNames()), self.myExpression.getValue(), op, self.myNumber, parentGeneratorName)
        return s

class BottomCommand(TopCommand):
    NAME = "BOTTOM"
    SHORT_HELP = "BOTTOM <number> expression - Returns at most <number> of bottom records ordered by expression"
    LONG_HELP = """BOTTOM <number> expression
    Returns <number> of records with minimum values of expression in increasing order
    Heap sorting is used. O(n*log(number))
"""
    def __init__(self, number, exp):
        TopCommand.__init__(self, number, exp, ascending = True)


class ExpandCommand(SelectCommand):
    NAME = "EXPAND"
    SHORT_HELP = "EXPAND exp as name [, ...] [SELECT <repeated-exp>, ...] - expands iterable expression"
    LONG_HELP = """EXPAND exp as name [, ...] [SELECT <repeated-exp>, ...]
    Expands iterable expressions (e.g. lists, dictionaries, sets) to multiple records
    
    For example:
        EXPAND request.path.split("/") as component SELECT len(component), request.param["id"]
        EXPAND request.params.iteritems() as paramName, paramValue
"""
    def __init__(self, iterableExpr, nameList, namedExpressions=None):
        SelectCommand.__init__(self)
        self.myIterableExpr = iterableExpr
        self.myNameList = nameList
        if namedExpressions:
            for exp in namedExpressions:
                self.add(exp)
    def getVariableNames(self):
        return self.myNameList + SelectCommand.getVariableNames(self)
    def getReturnValues(self):
        return self.myNameList + SelectCommand.getReturnValues(self)
    def getBody(self):
        if len(self.myNameList) == 1:
            s = """
        for %s in %s:
            yield %s
""" % (self.myNameList[0], self.myIterableExpr.getValue(), self.getReturn())
        else:
            s = """
        for %s in %s:
            yield %s
""" % (createTupleString(self.myNameList), self.myIterableExpr.getValue(), self.getReturn())
        return s

class PassCommand(TypicalCommand):
    NAME = "PASS"
    SHORT_HELP = "PASS <expression>[; <expression> ...] - executes expressions"
    LONG_HELP = """PASS <expression>[; <expression> ...]
    PASS is used to execute expressions (e.g. imported functions)
    that don't modify record variables explicitly.
"""
    def __init__(self):
        TypicalCommand.__init__(self)
        self.myExpressionList = []
    def add(self, exp):
        self.myExpressionList.append(exp)
    def getVariableNames(self):
        return self.myParent.getVariableNames()

    def getBody(self):
        s = ""
        for exp in self.myExpressionList:
            s += "        %s\n" % exp.getValue()
        s += "        yield %s" % createTupleString(self.getVariableNames())
        return s

    def getGlobalExpressions(self):
        globalExps = TypicalCommand.getGlobalExpressions(self)
        for exp in self.myExpressionList:
            globalExps += exp.getGlobalExpressions()
        return globalExps

commandClasses = [AccumulateCommand, SelectCommand, DistinctCommand, IfCommand, LimitCommand,
                  ParseRequestCommand, ParseResponseCommand, ParseUriCommand,
                  ForSelectCommand, ForDistinctSelectCommand, ForInSelectCommand,
                  SortbyCommand, TopCommand, BottomCommand,
                  ExpandCommand, MatchCommand, PassCommand]



