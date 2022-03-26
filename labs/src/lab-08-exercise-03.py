players = []
scores = []

for i in range(5):
  name = input("Dose onoma paikti: ")
  players.append(name)

for i in range(5):
  name = int(input("Dose score paixnidiou: "))
  scores.append(name)

for i in range(1,5):
  for j in range(4, i-1, -1):
    if scores[j-1] > scores[j]:
      temp = scores[j-1]
      scores[j-1] = scores[j]
      scores[j] = temp
      temp2 = players[j-1]
      players[j-1] = players[j]
      players[j] = temp2

print(players)
print(scores)

sum = 0

for i in scores:
  sum = sum + i

mo = sum / 5

for i in range(5):
  print("H diafora tou score tou paikti ", players[i], " apo ton meso oro einai: ", mo - scores[i])
