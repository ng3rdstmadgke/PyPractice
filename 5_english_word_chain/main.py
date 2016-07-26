#!/usr/bin/env python3
import sqlite3
import os
import random


class WordChain(object):
    def __init__(self, dictionary_file):
        """
        DBUtilインスタンスの作成する
        dictionaryテーブルに初期データを登録する
        先攻ユーザーを決める
        """
        self.ins = DBUtil(dictionary_file)
        self.ins.insert_into_dictionary()
        self.turn = random.choice(["CPU", "USER"])

    def main(self):
        """
        しりとりを実行する
        :return: -
        """
        flg = 0
        if self.turn == "USER":
            while True:
                input_word = self.user_input()
                if self.ins.confirm_word_in_dictionary(input_word) is False:
                    continue
                else:
                    break
            self.ins.delete_used_word_from_dictionary(input_word)
            self.ins.insert_into_used_words(input_word)
            while True:
                ret = self.cpu_turn()
                if ret[1] != 0:
                    break
                ret = self.user_turn()
                if ret[1] != 0:
                    break
        else:
            words_list = self.ins._select_all_from_dictionary()
            input_word = random.choice(words_list)[1]
            self.ins.delete_used_word_from_dictionary(input_word)
            self.ins.insert_into_used_words(input_word)
            print("CPU : {}".format(input_word))
            while True:
                ret = self.user_turn()
                if ret[1] != 0:
                    break
                ret = self.cpu_turn()
                if ret[1] != 0:
                    break

        message = self.judge(ret)
        print(message)

    def user_input(self):
        """
        標準入力からユーザーに単語を入力される。
        入力された単語を返す。
        :return: str
        """
        user_word = input("USER : ")
        return user_word

    def user_turn(self):
        """
        ユーザーターンの処理
        1. dictionaryテーブルに使用できる単語があるか調べる >> なければflg=1と空文字列を返す
        2. 単語を入力する。入力された単語がdictionaryテーブルに存在しない場合はもう一度やり直し。
        3. 入力した単語の先頭文字と直前に入力された単語の末尾文字が一致するかを調べる >> しなければflg=2と今回入力した単語を返す
        4. 入力した単語が以前使われていないか調べる >> 使われていた場合flg=3と今回入力した単語を返す
        5. 特にルール違反がなければdictionaryテーブルの当該単後にデリートフラグを立て、used_wordsテーブルに単語を登録し、flg=0と今回入力した単語を返す
        :return: [input_word(str), flg(int)]
        """
        if self.ins.fetch_optimal_word_from_dictionary() is False:
            return ["", 1]
        while True:
            input_word = self.user_input()
            if self.ins.confirm_word_in_dictionary(input_word) is False:
                continue
            else:
                break
        if self.ins.compare_start_and_end(input_word) is False:
            return [input_word, 2]
        if input_word in self.ins.fetch_used_words_list():
            return [input_word, 3]
        self.ins.delete_used_word_from_dictionary(input_word)
        self.ins.insert_into_used_words(input_word)
        return [input_word, 0]

    def cpu_turn(self):
        """
        CPUターンの処理
        1. 直前に使用した単語の末尾文字と同じ先頭文字を持つ単語をdictionaryテーブルから探す >> なければflg=1と空文字列を返す
        2. 特にルール違反がなければdictionaryテーブルの当該単後にデリートフラグを立て、used_wordsテーブルに単語を登録し、flg=0と今回入力した単語を返す
        :return: [input_word(str), flg(int)]
        """
        input_word = self.ins.fetch_optimal_word_from_dictionary()
        if input_word is False:
            return ["", 1]
        else:
            self.ins.delete_used_word_from_dictionary(input_word)
            self.ins.insert_into_used_words(input_word)
            print("CPU : {}".format(input_word))
            return [input_word, 0]

    def judge(self, ret):
        """
        引数にとったフラグから適切なメッセージを返す
        flg=1 : dictionaryテーブルに使える単語が存在しないため、USERの勝利
        flg=2 : 直前の単語の末尾文字と今回の単語の先頭文字が異なるため、CPUの勝利
        flg=3 : 同じ単語を２度使用したため、CPUの勝利
        :param ret: リスト形式の単語とフラグ([word(str), flg(int)])
        :return: -
        """
        word_length = len(self.ins.fetch_used_words_list())
        if ret[1] == 1:
            message = "まいりました！あなたの勝ちです。今回のしりとりでは {} 個の単語を使用しました。".format(word_length)
            return message
        elif ret[1] == 2:
            message = "しりとりルール違反です。私の勝ちです。今回のしりとりでは {} 個の単語を使用しました。".format(word_length)
            return message
        else:
            player = self.ins.search_player_which_use_the_word(self.turn, ret[0])
            message = "その言葉は {} 回目に {} が使用しています。わたしの勝ちです。今回のしりとりでは {} 個の単語を使用しました。".format(player[1], player[0], word_length)
            return message


