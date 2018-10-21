
# ga
INIT = 0
KILL_ALL = 1
WATERFALL_INC = 1

TEST_SETTING = 10000

WATERFALL_THRESHOLD = TEST_SETTING

TCP_CONGESTION_CONTROL = 0
MUTANT_RATE = 0.5

ORIGIN = 'org'
BEHAVE = 'behave'
STATIC_SCORE = 'static_score'
EXECUTABLE_SCORE = 'executable_score'
DYNAMIC_STABLE_SCORE = 'dynamic_stable_score'

LINEAR_INC = 0
EXPONENTIAL_GROWTH = 1

## adjust
MIN_POPULATION = 2
MAX_POPULATION = TEST_SETTING
KP_INIT = 2
KI_INIT = 0
KD_INIT = 2
TENSE_SCORE = 0.0001
NORMAL_TENSE_SCORE = 0.01
TENSE_SCORE_K = 100
LAST_GEN_COUNT = 10

CONST_K = 0.5

MAX_KI = 0.001
MAX_SCORE = 0.5

# data record
CREATE_TABLE_HEAD = 'CREATE TABLE IF NOT EXISTS PID_RECORD_HISTORY '
CREATE_TABLE_PK = '( id int UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,'
CREATE_TABLE_FH = CREATE_TABLE_HEAD + CREATE_TABLE_PK
CREATE_TABLE_END = 'updated timestamp,created timestamp) charset=utf8;'
COLUMN_TYPE = ' varchar(15)'

TABLE_STRUCTURE = 'DESC PID_RECORD_HISTORY'
ALTER_TABLE_HEAD = 'ALTER TABLE ADD '

INSERT_HEAD = 'INSERT INTO PID_RECORD_HISTORY '
INSERT_MID = ') VALUES '
INSERT_END = ');'

GET_PROJECT_DATA = 'select * from pid_origin where project_group={} and pid_group={}'

DEFALUT_GEN_PROJECT_GROUP = 0

# BenchMark
PASSBY_UP = 1
PASSBY_DOWN = 2
REACT = 'react'
RESPONESE = 'response'

## adjust
SET_DATA = 0
INIT_DATA = 0
