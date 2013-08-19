import logging

debugMode = False
basicLog = None
compileLog = None

def setDebugMode():
    global debugMode
    global basicLog
    global compileLog
    if debugMode:
        return
    debugMode = True

    logging.basicConfig(
        level = logging.DEBUG,
        filename = "parselog.txt",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
    )
    basicLog = logging.getLogger()
    compileLog = getCompileLog()

# logger used to dump output of compilation
def getCompileLog():
    log = logging.getLogger("compile")
    logFh = logging.FileHandler('compile.log')
    logFh.setLevel(logging.INFO)
    logFormatter = logging.Formatter('%(asctime)s: %(message)s')
    logFh.setFormatter(logFormatter)
    log.addHandler(logFh)
    return log

