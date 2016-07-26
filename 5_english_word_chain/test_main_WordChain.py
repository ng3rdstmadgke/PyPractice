import unittest
from unittest import mock
from main import WordChain
import os

class MyTestCase(unittest.TestCase):
    def setUp(self):
        with open("test_dictionary.txt", "w") as f:
            f.write("ab\nbc\ncd\nde")

    def tearDown(self):
        if os.path.exists("test_dictionary.txt"):
            os.remove("test_dictionary.txt")

    def test_user_input(self):
        with mock.patch("builtins.input", return_value="hello") as mock_input:
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.user_input()
        self.assertEqual(ret, "hello")

    def test_judge_flg_1(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["a", "b", "c"]) as mock_dbutil:
            wordchain = WordChain("test_dictionary.txt")
            message = wordchain.judge(["d", 1])
        self.assertEqual(message, "まいりました！あなたの勝ちです。今回のしりとりでは 3 個の単語を使用しました。")

    def test_judge_flg_2(self):
        with mock.patch("main.DBUtil.fetch_used_words_list", return_value=["a", "b", "c"]) as mock_dbutil:
            wordchain = WordChain("test_dictionary.txt")
            message = wordchain.judge(["d", 2])
        self.assertEqual(message, "しりとりルール違反です。私の勝ちです。今回のしりとりでは 3 個の単語を使用しました。")

    def test_judge_flg_3(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_used_words_list.return_value = ["a", "b", "c"]
        mock_dbutil.search_player_which_use_the_word.return_value = ["CPU", "1"]
        with mock.patch("main.DBUtil", return_value=mock_dbutil):
            wordchain = WordChain("test_dictionary.txt")
            message = wordchain.judge(["d", 3])
        self.assertEqual(message, "その言葉は 1 回目に CPU が使用しています。わたしの勝ちです。今回のしりとりでは 3 個の単語を使用しました。")

    def test_cpu_turn_1(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = False
        with mock.patch("main.DBUtil", return_value=mock_dbutil):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.cpu_turn()
        self.assertEqual(ret, ["", 1])

    def test_cpu_turn_0(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = "hello"
        with mock.patch("main.DBUtil", return_value=mock_dbutil):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.cpu_turn()
        self.assertEqual(ret, ["hello", 0])

    def test_user_turn_0(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = "hash"
        mock_dbutil.confirm_word_in_dictionary.side_effect = [False, "hello"]
        mock_dbutil.compare_start_and_end.return_value = True
        mock_dbutil.fetch_used_words_list.return_value = []
        with mock.patch("main.DBUtil", return_value=mock_dbutil), \
             mock.patch("main.WordChain.user_input", return_value="hello"):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.user_turn()
        self.assertEqual(ret, ["hello", 0])

    def test_user_turn_1(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = False
        with mock.patch("main.DBUtil", return_value=mock_dbutil):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.user_turn()
        self.assertEqual(ret, ["", 1])


    def test_user_turn_2(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = "hash"
        mock_dbutil.confirm_word_in_dictionary.side_effect = [False, "hello"]
        mock_dbutil.compare_start_and_end.return_value = False
        with mock.patch("main.DBUtil", return_value=mock_dbutil), \
             mock.patch("main.WordChain.user_input", return_value="hello"):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.user_turn()
        self.assertEqual(ret, ["hello", 2])

    def test_user_turn_3(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.fetch_optimal_word_from_dictionary.return_value = "hash"
        mock_dbutil.confirm_word_in_dictionary.side_effect = [False, "hello"]
        mock_dbutil.compare_start_and_end.return_value = True
        mock_dbutil.fetch_used_words_list.return_value = ["hello"]
        with mock.patch("main.DBUtil", return_value=mock_dbutil), \
             mock.patch("main.WordChain.user_input", return_value="hello"):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.user_turn()
        self.assertEqual(ret, ["hello", 3])


if __name__ == '__main__':
    unittest.main()
