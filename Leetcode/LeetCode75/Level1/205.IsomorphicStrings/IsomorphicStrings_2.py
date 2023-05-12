class Solution:
    def append_dict(self, str):

        # str_dict = {s: [] for s in dict.fromkeys(string)}

        # for i, alpha in enumerate(string):
        #     str_dict[alpha].append(i)

        dict_data = {}
        for i in range(len(str)):
            if str[i] not in dict_data :
                dict_data[str[i]] = []
                dict_data[str[i]].append(i)
            else :
                dict_data[str[i]].append(i)
        return dict_data


    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = self.append_dict(s)
        t_dict = self.append_dict(t)

        return list(s_dict.values()) == list(t_dict.values())