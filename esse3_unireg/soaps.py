import logging

from django.conf import settings
from django.utils.module_loading import import_string
from soapfish import soap, xsd

from . soap_exceptions import (Schema_UserNotFoundException,
                               UserNotFoundException,
                               Schema_SystemException,
                               SystemException)

logger = logging.getLogger(__name__)
FQDN = getattr(settings, 'FQDN', 'http://localhost:8000')


class User(xsd.ComplexType):
    """<xs:complexType name="User">
        <xs:sequence>
          <xs:element minOccurs="1" name="Birthdate" nillable="true" type="xs:dateTime"/>
          <xs:element minOccurs="1" name="Birthplace" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="CodiceFiscale" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Email" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Name" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Nationality" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Passport" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Sex" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Surname" nillable="true" type="xs:string"/>
          <xs:element minOccurs="1" name="Username" nillable="true" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
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
        return '{} [{}]'.format(self.Username, self.CodiceFiscale)


class GetUser(xsd.ComplexType):
    CodiceFiscale  = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Username = xsd.Element(xsd.String, minOccurs=1, nillable=True)


Schema_User = xsd.Schema(
    targetNamespace='{}/soap/user.xsd'.format(FQDN),
    elementFormDefault='unqualified',
    simpleTypes=[],
    attributeGroups=[],
    groups=[],
    complexTypes=[User, GetUser], # Status],
    elements = {
                'getUser': xsd.Element(GetUser),
                'user': xsd.Element(User)},
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
        return SystemException(Message=_msg, Code=500 )
    if not res:
        return UserNotFoundException(Message='User [{}] not found'.format(user_id),
                                     Code=404)
    return User(**res)


get_user_details_method = xsd.Method(
    function=get_user_details,
    soapAction='{}/soap/user_registry/get_user_details'.format(FQDN),
    input='getUser',
    #  inputPartName='parameters',
    output='user',
    #  outputPartName='parameters',
    operationName='GetUser',
    #  style='document'
)


UserRegistrySoapService = soap.Service(
    name = 'UserRegistrySoapPort',
    targetNamespace='{}/soap/user_registry.wsdl'.format(FQDN),
    location='{}/soap/user_registry'.format(FQDN),  # where request should be sent.
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
