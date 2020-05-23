# Esse3-UserRegistry-SOAP
Servizio SOAP che consente a Cineca Esse3 di interrogare le informazioni anagrafiche degli utenti.


#### Example
````
pip install -r requirements.txt
cd example
./manage.py runserver
````


#### Resources

- http://localhost:8000/soap/user_registry?wsdl
- http://localhost:8000/soap/user_registry


#### Configuration

In `settings.py` configure `SOAP_UNIREG_IDENTITY_HANDLER` to handle the SOAP query
to one or many data sources, see `example.exampe.settings.py`.

Example
````
# SOAP get_user_details identity handler
SOAP_UNIREG_IDENTITY_HANDLER = 'esse3_unireg.identity_handlers.identity_example'
````

#### Usage

````
from zeep import Client

client = Client('http://localhost:8000/soap/user_registry?wsdl')

client.service.GetUser(Username='gdm')
client.service.GetUser(CodiceFiscale='ciccio18')
````


#### SoapFish hints

Just to take a look to a wsdl to py code...
```
wsdl2py -s UserRegistryService.wsdl
```


#### Resources
- https://github.com/soapteam/soapfish/blob/master/docs/tutorial.rst
