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
            "ChuurenPoutou" : "九蓮宝燈",
            "DaburuChuurenPoutou" : "",
            "DaburuKokushiMusou" : "",
            "Daichisei" : "大七星",
            "Daisangen" : "大三元",
            "Daisharin" : "大車輪",
            "DaiSuushii" : "大四喜",
            "KokushiMusou" : "国士無双",
            "Paarenchan" : "",
            "RenhouYakuman" : "",
            "Ryuuiisou" : "緑一色",
            "Sashikomi" : "",
            "Shousuushii" : "小四喜",
            "Suuankou" : "四暗刻",
            "SuuankouTanki" : "四暗刻",
            "Suukantsu" : "四槓子",
            "Tenhou" : "天和",
            "Tsuuiisou" : "字一色",
        }

        return

    def hand_translate(self, hand_name):
        translated_hand_name = self.hands[hand_name]
        return translated_hand_name

    def yakuman_translate(self, hand_name):
        translated_hand_name = self.yakumans[hand_name]
        return translated_hand_name

    def translate(self, hand_name, is_yakuman=False):
        if(is_yakuman):
            return self.yakuman_translate(hand_name)
        else:
            return self.hand_translate(hand_name)

    
