"""
Accumulate classes
"""

class AccumulateCoals:
    def __init__(self):
        self.coalFlows = {}

    def accumulate(self, **argv):
        """Accumulates multiple coal records from the same transaction to the single one"""
        coal = argv['coal']
        flowIdTuple = (coal.vaId, coal.flowId, coal.transactionId, coal.sysId)
        aggregatedCoal = self.coalFlows.get(flowIdTuple, None)
        isLast = coal.HasField("decoding")
        if not aggregatedCoal:
            aggregatedCoal = coal
            self.coalFlows[flowIdTuple] = aggregatedCoal
        else:
            aggregatedCoal.MergeFrom(coal)
    
        if isLast:
            # take some attributes from the last coal
            del self.coalFlows[flowIdTuple]
            return aggregatedCoal
        else:
            return None

