from . import *

class People:
    """
    This class would create a set of people and assign random preferance of mate
    """

    men = {}
    women = {}
    allPair = []
    match_man = {}
    match_women = {}


    def __init__(self, num):
        # initialzing the class
        for i in range(num):
            self.men[i] = RandomMatch.RandomMatch(num)
            self.women[i] = RandomMatch.RandomMatch(num)

            for j in range(num):
                self.allPair.append([i,j])

    def output(self):
        output = []

        o1 = []

        temp = self.match()
        if temp == None:
            o1 = "No super match exist"

        else:
            for i in temp:
                o1.append([i, temp[i][0]])

        output.append(o1)

        o2 = {}

        for i in self.men:
            temp = self.men[i].head
            l = []

            while temp:
                l.append(temp.val)
                temp = temp.next

            o2[i] = l

        output.append(o2)

        o3 = {}
        for i in self.women:
            temp = self.women[i].head
            l = []

            while temp:
                l.append(temp.val)
                temp = temp.next

            o3[i] = l
        output.append(o3)

        return output


    def match(self):
        # assigning match to null
        self.match_men = {}
        self.match_women = {}

        self.allPair = []
        for i in range(len(self.men)):
            for j in range(len(self.men)):
                self.allPair.append([i,j])

        # checking if we still have freeMan
        freeMan = self.freeMan()

        while freeMan != []:
            # matching every man
            for i in freeMan:

                if self.matchMan(i) == -1 or len(self.allPair) == 0:
                    return None

            # findind multiple matched women
            temp = self.findMultipleWomenMatched()

            # breakking all of her match and deleting bad pairs
            for w in temp:
                self.breakAllCurrentMatches(w)
                self.deleteBadPairs(w)

            freeMan = self.freeMan()

        return self.match_men



    def deleteBadPairs(self, w):
        prefer = self.women[w].tail
        while prefer != None:
            if [prefer.val[0],w] in self.allPair:
                for i in prefer.val:
                    self.allPair.remove([i,w])
                break

            prefer = prefer.pre



    def findMultipleWomenMatched(self):
        multiple = []

        for i in self.match_women:
            if len(self.match_women[i]) > 1:
                multiple.append(i)

        return multiple

    def matchMan(self, man):
        prefer = self.men[man].head

        # matching man with women in his prefer list
        while prefer:

            for w in prefer.val:
                matched = self.matchWomenWithMen(man, w)

                if matched:
                    return 1

            # if no match found try for next set of preferance
            prefer = prefer.next


        # if no match found in the list return -1
        return -1

    def matchWomenWithMen(self, man, woman):
        # if pair is not desirable
        if [man, woman] not in self.allPair:
            return False

        # if women is not matched, match man and women
        elif woman not in self.match_women:
            if man in self.match_men:
                self.match_men[man].append(woman)

            else:
                self.match_men[man] = [woman]

            self.match_women[woman] = [man]

            return True

        # if women is matched, try to findout more desirable match
        else:
            man2 = self.match_women[woman][0]
            prefer = self.women[woman].head

            while prefer:
                # if both man have same preferace
                if man in prefer.val and man2 in prefer.val:
                    self.match_women[woman].append(man)

                    if man in self.match_men:
                        self.match_men[man].append(woman)

                    else:
                        self.match_men[man] = [woman]

                    return True

                # if woman prefer her current match more
                elif man2 in prefer.val:
                    return False

                # if wome prefer the man more
                elif man in prefer.val:
                    # break all current matched of women
                    self.breakAllCurrentMatches(woman)
                    self.match_women[woman] = [man]

                    if man in self.match_men:
                        self.match_men[man].append(woman)

                    else:
                        self.match_men[man] = [woman]

                    return True

                prefer = prefer.next



    def breakAllCurrentMatches(self, woman):

        for i in self.match_women[woman]:
            self.match_men[i].remove(woman)

            if self.match_men[i] == []:
                del self.match_men[i]

        del self.match_women[woman]

    def freeMan(self):
        # finding all free man
        freeMan = []

        for i in range(len(self.men)):
            if i not in self.match_men:
                freeMan.append(i)

        return freeMan
