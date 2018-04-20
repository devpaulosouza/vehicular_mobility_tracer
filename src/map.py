#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyio as io
import json

print('map.py: populating...')

data = {
    't': io.getTimes(),
    'id': io.getIds(),
    'x':  io.getXs(), 
    'y':  io.getYs(), 
    's':  io.getSpeeds()
}

print('map.py: %d read objects' %(len(data['id'])))

cars = {}

moment = data['t'][0];

print(type(moment))

res = [[]]
count_time = 0
current_time = -1
d_momento = 30 # mínimo de segundos para ler um novo registro

for i in range(0, len(data['id'])):
    cid = str(data['id'][i])
    t = data['t'][i]
    x = data['x'][i]
    y = data['y'][i]
    s = data['s'][i]

    # se o carro estiver em um tempo maior que o momento que está sendo salvo
    # + o tempo mínimo de medição. Aumenta o momento para momento + tempo minimo
    if data['t'][i] > moment+d_momento:
        moment = data['t'][i]
    # verifica se o carro na linha lida está no tempo a ser salvo na saída.
    # desta forma, é filtrado a saída apenas em carros que foram gravados
    # dados naquele momento.
    if (data['t'][i] == moment):
        if not cid in cars:
            cars[cid] = data['id'][i];
            cars[cid] = []
        # verifica se o tempo atual que está sendo agrupado é diferente do tempo 
        # a ser inserido. Se for diferente, cria um novo grupo
        if current_time != t:
            count_time += 1
            current_time = t
            res.append([])

        # armazena agrupando por carros
        cars[cid].append({'t': t,'x': x, 'y': y, 's': s})
        # armazena agrupando por tempos
        res[count_time].append({'t': t,'x': x, 'y': y, 's': s})

print('cars in road = %s' %len(cars))

f = open('../outputs/momentum.json', 'w+')
f.write(json.dumps(res, indent=2))
f.close()

#io.writeJSON(ids=data['id'], xlist=data['x'], ylist=data['y'], speeds=data['s'])

