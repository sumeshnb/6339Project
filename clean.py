import os
import re
from collections import Counter

symbols = [',','.',';',':','"','<','>','?','/','\\','!','$','%','^','^','&','*','-','\'','(',')','=']

def cleanText(word):
    global symbols
    a = word.split()
    newWord = ''
    for i in a:
        if not '@' in i and not '#' in i and not 'http:' in i and not 'https:' in i:
            for j in symbols:
               i = i.replace(j,'') 
            newWord = newWord + i + ' '
    return newWord.rstrip()

def write(tweets,text,f,name):
    tweets[text] = name
    a = cleanText(text)
    if len(a) > 0:
        f.write(a)
        f.write('\n')
    return tweets

path="H:\\masters\\sem5\\special_topics_in_advanced_db\\"

f1 = open(path+'movie tweets\\the_longest_ride.txt','w')
f2 = open(path+'movie tweets\\ex_machina.txt','w')
f3 = open(path+'movie tweets\\desert_dancer.txt','w')
f4 = open(path+'movie tweets\\clouds_of_sils_maria.txt','w')
f5 = open(path+'movie tweets\\kill_me_three_times.txt','w')
f6 = open(path+'movie tweets\\lost_river.txt','w')
f7 = open(path+'movie tweets\\while_we_are_young.txt','w')
f8 = open(path+'movie tweets\\selma.txt','w')
f9 = open(path+'movie tweets\\danny_collins.txt','w')
f10 = open(path+'movie tweets\\the_second_best_exotic_marigold_hotel.txt','w')
f11 = open(path+'movie tweets\\fifty_shades_of_grey.txt','w')
f12 = open(path+'movie tweets\\into_the_woods.txt','w')
f13 = open(path+'movie tweets\\the_imitation_game.txt','w')
f14 = open(path+'movie tweets\\seventh_son.txt','w')
f15 = open(path+'movie tweets\\the_spongebob_movie_sponge_out_of_water.txt','w')
f16 = open(path+'movie tweets\\paddington.txt','w')
f17 = open(path+'movie tweets\\american_sniper.txt','w')
f18 = open(path+'movie tweets\\night_at_the_musuem_secret_of_the_tomb.txt','w')
f19 = open(path+'movie tweets\\cinderella.txt','w')
f20 = open(path+'movie tweets\\furious7.txt','w')
f21 = open(path+'movie tweets\\the_gunman.txt','w')
f22 = open(path+'movie tweets\\do_you_believe.txt','w')
f23 = open(path+'movie tweets\\run_all_night.txt','w')
f24 = open(path+'movie tweets\\kingsman.txt','w')
f25 = open(path+'movie tweets\\insurgent.txt','w')
f26 = open(path+'movie tweets\\chappie.txt','w')
f27 = open(path+'movie tweets\\focus.txt','w')
f28 = open(path+'movie tweets\\get_hard.txt','w')
f29 = open(path+'movie tweets\\home.txt','w')
f30 = open(path+'movie tweets\\woman_in_gold.txt','w')
f31 = open(path+'movie tweets\\it_follows.txt','w')

