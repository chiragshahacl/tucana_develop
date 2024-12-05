import base64
from datetime import UTC, datetime, timedelta

import jwt
from behave import given, step
from starlette import status

from app.auth.crypto import JWTClaims
from app.auth.enums import RoleNames

LOCAL_PRIVATE_KEY = (
    "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpN"
    "SUlKS0FJQkFBS0NBZ0VBcHlEaC9BSllFdXFuMlRGVXhqa"
    "zc5eno2V1VGcmJ3Rk5DaFdyWWUvY3ROK3ZpdnJVCnVPak"
    "t6YXFHZ3VwT0tKclZlSE8wMTJkM1ZrRGozM1p1QzROd2x"
    "xZjYvOUY4QnFCd3BoWHVsNkhOelB6YmdBL28KbUdBN1I4"
    "aXZpZ2l3VC8rY2lseEJ4V004WFdFRmZNTmdCdGhVbGtDe"
    "FB5MnRkRjNJNTdTbVBtUzdhNjNsZ3RWTgpxSXZvMVdVVl"
    "IzeVpPelA4OGU1Y0FsTXZYaGkvTmMrZFlTckZZdVpON1F"
    "wbTJCMmVIQzVmQlI4TXFRQ0lWL2JvCjdoVmx3d2R6dll5"
    "WkdkN3p4dzNwVERGYXliSjcxVmh2Nk5oVmpYdkIrckVDT"
    "W9KMWFxRExjdkFwcE1yT29wUkMKRjZxR0pUZDRobWhlUE"
    "NQc3kvb3V0TnFhOVNHK3VxSlVFR29tSjNyaGJadzdJdlo"
    "3T0VSQXN2eE9rbCs4MVNjcQo3elIrb0pEN0RzTFcvOFBv"
    "RXlsMnc4b1dyWkNWZTRjNFNUL2dKOGxlVDlBbkNBcnN1Q"
    "VpDR2JJZ3B2MnRDKzVyCnAwZTRkR3JGdlRoNVpaVmx6b2"
    "pvOW1JdmNTZHlZRGFiY0dMZTEzNmgwU1VjNDNYbDJrTXl"
    "aRDUrN2ZoelNMMkMKVjhQM282eE0rb1c1NlJ3QjE5S1BP"
    "cVZ3Uit0eVBTVE1MMXpaTGw5bmkvbW1ndk1uTTQrTlpkM"
    "FliaXZ3Zy9GaAp6RkRrT2dwVEtmNWNvU2Z1SUpPYmtieT"
    "NNZ2MzM3NWQm1JZ2dXNnFjR2tzNFlEVC9SSEY1ZUZFNm5"
    "2YVZTMy9pCnpOTmY0eFQvZTQ5dHRweG9MSTZNc0Fub2Zp"
    "Q0YwS0d4b1FiNUU0YnlndXRieS94NUh3NmJNNm9PeDZzQ"
    "0F3RUEKQVFLQ0FnQWtkSnhHdzk0aFZqVkJ2Nng5eHF0Sm"
    "JYQXdld0FyeVExY2QwaVlodUZPUlFLK0hxTzdKL0JnOTJ"
    "MNgorSkFPOUdNL01JSVFnSDI3LzFDVmhIaFJvNXl5Q0Rk"
    "TWlRMzBSaGY4YW9sT1l4bUlydGxVY0dQc3BRVVpUZkhZC"
    "mVyZTI0NHRxZE9CVjVhVWJ1MWVlbE9HRDdMbGF3d2JHd0"
    "xoMnl5UlJRb3NHemlOQnhEOXRrQWl1RE1LL2xacVUKS3Q"
    "0ajExM0VDaG5nMmZOWm82MUYyQ0U4dWo4dktReHplZExn"
    "TG1tNFBQYzJIMFU4TWlVTGh3emRMaWF4NlpTNgpFb3FzN"
    "VlDb2VXVGIzV0l2My9KNklaM2JuU0RnU1ZBUlZuNGp0V2"
    "hXVjNlNWZTQ2dWU3JJdE8xTHkwTVNxQ3h1CnFTSnhIT2N"
    "Bd1hSaHQ5T1lTQUdhSldHUDZRK2tMMmRSOEJTdTVoU1U4"
    "ZVR3VDhCTitaRlNXWmlLWXdPNlkrTkYKbXZLemN2cUFJU"
    "EtYRFhUYTlWZjVPcG41Q0t4SHpmU3ozalViemtNZ1lBNz"
    "FRMWFxYzZQT2xaYnI0dWxJd2pPdApRWDdvV0o2K2Y5QUd"
    "QUFdwQ3pnNFpMWXFUeE12dVBTYi9ia2Ixcks5U1NIUVB1"
    "OElEb1I1M1E4OUN0VVZWWnhRCnlyY2xCUkR4ZFNjeEo4b"
    "Ww2ajBzRVY4V2FjK1FhTG1xM0E2cDJZeHhmMnZDUVhybG"
    "Fnb3RnZnRxdW9mcUZZWSsKWEdkOEdVN0pSaFZZNDZwbzh"
    "hYSt1dHptV0tobERYSHdnODBvZFhnR0RQbjlUK2d1QUZ2"
    "MWJlNXpJeFhNWWZ5eApWQ2x4WlJTRk9HeENOTkZjVEVGO"
    "DdSSGRiMGtMR0t0MTFMdWpNWUNyVmJ0UW5WSXlxUUtDQV"
    "FFQTRlUGp0bStRCjBmK290emFYTnpkaGU4ZFNoL1Nicyt"
    "XYVhOK0xvK1BCOVdPYVY0andaWVVjSFlDZEFGKzhrdTdC"
    "QXN4dlBHTnIKMmExVkJXSmFHN1dVNktVaW1xaG1pcUNNb"
    "mpSdzVoazhLeHNrY0xJM2laRFZINm5aR0hPQlZuSkphWD"
    "grZ2c3Sgo4a0o3VXY4SHhQY0g0VDJvSVphUWlkUEtsQXp"
    "xUVR2MTM3YUVweTZ4TjRlenlZUGpsYzU2bWYyL2VDU25S"
    "TktMClNsZWpQN2lsWWhFQ3FXalh2UmVrOCtKYU55S2JSO"
    "FQ2TC9kenRsZWc2NHlPMTkyUks3SXF4WlFIZ3luZllqN1"
    "MKdGkxME8xUjFCdm5sOVFMOGN2OWYwYkltc00xTU52dDR"
    "ZazJMajdEalZhLytmTlAxNlBONHd2UlFXOVc0RzBwWApy"
    "UmxZQjYzaUh1WUJvd0tDQVFFQXZXZlp5M1d2alI0dUwrQ"
    "m9HU054M0t5WnNwQkFDMnFiN1pNd2ovT1F6QUNZCjlOWV"
    "NObHYvcXdiSWxGZy9SRXNqTko4bWFQY013MEFsTlovTmx"
    "nc2Y3L0I1bzNZQ0lKT2xGWVpiZGEyRVhqcXIKc2tGNHFE"
    "ZC9LQVYrSHRGSmJ2cTEwVGtWY216Q1F5SVR5bkM5L3UzM"
    "npvRGxUWEJFU3grT1h3bHR4YkEvcmd0NQpkRmJuNlRCWl"
    "phN3pjcWlCUlBCNGlwK0w1ZHZrckdWalQrZzBtVmdVQ21"
    "2USs5OXBNN2Z1Wk56NzhGYXhIZmRCCmU2RlpFUkxxcStw"
    "aHhWNkUzQ0pOWHJOZXhtSUgzWmk1SHBZVHZYcnppWEF1T"
    "VE0aWNDbGN6Y0xCNHhlT3F3Z2QKcVVjbExQK0tmVXVpUD"
    "ZMMGtvUjl6SXBzWWIrSEhGU2gvdUkrejBaU1dRS0NBUUF"
    "ZQU5OTnE0VkVDMXF1UFVyTQpQMEpJbU9HWU9OSGl4OThq"
    "UjAzYldIUmYwdm12bTRtUUFCa0F1WTMxWURiMWxoRkVid"
    "HpUR2UxMzhBYzh6enFyCi94dVhyUlNFUXFqQ3lsU202d0"
    "9rTDhKSkFsVlk5RmNhY3gxeWcrWGh4MFJUSDBuVndBT3d"
    "aa25uU0ZFNmZJY2kKMHUwdmJoSFRuK0EwQlNGZG9oR3la"
    "T0MzcVBsbm1ucVNZQVVtd0xFS1ZpcUkrb0hDRG9NSHVTZ"
    "TcrcHdLUldDdApqd2t0WDBxdGVUbTZBSzk5ZEZ2endHYW"
    "xlakg5aWtvN1BYQmdWOWI1UWJGeDFVMEhEd2dCdEpOSGN"
    "JVU5XT2dtCm1aOXA3YXROdlAwOWx5U3RYT05nWkZCaWdj"
    "TDJ2ZUVxVmMxQkRuVHZFQkFoQnowU3hSOFBKMU14dmFPe"
    "ERUVWQKKzJycEFvSUJBUUMydi9jekN2QkJsdmMxbHE2YV"
    "lzckFBNEdnK3ZId2tnSzFiaW1URzQyQWFLc3N3VWg5VHJ"
    "NWApUOHBFNkFqVFdqUXoxOE4xejdsdXd2dWtDL2FQYVZo"
    "OWFHZlZRazIzSlA1S0VJTTZ2aHRUMkFSR1VFbWM5VDhwC"
    "lhITmVSTTAzMll1SXZpMWxaRzdqMjRPQTl0czdtRnRrME"
    "pWdTdIM1loakFXbnNCZDJEcjVNWFVVdmEyeUg4YUMKQ0J"
    "ZNWNVQ1pSZlRvdkJ4OXduZVhwNVAxUzdWRXArbGVUTDB0"
    "NlZoV1lJZ1NwZTRvN1Z5ajd5Z3RvM2FPdE5QYwo0SjlKa"
    "25OYSszWHZnOTVVUjg0VEVBSzk4a3hGck5aQ3JBekZwRC"
    "t5UFJhZ0tlUnR1eE1iRHcrZmYxZnRYUHRBCi9iTWs5NVJ"
    "Ic3JLMm9uRUV0NG9qMmIwY2N5dnJUb3l4QW9JQkFEamZ3"
    "WjIxZWRQL1ZCMFlIMHo0bGM5b3pUT0YKbXg5M21XTDZyN"
    "jF0NmpVT09zZTRuNE4wZERtbWJRY0h5V21FWTkvMVdDbz"
    "F6L3RBMC91OS9tQzZNYkVoQjEraApGOUFCQWRZN1dpcnV"
    "zYkJZakFldSt2NWlOMTVXYUwrVURQb0I3Wjc5S00rZVVV"
    "OWc4TUI3a3VCYmJiMm00SzUrCjlpWDdkT3hYRkRFeHQxM"
    "zh4eFAvK1p2UG1UNDBOajIrUllndHNsR25zbXNPeVk0dm"
    "0rYk82MnZMMDd3UzlObysKR0lZSjhyMVNiVUZrWnpnaWU"
    "1WkhwM28yd3J2Vy9GajlWWlBxbGhGQ2V4TUdYMTlybm5P"
    "ZW4zcW01MlFGS0MxZgorbjZHZEVzdGdiNXVKeUtseGZqe"
    "DQwNDJBZGFORXJKUjZLNmdMZXpVK2Y0aTNCQzNrUzZpYm"
    "VhOGQ1cz0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0"
    "tLS0K"
)


