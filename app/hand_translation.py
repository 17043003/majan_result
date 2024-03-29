class HandTranslation:
    def __init__(self):
        self.hands = {
            "Chankan" : "槍槓(チャンカン)",
            "Chantai" : "混全帯幺九(チャンタ)",
            "Chiitoitsu" : "七対子(チートイツ)",
            "Chinitsu" : "清一色(チンイツ)",
            "Yakuhai (chun)" : "役牌(中)",
            "DaburuOpenRiichi" : "ダブルオープンリーチ",
            "Double Riichi" : "ダブル立直",
            "Dora" : "ドラ",
            "Haitei Raoyue" : "海底撈月(ハイテイ)",
            "Yakuhai (haku)" : "役牌(白)",
            "Yakuhai (hatsu)" : "役牌(發)",
            "Honitsu" : "混一色(ホンイツ)",
            "Honroutou" : "混老頭(ホンロウトウ)",
            "Houtei Raoyui" : "河底撈魚(ホウテイ)",
            "Iipeiko" : "一盃口(イーペーコー)",
            "Ippatsu" : "一発",
            "Ittsu" : "一気通貫",
            "Junchan" : "純全帯公九(ジュンチャン)",
            "Nagashi Mangan" : "流し満貫",
            "OpenRiichi" : "オープンリーチ",
            "Pinfu" : "平和(ピンフ)",
            "Renhou" : "人和",
            "Riichi" : "立直(リーチ)",
            "Rinshan Kaihou" : "嶺上開花(リンシャンカイホウ)",
            "Ryanpeikou" : "二盃口(リャンペーコー)",
            "San Ankou" : "三暗刻",
            "San Kantsu" : "三槓子(サンカンツ)",
            "Sanshoku Doujun" : "三色同順",
            "Sanshoku Doukou" : "三色同刻",
            "Shou Sangen" : "小三元",
            "Tanyao" : "断么九(タンヤオ)",
            "Toitoi" : "対々和(トイトイホー)",
            "Menzen Tsumo" : "門前清自摸和",
            "Yakuhai (east)" : "役牌(東)",
            "Yakuhai (north)" : "役牌(北)",
            "Yakuhai (wind of place)" : "役牌(場風)",
            "Yakuhai (wind of round)" : "役牌(自風)",
            "Yakuhai (south)" : "役牌(南)",
            "Yakuhai (west)" : "役牌(西)",
        }

        self.yakumans = {
            "Chiihou" : "地和",
            "Chinroutou" : "清老頭",
            "Chuuren Poutou" : "九蓮宝燈",
            "Daburu Chuuren Poutou" : "純正九蓮宝燈",
            "Kokushi Musou Juusanmen Matchi" : "国士無双十三面待ち",
            "Daichisei" : "大七星",
            "Daisangen" : "大三元",
            "Daisharin" : "大車輪",
            "Dai Suushii" : "大四喜",
            "Kokushi Musou" : "国士無双",
            "Paarenchan" : "八連荘",
            "RenhouYakuman" : "人和",
            "Ryuuiisou" : "緑一色",
            "Sashikomi" : "",
            "Shousuushii" : "小四喜",
            "Suu Ankou" : "四暗刻",
            "Suu Ankou Tanki" : "四暗刻",
            "Suu Kantsu" : "四槓子",
            "Tenhou" : "天和",
            "Tsuu Iisou" : "字一色",
        }

        self.fu_reason = {
            "base" : "基本符",
            "penchan" : "ペンチャン",
            "kanchan" : "カンチャン",
            "valued_pair" : "役牌雀頭",
            "double_valued_pair" : "ダブル役牌雀頭",
            "pair_wait" : "単騎待ち",
            "tsumo" : "ツモ",
            "hand_without_fu" : "",
            "closed_pon" : "暗刻(中張牌)",
            "open_pon" : "明刻(中張牌)",
            "closed_terminal_pon" : "暗刻(幺九牌)",
            "open_terminal_pon" : "明刻(幺九牌)",
            "closed_kan" : "暗槓(中張牌)",
            "open_kan" : "明槓(中張牌)",
            "closed_terminal_kan" : "暗槓(幺九牌)",
            "open_terminal_kan" : "明槓(幺九牌)"
        }

        return

    def hand_translate(self, hand_name):
        translated_hand_name = self.hands[hand_name]
        return translated_hand_name

    def yakuman_translate(self, hand_name):
        translated_hand_name = self.yakumans[hand_name]
        return translated_hand_name

    def fu_translate(self, reason):
        return self.fu_reason[reason]


    def translate(self, hand_name, is_yakuman=False):
        if(is_yakuman):
            return self.yakuman_translate(hand_name)
        else:
            return self.hand_translate(hand_name)

    
