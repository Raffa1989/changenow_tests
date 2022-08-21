import requests

from step_vars import (
    step_1, step_2, step_3, step_4, step_5,
    step_6, step_7, step_8, step_9_pass,
    step_9_fail, step_10, step_11,
    step_12_with_toNetwork, step_12_withoutNetwork,
    step_13, step_14, step_15,
    step_16, step_17, step_18, step_19
)


class TestChangeNowAPIv2:

    def test_1_create_exchange_transaction_with_fiat(self):  # 401 ошибка
        # your_api_key
        # в документации не указано какой должен быть API (приватный или нет)
        # в документации не совсем понятно какие параметры опциональные, а какие обязательные
        """
        Метод оценки суммы обмена
        :return:
        """
        response = requests.post(**step_1)
        assert response.status_code == 200
        assert len(response.json()) != 0

    def test_2_transaction_status(self):
        # your_api_key
        # в документации не указано какой должен быть API (приватный или нет)
        """
        Метод получения информации об отправленной транзакции по ее идентификатору
        :return:
        """
        response = requests.get(**step_2)
        assert response.status_code == 200

    def test_3_estimate(self):  # 401 ошибка
        # your_api_key
        # в документации не указано какой должен быть API (приватный или нет)
        # в документации не совсем понятно какие параметры опциональные, а какие обязательные
        """
        Метод оценки суммы обмена
        :return:
        """
        response = requests.get(**step_3)
        assert response.status_code == 200

    def test_4_marketinfo(self):
        """
        Метод получения минимального и максимального диапозона
        :return:
        """
        response = requests.get(**step_4)
        assert response.status_code == 200
        assert len(response.json()) != 0

    def test_5_fiat_healthcheck_service(self):
        """
        Проверяет состояние службы обмена
        :return:
        """
        response = requests.get(**step_5)
        assert response.status_code == 200

    def test_6_fiat_currencies(self):
        """
        Метод получения информации о валютах, которые можно использовать для покупки криптовалют
        :return:
        """
        response = requests.get(**step_6)
        assert response.status_code == 200

    def test_7_crypto_currencies(self):
        """
        Метод получения информации о криптовалютах, которые клиент может купить
        :return:
        """
        response = requests.get(**step_7)
        assert response.status_code == 200

    def test_8_list_of_available_currencies(self):
        # Partner's api key
        """
        Тестирование списка доступных валют. Ответ содержит массив
        объектов с информацией о валюте
        :return:
        """
        response = requests.get(**step_8)
        assert response.status_code == 200
        assert len(response.json()) != 0
        # проверка, что тип значений совпадает с документацией (проверка первого словаря в JSON)
        assert isinstance(response.json()[0].get('ticker'), str)
        assert isinstance(response.json()[0].get('name'), str)
        assert isinstance(response.json()[0].get('image'), str)
        assert isinstance(response.json()[0].get('hasExternalId'), bool)
        assert isinstance(response.json()[0].get('isFiat'), bool)
        assert isinstance(response.json()[0].get('featured'), bool)
        assert isinstance(response.json()[0].get('isStable'), bool)
        assert isinstance(response.json()[0].get('supportsFixedRate'), bool)
        assert isinstance(response.json()[0].get('network'), str)
        assert isinstance(response.json()[0].get('tokenContract'), (str, type(None)))
        assert isinstance(response.json()[0].get('buy'), bool)
        assert isinstance(response.json()[0].get('sell'), bool)
        assert isinstance(response.json()[0].get('legacyTicker'), str)

    def test_9_1_minimal_exchange_amount(self):
        # Partner's api key
        # with toNetwork
        # параметр toNetwork в документации опциональный, по факту без него тест падает
        """
        Тестирование минимальной суммы объекта. Если Вы попытаетесь обменять меньше,
        транзакция, скорее всего, не удастся
        :return:
        """
        response = requests.get(**step_9_pass)
        assert response.status_code == 200
        # проверка, что обязательный параметр есть в response
        assert step_9_pass['params']['fromCurrency'] == response.json()['fromCurrency']

    def test_9_2_minimal_exchange_amount(self):
        # Partner's api key
        # without toNetwork
        """
        Тестирование минимальной суммы объекта. Если Вы попытаетесь обменять меньше,
        транзакция, скорее всего, не удастся
        :return:
        """
        response = requests.get(**step_9_fail)
        assert response.status_code != 200
        # проверка, что обязательный параметр есть в response

    def test_10_list_of_all_available_pairs(self):
        # your_api_key
        # в документации не указано какой должен быть API (приватный или нет)
        # в документации нет данных какие параметры являются обязательными
        """
        Ответ содержит массив пар тикеров, разделенных подчеркиванием
        :return:
        """
        response = requests.get(**step_10)
        assert response.status_code == 200
        assert len(response.json()) != 0

    def test_11_exchange_range(self):
        # Partner's api key
        """
        Диапазон обмена. Если Вы пытаетесь обменять меньше минимума или больше максимума,
        транзакция, скорее всего, не состоится
        :return:
        """
        response = requests.get(**step_11)
        assert response.status_code == 200
        assert len(response.json()) != 0

        # проверка, что обязательные параметры есть в response
        assert step_11['params']['fromCurrency'] == response.json()['fromCurrency']
        assert step_11['params']['toCurrency'] == response.json()['toCurrency']

        # проверка, что тип значений совпадает с документацией
        assert isinstance(response.json().get('fromCurrency'), str)
        assert isinstance(response.json().get('fromNetwork'), str)
        assert isinstance(response.json().get('toCurrency'), str)
        assert isinstance(response.json().get('toNetwork'), str)
        assert isinstance(response.json().get('flow'), str)
        assert isinstance(response.json().get('minAmount'), (int, float))
        assert isinstance(response.json().get('maxAmount'), (int, float, type(None)))

    def test_12_1_estimated_exchange_amount(self):
        # Partner's api key
        # with toNetwork
        # параметр toNetwork в документации опциональный, по факту без него тест падает
        """
        Возвращается предполагаемая сумма обмена
        """
        response = requests.get(**step_12_with_toNetwork)
        assert response.status_code == 200

    def test_12_2_estimated_exchange_amount_2(self):
        # Partner's api key
        # without toNetwork
        """
        Возвращается предполагаемая сумма обмена
        """
        response = requests.get(**step_12_withoutNetwork)
        assert response.status_code != 200

    def test_13_create_exchange_transaction(self):
        # your_api_key
        """
        Ответ содержит объект с информацией о транзакции
        :return:
        """
        response = requests.post(**step_13)
        assert response.status_code == 200

    def test_14_transaction_status(self):  # 403 ошибка
        # Partner's api key
        """
        Ответ содержит объект с информацией о транзакции. Поля в ответе различаются
        в зависимости от статуса и типа транзакции
        :return:
        """
        response = requests.get(**step_14)
        assert response.status_code == 200
        assert len(response.json()) != 0

    def test_15_address_validation(self):
        """
        Показывает действителен ли адрес
        :return:
        """
        response = requests.get(**step_15)
        assert response.status_code == 200
        assert len(response.json()) != 0

    def test_16_user_addresses(self):
        """
        Возвращает список адресов, привязанных к имени адреса
        :return: 
        """
        response = requests.get(**step_16)
        assert response.status_code == 200
        assert len(response.json()) != 0

        # проверка, что тип значений совпадает с документацией
        assert isinstance(response.json().get('success'), bool)
        assert isinstance(response.json().get('addresses'), list)
        assert isinstance(response.json().get('addresses')[0].get('currency'), str)
        assert isinstance(response.json().get('addresses')[0].get('chain'), str)
        assert isinstance(response.json().get('addresses')[0].get('address'), str)
        assert isinstance(response.json().get('addresses')[0].get('protocol'), str)

    def test_17_estimated_exchange_network_fee(self):  # 403 ошибка
        # your_api_key
        """
        Конечная точка, которая показывает комиссию за обмен
        :return:
        """
        response = requests.get(**step_17)
        assert response.status_code == 200
        # Необходимо связаться с менеджером по работе с клиентами

    def test_18_market_estimate(self):  # 403 ошибка
        # Partner's api key
        """
        Оценочные суммы прямого и обратного рынка
        :return:
        """
        response = requests.get(**step_18)
        assert response.status_code == 200

    def test_19_exchanges(self):  # 401 ошибка
        # Partner's api key
        # тест не пройден - отсутствует приватный ключ (не прислали)
        """
        Возвращает список партнерских транзакций в соответствии с выбранными параметрами
        :return:
        """
        response = requests.get(**step_19)
        assert response.status_code == 200
        assert len(response.json()) != 0
