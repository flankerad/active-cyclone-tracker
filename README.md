# Active Cyclone Tracker

ACT is a simple *dockerized Python* app crawls active cyclones in *Celery* task with *Redis broker*, stores data in *Postgres* table & exposes it via GET API without any frameworks. Everything is deployed by *docker-compose -d*.
> Crawler is runs as a Celery task every hour & scraps [Rammb Colostate](https://rammb-data.cira.colostate.edu/tc_realtime/) to get info on active cyclones around the world and stores info in a Postgres table.


### Made with
```bash
Python 3.6
Docker
docker-compose
Postgres
Redis
```
### Up & Running

```bash
docker-compose up -d
```
### API

Fetch data based on condtions.
 > *SELECT column1_name,column2_name FROM active_cyclones WHERE <column1_name>=<value1> AND <column2_name>=<value2>*
```
http://0.0.0.0:8000/?search='column1_name,column2_name'&<column1_name>='<value1>'&<column2_name>='<value2>'
```

### Table
> Active cyclones

```
   Column   |            Type             | Collation | Nullable |      Default      |
------------+-----------------------------+-----------+----------+-------------------+
 cid        | character varying(50)       |           | not null |                   |
 name       | character varying(50)       |           | not null |                   |
 region     | character varying(50)       |           | not null |                   |
 url        | character varying(150)      |           |          |                   |
 img        | character varying(255)      |           |          |                   |
 speed      | character varying(45)       |           |          |                   |
 type       | character varying(45)       |           |          |                   |
 updated_at | timestamp without time zone |           | not null |                   |
 created_at | timestamp without time zone |           |          | CURRENT_TIMESTAMP |

```

