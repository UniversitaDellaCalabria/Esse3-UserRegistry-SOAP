from soapfish import xsd


class UserNotFoundException(xsd.ComplexType):
    Message = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Code = xsd.Element(xsd.Integer, minOccurs=1, nillable=True)


Schema_UserNotFoundException = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='/soap/user/exceptions/not-found',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[UserNotFoundException,],
    elements={'UserNotFoundException': xsd.Element(UserNotFoundException)},
)

class SystemException(xsd.ComplexType):
    Message = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Code = xsd.Element(xsd.Integer, minOccurs=1, nillable=True)


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
