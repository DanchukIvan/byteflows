from yarl import URL

__all__: list[str] = ["PROXY_LIST", "build_proxyurl"]


class ProxyList(list):
    ...


PROXY_LIST = ProxyList()


def build_proxyurl(
    *,
    address: str = "",
    port: int | None = None,
    username: str = "",
    password: str = "",
    display_url: bool = False,
) -> str:
    url_string: URL = (
        URL(address)
        .with_port(port)
        .with_password(password)
        .with_user(username)
    )
    PROXY_LIST.append(url_string.human_repr())
    if display_url:
        print(f"Prepared proxy url {url_string.human_repr()}")
    return url_string.human_repr()