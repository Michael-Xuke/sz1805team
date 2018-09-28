from alipay import AliPay
from django.shortcuts import redirect

from Alipay import settings

# Create your views here.


def alipay(request):
    alipay = AliPay(
        appid="2016092100560320",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=settings.app_private_key_string,
        alipay_public_key_string=settings.alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False  # 默认False
    )

    subject = 'pay for knowledge'
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="xxx20180928354435",
        total_amount=1000,
        subject=subject,
        return_url="http://1000phone.com",
        notify_url="https://example.com/notify"  # 可选, 不填则使用默认notify url
    )

    url = "https://openapi.alipaydev.com/gateway.do?" + order_string
    return redirect(url)

