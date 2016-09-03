#!/usr/bin/env python
import string


class Base64:
    def __init__(self):
        self.letter_list = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/")

    def encode_base64(self, text):
        # Unicode文字列をutf8でエンコードし、バイト列に変換
        bytes_text = text.encode("utf8")
        bit_length = len(bytes_text) * 8

        # バイト列を二進数表記の文字列に変換 (二進数の桁が６の倍数になるように末尾に0を入れて調節する)
        mod = "0" * (6 - (bit_length % 6))
        binary = ""
        for i in bytes_text:
            binary += format(i, "b").zfill(8)
        binary += mod

        # 二進数表記の文字列を6bit区切りのリストに変換
        six_bit_list = []
        cnt = 0
        while cnt < bit_length:
            six_bit_list.append(binary[cnt:cnt+6])
            cnt += 6

        # 6bitの二進数をletter_listの対応する文字に変換
        ret = ""
        for i in six_bit_list:
            ret += self.letter_list[int(i, 2)]

        # 文字数が4の倍数になるように調節
        if len(ret) % 4 != 0:
            add = "=" * (4 - (len(ret) % 4))
            ret += add
        return ret

    def decode_base64(self, cipher):
        # バリデーション
        cipher = cipher.replace("=", "")

        # base64を二進数表記の文字列に変換する (二進数の桁が８の倍数になるように末尾の0を削除して調節する)
        binary = ""
        bit_length = len(cipher) * 6
        for i in cipher:
            letter_index = self.letter_list.index(i)
            binary += format(letter_index, "b").zfill(6)
        if bit_length % 8 != 0:
            diff = bit_length % 8
            binary = binary[:-diff]

        # 二進数表記の文字列を10進数のintに変換する
        digit = int(binary, 2)

        # 10進数をバイト列に変換する
        length = len(binary) // 8
        bytes_text = digit.to_bytes(length, "big")

        # バイト列をutf8でデコードし、Unicode文字列に変換
        text = bytes_text.decode("utf-8")
        return text


if __name__ == "__main__":
    ins = Base64()
    base64_cipher = ins.encode_base64("私はk-taです。よろしくお願いします！")
    print(base64_cipher)
    plane_text = ins.decode_base64("56eB44Gvay10YeOBp+OBmeOAguOCiOOCjeOBl+OBj+OBiumhmOOBhOOBl+OBvuOBme+8gQ==")
    print(plane_text)
