# ELK Essential Training

## Overview

* Use Cases
    1. Security/log analytics (Monitoring)
    2. Marketing (Data Mining)
    3. Operations (Ops)
    4. Search 

* Concepts
    * Cluster -> Node -> Shard/Replica -> Index -> Type -> Document  (Type was deprecated in Elasticsearch7)

## Setup

* On Cloud : [ElasticCould](https://www.elastic.co/cloud/?ultron=[EL]-[B]-[APAC]-ANZ-BMM&blade=adwords-s&Device=c&thor=%2Belastic%20%2Bcloud&gclid=CjwKCAjwssD0BRBIEiwA-JP5rDJ5Qax9FFZjJYA2hjV_lr6z0DQNEIhwO1IufItrRBmQdVuXfpKShRoC8LkQAvD_BwE)

* Locally
    * Install java
    * Install ELK
    * /usr/share/kibana/bin/kibana
    * Go to ip:5601/

* Play ground
    * Basic 

  ``` javascript
    GET _cat/nodes?v //?v mean pretty the format
    GET _cat/indices?v   //index information
    GET _cat/health?v  // running status

    PUT /sales  //create an index
    PUT /sales/order/123  //add a document 'order' is type, in Elasticsearch V7, the type has been deprecated
    {
        "orderID" : "123",
        "orderAmount":"500"
    }
    GET sales/order/123  //get the document
    DELETE sales  //delete index
  ```

    * Bulk API
        * /_bulk
        * --data-binary

    ``` javascript
    POST _bulk
    { "index" : { "_index" : "my-test-console", "_type" : "my-type", "_id" : "1" } }
    { "col1" : "val1" }
    { "index" : { "_index" : "my-test-console", "_type" : "my-type", "_id" : "2" } }
    { "col1" : "val2"}
    { "index" : { "_index" : "my-test-console", "_type" : "my-type", "_id" : "3" } }
    { "col1" : "val3" }
    ```

    * Load a json data file
        1. Run command curl -H 'Content-Type: application/x-ndjson' -XPOST '13.72.226.46:9200/bank/account/_bulk?pretty' --data-binary @accounts.json
        2. Configure an index pattern on Kibana (management -> index pattern)
    * Set data types
        * Core
        * Complex (json)

        ``` javascrpt
        curl -H 'Content-Type: application/x-ndjson' -XPOST '13.72.226.46:9200/_bulk?pretty' --data-binary @logs.jsonl
        ```

        * Geo
        * Specialized (ip, token)
## Querying Data

* Simple queries

```javascript
    GET bank/account/_search
    GET bank/account/_search
    {
    "query": {
        "match":{
        "state": "CA"
        }
    }
    }
    {
    "query": {
        "bool":{
        "must": [  
            {"match":{
            "state":"CA"
            }
            }
        ]
        }
    }
    }
    GET bank/account/_search
    //#region 
    //each return item has _score property/metadata  
    //query -> bool -> match/must/must_not/should (should is interesting, each critearia in [] can be added a boost attribute, and the matching item's score will be time the boost value)
    //#endregion

    GET bank/account/_search
    {
    "query": {
        "bool":{
            "should": [
                {"match":{ "state":"CA" } },
                {"match":{ "gender": {"query": "M", "boost": 3} } }
            ]
        }
    }
    }

```

* term query

```javascript
GET bank/account/_search
{
  "query": {
    "term": {  //term can used with numeric and enum
      "account_number" : 516
    }
  }
}
GET bank/account/_search
{
  "query": {
    "term": {  //not text
      "state" : "RI"  //return empty
    }
  }
}
GET bank/account/_search
{
  "query": {
    "term": {  //term can used with a array
      "account_number" : [516,432]
    }
  }
}
GET bank/account/_search
{
  "query": {
    "range": {  //range
      "account_number" : {
          "gte" : 516,  //greater than equal
          "lte" : 851,   //less than equal
          "boost":2
      }
    }
  }
}

```

* Analysis and tokenization

``` javascript
GET bank/_analyze
{
    "tokenizer":"standard",  //there are many tokenizers: standard, english, letter, email...
                            // they can be used for 
    "text": "good good study, day day up"
}
```

## Analyzing your daa

* Basic aggregations

``` javascript
GET bank/account/_search
{
  "size": 1,  //get one item in result
  "aggs": {   //aggregate
    "states": {
      "terms": {
        "field": "state.keyword"  //by state
      },
      "aggs": {   //for each state aggregate again
        "avg_bal": {
          "avg": {   //get average balance
            "field": "balance"
          }
        },
        "gender":{   //and divident by gender inside each state
          "terms": {
            "field": "gender.keyword"
          },
          "aggs": {   //for each gender get aggregate again by stats
            "stats_ban": {
              "stats": {
                "field": "balance"
              }
            }
          }
        }
      }
    }
  }
}
```

* Filtering aggregations
* Percentiles and histograms