class DBUtil(object):
    def __init__(self, dictionary_file):
        """
        word_chain.dbというファイルを作成し、used_wordsテーブルと、dictionaryテーブルを作成する。
        used_wordsテーブル : 使用済みの単語を格納する
        dictionaryテーブル : しりとりで使用できる単語を格納する
        """
        self.dictionary_file = dictionary_file
        if os.path.exists("word_chain.db") is True:
            os.remove("word_chain.db")
        self.con = sqlite3.connect("word_chain.db")
        self.cur = self.con.cursor()
        used_words = "create table used_words(id integer primary key, word text, start text, end text)"
        dictionary = "create table dictionary (id integer primary key, word text, del integer)"
        self.cur.execute(used_words)
        self.cur.execute(dictionary)

    def insert_into_dictionary(self):
        """
        辞書の初期データをdictionaryテーブルに登録する。
        :return: -
        """
        with open(self.dictionary_file, "r") as f:
            dictionary_data = f.read()
        sql = "insert into dictionary (word, del) values ('" + dictionary_data.replace("\n", "', 0), ('") + "', 0)"
        self.cur.execute(sql)
        self.con.commit()

    def delete_used_word_from_dictionary(self, word):
        """
        dictionaryテーブルの指定した単語にデリートフラグを立てる
        :param word: デリート対象の単語(str)
        :return: -
        """
        sql = "update dictionary set del = 1 where word = '{}'".format(word)
        self.cur.execute(sql)
        self.con.commit()

    def _select_all_from_dictionary(self):
        """
        dictionaryテーブルの全データを取得し、リスト形式で返す
        :return: [(index(int), word(str), delete_flg(int), (...), ...]
        """
        sql = "select * from dictionary"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def fetch_optimal_word_from_dictionary(self):
        """
        used_wordsテーブルに登録された最新の単語の末尾の文字を先頭とする単語をdictionaryテーブルから選択する。
        dictionaryテーブルから選択する単語はデリートフラグが立っていないもののみ。
        単語が存在すれば単語(str)、存在しなければFalse(bool)を返す。
        :return: str もしくは bool
        """
        start = self._select_all_from_used_words()[-1][3]
        sql = "select * from dictionary where word like '{}%' and del = 0".format(start)
        self.cur.execute(sql)
        fetch_list = self.cur.fetchall()
        if fetch_list:
            fetch_word = random.choice(fetch_list)
            return str(fetch_word[1])
        else:
            return False

    def confirm_word_in_dictionary(self, word):
        """
        指定した単語が辞書に存在するか確認する。
        単語が存在すればTrue, しなければFalseを返す
        :param word: 存在確認したい単語。(str)
        :return: bool
        """
        sql = "select * from dictionary where word = '{}'".format(word)
        self.cur.execute(sql)
        fetch_word = self.cur.fetchall()
        if fetch_word:
            return True
        else:
            return False

    def _select_all_from_used_words(self):
        """
        used_wordsテーブルから全てのデータを取得しリストで返す。
        :return: [(index(int), word(str), start(str), end(str)), (...), ...]
        """
        sql = "select * from used_words"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def insert_into_used_words(self, word):
        """
        指定した単語をused_wordsテーブルに登録する。
        :param word: used_wordsテーブルに登録したい単語。(str)
        :return: -
        """
        insert_word = str(word)
        start = insert_word[0]
        end = insert_word[-1]
        sql = "insert into used_words (word, start, end) values (?, ?, ?)"
        self.cur.execute(sql, (insert_word, start, end))
        self.con.commit()

        pass

    def fetch_used_words_list(self):
        """
        used_wordsテーブルに登録されている単語をリストで返す。
        :return: [word1(str), word2(str), ...]
        """
        used_words_list = []
        all_data = self._select_all_from_used_words()
        for i in all_data:
            used_words_list.append(str(i[1]))
        return used_words_list

    def search_player_which_use_the_word(self, senko, word):
        """
        指定した単語がused_wordsテーブルに含まれているか確認する。
        含まれていた場合、使用したプレイヤー名と、何回目に単語を使用したかをリストで返す。[player, turn]
        含まれていなかった場合、Falseを返す。
        :param senko: 先攻のユーザー名(str) # "CPU" or "USER"
        :param word: 判断対象の単語(str)
        :return: [player(str), turn(int)] もしくは False
        """
        used_word_list = self.fetch_used_words_list()
        if word in used_word_list:
            word_index = used_word_list.index(word) + 1
            if senko == "USER":
                if word in used_word_list[0::2]:
                    ret = ["USER", word_index]
                else:
                    ret = ["CPU", word_index]
            else:
                if word in used_word_list[0::2]:
                    ret = ["CPU", word_index]
                else:
                    ret = ["USER", word_index]
            return ret
        else:
            return False

    def compare_start_and_end(self, word):
        """
        指定した単語の先頭の文字と、used_wordsテーブルに登録されている最新の単語の末尾の文字が一致するかを判定する。
        一致すればTrue、一致しなければFalseを返す
        :param word: 判定対象の単語(str)
        :return: bool
        """
        input_word_start = word[0]
        all_data = self._select_all_from_used_words()
        last_word_end = all_data[-1][3]
        if input_word_start == last_word_end:
            return True
        else:
            return False

if __name__ == "__main__":
    ins = WordChain("dictionary.txt")
    ins.main()