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

    @staticmethod
    def getter(varname):
        return ("def get{}(self):\n\treturn({});".format(varname.title(), varname));

    @staticmethod
    def setter(varname):
        return ("def set{}(self, {}):\n\tself.{} = {};".format(varname.title(), varname, varname, varname));

    @staticmethod
    def generateGettersAndSetters(classObj):
        ret = dict();
        keys = list(classObj.getVariables().keys());
        for index in range(len(keys)):
            tmp = list(); keyname = keys[index];
            tmp.append(AppUtils.getter(keyname));
            tmp.append(AppUtils.setter(keyname));
            ret[keyname] = tmp;
        return (ret);


