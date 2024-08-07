from paystackapi.paystack import Paystack

from config.settings.base import env

paystack_secret_key = env("PAYSTACK_SECRET_KEY")
paystack = Paystack(secret_key=paystack_secret_key)


class PaystackUtils:
    paystack = paystack

    @staticmethod
    def initialize_transaction(amount, email, callback_url, reference):
        response = paystack.transaction.initialize(
            amount=amount, email=email, callback_url=callback_url, reference=reference
        )
        return response

    @staticmethod
    def verify_transaction(ref):
        response = paystack.transaction.verify(ref)
        return response
