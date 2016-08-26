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

    def test_main_cpu_turn_break_cpu_turn(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil._select_all_from_dictionary.return_value=[("1", "hello", "h", "o")]
        with mock.patch("random.choice", side_effect=["CPU", "hello"]), \
            mock.patch("main.DBUtil", return_value=mock_dbutil), \
            mock.patch("main.WordChain.user_turn", return_value=["optimal", 0]), \
            mock.patch("main.WordChain.cpu_turn", return_vaule=["", 1]), \
            mock.patch("main.WordChain.judge", return_value="winner user"):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.main()
        self.assertEqual(ret, "winner user")

    def test_main_cpu_turn_break_user_turn(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil._select_all_from_dictionary.return_value=[("1", "hello", "h", "o")]
        def mock_judge(ret_value):
            print(ret_value)
            if ret_value[1] == 2:
                return "OK"
            else:
                return "NG"
        with mock.patch("random.choice", side_effect=["CPU", "hello"]), \
            mock.patch("main.DBUtil", return_value=mock_dbutil), \
            mock.patch("main.WordChain.user_turn", return_value=["optimal", 2]), \
            mock.patch("main.WordChain.judge", side_effect=mock_judge):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.main()
        self.assertEqual(ret, "OK")

    def test_main_user_turn_break_cpu_turn(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.confirm_word_in_dictionary.side_effect=[False, True]
        with mock.patch("random.choice", return_value="USER"), \
            mock.patch("builtins.input", return_value="hello"), \
            mock.patch("main.DBUtil", return_value=mock_dbutil), \
            mock.patch("main.WordChain.cpu_turn", return_vaule=["", 1]), \
            mock.patch("main.WordChain.judge", return_value="winner user"):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.main()
        self.assertEqual(ret, "winner user")

    def test_main_user_turn_break_user_turn(self):
        mock_dbutil = mock.MagicMock()
        mock_dbutil.confirm_word_in_dictionary.side_effect=[False, True]
        def mock_judge(ret_value):
            print(ret_value[1])
            if ret_value[1] == 3:
                return "3"
            elif ret_value[1] == 2:
                return "2"
            elif ret_value[1] == 1:
                return "1"
            else:
                return "else"
        with mock.patch("random.choice", return_value="USER"), \
            mock.patch("main.WordChain.user_input", return_value="hello"), \
            mock.patch("main.DBUtil", return_value=mock_dbutil), \
            mock.patch("main.WordChain.cpu_turn", return_vaule=["else", 0]), \
            mock.patch("main.WordChain.user_turn", return_value=["enter", 3]), \
            mock.patch("main.WordChain.judge", side_effect=mock_judge):
            wordchain = WordChain("test_dictionary.txt")
            ret = wordchain.main()
        self.assertEqual(ret, "OK")


if __name__ == '__main__':
    unittest.main()
