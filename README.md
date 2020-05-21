# Esse3-UserRegistry-SOAP
Servizio SOAP che consente a Cineca Esse3 di interrogare le informazioni anagrafiche degli utenti

#### Example
````
pip install -r requirements.txt
cd example
./manage.py runserver
````


#### Resources

- http://localhost:8000/soap/user_registry?wsdl
- http://localhost:8000/soap/user_registry


#### Usage

````
from zeep import Client

client = Client('http://localhost:8000/soap/user_registry?wsdl')

client.service.GetUser(Username='pippo')
client.service.GetUser(CodiceFiscale='sdfgdfysdf767f8g')
````


#### SoapFish hints
```
wsdl2py -s UserRegistryService.wsdl
```


#### Risorse
- https://github.com/soapteam/soapfish/blob/master/docs/tutorial.rst
