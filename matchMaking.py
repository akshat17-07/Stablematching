from imports import *

class matchMaking():
    """docstring formatchMaking."""


    def __init__(self, num):
        self.length = num
        self.people = People(num)

    def notEngMen(self):
        # this function would return all the not eng man
        notEng = []

        for i in range(self.length):

            if not self.people.getMan(i).isEng():
                notEng.append(i)

        return notEng

    def mutipleEngWomen(self):
        multiple = []

        for i in range(self.length):
            if self.people.getWomen(i).multiplePair():
                multiple.append(i)

        return multiple

    def findSutableMatch(self):
        # this function would find the all suitable matchs

        mates = []
        flag = False

        while True:
            temp = self.notEngMen()
            print(temp)
            if not len(temp):
                break

            for i in temp:
                man = self.people.getMan(i)
                match = man.makeMatch()

                if not match:
                    return None

                for j in match:
                    women = self.people.getWomen(j)

                    if women.isEng():
                        t = women.morePrefect(i)
                        if t == i:
                            women.eng = [i]
                        elif not t:
                            women.getEng(i)

                        else:
                            man.removeMatch(j)

                    else:
                        women.getEng(i)

                    self.people.setWomen(j, women)

                self.people.setMan(i, man)

                temp = self.mutipleEngWomen()
                print(temp)
                if not len(temp) and flag:
                    return None

                elif not len(temp):
                    flag = True

                else:
                    flag = False
                    for w in temp:
                        women = self.people.getWomen(w)
                        toRemove = women.removeBad()
                        for m in toRemove:
                            man = self.people.getMan(m)
                            man.removeMatch(w)

                            self.people.setMan(m, man)

                        self.people.setWomen(w, women)
            return "ok"




if __name__ == "__main__":
    a = matchMaking(5)
    print(a.findSutableMatch())
