import inspect;

class AppUtils(object):

    @staticmethod
    def parseException(infoObj):
        retJson = dict();
        expClass, expObject, tracebackObj = infoObj;
        tracebackInfo = inspect.getframeinfo(tracebackObj);

        retJson["expclass"] = expClass.__name__;
        retJson["expmessage"] = expObject.__str__();
        retJson["filename"] = tracebackInfo.filename;
        retJson["function"] = tracebackInfo.function;
        retJson["lineno"] = tracebackInfo.lineno;

        return (retJson);