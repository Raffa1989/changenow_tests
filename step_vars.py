import os


BASE_URL = 'https://api.changenow.io/v2/'
OWN_API_KEY = os.environ.get('OWN_API_KEY')

step_1 = {
    'url': BASE_URL + 'fiat-transaction',
    'headers': {
        'x-api-key': OWN_API_KEY
    },
    'json': {
        'from_amount': 1200.24,
        'from_currency': 'EUR',
        'to_currency': 'BTC',
        'from_network': None,
        'to_network': 'BNB',
        'payout_address': 'mtXWDB6k5yC5v7TcwKZHB89SUp85yCKshy',
        'payout_extra_id': '1',
        'deposit_type': 'SEPA_1',
        'payout_type': 'SEPA_1',
        'external_partner_link_id': ''
    }
}

step_2 = {
    'url': BASE_URL + 'fiat-status/',
    'params': {
        'id': 'id'
    }
}

step_3 = {
    'url': BASE_URL + 'fiat-estimate',
    'headers': {
        'x-api-key': OWN_API_KEY
    },
    'params': {
        'from_currency': 'USD',
        'from_network': '',
        'from_amount': 1488,
        'to_currency': 'BTC',
        'to_network': '',
        'deposit_type': '',
        'payout_type': ''
    }
}

step_4 = {
    'url': BASE_URL + 'fiat-market-info/min-max-range/eur_btc',
}

step_5 = {
    'url': BASE_URL + 'fiat-status'
}

step_6 = {
    'url': BASE_URL + 'fiat-currencies/fiat'
}

step_7 = {
    'url': BASE_URL + 'fiat-currencies/crypto'
}

step_8 = {
    'url': BASE_URL + 'exchange/currencies',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    }
}

step_9_pass = {
    'url': BASE_URL + 'exchange/min-amount',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params':
        {'fromCurrency': 'btc',
         'toCurrency': 'usdt',
         'toNetwork': 'eth'
         }
}

step_9_fail = {
    'url': BASE_URL + 'exchange/min-amount',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'btc',
        'toCurrency': 'usdt'
    }
}

step_10 = {
    'url': BASE_URL + 'exchange/available-pairs',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
}

step_11 = {
    'url': BASE_URL + 'exchange/range',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'btc',
        'toCurrency': 'eth'
    }
}

step_12_with_toNetwork = {
    'url': BASE_URL + 'exchange/estimated-amount',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'btc',
        'toCurrency': 'usdt',
        'fromAmount': 0.1,
        'toAmount': 0.1,
        'toNetwork': 'eth'
    }
}

step_12_withoutNetwork = {
    'url': BASE_URL + 'exchange/estimated-amount',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'btc',
        'toCurrency': 'usdt',
        'fromAmount': 0.1,
        'toAmount': 0.1,
    }
}

step_13 = {
    'url': BASE_URL + 'exchange',
    'headers': {
        'Content-Type': 'application/json',
        'x-changenow-api-key': OWN_API_KEY
    },
    'json': {
        'fromCurrency': 'btc',
        'toCurrency': 'eth',
        'fromNetwork': 'btc',
        'toNetwork': 'eth',
        'fromAmount': '0.003',
        'address': '0x57f31ad4b64095347F87eDB1675566DAfF5EC886',
        'flow': 'standard'
    }
}

step_14 = {
    'url': BASE_URL + 'exchange/by-id',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'id': '5677b0657a1795'
    }
}

step_15 = {
    'url': BASE_URL + 'validate/address',
    'params': {
        'currency': 'eth',
        'address': '0x57f31ad4b64095347F87eDB1675566DAfF5EC886'
    }
}

step_16 = {
    'url': BASE_URL + 'addresses-by-name',
    'params': {
        'name': 'luke@stokes'
    }
}

step_17 = {
    'url': BASE_URL + 'exchange/network-fee',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'usdt',
        'toCurrency': 'usdt',
        'fromAmount': 100

    }
}

step_18 = {
    'url': BASE_URL + 'markets/estimate',
    'headers': {
        'x-changenow-api-key': OWN_API_KEY
    },
    'params': {
        'fromCurrency': 'usdt',
        'toCurrency': 'btc',
    }
}

step_19 = {
    'url': BASE_URL + 'exchanges',
    'headers': {
        'x-changenow-api-key': 'newprivateapikey'  # приватный ключ отсутствует (запросила - не прислали)
    },
}
