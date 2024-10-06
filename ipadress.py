class IAddressIPv4:
    def __init__(self, address: str):
        self.address = address

    def isValid(self) -> bool:
        """Ověřuje, zda je IP adresa platná."""
        parts = self.address.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False

        return True

    def set(self, address: str):
        """Nastaví novou IP adresu."""
        self.address = address
        return self

    def getAsString(self) -> str:
        """Vrací IP adresu jako řetězec."""
        return self.address

    def getAsInt(self) -> int:
        """Převádí IP adresu na 32bitové celé číslo."""
        parts = [int(part) for part in self.address.split('.')]
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

    def getAsBinaryString(self) -> str:
        """Vrací binární reprezentaci IP adresy jako řetězec."""
        parts = [int(part) for part in self.address.split('.')]
        binary_string = ''.join(f'{part:08b}' for part in parts)
        return binary_string

    def getOctet(self, number: int) -> int:
        """Vrací hodnotu konkrétního oktetu (1 až 4)."""
        parts = self.address.split('.')
        if not (1 <= number <= 4):
            raise ValueError('Číslo oktetu musí být mezi 1 a 4.')

        return int(parts[number - 1])

    def getClass(self) -> str:
        """Vrací třídu IP adresy (A, B, C, D, E)."""
        first_octet = self.getOctet(1)

        if 0 <= first_octet <= 127:
            return 'A'
        elif 128 <= first_octet <= 191:
            return 'B'
        elif 192 <= first_octet <= 223:
            return 'C'
        elif 224 <= first_octet <= 239:
            return 'D'
        else:
            return 'E'

    def isPrivate(self) -> bool:
        """Kontroluje, zda je IP adresa soukromá."""
        first_octet = self.getOctet(1)
        second_octet = self.getOctet(2)

        if first_octet == 10:
            return True
        elif first_octet == 172 and 16 <= second_octet <= 31:
            return True
        elif first_octet == 192 and second_octet == 168:
            return True

        return False


ip = IAddressIPv4('192.168.1.1')
print('Platná IP:', ip.isValid())          
print('IP jako string:', ip.getAsString())  
print('IP jako int:', ip.getAsInt())     
print('IP jako binární string:', ip.getAsBinaryString()) 
print('První oktet:', ip.getOctet(1))      
print('Třída IP:', ip.getClass())          
print('Je soukromá?', ip.isPrivate())     
