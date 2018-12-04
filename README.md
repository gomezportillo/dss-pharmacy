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
