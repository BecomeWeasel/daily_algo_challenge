from sys import stdin
from collections import defaultdict

n = int(stdin.readline())


def sol():
    global n
    # 중복되는 주소가 많으니 dict 사용
    bin_ip_addr_dict = defaultdict(str)

    for _ in range(n):
        addr = stdin.readline().rstrip()
        single_bin_ip_addr = ""
        for word in addr.split("."):
            # IP 주소 Byte 단위 int를 binary로 변환하고
            # 8글자 패딩
            single_bin_ip_addr += bin(int(word))[2:].zfill(8)
        bin_ip_addr_dict[addr] = single_bin_ip_addr

    bin_ip_addrs = list(bin_ip_addr_dict.values())

    def c(s):
        # convert_binary_string_to_binary
        return int(s, 2)

    m = 0

    for i in range(len(bin_ip_addrs)):
        for j in range(len(bin_ip_addrs)):
            # IP 주소간의 xor 연산
            r = bin(c(bin_ip_addrs[i]) ^ c(bin_ip_addrs[j]))
            # xor 연산시 ip 주소간의 차이가 없으면 0b0
            if int(r, 2) == 0:
                m = max(m, 0)
            # xor 연산시 차이가 있으면 0b1... r의 길이에서 2를 빼준값이 차이
            else:
                m = max(m, len(r) - 2)

    # 네트워크 주소 규칙에 맞게 주소와 마스크의 single_bin_ip_addr 생성
    network_addr_bin = bin_ip_addrs[0][: len(bin_ip_addrs[0]) - m] + m * "0"
    network_mask_bin = (32 - m) * "1" + m * "0"

    network_addr, network_mask = [], []

    # binary를 Byte 단위로 int로 변환
    for i in range(0, 32, 8):
        network_addr.append(int(network_addr_bin[i : i + 8], 2))
        network_mask.append(int(network_mask_bin[i : i + 8], 2))

    print(".".join(map(str, network_addr)))
    print(".".join(map(str, network_mask)))


sol()
