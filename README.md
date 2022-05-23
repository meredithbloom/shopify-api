# Shopify Backend Internship

**Meredith Bloom**

## Stack

Django / Python

Additional packages: Django REST Framework

## Models

**Gadget** - Basic Inventory


| key | value |
| ----------- | ----------- |
| name | *mandatory* String, max 50 characters. |
| description | *optional* String, max 400 characters. |
| image_url | *optional* String, max 255 characters. |
| location | *optional* Foreign key. Location instance ID number. Integer. |

### RAW JSON FORMAT FOR POST/PUT REQUESTS

```
{
    "name" : "Lightsaber",
    "description" : "Deadly, although elegant weapon wielded by the Jedi.",
    "image_url" : "https://www.denofgeek.com/wp-content/uploads/2015/09/star_wars_the_force_awakens.jpg?fit=620%2C368",
    "location": "5"
}
```

**Location** - Assign inventory to location via location instance id #

| key | value |
| ----------- | ----------- |
| name | *mandatory* String, max 50 characters. |
| gadgets | *mandatory* Array. New locations should be initialized with empty array [].|

### RAW JSON FORMAT FOR POST/PUT REQUESTS

```
{
    "name" : "Tatooine"
}
```

## Routes

### GET - by model, by id

`/api/gadgets` - List of all gadgets, ordered by id number (auto generated whenever new model instance is created)

`api/gadgets/<id>` - Show specific gadget by id number


`api/locations/` - List all locations, ordered by id number. Location JSON includes array of gadget objects that are stored at given location.

`api/locations/<id>` - Show specific location by id number


### POST 

`/api/gadgets` - Create new gadget. Only required fields are name and location(id).

```
{
    "name": "Xray Goggles",
    "location": 1
}
```

`api/locations/` - Create new location. Both name and gadgets field are required. Gadgets field can be initialized as empty array.

```
{
    "name": "Atlantis",
    "gadgets": []
}
```

### PUT (UPDATE)

`api/gadgets/<id>` - Can update all gadget fields except for id. Can switch to new location via put route.

```
{
    "id": 4,
    "name": "X-Ray Goggles",
    "location": 5
}
```


`api/locations/<id>` - Can update location name, **not** gadgets in gadget list.

```
{
    "id": 3,
    "name": "Mars Rover",
    "gadgets": []
}
```

### DELETE 

`api/gadgets/<id>` - Delete gadget by ID.


`api/locations/<id>` - Delete location by ID. Will cascade delete any gadgets stored at that location.
