from django.conf import settings
from soapfish import xsd


class UserNotFoundException(xsd.ComplexType):
    #  name = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    #  type = xsd.Element(xsd.Integer, minOccurs=1, nillable=True)
    pass


Schema_UserNotFoundException = xsd.Schema(
    targetNamespace='{}/soap/User.xsd'.format(settings.FQDN),
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[UserNotFoundException,],
    elements={'UserNotFoundException': xsd.Element(UserNotFoundException)},
)

class SystemException(xsd.ComplexType):
    #  name = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    #  type = xsd.Element(xsd.Integer, minOccurs=1, nillable=True)
    pass


Schema_SystemException = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='/soap/system/exceptions/internal-error',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[SystemException,],
    elements={'SystemException': xsd.Element(SystemException)},
)
