
from psutil import net_if_addrs, net_if_stats

def get_devlist():
    addresses = net_if_addrs()
    stats = net_if_stats()
    available_networks = []
    for intface, addr_list in addresses.items():
        if intface in stats and getattr(stats[intface], "isup"):
            addrlist = []
            for addr in addr_list:
                addrlist.append(getattr(addr, 'address'))
            available_networks.append((intface, addrlist))

    return available_networks

if __name__ == "__main__":
    print(get_devlist())