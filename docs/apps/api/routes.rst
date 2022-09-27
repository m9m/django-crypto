=======
GET /
=======
-------
Purpose
-------
Index 

-------
Headers
-------
default

----
Body
----
None

--------
Response
--------
JSON

=========
GET news/
=========
-------
Purpose
-------
Poll for the default news

-------
Headers
-------
default

----
Body
----
None

--------
Response
--------

::

    JSON Text
    ├── data
    │   └── reels
    └── version 

=========
GET price
=========
-------
Purpose
-------
Poll for coin(s) base off the ticker values supplemented as query parameters

-------
Headers
-------
default

----
Body
----
Query params
*coins=ticker,ticker,ticker (btc,eth,zec)

--------
Response
--------

::

    JSON Text
    ├── data
    │   └── bitcoin
    |   └── ethereum
    |   └── etc...
    └── version 

