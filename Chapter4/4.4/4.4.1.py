#切片 slice
players=['charles','martina','nichael','florence','eli']
print(players[0:3])

players=['charles','martina','nichael','florence','eli']
print(players[1:4])

#不选定开始，则从头提取
players=['charles','martina','nichael','florence','eli']
print(players[:4])
#不选定结束，则结束在最后一个元素
print(players[0:])
#倒着选取
print(players[-3:])
#隔空选取
print(players[::2])