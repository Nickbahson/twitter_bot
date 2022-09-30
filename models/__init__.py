import re

"""

"""


def channel_name(tweet):
    print('++++++++++++++ A new tweet +++++++++++++++++++')
    print(tweet)
    print('++++++++++++++ Any new tweet +++++++++++++++++++')
    general_channel_pattern = re.compile(r'(don\'t know|can\'t tell|why is)')
    matches = general_channel_pattern.finditer(tweet)
    for match in matches:
        if match[0]:
            print(match[0])
            return "#general"

    sales_channel_pattern = re.compile(r'(buy|bougth|sold|sales)')
    matches = sales_channel_pattern.finditer(tweet)
    for match in matches:
        if match[0]:
            print(match[0])
            return "#sales"

    # unknowns_channel_pattern = re.compile(r'\.')
    # matches = unknowns_channel_pattern.finditer(tweet)
    # if matches[0]:
    #     print(matches[0])
    #     return "unknown"

    return "#random"
