import config

CONFIG = config.configuration()
locations = CONFIG.LOCATIONS

def process(raw): 
    locations = [] 
    file = open(raw)
    for line in file:
        line = line.strip()
        print(line)
        if len(line) == 0 or line[0] == '#':
            continue
        parts = line.split(',')
        locations.append({"name": str(parts[0]), "lat": float(parts[1]) ,"lng": float(parts[2]), "web":str(parts[3])})

    file.close()
    return locations

def main():
    f = locations
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

