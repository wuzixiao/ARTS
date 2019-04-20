# Simple Introduction of NoSQL

### Some questions I got before I start to read the paper
* What is NoSQL
* Why do we have NoSQL
* How many kinds of NoSQL
* Is NoSQL ACID

### What is NoSql?
NoSql is **Not only SQL**. Traditional relational database like Mysql, SqlServer are very good at store text based information. For example, in a trading platform, most of data like personal information, account information, transaction are text based information, and they are contected with each other. Personal infor and account infor are many to many relationship, transaction infor and account infor and many to one relationship.  

### Why do we have NoSql?
The last company I worked for in China is a social network company, they use Nosql(Redis) for saving user's timeline. Not only Redis is faster than RDB, but also it supports different forms of Data, and it is easy to scale.

Nowdays, big data use cases are more and more popular. There are 4 dimension of BigData:
* Velocity
* Varity
* Volume
* Complexity

NoSql is more suitable to deal with this kind of data.

### How many kinds of NoSql?
* Document Store
	* MongoDB and CouchDB
* Key-Value Store
	* Redis, DyanmoDB, Azure Table Storage, BerkeleyDB
* Graph Database
	* Neo4j, VertexDB, AllegroGraph, Gstore

### Is NoSql ACID?
Actually, Nosql and ACID are orthogonal.  In early vervion of MongoDB, it doesn't support ACID. When you update multiple Document in one command, it could fail in the middle. From version4.0, it support transational function. Actually, I don't need ACID all the time, maybe in most cases, we don't. 

### A little bit more about Graph Database
There are 5 keywords:
1. Nodes
2. Relationships
3. Properties
4. Path
5. Traversal

As far as I know it is very fast. But comparing with other Nosql DB, the data design in graph Sql is not straight forward as RDBMS. Later I will read more about Graph DB and share here.

