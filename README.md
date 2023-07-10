# RuleEngine
Rule engine assignment

Created rule engine with basic operations like _>, <, >=, <=, ==, startsWith, endsWith, length_.

There are two api-endpoints:
**add-rule/**  - to specify rules array consisting of conditions, actions
**evaluate/**  - to calculate the results based on trained rule engine.


body structure of _add-rule/_:
**rules** is the list of multiple _rule_ associated with the rule engine
**rule** object consist of array of condition and its corresponding action
**condition** object consist of 3 keys: "var_name"- variable name; "edge_value": value to be compared with; "operator": operation to be performed between variable and value (it must be among _>, <, >=, <=, ==, startsWith, endsWith, length_)

{
    "rules": [
        {
            "conditions": [
                {"var_name": "calls", "operator": ">", "edge_value": 10},
                {"var_name": "calls", "operator": "<=", "edge_value": 15}
            ],
            "actions": "Rs 300"
        },
        {
            "conditions": [
                {"var_name": "calls", "operator": ">", "edge_value": 20},
                {"var_name": "conversion", "operator": ">", "edge_value": 15}
            ],
            "actions": "Rs 600"
        }
    ]
}

body structure of _evaluate/_:
**data_calc** is the list of evaluation queries objects 
**name** is mandatory, it is unique identifier,
**v1, v2** are variable names that are defined in conditions , and results are evaluated based on that
**value1, value2** are values for corresponding variables
{
    "data_calc": [
        {
            "name": "Ram",
            "v1": value1,
            "v2":value2
        },
        {
            "name": "Shyam",
            "v1": 28,
            "v2":20
        }
    ]
}

I have attached some samples below of body and response of apis.

_Sample 1_
**Rules**
calls > 10, calls <= 15 => 300rs
calls > 20, conversation > 15 => 600rs
**Test Case**
Ram: calls = 15, conversion = 10
Shyam: calls = 28, conversion = 20


**add-rule/**
cURL:
curl --location 'http://127.0.0.1:8000/add-rule/' \
--header 'Content-Type: application/json' \
--data '{
    "rules": [
        {
            "conditions": [
                {"var_name": "calls", "operator": ">", "edge_value": 10},
                {"var_name": "calls", "operator": "<=", "edge_value": 15}
            ],
            "actions": "Rs 300"
        },
        {
            "conditions": [
                {"var_name": "calls", "operator": ">", "edge_value": 20},
                {"var_name": "conversion", "operator": ">", "edge_value": 15}
            ],
            "actions": "Rs 600"
        }
    ]
}'

response:
{
    "message": "Success: Rule added",
    "rules": [
        {
            "conditions": [
                {
                    "var_name": "calls",
                    "operator": ">",
                    "edge_value": 10
                },
                {
                    "var_name": "calls",
                    "operator": "<=",
                    "edge_value": 15
                }
            ],
            "actions": "Rs 300"
        },
        {
            "conditions": [
                {
                    "var_name": "calls",
                    "operator": ">",
                    "edge_value": 20
                },
                {
                    "var_name": "conversion",
                    "operator": ">",
                    "edge_value": 15
                }
            ],
            "actions": "Rs 600"
        }
    ]
}


**evaluate/** 
cURL:
curl --location 'http://127.0.0.1:8000/evaluate/' \
--header 'Content-Type: application/json' \
--data '{
    "data_calc": [
        {
            "name": "Ram",
            "calls": 15,
            "conversion":10
        },
        {
            "name": "Shyam",
            "calls": 28,
            "conversion":20
        }
    ]
}'

response:
{
    "result": [
        {
            "name": "Ram",
            "value": "Rs 300"
        },
        {
            "name": "Shyam",
            "value": "Rs 600"
        }
    ]
}



_Sample 2_
**Rules**
if place startsWith _d_, endsWith _i_ => then place is delhi
if place startsWith _b_, and its length is 6 => then place is bombay

**Test Case**
l1: place = d___i
l2: place = bom___


**add-rule/**
cURL:
curl --location 'http://127.0.0.1:8000/add-rule/' \
--header 'Content-Type: application/json' \
--data '{
    "rules": [
        {
            "conditions": [
                {"var_name": "place", "operator": "startsWith", "edge_value": "d"},
                {"var_name": "place", "operator": "endsWith", "edge_value": "i"}
            ],
            "actions": "delhi"
        },
        {
            "conditions": [
                {"var_name": "place", "operator": "startsWith", "edge_value": "b"},
                {"var_name": "place", "operator": "length", "edge_value": 6}
            ],
            "actions": "bombay"
        }
    ]
}'

response:
{
    "message": "Success: Rule added",
    "rules": [
        {
            "conditions": [
                {
                    "var_name": "place",
                    "operator": "startsWith",
                    "edge_value": "d"
                },
                {
                    "var_name": "place",
                    "operator": "endsWith",
                    "edge_value": "i"
                }
            ],
            "actions": "delhi"
        },
        {
            "conditions": [
                {
                    "var_name": "place",
                    "operator": "startsWith",
                    "edge_value": "b"
                },
                {
                    "var_name": "place",
                    "operator": "length",
                    "edge_value": 6
                }
            ],
            "actions": "bombay"
        }
    ]
}


**evaluate/** 
cURL:
curl --location 'http://127.0.0.1:8000/evaluate/' \
--header 'Content-Type: application/json' \
--data '{"data_calc": [
        {
            "name": "l1",
            "place": "d___i"
        },
        {
            "name": "l2",
            "place": "bom___"
        }
    ]
}'

response:
{
    "result": [
        {
            "name": "l1",
            "value": "delhi"
        },
        {
            "name": "l2",
            "value": "bombay"
        }
    ]
}