filenames = next(os.walk(path+'tweets'))[2]
count = 0
tweets = {}
for name in filenames:
    content = open(path+'tweets\\'+name,'r')
    count1 = 0
    for line in content:
        a = str(line)
        if ',"text"' and ',"source"' in a:
        
            count1 = count1 + 1
            firstIndex = a.index(',"text"')
            firstIndex = firstIndex + 9
            secondIndex = a.index(',"source"')
            secondIndex = secondIndex - 1
            text = a[firstIndex:secondIndex]

            if not text in tweets:
                text = text.lower()
                if text.find('The Longest Ride'.lower()) != -1 or text.find('thelongestride') != -1 or text.find('longestride') != -1 or text.find('longest ride') != -1 :
                    tweets = write(tweets,text,f1,'the_longest_ride')
                elif text.find('Ex Machina'.lower()) != -1 or text.find('ExMachina'.lower()) != -1 :
                    tweets = write(tweets,text,f2,'ex_machina')
                elif text.find('Desert Dancer'.lower()) != -1 or text.find('DesertDancer'.lower()) != -1 :
                    tweets = write(tweets,text,f3,'desert_dancer')
                elif text.find('Clouds of Sils Maria'.lower()) != -1 or text.find('CloudsOfSilsMaria'.lower()) != -1 or text.find('Sils Maria'.lower()) != -1 or text.find('SilsMaria'.lower()) != -1:
                    tweets = write(tweets,text,f4,'clouds_of_sils_maria')
                elif text.find('Kill Me Three Times'.lower()) != -1 or text.find('KillMeThreeTimes'.lower()) != -1 :
                    tweets = write(tweets,text,f5,'kill_me_thee_times')
                elif text.find('Lost River'.lower()) != -1 or text.find('LostRiver'.lower()) != -1 :
                    tweets = write(tweets,text,f6,'lost_river')
                elif text.find('While We\'re Young'.lower()) != -1 or text.find('While We are Young'.lower()) != -1 or text.find('WhileWeAreYoung'.lower()) != -1:
                    tweets = write(tweets,text,f7,'while_we_are_young')
                elif text.find('selma'.lower()) != -1 :
                    tweets = write(tweets,text,f8,'selma')
                elif text.find('Danny Collins'.lower()) != -1 or text.find('DannyCollins'.lower()) != -1 :
                    tweets = write(tweets,text,f9,'danny_collins')
                elif text.find('The Second Best Exotic Marigold Hotel'.lower()) != -1 :
                    tweets = write(tweets,text,f10,'the_second_best_exotic_marigold_hotel')
                elif text.find('Fifty Shades of Grey'.lower()) != -1 or text.find('FiftyShades'.lower()) != -1 :
                    tweets = write(tweets,text,f11,'fifty_shades_of_grey')
                elif text.find('Into the Woods'.lower()) != -1 or text.find('IntotheWoods'.lower()) != -1 :
                    tweets = write(tweets,text,f12,'into_the_woods')
                elif text.find('The Imitation Game'.lower()) != -1 or text.find('TheImitationGame'.lower()) != -1 or text.find('Imitation Game'.lower()) != -1 or text.find('ImitationGame'.lower()) != -1:
                    tweets = write(tweets,text,f13,'the_imitation_game')
                elif text.find('Seventh Son'.lower()) != -1 or text.find('SeventhSon'.lower()) != -1 :
                    tweets = write(tweets,text,f14,'seventh_son')
                elif text.find('The SpongeBob Movie: Sponge Out of Water'.lower()) != -1 or text.find('SpongeBobMovie'.lower()) != -1 or text.find('SpongeBob'.lower()) != -1:
                    tweets = write(tweets,text,f15,'the_spongebob_movie_out_of_water')
                elif text.find('Paddington'.lower()) != -1 :
                    tweets = write(tweets,text,f16,'paddington')
                elif text.find('American Sniper'.lower()) != -1 or text.find('AmericanSniper'.lower()) != -1 :
                    tweets = write(tweets,text,f17,'american_sniper')
                elif text.find('Night at the Museum: Secret of the Tomb'.lower()) != -1 or text.find('Night at the Museum'.lower()) != -1 :
                    tweets = write(tweets,text,f18,'night_at_the_museum_secret_of_the_tomb')
                elif text.find('cinderella'.lower()) != -1 :
                    tweets = write(tweets,text,f19,'cinderella')
                elif text.find('furious7'.lower()) != -1 or text.find('furious 7'.lower()) != -1 :
                    tweets = write(tweets,text,f20,'furious7')
                elif text.find('the gunman'.lower()) != -1 or text.find('thegunman'.lower()) != -1 :
                    tweets = write(tweets,text,f21,'the_gunman')
                elif text.find('do you believe'.lower()) != -1 :
                    tweets = write(tweets,text,f22,'do_you_believe')
                elif text.find('run all night'.lower()) != -1 :
                    tweets = write(tweets,text,f23,'run_all_night')
                elif text.find('kingsman'.lower()) != -1 :
                    tweets = write(tweets,text,f24,'kingsman')
                elif text.find('insurgent'.lower()) != -1 or text.find('insurgentmovie'.lower()) != -1 :
                    tweets = write(tweets,text,f25,'insurgent')
                elif text.find('chappie'.lower()) != -1 or text.find('chappiemovie'.lower()) != -1 or text.find('chappiethemovie'.lower()) != -1 :
                    tweets = write(tweets,text,f26,'chappie')
                elif text.find('focus movie'.lower()) != -1 :
                    tweets = write(tweets,text,f27,'focus')
                elif text.find('gethard'.lower()) != -1 or text.find('get hard'.lower()) != -1 :
                    tweets = write(tweets,text,f28,'get_hard')
                elif text.find('home movie'.lower()) != -1 or text.find('homemovie'.lower()) != -1 or text.find('DreamWorksHOME'.lower()) != -1 :
                    tweets = write(tweets,text,f29,'home')
                elif text.find('woman in gold'.lower()) != -1 or text.find('womaningold'.lower()) != -1 :
                    tweets = write(tweets,text,f30,'woman_in_gold')
                elif text.find('itfollows'.lower()) != -1 or text.find('itfollowsfilm'.lower()) != -1 :
                    tweets = write(tweets,text,f31,'it_follows')
##        if count1 == 100:
##            break
    print(count)
    count = count + 1
##    print(tweets)
##    if count == 1:
##        break
print(Counter(tweets.values()))
