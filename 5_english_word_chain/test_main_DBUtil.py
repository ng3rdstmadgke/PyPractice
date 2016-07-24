import unittest
from main import DBUtil
import sqlite3
import os
from unittest import mock

class MyTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists("test_dictionary.txt"):
            os.remove("test_dictionary.txt")
        with open("test_dictionary.txt", "w") as f:
            f.write("test\nhello")
        self.dbutil = DBUtil("test_dictionary.txt")

    def tearDown(self):
        if os.path.exists("test_dictionary.txt"):
            os.remove("test_dictionary.txt")

    def test_insert_into_dictionary(self):
        self.dbutil.insert_into_dictionary()
        con = sqlite3.connect("word_chain.db")
        cur = con.cursor()
        sql = "select * from dictionary"
        cur.execute(sql)
        data = cur.fetchall()
        self.assertEqual(data, [(1, "test", 0), (2, "hello", 0)])

    def test_delete_used_word_from_dictionary(self):
        self.dbutil.insert_into_dictionary()
        self.dbutil.delete_used_word_from_dictionary("hello")
        con = sqlite3.connect("word_chain.db")
        cur = con.cursor()
        sql = "select * from dictionary"
        cur.execute(sql)
        data = cur.fetchall()
        self.assertEqual(data, [(1, "test", 0), (2, "hello", 1)])

    def test_select_all_from_dictionary(self):
        self.dbutil.insert_into_dictionary()
        data = self.dbutil._select_all_from_dictionary()
        self.assertEqual(data, [(1, "test", 0), (2, "hello", 0)])

    def test_fetch_optimal_word_from_dictionary_1(self):
        self.dbutil.insert_into_dictionary()
        with mock.patch("main.DBUtil._select_all_from_used_words", return_value=[(1, "stash", "s", "h"), (2, "hash", "h", "h")]):
            word = self.dbutil.fetch_optimal_word_from_dictionary()
        self.assertEqual(word, "hello")


    def test_fetch_optimal_word_from_dictionary_2(self):
        self.dbutil.insert_into_dictionary()
        with mock.patch("main.DBUtil._select_all_from_used_words",
                        return_value=[(1, "hello", "h", "o"), (2, "demo", "d", "o")]):
            word = self.dbutil.fetch_optimal_word_from_dictionary()
        self.assertEqual(word, False)

    def test_confirm_word_in_dictionary_True(self):
        self.dbutil.insert_into_dictionary()
        ret = self.dbutil.confirm_word_in_dictionary("hello")
        self.assertEqual(ret, True)


    def test_confirm_word_in_dictionary_False(self):
        self.dbutil.insert_into_dictionary()
        ret = self.dbutil.confirm_word_in_dictionary("demo")
        self.assertEqual(ret, False)

    def test_select_all_from_used_words(self):
        con = sqlite3.connect("word_chain.db")
        cur = con.cursor()
        cur.execute("INSERT INTO used_words (word, start, end) VALUES ('test', 't', 't'), ('team', 't', 'm')")
        con.commit()
        data = self.dbutil._select_all_from_used_words()
        self.assertEqual(data, [(1, "test", "t", "t"), (2, "team", "t", "m")])

    def test_insert_into_used_words(self):
        self.dbutil.insert_into_used_words("hello")
        con = sqlite3.connect("word_chain.db")
        cur = con.cursor()
        cur.execute("select * from used_words")
        data = cur.fetchall()
        self.assertEqual(data, [(1, "hello", "h", "o")])

    def test_fetch_used_words_list(self):
        with mock.patch("main.DBUtil._select_all_from_used_words", return_value=[(1, "test", "t", "t"), (2, "team", "t", "m")]):
            data = self.dbutil.fetch_used_words_list()
        self.assertEqual(data, ["test", "team"])

    def test_search_player_which_use_the_word_senko_user_1(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["ham", "spam", "egg"]):
            ret = self.dbutil.search_player_which_use_the_word("USER", "egg")
        self.assertEqual(ret, ["USER", 3])

    def test_search_player_which_use_the_word_senko_user_2(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["ham", "spam", "egg"]):
            ret = self.dbutil.search_player_which_use_the_word("USER", "spam")
        self.assertEqual(ret, ["CPU", 2])

    def test_search_player_which_use_the_word_senko_cpu_1(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["ham", "spam", "egg"]):
            ret = self.dbutil.search_player_which_use_the_word("CPU", "egg")
        self.assertEqual(ret, ["CPU", 3])

    def test_search_player_which_use_the_word_senko_cpu_2(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["ham", "spam", "egg"]):
            ret = self.dbutil.search_player_which_use_the_word("CPU", "spam")
        self.assertEqual(ret, ["USER", 2])

    def test_compare_start_and_end_ture(self):
        with mock.patch("main.DBUtil._select_all_from_used_words", return_value=[(1, "ham", "h", "m")]):
            ret = self.dbutil.compare_start_and_end("man")
        self.assertEqual(ret, True)

    def test_compare_start_and_end_false(self):
        with mock.patch("main.DBUtil._select_all_from_used_words", return_value=[(1, "ham", "h", "m")]):
            ret = self.dbutil.compare_start_and_end("spam")
        self.assertEqual(ret, False)










if __name__ == "__main__":
    unittest.main()