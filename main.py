from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from random import randint, getrandbits
from os import getenv

from dotenv import load_dotenv
load_dotenv()


def randbool():
    return bool(getrandbits(1))


def change_ja3(o: Options):
    put = o.set_preference
    put('security.tls.enable_delegated_credentials', randbool())
    put('security.tls.enable_post_handshake_auth', randbool())
    put('security.tls13.aes_128_gcm_sha256', randbool())
    put('security.tls13.aes_256_gcm_sha384', randbool())
    put('security.tls13.chacha20_poly1305_sha256', randbool())
    put('security.tls13.aes_128_gcm_sha256', randbool())
    put('security.tls13.aes_256_gcm_sha384', randbool())
    put('security.ssl3.dhe_rsa_aes_128_sha', randbool())
    put('security.ssl3.dhe_rsa_aes_256_sha', randbool())
    put('security.ssl3.ecdhe_ecdsa_aes_128_gcm_sha256', randbool())
    put('security.ssl3.ecdhe_ecdsa_aes_128_sha', randbool())
    put('security.ssl3.ecdhe_ecdsa_aes_256_gcm_sha384', randbool())
    put('security.ssl3.ecdhe_rsa_chacha20_poly1305_sha256', randbool())
    put('security.ssl3.ecdhe_ecdsa_chacha20_poly1305_sha256', randbool())
    put('security.ssl3.ecdhe_ecdsa_aes_256_sha', randbool())
    put('security.ssl3.ecdhe_rsa_aes_128_gcm_sha256', randbool())
    put('security.ssl3.ecdhe_rsa_aes_128_sha', randbool())
    put('security.ssl3.ecdhe_rsa_aes_256_gcm_sha384', randbool())
    put('security.ssl3.ecdhe_rsa_aes_256_sha', randbool())
    put('security.ssl3.rsa_aes_128_gcm_sha256', randbool())
    put('security.ssl3.rsa_aes_128_sha', randbool())
    put('security.ssl3.rsa_aes_256_gcm_sha384', randbool())
    put('security.ssl3.rsa_aes_256_sha', randbool())
    put('security.ssl.disable_session_identifiers', randbool())
    put('security.ssl.enable_ocsp_stapling', randbool())
    put('security.ssl.enable_alpn', randbool())


def main():
    try:
        options = Options()
        change_ja3(options)

        options.binary_location = getenv('FIREFOX_BINARY_LOCATION')

        driver = Firefox(options=options)
        driver.get(getenv('JA3_CHECK_URL'))

        print(driver.page_source)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