FAKE_JWT_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDUgDY89yX2DU026ASRMEA+lIRHd5lD+4Wcv1etudmqHnO2iEKO
TubdUMLanNv4OEAkOCL2QO37+xEyOJaztqeykHpx8S3XR2FUoCRb7RpPdaTBFh5e
Je306ZyA2MjrMI2GVKBshmKgToPg3TtxwOevJ1dNTSnH4zae2UAEpFbdhQIDAQAB
AoGBAJL2CIypMCu2j0wFsgLnJ8cf10vFvs1xSbpZ6j1PZuVsIgJ+wejBUJCGpfui
t842uMVTvXoo9W1q+T2OPUsUa2ykBfBeLBfgA7di4mpQcHGld+JD4ymPlEwW+fuM
TKVoYIBRj4R7MtXPGFYdTTpnKXSbN3c5jfcXnp8DPLPzEYeRAkEA8bVUzGNGWFk3
7T/beIgWj5Bf9Q6aZHohHa9/zFILzZVPEiv99xGK2fToW+ds1F6n3ksWESagfAGN
h18zVKg2qwJBAOEQxnRFO+S7TLdyOF4wSvwfIpfkYM5R5Qn/1RHuRDC2VMEWwA9D
nN29JMzzRzWUMM6pYXRrh4blO2wnw42w/I8CQQCRTfdKX6vcVNZANBFWJkmZyKtH
AJ5kJN9fny9uvywFTOsZ+4RTUSJt4MMG7NsJ2FWGVxFPAi+cHLreVKbhD7a9AkAN
YuwK2ltXnXRQrPCBWan8GPX7xs+jNefDkn3f1SYlJ5Me8PV3cvQPlEJuFkI0A55r
jFOJkyO6eEPyiOLuuIotAkAESIKxaC4vSNH46H8XphGOHu1W5WXqnOYUZMiIh33G
qN+N9AJtoHPFN2GU36eKg57A55bJ4V1T4NfJKd1EMi2O
-----END RSA PRIVATE KEY-----"""


def get_token_claims(roles: list[RoleNames], username: str, sub: str) -> dict:
    iat = datetime.now(UTC)
    claims = JWTClaims(
        sub=sub,
        nbf=iat.timestamp(),
        exp=(iat + timedelta(days=1)).timestamp(),
        roles=[r.value for r in roles],
        username=username,
    ).model_dump()
    return claims


def generate_valid_jwt_token(
    roles: list[RoleNames],
    username: str = "olivia",
    sub: str = "6feb4bf0-63c6-49fd-afaa-4498b5dc56b0",
) -> str:
    key1 = base64.b64decode(LOCAL_PRIVATE_KEY).decode("utf-8")
    claims = get_token_claims(roles, username, sub)
    token = jwt.encode(claims, key=key1, algorithm="RS256")
    return f"Bearer {token}"


def generate_invalid_jwt_token(
    roles: list[RoleNames],
    username: str = "olivia",
    sub: str = "6feb4bf0-63c6-49fd-afaa-4498b5dc56b0",
) -> str:
    claims = get_token_claims(roles, username, sub)
    token = jwt.encode(claims, key=FAKE_JWT_PRIVATE_KEY, algorithm="RS256")
    return f"Bearer {token}"


@given("the application is running")
def step_impl(context):
    pass


@step("valid credentials are provided")
def step_impl(context):
    roles = getattr(context, "roles", [])
    username = getattr(context, "username", "olivia")
    sub = getattr(context, "sub", "810dbc3c-c18f-4bbd-9a1b-014fc1684d93")
    context.internal_token = generate_valid_jwt_token(roles, username, sub)
    context.request["headers"] = {"Authorization": context.internal_token}


@step("the user is told the request payload was not valid")
def step_impl(context):
    assert context.response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@step("the user is told the request was successful")
def step_impl(context):
    assert context.response, "no response"
    assert 204 >= context.response.status_code >= 200, context.response.text


@step("invalid credentials are provided")
def step_impl(context):
    context.internal_token = generate_invalid_jwt_token([])
    context.request["headers"] = {"Authorization": context.internal_token}


@step("the user is told the request was unauthorized")
def step_impl(context):
    assert (
        context.response.status_code == status.HTTP_401_UNAUTHORIZED
    ), context.response.status_code


@step("the user is told the request was forbidden")
def step_impl(context):
    assert context.response.status_code == status.HTTP_403_FORBIDDEN, context.response.status_code


@step("the requester has role `{role_name}`")
def step_impl(context, role_name: str):
    context.roles = [RoleNames(role_name)]
    context.username = "admin@sibel.com"