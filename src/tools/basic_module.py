import os
import json
import logging
import numpy as np
import pandas as pd
import warnings
import configparser
from logging.config import fileConfig
import re
import traceback
from Ticktock import ticktock

warnings.filterwarnings("ignore")

basePath = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(basePath, '../../config/algorithms.ini'))
'''
读取日志配置
'''
fileConfig(os.path.join(basePath, '../../config/logging_config.ini'), disable_existing_loggers=False)
logger = logging.getLogger()
'''
读取状态码
'''
default_error_code = int(config['Output'].get('default_error_code'))
default_error_message = config['Output'].get('default_error_message')
normal = int(config['ErrorCode'].get('normal'))
success = int(config['ErrorCode'].get('success'))
input_error = int(config['ErrorCode'].get('input_error'))
text_empty = int(config['ErrorCode'].get('text_empty'))
keyword_list_empty = int(config['ErrorCode'].get('keyword_list_empty'))
columbus_error = int(config['ErrorCode'].get('columbus_error'))
class_evaluation_error = int(config['ErrorCode'].get('class_evaluation_error'))
jabber_error = int(config['ErrorCode'].get('jabber_error'))
'''
设置全局变量
'''

re_question = re.compile('\?|？')
pauseword = open(os.path.join(basePath, '../../data/base/tagDicts/pauseWord.txt'), 'r', encoding='utf-8').read().strip().split('\n')
re_pauseword = re.compile('|'.join(pauseword))
re_no_char = compiled_rule = re.compile(r'[^\w]|_')