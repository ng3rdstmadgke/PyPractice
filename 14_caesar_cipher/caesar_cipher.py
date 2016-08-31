#!/usr/bin/env python

class Caesar_Decoder(object):
    def __init__(self, text):
        self.text = text
        self.dictionary = tuple("abcdefghijklmnopqrstuvwxyz .,-")
        self.mapper = list("abcdefghijklmnopqrstuvwxyz .,-")

    def _round_mapper(self):
        mapper = self.mapper.copy()
        ret = mapper[1:] + list(mapper[0])
        self.mapper = ret

    def _decode_text_gen(self):
        ret = ""
        for i in self.text:
            if i in self.dictionary:
                code_index = self.dictionary.index(i)
                ret += self.mapper[code_index]
            else:
                ret += i
        return ret

    def decode(self):
        for i in range(30):
            self._round_mapper()
            ret = self._decode_text_gen()
            if " person " in ret:
                return ret
        return None


if __name__ == "__main__":
    text = "qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu" \
           " zir -ibtqi-qp-qaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi" \
           " rruoumxakir -ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki" \
           " -puzmzoqai -i-qscxmbu zaimzpir -i btq-iymbbq-a;iz" \
           " -iatmxximzgi.q-a zinqiuzimzgiemgipuao-uyuzmbqpimsmuzabir" \
           " -ia. za -uzsiacotiimi.qbubu zj"
    ins = Caesar_Decoder(text)
    ret = ins.decode()
    print(ret)