INIT = 0
MAX_POPULATION = 100
KP_INIT = 2
KI_INIT = 0
KD_INIT = 2
TENSE_SCORE = 5
LAST_GEN_COUNT = 10
KILL_ALL = 1
WATERFALL_INC = 1
WATERFALL_THRESHOLD = 5

TCP_CONGESTION_CONTROL = 0

LINEAR_INC = 0
EXPONENTIAL_GROWTH = 1

CONST_K = 0.5

MAX_KI = 0.5
MAX_SCORE = 98

CREATE_TABLE_HEAD = 'CREATE TABLE IF NOT EXISTS PID_RECORD_HISTORY '
CREATE_TABLE_PK = '( id int UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,'
CREATE_TABLE_FH = CREATE_TABLE_HEAD + CREATE_TABLE_PK
CREATE_TABLE_END = ') charset=utf8;'
COLUMN_TYPE = ' varchar(15)'

INSERT_HEAD = 'INSERT INTO PID_RECORD_HISTORY '
INSERT_MID = ') VALUES '
INSERT_END = ');'
