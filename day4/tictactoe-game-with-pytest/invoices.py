from collections import defaultdict

import pytest

with open('...') as f:
    pass

with create_dag() as dag:
    pass

with pytest.raises:
    pass

with lock_mutex as lock:
    pass





class Invoice:
    vats = {
            "Israel": 1.18,
            "Italy": 1.22,
            "Japan": 1.08,
            "Jordan": 1.16,
            "Thailand": 0.07,
            }

    @classmethod
    def vat_by_country(cls, country):
        return cls.vats[country]


class NoVatInvoice(Invoice):
    vats = defaultdict(lambda: 0)


print(Invoice.vat_by_country("Israel"))
print(Invoice.vat_by_country("Thailand"))
