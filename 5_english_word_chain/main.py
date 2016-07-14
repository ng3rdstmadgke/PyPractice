#!/usr/bin/env python3
import sqlite3
import os


class WordChain(object):
    def __init__(self):
        pass
    def main(self):
        pass
    def _decide_turn(self):
        pass
    def _play_word_chain(self):
        pass
    def _confirm_word_list(self):
        pass
    def _input_cpu(self):
        pass
    def _input_user(self):
        pass
    def _judge_user_word(self):
        pass
    def _processing_flag(self):
        pass

class DButil(object):
    def __init__(self):
        if os.path.exists("word_chain.db") is True:
            os.remove("word_chain.db")
        self.con = sqlite3.connect("word_chain.db")
        create_table = "create table word_chain(id integer primary key, word varchar(100), start_word varchar(1), last_word varchar(1))"


    def _all_select(self):
        pass
    def _cpu_select(self):
        pass
    def _user_select(self):
        pass
    def _last_word(self):
        pass
    def _insert_word(self):
        pass
    def _delete_all(self):
        pass