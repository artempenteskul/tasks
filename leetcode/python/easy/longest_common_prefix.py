# task number - 14

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    current_prefix = strs[0]

    for s in strs:
        while not s.startswith(current_prefix) and current_prefix:
            current_prefix = current_prefix[:-1]

    return current_prefix


if __name__ == '__main__':
    print(longest_common_prefix(["flower", "flow", "flight"]))  # fl
    print(longest_common_prefix(["dog", "racecar", "car"]))  # ''
    print(longest_common_prefix([""]))  # ''
