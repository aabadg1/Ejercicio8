import json

def store(var, filename):
    json.dump(json.dumps(var), open(filename,'w')) #json escribe en disco sin tener que ir linea a linea

def retrieve(filename):
    var = json.loads(json.load(open(filename,'r')))
    return var