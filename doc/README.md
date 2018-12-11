# API documentation

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [API documentation](#api-documentation)
	- [Status](#status)
	- [Products](#products)
	- [Pharmacies](#pharmacies)
	- [Cart](#cart)
	- [Order](#order)
		- [Errors](#errors)
	- [Users](#users)

<!-- /TOC -->

## Status

**GET** `/rest/status` will return the status of the server following structure.

```
{  
  "version":0.7
  "repository":"https://github.com/gomezportillo/dss-pharmacy",
  "server_dev":"Pedro Manuel Gómez-Portillo",
   "android_dev":"Juan Carlos Serrano",
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

**POST** or **PUT** `/rest/products` indicating _name_, _description_, _pharmacy_ and _price_ will create a new product or override it if already exists one with the same name.

**DELETE** `/rest/products` indicating the _name_ of the product to be deleted will delete it.

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

**POST** or **PUT** `/rest/pharmacies` indicating _name_, _latitude_ and _longitude_ will create a new pharmacy or override it if already exists one with the same name.

**DELETE** `/rest/pharmacies` indicating the _name_ of the pharmacy will delete it.

## Cart

**GET** `/rest/cart/all` will return the list of all the products in the cart with the following format.

```
[  
   {  
      "description":"Cures headache",
      "name":"Ibuprofen",
      "pharmacy":"Pharmacy 1",
      "price":"7",
      "quantity":2
   },
   {  
      "description":"Cures flu",
      "name":"Frenadol",
      "pharmacy":"Pharmacy 2",
      "price":"12",
      "quantity":1
   }
]
```

**POST** or **PUT** `/rest/cart` indicating _name_, _description_, _pharmacy_ and _price_ will create a new product in the cart with quantity **1** or add it **+1** quantity if already exists one with the same name.

**DELETE** `/rest/cart/all` will delete the whole shopping cart.


## Order

**GET** `/rest/orders/all` will return the list of all the orders in the cart with the following format.

```
[  
   {  
      "email":"user1@email.com",
      "products":[  
         {  
            "description":"Cures headache",
            "name":"Ibuprofen",
            "pharmacy":"Pharmacy 1",
            "price":"7",
            "quantity":1
         }
      ],
      "type":"Reserve"
   },
   {  
		 "email":"user2@email.com",
      "products":[  
         {  
            "description":"Cures flu",
            "name":"Frenadol",
            "pharmacy":"Pharmacy 2",
            "price":"12",
            "quantity":2
         },
         {  
            "description":"Cures wounds",
            "name":"Bandage",
            "pharmacy":"Pharmacy 1",
            "price":"10",
            "quantity":1
         }
      ],
      "type":"Purchase"
   }
]
```

**POST** or **PUT** `/rest/order` indicating _email_ and _type_ will create a new order with the products that are currently on the cart (no need to specify them). The type of the order can be **Reserve** if it is a reserve or **Purchase** if the user has bought the products. No reestrictions regarding quantity or pharmacies are applied.

### Errors

* If the email of the user is not found in the system, the server will return a JSON message with code `404` as follows.

```
{  
   "status" : "404",
   "message" : "User with email $email not found."
}
```

* If the cart is empty, the server will return a JSON message with the code `409` as follows.

```
{  
   "status" : "409",
   "message" : "Cart cannot be empty."
}
```

## Users

**GET** `/rest/users/all` will return the list of all users with the following format.

```
[  
   {  
      "email":"admin",
      "name":"Administrator",
      "password":"admin"
   },
   {  
      "email":"gomezportillo@dss.com",
      "name":"Pedro Manuel G\u00f3mez-Portillo",
      "password":1234
   },
   {  
      "email":"xenahort@dss.com",
      "name":"Juan Carlos Serrano",
      "password":"secretpassword"
   }
]
```

**POST** or **PUT** `/rest/users` indicating _email_, _name_ and _password_ will create a new users or override it if already exists one with the same email.

**DELETE** `/rest/users` indicating the _email_ of the users to be deleted will delete it.
