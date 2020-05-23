import logging

from django.conf import settings
from django.utils.module_loading import import_string
from soapfish import soap, xsd

from . soap_exceptions import (Schema_UserNotFoundException,
                               UserNotFoundException,
                               Schema_SystemException,
                               SystemException)

logger = logging.getLogger(__name__)


class User(xsd.ComplexType):
    """
    """
    CodiceFiscale  = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Username = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Birthdate = xsd.Element(xsd.DateTime, minOccurs=1, nillable=True)
    Birthplace = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Email = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Name  = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Nationality = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Passport = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Sex = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Surname = xsd.Element(xsd.String, minOccurs=1, nillable=True)

    def __repr__(self):
        return '{} [{}]'.format(self.Username,
                                self.CodiceFiscale)


class GetUser(xsd.ComplexType):
    CodiceFiscale  = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Username = xsd.Element(xsd.String, minOccurs=1, nillable=True)


Schema_User = xsd.Schema(
    targetNamespace='{}/soap/User.xsd'.format(settings.FQDN),
    elementFormDefault='unqualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[User, GetUser, UserNotFoundException],
    elements = {
                'getUser': xsd.Element(GetUser),
                'User': xsd.Element(User)},
)


def get_user_details(request, user_id):
    """
    Fill the method you need to get the users values
    and return a User ComplexType
    """
    try:
        func = import_string(getattr(settings, 'SOAP_UNIREG_IDENTITY_HANDLER'))
        res = func(user_id)
    except Exception as e:
        _msg = 'SOAP Internal ERROR: {}'.format(e)
        logger.error(_msg)
        return SystemException()
    if not res:
        logger.warn('The user [{}] does not exists'.format(user_id))
        return UserNotFoundException()
    user = User(**res)
    logger.debug('User [{}] found'.format(user))
    return user


get_user_details_method = xsd.Method(
    function=get_user_details,
    soapAction='{}/soap/user_registry/get_user_details'.format(settings.FQDN),
    input='getUser',
    #  inputPartName='parameters',
    output='User',
    #  outputPartName='parameters',
    operationName='GetUser',
    #  style='document'
)


UserRegistrySoapService = soap.Service(
    name = 'UserRegistrySoapPort',
    targetNamespace='{}/soap/user_registry.wsdl'.format(settings.FQDN),
    location='{}/soap/user_registry'.format(settings.FQDN),  # where request should be sent.
    schemas=[Schema_User,
             #  Schema_UserNotFoundException,
             #  Schema_SystemException
             ],
    #  version=soap.SOAPVersion.SOAP11,
    methods=[get_user_details_method],
)


if __name__ == '__main__':
    user = User()
    user.Username = 'that-guy'

    # export to xml
    xml = user.xml('user_registry').decode()
    print(xml)

    # parse from xml
    usr_prop_2 = UserProperty.parsexml(xml)
