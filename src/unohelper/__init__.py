import uno

def _mode_to_str(mode):
    return "[]"

def _propertymode_to_str(mode):
    return ""


def inspect(obj, out):
    pass


def createSingleServiceFactory(*args, **kwargs):
    pass


class _ImplementationHelperEntry:
    def __init__(self, ctor, serviceNames):
        pass


class ImplementationHelper:
    def __init__(self):
        pass

    def addImplementation(self, ctor, implementationName, serviceNames):
        pass

    def writeRegistryInfo(self, regKey, smgr):
        pass

    def getComponentFactory(self, implementationName, regKey, smgr):
        pass

    def getSupportedServiceNames(self, implementationName):
        pass

    def supportsService(self, implementationName, serviceName):
        pass


class ImplementationEntry:
    def __init__(self, implName, supportedServices, clazz):
        pass


def writeRegistryInfoHelper(smgr, regKey, seqEntries):
    pass


def systemPathToFileUrl(systemPath):
    "returns a file-url for the given system path"
    pass


def fileUrlToSystemPath(url):
    "returns a system path (determined by the system, the python interpreter is running on)"
    pass


def absolutize(path, relativeUrl):
    "returns an absolute file url from the given urls"
    pass

def getComponentFactoryHelper(implementationName, smgr, regKey, seqEntries):
    pass


def addComponentsToContext(
    toBeExtendedContext, contextRuntime, componentUrls, loaderName
):
    pass

# never shrinks !
_g_typeTable = {}


def _unohelper_getHandle(self):
    pass


class Base:
    def getTypes(self):
        pass

    def getImplementationId(self):
        return ()


class CurrentContext(Base):
    """A current context implementation, which first does a lookup in the given
    hashmap and if the key cannot be found, it delegates to the predecessor
    if available
    """

    def __init__(self, oldContext, hashMap):
        pass

    def getValueByName(self, name):
        pass


# -------------------------------------------------
# implementation details
# -------------------------------------------------
class _FactoryHelper_(Base):
    def __init__(self, clazz, implementationName, serviceNames):
        pass

    def getImplementationName(self):
        pass

    def supportsService(self, ServiceName):
        pass

    def getSupportedServiceNames(self):
        pass

    def createInstanceWithContext(self, context):
        pass

    def createInstanceWithArgumentsAndContext(self, args, context):
        pass

