import sys
from os import path

dirname = path.dirname(__file__)

def dadosDeAlunos(filename):
  try:
    filepath = path.join(dirname, 'entrada', filename)
    with open(filepath) as file:
        data = file.readlines()
        return data
  except:
    print('erro ao ler arquivo')

def gerarArquivoDisciplinas(filename, data): 
  try:
    with open(path.join(dirname, 'saida', filename), 'w') as file:
      for line in data:
        file.write(f'{line[0]};{line[1]}')
        file.write('\n')
  except :
    print('erro ao criar arquivo')

def gerarMedia(filename, data): 
  try:
    with open(path.join(dirname, 'saida', filename), 'w') as file:
      for line in data:
        av = float(f'{line[3][0:2]}.{line[3][2:3]}')
        av2 = float(f'{line[3][3:5]}.{line[3][5:6]}')
        av3 = float(f'{line[3][6:8]}.{line[3][8:9]}')
        file.write(f'{line[0]};{line[1]};{av};{av2};{av3};{media(av, av2, av3)}')
        file.write('\n')
  except :
    e = sys.exc_info()[0]
    print('erro ao criar o arquivo', e)

def extractDisciplines():
  try:
    disciplines = []
    data = dadosDeAlunos('alunos.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] not in disciplines:
        disciplines.append(item[2])
    return disciplines
  except: 
    return []
  
def lerDadosDeAlunos(discipline):
  try:
    students = []
    data = dadosDeAlunos('alunos.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] == discipline:
        students.append(item)
    return students
  except: 
    return []  

def media(av1, av2, av3):
  if av1 >= av2 and av2 >= av3:
    return (av1 + av2 ) / 2
  elif av1 >= av2 and av2 <= av3:
    return (av1 + av3 ) / 2
  else:
    return (av2 + av3 ) / 2

for d in extractDisciplines():
  s = lerDadosDeAlunos(d)
  # print(d, s)
  gerarArquivoDisciplinas(f'{d}.csv', s)
  gerarMedia(f'{d}_notas.csv', s)