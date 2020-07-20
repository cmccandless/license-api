# license-api
Unofficial REST API for https://choosealicense.com/

## API

### Get All Licenses

```Bash
curl -f https://licenseapi.herokuapp.com/licenses
```

### Get Single License

*Use the `id` field from the all licenses response.

```Bash
curl -f https://licenseapi.herokuapp.com/licenses/gpl-3.0
```

### Get Rules

```Bash
curl -f https://licenseapi.herokuapp.com/rules
```

### Get API version

```Bash
curl -f https://licenseapi.herokuapp.com/version
```


### Get API Status

```Bash
curl -f https://licenseapi.herokuapp.com/status
```

## CLI

https://github.com/cmccandless/license-cli

## Rate Limiting

Requests from a single host are limited to 200/day, 50/hour
