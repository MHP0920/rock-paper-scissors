import random

class Info:
    def __init__(self):
        self.valid_options = {'D': "K", "L": "D", "K": "L"}
        self.converter = {"D": "Đấm", "L": "Lá", "K": "Kéo"}
        self.valid_status = {
            'unvalid-option': False,
            'pl-is-winner': "Người chơi chiến thắng",
            'cp-is-winner': "Máy chiến thắng",
            "unknown-error": False,
            "success": True,
            "continue": True,
            "exit": exit
        }
        self.chosen = list(self.valid_options.keys())
        self.valid_status_keys = list(self.valid_status.keys())
        self.player_choose = None
        self.computer_choose = None
        self.ciz = self.Customize()
    def Customize(self):
        return {
            "Basis-info": [
                "+".center(50, '='),
                "TRÒ CHƠI ĐẤM LÁ KÉO".center(50),
                "Chào mừng bạn đến với trò chơi của {}!",
                "Chúc bạn có những giờ chơi thật vui vẻ!",
                "+".center(50, '='),
            ],
            "Input-info": [
                "Lượt game thứ {}".center(50, '-'),
                """Mời người chơi nhập lựa chọn\nĐấm: D\nLá: L\nKéo: K\nLựa chọn của bạn: """,
                "Bạn có muốn chơi tiếp không? (Y/N): "
            ],
            "Result-info": [
                "Kết quả".center(50, '-'),
                "Bạn chọn: {}",
                "Máy chọn: {}"
            ],
            "Message-info": [
                "Người chơi chọn không hợp lệ",
                "Lựa chọn của người chơi là hợp lệ",
                "Người chơi đã chiến thắng!",
                "Máy đã chiến thắng!",
                "Người chơi và máy đã hòa!"
            ]
        }

class Validate():
    def __init__(self):
        self.inf = Info()
    def Winner(self, pl, cp):
        _pl_real = self.inf.valid_options[pl]
        _cp_real = self.inf.valid_options[cp]
        if _pl_real == cp:
            return 1
        elif _cp_real == pl:
            return 0
        return 3
    def CheckValidGame(self, pl):
        if not any(x==pl for x in self.inf.chosen):
            return {"message": self.inf.ciz["Message-info"][0], "status": self.inf.valid_status_keys[0]}
        return {"message": self.inf.ciz["Message-info"][1], "status": self.inf.valid_status_keys[4]}
    def CheckValidLoop(self, inp:str):
        inp = inp.lower()
        if inp == "y":
            return {"status": self.inf.valid_status_keys[5]}
        if inp == 'n':
            return {"status": self.inf.valid_status_keys[6]}
        else:
            return {"status": self.inf.valid_status_keys[0]}
class Game_play(Info):
    def __init__(self):
        self.validate = Validate()
        self.info = Info()
        self.current_round = 1
        self.author = "Trần Minh Hiếu (MHP)"
        self.Start()
    def Start(self):
        print(self.info.ciz['Basis-info'][0])
        print(self.info.ciz['Basis-info'][1])
        print(self.info.ciz['Basis-info'][2].format(self.author))
        print(self.info.ciz['Basis-info'][3])
        print(self.info.ciz['Basis-info'][4]) 
        self.Get_input()
    def Get_Computer_Choose(self):
        return random.randint(0,2)
    def Get_input(self):
        print(self.info.ciz['Input-info'][0].format(str(self.current_round)))
        _player = input(self.info.ciz["Input-info"][1])
        _computer = self.info.chosen[self.Get_Computer_Choose()]
        _valid = self.validate.CheckValidGame(_player)
        if not self.info.valid_status[_valid["status"]]:
            print(_valid['message'])
            return self.Loop()
        else:
            self.Endgame(_player, _computer)
    def Endgame(self, pl: str, cp: str):
        print(self.info.ciz['Result-info'][0])
        print(self.info.ciz["Result-info"][1].format(self.info.converter[pl]))
        print(self.info.ciz["Result-info"][2].format(self.info.converter[cp]))
        _winner = self.validate.Winner(pl, cp)
        if _winner == 0:
            print(self.info.ciz['Message-info'][3])
        elif _winner == 1:
            print(self.info.ciz['Message-info'][2])
        else:
            print(self.info.ciz['Message-info'][4])
        self.Loop()
    def Loop(self):
        _ask = input(self.info.ciz['Input-info'][2])
        _ask = self.validate.CheckValidLoop(_ask)
        if self.info.valid_status[_ask['status']] == True:
            self.current_round += 1
            return self.Get_input()
        elif self.info.valid_status[_ask['status']] == False:
            print(self.info.ciz["Message-info"][0])
            return self.Loop()
        else:
            self.info.valid_status[_ask['status']]()

Game_play()