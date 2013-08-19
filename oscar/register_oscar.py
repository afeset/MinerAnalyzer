import miner_globals
from include.a.line.report.coal_report_pb2 import CoalRecordGpb
from infra.log.msg_data_pb2 import MsgDataGpb
from line.va.transaction_pb2 import TransactionSummaryGpb
from frecords import FRecord
from meta_file import MetaData

# define symbols for completion
miner_globals.addCompletionSymbol('coal', CoalRecordGpb())
miner_globals.addCompletionSymbol('msgData', MsgDataGpb())
miner_globals.addCompletionSymbol('transaction', TransactionSummaryGpb())
miner_globals.addCompletionSymbol('frecord', FRecord(words=["F"] + ["0"]*49, version="3.0"))
miner_globals.addCompletionSymbol('metadata', MetaData())

# define targets
miner_globals.addExtensionToTargetMapping(".qbl", "coal")
miner_globals.addTargetToClassMapping("qdl", "qbl_targets.iQdl", None, "reads qwilt debug log. attachmentTypes=[] may specify\nlist of additional gpbs accepted in debug message attachments (which are ignored otherwise)")
miner_globals.addTargetToClassMapping("coal", "qbl_targets.iCoal", "qbl_targets.oCoal", "coal logs")
miner_globals.addTargetToClassMapping("transaction", "qbl_targets.iTransaction", None, "transaction logs")
miner_globals.addTargetToClassMapping("trx-log", "qbl_targets.iTransaction", None, "transaction logs")
miner_globals.addTargetToClassMapping("gpbchain", None, "qbl_targets.oGPBChain", "general gpb chain output - first message should be msgData")
miner_globals.addTargetToClassMapping("frecord", "frecords.iFrecordTarget", "frecords.oFrecordTarget", "reads frecords created by line or delivery filters out other types of messages")

miner_globals.addExtensionToTargetMapping(".meta", "metadata")
miner_globals.addTargetToClassMapping("metadata", "meta_file.iMeta", None, "reads oscar meta files to metadata variable")

# add accumulation classes
miner_globals.addAccumulator("coal", "coals_accumulator.CoalsAccumulator")
miner_globals.addAccumulator("frecord", "frecords.FRecordsAccumulator")

# add parser mappings
miner_globals.addParserMapping("request", "coal", "qbl_targets.parseRequestFromCoal")
miner_globals.addParserMapping("response", "coal", "qbl_targets.parseResponseFromCoal")
miner_globals.addParserMapping("uri", "frecord", "frecords.parseUriFromFrecord")
miner_globals.addParserMapping("uri", "metadata", "meta_file.parseUriFromMeta")
