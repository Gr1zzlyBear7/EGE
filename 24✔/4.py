string = open('4.txt').readline()
print(string.count('BOSS') - string.count('BOSSJ') + string.count('JBOSSJ') - string.count('JBOSS'))