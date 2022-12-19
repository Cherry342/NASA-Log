file= open("NASA_access_log_Jul95")

from _collections_abc import defaultdict
items=file(list)
ip_adresses = []
try:
    for line in file:
        print(file)

    ip_adresses.append(line.split(" ")[0])
    print(line.split(" ")[0])
    #from _collections_abc
    #print(file(list))


except:
    print("uh-oh")
    pass


