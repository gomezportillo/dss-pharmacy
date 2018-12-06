# Pharmacy managing project

This repository corresponds to the server of the project.

## Deploy URL

The server is automatically deployed in the following URL after each commit.

https://dss-pharmacy.herokuapp.com/status

## Documentation

### API RESTful

The server will return JSON messages. All models will work under the _(URL)/rest/model_ route.

* **/rest/status** will return the status of the server following structure.

```
{"authors":{"mobile-app":"@xenahort","server":"@gomezportillo"},"status":"OK","version":0.1}
```

* **/rest/pharmacies** will return the list of registered pharmacies with the following structure.

```
{"Farmacia 1":{"latitude":37.198366,"longitude":-3.624976},"Farmacia 2":{"latitude":37.195993,"longitude":-3.622784}}
```
