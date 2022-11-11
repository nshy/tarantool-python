# pylint: disable=C0301,W0105,W0401,W0614

IPROTO_REQUEST_TYPE = 0x00
IPROTO_SYNC = 0x01
# replication keys (header)
IPROTO_SERVER_ID = 0x02
IPROTO_LSN = 0x03
IPROTO_TIMESTAMP = 0x04
IPROTO_SCHEMA_ID = 0X05
#
IPROTO_SPACE_ID = 0x10
IPROTO_INDEX_ID = 0x11
IPROTO_LIMIT = 0x12
IPROTO_OFFSET = 0x13
IPROTO_ITERATOR = 0x14
IPROTO_INDEX_BASE = 0x15
#
IPROTO_KEY = 0x20
IPROTO_TUPLE = 0x21
IPROTO_FUNCTION_NAME = 0x22
IPROTO_USER_NAME = 0x23
#
IPROTO_SERVER_UUID = 0x24
IPROTO_CLUSTER_UUID = 0x25
IPROTO_VCLOCK = 0x26
IPROTO_EXPR = 0x27
IPROTO_OPS = 0x28
#
IPROTO_DATA = 0x30
IPROTO_ERROR_24 = 0x31
#
IPROTO_METADATA = 0x32
IPROTO_SQL_TEXT = 0x40
IPROTO_SQL_BIND = 0x41
IPROTO_SQL_INFO = 0x42
IPROTO_SQL_INFO_ROW_COUNT = 0x00
IPROTO_SQL_INFO_AUTOINCREMENT_IDS = 0x01
#
IPROTO_ERROR = 0x52
#
IPROTO_VERSION = 0x54
IPROTO_FEATURES = 0x55
IPROTO_CHUNK = 0x80

IPROTO_GREETING_SIZE = 128
IPROTO_BODY_MAX_LEN = 2147483648

REQUEST_TYPE_OK = 0x00
REQUEST_TYPE_SELECT = 0x01
REQUEST_TYPE_INSERT = 0x02
REQUEST_TYPE_REPLACE = 0x03
REQUEST_TYPE_UPDATE = 0x04
REQUEST_TYPE_DELETE = 0x05
REQUEST_TYPE_CALL16 = 0x06
REQUEST_TYPE_AUTHENTICATE = 0x07
REQUEST_TYPE_EVAL = 0x08
REQUEST_TYPE_UPSERT = 0x09
REQUEST_TYPE_CALL = 0x0a
REQUEST_TYPE_EXECUTE = 0x0b
REQUEST_TYPE_PING = 0x40
REQUEST_TYPE_JOIN = 0x41
REQUEST_TYPE_SUBSCRIBE = 0x42
REQUEST_TYPE_ID = 0x49
REQUEST_TYPE_ERROR = 1 << 15

SPACE_SCHEMA = 272
SPACE_SPACE = 280
SPACE_INDEX = 288
SPACE_FUNC = 296
SPACE_VSPACE = 281
SPACE_VINDEX = 289
SPACE_VFUNC = 297
SPACE_USER = 304
SPACE_PRIV = 312
SPACE_CLUSTER = 320

INDEX_SPACE_PRIMARY = 0
INDEX_SPACE_NAME = 2
INDEX_INDEX_PRIMARY = 0
INDEX_INDEX_NAME = 2

ITERATOR_EQ = 0
ITERATOR_REQ = 1
ITERATOR_ALL = 2
ITERATOR_LT = 3
ITERATOR_LE = 4
ITERATOR_GE = 5
ITERATOR_GT = 6
ITERATOR_BITSET_ALL_SET = 7
ITERATOR_BITSET_ANY_SET = 8
ITERATOR_BITSET_ALL_NOT_SET = 9
ITERATOR_OVERLAPS = 10
ITERATOR_NEIGHBOR = 11

IPROTO_FEATURE_STREAMS = 0
IPROTO_FEATURE_TRANSACTIONS = 1
IPROTO_FEATURE_ERROR_EXTENSION = 2
IPROTO_FEATURE_WATCHERS = 3

# Default value for connection timeout (seconds)
CONNECTION_TIMEOUT = None
# Default value for socket timeout (seconds)
SOCKET_TIMEOUT = None
# Default maximum number of attempts to reconnect
RECONNECT_MAX_ATTEMPTS = 10
# Default delay between attempts to reconnect (seconds)
RECONNECT_DELAY = 0.1
# Default value for transport
DEFAULT_TRANSPORT = ""
# Value for SSL transport
SSL_TRANSPORT = "ssl"
# Default value for a path to SSL key file
DEFAULT_SSL_KEY_FILE = None
# Default value for a path to SSL certificate file
DEFAULT_SSL_CERT_FILE = None
# Default value for a path to SSL certificatea uthorities file
DEFAULT_SSL_CA_FILE = None
# Default value for list of SSL ciphers
DEFAULT_SSL_CIPHERS = None
# Default cluster nodes list refresh interval (seconds)
CLUSTER_DISCOVERY_DELAY = 60
# Default cluster nodes state refresh interval (seconds)
POOL_REFRESH_DELAY = 1
# Default maximum number of attempts to reconnect for pool instance
POOL_INSTANCE_RECONNECT_MAX_ATTEMPTS = 0
# Default delay between attempts to reconnect (seconds)
POOL_INSTANCE_RECONNECT_DELAY = 0

# Tarantool 2.10 protocol version is 3
CONNECTOR_IPROTO_VERSION = 3
# List of connector-supported features
CONNECTOR_FEATURES = [IPROTO_FEATURE_ERROR_EXTENSION,]
