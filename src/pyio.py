#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import json
from datetime import datetime

folder = '/home/paulo/vehicular_mobility_trace/'
default_chunk_size = 10000000

if (len(sys.argv) <= 2) :
    try:
        chunk_size = int(sys.argv[1]) if len(sys.argv) == 2 else default_chunk_size
    except ValueError:
        print('invalid parameter. value must be int.')
        sys.exit(1)
else:
    chunk_size = default_chunk_size

print('reading %s items...' %(chunk_size))

chunks = pd.read_table(
        folder+'dataset/koln.tr',
        sep=' ',
        header=None,
        chunksize=chunk_size,
        names=['t', 'idv', 'x', 'y', 's']
        )

df = chunks.get_chunk(chunk_size)

x_list = df['x'].values.tolist()
y_list = df['y'].values.tolist()
speeds = df['s'].values.tolist()
ids    = df['idv'].values.tolist()
times = df['t'].values.tolist()

def getXs ():
    return x_list
def getYs ():
    return y_list
def getSpeeds ():
    return speeds
def getIds():
    return ids
def getTimes ():
    return times

def writeJSON(ids=None, times=None,  xlist=None, ylist=None, speeds=None, filename='output.json'):
    """
    Grava os dados informados em formato json para leitura no módulo JavaScript
    ids lista de ids de veículos

    Argumentos:
    times -- lista com timestamp do dado coletado
    xlist -- lista com abscissas dos posicionamentos dos veículos
    ylist -- lista com ordenadas dos posicionamentos dos veículos
    speeds --  lista com velocidades dos veículos
    filename -- nome do arquivo a ser salvo na pasta tmp do projeto (default 'output.json')
    """

    if ids is not None:
        size = len(ids)    
    elif times is not None:
        size = len(times)
    elif xlist is not None:
        size = len(xlist)
    elif ylist is not None:
        size = len(ylist)
    elif speeds is not None:
        size = len(speeds)
    else:
        print('writeJSON() need more arguments.')
        return False
    
    data=[]
    for i in range(0, size):
        data.append({})
        if ids is not None:
            data[i]['idVehicle'] = ids[i]
        if times is not None:
            data[i]['time'] = times[i]
        if xlist is not None:
            data[i]['x'] = xlist[i]
        if ylist is not None:
            data[i]['y'] = ylist[i]
        if speeds is not None:
            data[i]['speed'] = speeds[i]

    f = open(folder+'tmp/'+filename, 'w+')
    f.write(json.dumps(data, indent=2))
    f.close()

