# flake8:noqa
# isort:skip_file
##############################################################################
# Note: Generated by soapfish.wsdl2py at 2020-05-22 13:22:13.373056+00:00
#       Try to avoid editing it if you might need to regenerate it.
##############################################################################

from soapfish import soap, xsd

BaseHeader = xsd.ComplexType

##############################################################################
# Schemas


# http://pda.cineca.it/unical/anagrafe


class UserPropertyType(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    propertyName = xsd.Element(xsd.String) # xsd.Element(__name__ + '.String')
    propertyValue = xsd.Element(xsd.String) # xsd.Element(__name__ + '.String')

    @classmethod
    def create(cls, propertyName, propertyValue):
        instance = cls()
        instance.propertyName = propertyName
        instance.propertyValue = propertyValue
        return instance


class UserProperties(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    userProperty = xsd.ListElement(UserPropertyType, tagname='userProperty', maxOccurs=xsd.UNBOUNDED)

    @classmethod
    def create(cls, userProperty):
        instance = cls()
        instance.userProperty = userProperty
        return instance


Schema_e8a30 = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='http://pda.cineca.it/unical/anagrafe',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[UserPropertyType],
    elements={'userProperties': xsd.Element(UserProperties())},
)


# it.cineca.pda.ws.anagrafe


Schema_d14fd = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='it.cineca.pda.ws.anagrafe',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[],
    elements={'string': xsd.Element(xsd.String)},
)


# it.cineca.pda.unical.userservices.exceptions


Schema_0d16e = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='it.cineca.pda.unical.userservices.exceptions',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[],
    elements={'string': xsd.Element(xsd.String)},
)


# java:it.cineca.pda.unical.userservices.exceptions


class UserNotFoundException(xsd.ComplexType):
    pass


Schema_65f1f = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='java:it.cineca.pda.unical.userservices.exceptions',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[UserNotFoundException],
    elements={'UserNotFoundException': xsd.Element(UserNotFoundException)},
)


# java:it.cineca.pda


class SystemException(xsd.ComplexType):
    pass


Schema_105a2 = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='java:it.cineca.pda',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[SystemException],
    elements={'SystemException': xsd.Element(SystemException)},
)


# java:it.cineca.pda.ws.anagrafe


class InvalidAteneoException(xsd.ComplexType):
    pass


class User(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    Birthdate = xsd.Element(xsd.DateTime, minOccurs=1, nillable=True)
    Birthplace = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    CodiceFiscale = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Email = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Name = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Nationality = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Passport = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Sex = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Surname = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Username = xsd.Element(xsd.String, minOccurs=1, nillable=True)

    @classmethod
    def create(cls, Birthdate, Birthplace, CodiceFiscale, Email, Name, Nationality, Passport, Sex, Surname, Username):
        instance = cls()
        instance.Birthdate = Birthdate
        instance.Birthplace = Birthplace
        instance.CodiceFiscale = CodiceFiscale
        instance.Email = Email
        instance.Name = Name
        instance.Nationality = Nationality
        instance.Passport = Passport
        instance.Sex = Sex
        instance.Surname = Surname
        instance.Username = Username
        return instance


Schema_e6ea1 = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace='java:it.cineca.pda.ws.anagrafe',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[InvalidAteneoException, User],
    elements={'InvalidAteneoException': xsd.Element(InvalidAteneoException)},
)


# http://it/cineca/pda/ws/anagrafe


class GetUserProperties(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    username = xsd.Element(xsd.String)
    codiceAteneo = xsd.Element(xsd.String)

    @classmethod
    def create(cls, username, codiceAteneo):
        instance = cls()
        instance.username = username
        instance.codiceAteneo = codiceAteneo
        return instance


class GetUserPropertiesResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    userProperties = xsd.Ref(__name__ + '.UserProperties')

    @classmethod
    def create(cls, userProperties):
        instance = cls()
        instance.userProperties = userProperties
        return instance


class GetUserDetails(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    username = xsd.Element(xsd.String)
    codiceAteneo = xsd.Element(xsd.String)

    @classmethod
    def create(cls, username, codiceAteneo):
        instance = cls()
        instance.username = username
        instance.codiceAteneo = codiceAteneo
        return instance


class GetUserDetailsResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    _return = xsd.Element(__name__ + '.User', tagname='return')

    @classmethod
    def create(cls, _return):
        instance = cls()
        instance._return = _return
        return instance


Schema_1e9f6 = xsd.Schema(
    imports=[Schema_e6ea1, Schema_e8a30],
    includes=[],
    targetNamespace='http://it/cineca/pda/ws/anagrafe',
    elementFormDefault='qualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[],
    elements={'getUserProperties': xsd.Element(GetUserProperties()), 'getUserPropertiesResponse': xsd.Element(GetUserPropertiesResponse()), 'getUserDetails': xsd.Element(GetUserDetails()), 'getUserDetailsResponse': xsd.Element(GetUserDetailsResponse())},
)


##############################################################################
# Operations


def getUserProperties(request, getUserProperties):
    # TODO: Put your implementation here.
    return getUserPropertiesResponse



def getUserDetails(request, getUserDetails):
    # TODO: Put your implementation here.
    return getUserDetailsResponse


##############################################################################
# Methods


getUserProperties_method = xsd.Method(
    function=getUserProperties,
    soapAction='',
    input='getUserProperties',
    inputPartName='parameters',
    output='getUserPropertiesResponse',
    outputPartName='parameters',
    operationName='getUserProperties',
    style='document',
)


getUserDetails_method = xsd.Method(
    function=getUserDetails,
    soapAction='',
    input='getUserDetails',
    inputPartName='parameters',
    output='getUserDetailsResponse',
    outputPartName='parameters',
    operationName='getUserDetails',
    style='document',
)


##############################################################################
# SOAP Service


UserRegistrySoapPort_SERVICE = soap.Service(
    name='UserRegistrySoapPort',
    targetNamespace='http://it/cineca/pda/ws/anagrafe',
    location='${scheme}://${host}/services/UserRegistry',
    schemas=[Schema_e8a30, Schema_d14fd, Schema_1e9f6, Schema_0d16e, Schema_65f1f, Schema_105a2, Schema_e6ea1],
    version=soap.SOAPVersion.SOAP11,
    methods=[getUserProperties_method, getUserDetails_method],
)


##############################################################################


# NOTE: Uncomment the following lines to turn on dispatching for Django:
# from soapfish.django_ import django_dispatcher
# dispatcher = django_dispatcher(UserRegistrySoapPort_SERVICE)


# NOTE: Put these lines in the urls.py for your project or application:
# urlpatterns += patterns('',
#     (r'^services\/UserRegistry$', '<module>.dispatcher'),
# )
