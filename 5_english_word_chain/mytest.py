#!/usr/bin/env python3
import sqlite3
import os

class DBUtil(object):
    def __init__(self):
        if os.path.exists("word_chain.db") is True:
            os.remove("word_chain.db")
        self.con = sqlite3.connect("word_chain.db")
        self.cur = self.con.cursor()
        used_words = "create table used_words(id integer primary key, word text, start text, last text)"
        dictionary = "create table dictionary (id integer primary key, word text, del integer)"
        self.cur.execute(used_words)
        self.cur.execute(dictionary)

    def insert_into_dictionary(self):
        with open("dictionary.txt", "r") as f:
            dictionary_data = f.read()
        sql = "insert into dictionary (word, del) values ('" + dictionary_data.replace("\n", "', 0), ('") + "', 0)"
        self.cur.execute(sql)
        self.con.commit()

    def delete_used_word_from_dictionary(self, word):
        sql = "update dictionary del = 1 where word = '{}'".format(word)
        self.cur.execute(sql)
        self.con.commit()

    def fetch_optimal_word_from_dictionary(self, word):
        start = word[0]
        sql = "select * from dictionary where word like '{}%'".format(start)
        self.cur.execute(sql)
        fetch_word = self.cur.fetchone()
        if fetch_word:
            return str(fetch_word[2])
        else:
            return False

    def confirm_word_in_dictionary(self, word):
        sql = "select * from dictionary where word = '{}'".format(word)
        self.cur.execute(sql)
        fetch_word = self.cur.fetchall()
        if fetch_word:
            return True
        else:
            retur False

    def _select_all_from_used_words(self):
        sql = "select * from used_words"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def insert_into_used_words(self, word):
        insert_word = str(word)
        start = insert_word[0]
        end = insert_word[-1]
        sql = "insert into used_word (word, start, end) values (?, ?, ?)"
        self.cur.execute(sql, (insert_word, start, end))
        self.con.commit()

        pass
    def fetch_used_words_list(self):
        used_words_list = []
        all_data = self._select_all_from_used_words()
        for i in all_data:
            used_words_list.append(str(i[1]))
        return used_words_list

    def search_player_which_use_the_word(self, senko, word):
        used_word_list = self.fetch_used_words_list()
        if word in used_word_list:
            word_index = used_word_list.index(word)
            if senko == "user":
                if word in used_word_list[0::2]:
                    ret = ["user", word_index]
                else:
                    ret = ["cpu", word_index]
            else:
                if word in used_word_list[0::2]:
                    ret = ["cpu", word_index]
                else:
                    ret = ["user", word_index]
            return ret
        else:
            return False

    def compare_start_and_end(self, word):
        input_word_start = word[0]
        all_data = self._select_all_from_used_words()
        last_word_end = all_data[-1][2]
        if input_word_start == last_word_end:
            return True
        else:
            return False

if __name__ == "__main__":
