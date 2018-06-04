# license-api
Unofficial REST API for choosealicense.com

## Examples:

### Get All Licenses

```Bash
curl -f https://licenseapi.herokuapp.com/licenses
```

### Get Single License

*Use the `id` field from the all licenses response.

```Bash
curl -f https://licenseapi.herokuapp.com/licenses/gpl-3.0
```
