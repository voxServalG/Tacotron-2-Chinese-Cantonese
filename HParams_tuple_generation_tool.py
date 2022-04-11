class HParams:
    def __init__(self, **kwargs):
        self.__hparam_list__ = []
        for key, value in kwargs.items():
            self.__single_pair = (key, value)
            self.__hparam_list__.append(self.__single_pair)

    def get_tuple(self):
        return self.__hparam_list__
