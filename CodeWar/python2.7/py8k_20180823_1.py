# -*- coding: utf-8 -*
import math

'''
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; 
the better the player the lower the handicap.
test.assert_equals(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]),['Open', 'Senior', 'Open', 'Senior'])
test.assert_equals(openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]),['Open', 'Open', 'Senior', 'Open'])
'''


def get_p(data):
    # Hmmm.. Where to start?
    list = []
    for i in range(len(data)):
        for j in range(1):
            if data[i][j] >= 55 and data[i][j + 1] > 7:
                list.append("Senior")
                break
            else:
                list.append("Open")
    return(list)


print(get_p([[45, 12],[55,21],[19, -2],[104, 20]]))