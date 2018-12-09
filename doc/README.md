# API documentation

## Status

**GET** `/rest/status` will return the status of the server following structure.

```
{  
   "authors":
   {  
      "mobile-app":"@xenahort",
      "server":"@gomezportillo"
   },
   "status":"OK",
   "version":0.5
}
```

## Products

**GET** `/rest/products/all` will return a list with all the products stored on the server.

```
[  
   {  
      "description":"Cures headache",
      "name":"Ibuprofen",
      "pharmacy":"Pharmacy 1",
      "price":7
   },
   {  
      "description":"Cures flu",
      "name":"Frenadol",
      "pharmacy":"Pharmacy 2",
      "price":12
   },
   {  
      "description":"Cures wounds",
      "name":"Bandage",
      "pharmacy":"Pharmacy 1",
      "price":10
   }
]
```

**POST** or **PUT** `/rest/products/` indicating _name_, _description_, _pharmacy_ and _price_ will create a new product or override it if already exists one with the same name.

**DELETE** `/rest/products/` indicating the _name_ of the product to be deleted will delete it.

## Pharmacies

**GET** `/rest/pharmacies/all` will return the list of registered pharmacies with the following structure.

```
[  
   {  
      "latitude":37.198366,
      "longitude":-3.624976,
      "name":"Pharmacy 1"
   },
   {  
      "latitude":37.195993,
      "longitude":-3.622784,
      "name":"Pharmacy 2"
   }
]
```

**POST** or **PUT** `/rest/pharmacies/` indicating _name_, _latitude_ and _longitude_ will create a new pharmacy or override it if already exists one with the same name.

**DELETE** `/rest/pharmacies/` indicating the _name_ of the pharmacy will delete it.

⚠️TO DO⚠️

<!--
* **/rest/users/all** will return the list of registered users with the following structure.

```
{  
   "gomezportillo@ugr.es":"Pedro Manuel Gomez-Portillo",
   "xenahort@ugr.es":"Juan Carlos Serrano"
}
```
-->
