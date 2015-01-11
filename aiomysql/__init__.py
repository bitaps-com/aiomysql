"""
aiomysql: A pure-Python MySQL client library for asyncio.

Copyright (c) 2010, 2013-2014 PyMySQL contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from pymysql import (DBAPISet, NULL, Binary, DATE, NUMBER,
                     BINARY, ROWID, STRING, TIME, TIMESTAMP)
from pymysql.constants import FIELD_TYPE
from pymysql.converters import escape_dict, escape_sequence, escape_string

from pymysql.times import (Date, Time, Timestamp,
                           DateFromTicks, TimeFromTicks, TimestampFromTicks)

from pymysql.err import (Warning, Error, InterfaceError, DataError,
                         DatabaseError, OperationalError, IntegrityError,
                         InternalError,
                         NotSupportedError, ProgrammingError, MySQLError)

from .connection import Connection, connect
from .pool import create_pool, Pool

__version__ = '0.0.1'

__all__ = [
    'Date',
    'Time',
    'Timestamp',
    'DateFromTicks',
    'TimeFromTicks',
    'TimestampFromTicks',
    'Binary',
    'FIELD_TYPE',
    'NULL',
    'NUMBER',
    'BINARY',
    'ROWID',
    'STRING',
    'TIME',
    'TIMESTAMP',
    'DATE',

    # Errors
    'Error',
    'DataError',
    'DatabaseError',
    'IntegrityError',
    'InterfaceError',
    'InternalError',
    'MySQLError',
    'NotSupportedError',
    'OperationalError',
    'ProgrammingError',
    'Warning',

    'DBAPISet',

    'apilevel',
    'escape_dict',
    'escape_sequence',
    'escape_string',
    'paramstyle',
    'threadsafety',
    "__version__",

    'Connection',
    'Pool'
    'connect',
    'create_pool',
]

(Connection, Pool, connect, create_pool)  # pyflakes

threadsafety = 1
apilevel = '2.0'
paramstyle = 'format'