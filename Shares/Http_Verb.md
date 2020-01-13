# Http Verb

## Common use http verbs
    * Post
    * Put
    * Get
    * Patch
    * Delete

## When to use it

| Verb   | Url        | Is Idempotent | PayLoad        | Return                 |
| ------ | ---------- | -------------- | -------------- | ---------------------- |
| Post   | /User/     | No             | User Entity    | The new entity with id |
| Put    | /User/{id} | Yes            | User Entity    | The entity             |
| Get    | /User/{id} | Yes            | None           | The entity             |
| Patch  | /User/{id} | No             | Partial Entity | The entity             |
| Delete | /User/{id} | No             | None           | None                   |

*Note*: You may confuse about why Patch is not idempotent. It is true that if you call with same payload multiple times in a row, the return would be the same. However, if you call with an other payload in between, the reutnr before and after the middle other payload would different. So it is not idempotent.

