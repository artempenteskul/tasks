# task number - 1108


def defang_ip_address(ip_address: str) -> str:
    return ip_address.replace('.', '[.]')


if __name__ == '__main__':
    input_ip_address = '1.1.1.1'
    print(f'Output ip-address after defang - {input_ip_address}')

    input_ip_address = '255.100.50.0'
    print(f'Output ip-address after defang - {input_ip_address}')
