with open('proxy_list.txt', 'r') as file:
    proxies = file.readlines()

socks5_proxies = ['socks5://' + proxy.strip() for proxy in proxies]

with open('proxy_list.txt', 'w') as file:
    file.write('\n'.join(socks5_proxies))
