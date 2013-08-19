"""
Accumulate coals
"""

class CoalsAccumulator:
    def __init__(self):
        self.coalFlows = {}

    def accumulate(self, coal):
        """Accumulates multiple coal records from the same transaction to the single one"""
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
            return [aggregatedCoal]
        else:
            return []
    def finish(self):
        return []
