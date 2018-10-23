
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
MAX_OUTPUT = 100

# data record
DB_ID = 'id'
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

PROJECT_TABLE_NAME = 'project_pid'
ORIGIN_TABLE_NAME = 'origin_pid'
MEASURE_TABLE_NAME = 'measure_pid'
ANALYSE_TABLE_NAME = 'analyze_pid'

INSERT_PROJECT = 'insert into '+PROJECT_TABLE_NAME+' (name,component_group_name,component_name) values ({},{},{});'
INSERT_ORIGIN = 'insert into '+ORIGIN_TABLE_NAME+' (project_group,pid_group,p,i,d,max_pid_out) values ({},{},{},{}, {},{},{},{});'
INSERT_MEASURE = 'insert into '+MEASURE_TABLE_NAME+' (group_sequence,continue_group_sequence,sub_group_sequence,turn_angle,light_trigger) values ({},{},{},{}, {},{});'
INSERT_ANALYSE = 'insert into '+ANALYSE_TABLE_NAME+' (group_sequence,sub_group_sequence,first_react_delta_time,first_response_delta_time,peak,stable) values ({},{},{},{}, {},{},{},{});'

UPDATE_ORIGIN = 'update '++'where id={}'

DEFALUT_GEN_PROJECT_GROUP = 0

# BenchMark
PASSBY_UP = 1
PASSBY_DOWN = 2
REACT = 'react'
RESPONESE = 'response'

## adjust
SET_DATA = 0
INIT_DATA = 0


# Postboy
BASE_URL = 'http://localhost:8080/'

ORIGIN_ADDR = 'origin'
MEASURE_ADDR = 'measure'
ANALYZE_ADDR = 'analyze'

NOTIFY_ADDR = 'notify'

## adjust
