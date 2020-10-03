# Foi feita uma estatística em cinco estados brasileiros para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código do estado;
# Número de veículos de passeio (em 2018);
# Número de acidentes de trânsito com vítimas (em 2018). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que estado pertence;
# Qual a média de veículos nos cinco estados juntas;
# Qual a média de acidentes de trânsito nos estados com menos de 5.000.000 veículos de passeio.


#### Função para calcular o maior e menor índice de acidentes
def index_accidents(list):
    accidents = []
    for i in list:
        index = i[2] / i[1]
        accidents.append(index)
    highestindex = max(accidents) * 100
    lowestindex = min(accidents) * 100
    hi_index = accidents.index(max(accidents))
    li_index = accidents.index(min(accidents))
    return print(f'O maior índice de acidentes é {highestindex:.2f}% do estado {list[hi_index][0]}. E o menor é {lowestindex:.2f}% do estado {list[li_index][0]}.')

#### Função para calcular a média de veículos
def average_vehicle(list):
    vehicle = []
    for i in list:
        accident = i[1]
        vehicle.append(accident)
    average = sum(vehicle) / len(vehicle)
    return print(f'A média de veículos entre os estados é de {average:.1f}.')

#### Função para calcular a média de acidentes
def average_accidents(list):
    accidents = []
    for i in list:
        if i[1] < 5000000:
            accidents.append(i[2])
    average = sum(accidents) / len(accidents)
    print (f'A média de acidentes em estados com menos de 5 milhões de veículos é de {average:.1f}.')


########## P R O G R A M A ##########
statitisc = [['3 - MG', 6169791, 12234], ['1 - SP', 18230138, 29984], ['2 - RJ', 4511484, 19152], ['4 - SC', 4428638, 11857], ['5 - RS', 4309287, 12812]]

index_accidents(statitisc)
average_vehicle(statitisc)
average_accidents(statitisc)