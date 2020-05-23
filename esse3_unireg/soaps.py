from django.conf import settings
from django.utils.module_loading import import_string
from soapfish import soap, xsd

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


class GetUser(xsd.ComplexType):
    CodiceFiscale  = xsd.Element(xsd.String, minOccurs=1, nillable=True)
    Username = xsd.Element(xsd.String, minOccurs=1, nillable=True)


Schema = xsd.Schema(
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
    func = import_string(getattr(settings, 'SOAP_UNIREG_IDENTITY_HANDLER'))
    res = func(user_id)
    #  import pdb; pdb.set_trace()
    return User(**res)


get_user_details_method = xsd.Method(
    function=get_user_details,
    soapAction='{}/soap/user_registry/get_user_details'.format(FQDN),
    input='getUser',
    output='user',
    operationName='GetUser',
)


UserRegistrySoapService = soap.Service(
    targetNamespace='{}/soap/user_registry.wsdl'.format(FQDN),
    location='{}/soap/user_registry'.format(FQDN),  # where request should be sent.
    schemas=[Schema,],
    methods=[get_user_details_method],
)


if __name__ == '__main__':
    usr_prop = UserProperty()
    usr_prop.username = 'that-guy'
    usr_prop.codiceateneo = 'unical'

    # export to xml
    xml = usr_prop.xml('user_registry').decode()
    print(xml)

    # parse from xml
    usr_prop_2 = UserProperty.parsexml(xml)
