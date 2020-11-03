import func_weather as f

try:
    coordinater = f.getCoordinater()
    f.setWeather(coordinater['lat'], coordinater['long'])

    x = True
    while x is True:
        print('')
        question2 = input('Deseja consultar a previsão de outro local (s/n)? ').lower()
        if question2 != 's':
            break
        newLocal = input('Digite a CIDADE e o ESTADO: ')
        try:
            newCoordinater = f.searchNewLocation(newLocal)
            f.setWeather(newCoordinater['lat'], newCoordinater['long'])
        except:
            print('Não foi possível obter a previsão para este local.')
except:
    print('Serviço indisponível no momento.')