import ipaddress

class Ipaddress():
    def __init__(self, ip='127.0.0.1/32'):
        self.ip = ip

    @property
    def ip(self):
        return '%s/%s' % (self._ip, self._mask)

    @ip.setter
    def ip(self, ip):
        ip_mask = ip.split('/')
        self._ip = ip_mask[0]
        self.masks = [self._bin_to_address(self._mask_to_bin(x)) for x in range(33)]
        self._mask = 32
        if len(ip_mask) == 2:
            try:
                self._mask = int(ip_mask[1])
            except ValueError:
                if self._mask in self.masks:
                    self._mask = self.masks.index(self._mask)
                else:
                    raise

    def _ip_to_bin(self, ip):
        chunks = ip.split('.')
        s = ''
        for chunk in chunks:
            s += format(int(chunk), '08b')
        return s

    def _mask_to_bin(self, mask):
        return '1' * mask + '0' * (32 - mask)

    def _bin_to_address(self, binary_address):
        chunks = []
        for i in range(4):
            chunk = binary_address[i * 8:i * 8 + 8]
            chunks.append(str(int(chunk, 2)))
        return '.'.join(chunks)

    @property
    def network(self):
        addr = int(self._ip_to_bin(self._ip), 2)
        msk = int(self._mask_to_bin(self._mask), 2)
        return self._bin_to_address(format(addr & msk, '32b'))

    @property
    def hosts(self):
        hsts = {}
        net = int(self._ip_to_bin(self.network), 2)
        hstc = 0
        if self._mask < 32:
            hstc = int('1' * (32 - self._mask), 2) - 1
        hsts['network'] = self._bin_to_address(format(net, '32b'))
        if self._mask == 32:
            hsts['broadcast'] = '-'
        else:
            hsts['broadcast'] = self._bin_to_address(format(net + hstc + 1, '32b'))
        hsts['hostcount'] = hstc
        if self._mask > 30:
            hsts['hostmin'] = '-'
            hsts['hostmax'] = '-'
        else:
            hsts['hostmin'] = self._bin_to_address(format(net + 1, '32b'))
            hsts['hostmax'] = self._bin_to_address(format(net + hstc, '32b'))
        return hsts

def main():
    ip = Ipaddress()
    ip.ip = '192.168.0.5/24'

    print(ip.ip, ip.hosts)


if __name__ == '__main__':
    main()