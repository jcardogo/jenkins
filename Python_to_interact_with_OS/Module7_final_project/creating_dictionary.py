import operator

Events = {"ERROR": 3, "INFO": 5, "BANANAS": 7, "PEARS": 2}
#print(sorted(Events.items())) #SORTING ON ALPHABETICAL ORDER
print(sorted(Events.items(), key=operator.itemgetter(1), reverse=True))



