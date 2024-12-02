#!/usr/bin/env bash

# Get the app path
env_path=$(dirname $(dirname "$0"))/.env

# create .env file
{
  # app auth
  echo "DEBUG=False"
  echo "LOGURU_LEVEL=DEBUG"
  echo "GUNICORN_WORKERS=1"
  echo "ENVIRONMENT=local"
  echo "APPLICATION_PORT=8009"
  echo "BASE_PATH=/auth"
  echo "PUBLISHER_BACKEND=app.common.event_sourcing.publisher.KafkaPublisher"
  echo "SIBEL_VERSION=0.1.0"
  echo "SENTRY_DSN=''"

  # Database config
  echo "DB_HOST=localhost"
  echo "DB_PORT=5432"
  echo "DB_NAME=test_auth"
  echo "DB_USERNAME=postgres"
  echo "DB_PASSWORD=cantguessthis"

  # Kafka config
  echo "KAFKA_HOST=localhost"
  echo "KAFKA_PORT=9092"
  echo "KAFKA_PASSWORD=cantguessthis"
  echo "KAFKA_CA_FILE_PATH=''"
  echo "KAFKA_CERT_FILE_PATH=''"
  echo "KAFKA_KEY_FILE_PATH=''"

  # Kafka topics
  echo "KAFKA_HEALTHCHECK_TOPIC='healthcheck'"

  # Auth verification
  echo "JWT_SIGNING_KEY=LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlKS0FJQkFBS0NBZ0VBcHlEaC9BSllFdXFuMlRGVXhqazc5eno2V1VGcmJ3Rk5DaFdyWWUvY3ROK3ZpdnJVCnVPakt6YXFHZ3VwT0tKclZlSE8wMTJkM1ZrRGozM1p1QzROd2xxZjYvOUY4QnFCd3BoWHVsNkhOelB6YmdBL28KbUdBN1I4aXZpZ2l3VC8rY2lseEJ4V004WFdFRmZNTmdCdGhVbGtDeFB5MnRkRjNJNTdTbVBtUzdhNjNsZ3RWTgpxSXZvMVdVVlIzeVpPelA4OGU1Y0FsTXZYaGkvTmMrZFlTckZZdVpON1FwbTJCMmVIQzVmQlI4TXFRQ0lWL2JvCjdoVmx3d2R6dll5WkdkN3p4dzNwVERGYXliSjcxVmh2Nk5oVmpYdkIrckVDTW9KMWFxRExjdkFwcE1yT29wUkMKRjZxR0pUZDRobWhlUENQc3kvb3V0TnFhOVNHK3VxSlVFR29tSjNyaGJadzdJdlo3T0VSQXN2eE9rbCs4MVNjcQo3elIrb0pEN0RzTFcvOFBvRXlsMnc4b1dyWkNWZTRjNFNUL2dKOGxlVDlBbkNBcnN1QVpDR2JJZ3B2MnRDKzVyCnAwZTRkR3JGdlRoNVpaVmx6b2pvOW1JdmNTZHlZRGFiY0dMZTEzNmgwU1VjNDNYbDJrTXlaRDUrN2ZoelNMMkMKVjhQM282eE0rb1c1NlJ3QjE5S1BPcVZ3Uit0eVBTVE1MMXpaTGw5bmkvbW1ndk1uTTQrTlpkMFliaXZ3Zy9GaAp6RkRrT2dwVEtmNWNvU2Z1SUpPYmtieTNNZ2MzM3NWQm1JZ2dXNnFjR2tzNFlEVC9SSEY1ZUZFNm52YVZTMy9pCnpOTmY0eFQvZTQ5dHRweG9MSTZNc0Fub2ZpQ0YwS0d4b1FiNUU0YnlndXRieS94NUh3NmJNNm9PeDZzQ0F3RUEKQVFLQ0FnQWtkSnhHdzk0aFZqVkJ2Nng5eHF0SmJYQXdld0FyeVExY2QwaVlodUZPUlFLK0hxTzdKL0JnOTJMNgorSkFPOUdNL01JSVFnSDI3LzFDVmhIaFJvNXl5Q0RkTWlRMzBSaGY4YW9sT1l4bUlydGxVY0dQc3BRVVpUZkhZCmVyZTI0NHRxZE9CVjVhVWJ1MWVlbE9HRDdMbGF3d2JHd0xoMnl5UlJRb3NHemlOQnhEOXRrQWl1RE1LL2xacVUKS3Q0ajExM0VDaG5nMmZOWm82MUYyQ0U4dWo4dktReHplZExnTG1tNFBQYzJIMFU4TWlVTGh3emRMaWF4NlpTNgpFb3FzNVlDb2VXVGIzV0l2My9KNklaM2JuU0RnU1ZBUlZuNGp0V2hXVjNlNWZTQ2dWU3JJdE8xTHkwTVNxQ3h1CnFTSnhIT2NBd1hSaHQ5T1lTQUdhSldHUDZRK2tMMmRSOEJTdTVoU1U4ZVR3VDhCTitaRlNXWmlLWXdPNlkrTkYKbXZLemN2cUFJUEtYRFhUYTlWZjVPcG41Q0t4SHpmU3ozalViemtNZ1lBNzFRMWFxYzZQT2xaYnI0dWxJd2pPdApRWDdvV0o2K2Y5QUdQUFdwQ3pnNFpMWXFUeE12dVBTYi9ia2Ixcks5U1NIUVB1OElEb1I1M1E4OUN0VVZWWnhRCnlyY2xCUkR4ZFNjeEo4bWw2ajBzRVY4V2FjK1FhTG1xM0E2cDJZeHhmMnZDUVhybGFnb3RnZnRxdW9mcUZZWSsKWEdkOEdVN0pSaFZZNDZwbzhhYSt1dHptV0tobERYSHdnODBvZFhnR0RQbjlUK2d1QUZ2MWJlNXpJeFhNWWZ5eApWQ2x4WlJTRk9HeENOTkZjVEVGODdSSGRiMGtMR0t0MTFMdWpNWUNyVmJ0UW5WSXlxUUtDQVFFQTRlUGp0bStRCjBmK290emFYTnpkaGU4ZFNoL1NicytXYVhOK0xvK1BCOVdPYVY0andaWVVjSFlDZEFGKzhrdTdCQXN4dlBHTnIKMmExVkJXSmFHN1dVNktVaW1xaG1pcUNNbmpSdzVoazhLeHNrY0xJM2laRFZINm5aR0hPQlZuSkphWDgrZ2c3Sgo4a0o3VXY4SHhQY0g0VDJvSVphUWlkUEtsQXpxUVR2MTM3YUVweTZ4TjRlenlZUGpsYzU2bWYyL2VDU25STktMClNsZWpQN2lsWWhFQ3FXalh2UmVrOCtKYU55S2JSOFQ2TC9kenRsZWc2NHlPMTkyUks3SXF4WlFIZ3luZllqN1MKdGkxME8xUjFCdm5sOVFMOGN2OWYwYkltc00xTU52dDRZazJMajdEalZhLytmTlAxNlBONHd2UlFXOVc0RzBwWApyUmxZQjYzaUh1WUJvd0tDQVFFQXZXZlp5M1d2alI0dUwrQm9HU054M0t5WnNwQkFDMnFiN1pNd2ovT1F6QUNZCjlOWVNObHYvcXdiSWxGZy9SRXNqTko4bWFQY013MEFsTlovTmxnc2Y3L0I1bzNZQ0lKT2xGWVpiZGEyRVhqcXIKc2tGNHFEZC9LQVYrSHRGSmJ2cTEwVGtWY216Q1F5SVR5bkM5L3UzMnpvRGxUWEJFU3grT1h3bHR4YkEvcmd0NQpkRmJuNlRCWlphN3pjcWlCUlBCNGlwK0w1ZHZrckdWalQrZzBtVmdVQ212USs5OXBNN2Z1Wk56NzhGYXhIZmRCCmU2RlpFUkxxcStwaHhWNkUzQ0pOWHJOZXhtSUgzWmk1SHBZVHZYcnppWEF1TVE0aWNDbGN6Y0xCNHhlT3F3Z2QKcVVjbExQK0tmVXVpUDZMMGtvUjl6SXBzWWIrSEhGU2gvdUkrejBaU1dRS0NBUUFZQU5OTnE0VkVDMXF1UFVyTQpQMEpJbU9HWU9OSGl4OThqUjAzYldIUmYwdm12bTRtUUFCa0F1WTMxWURiMWxoRkVidHpUR2UxMzhBYzh6enFyCi94dVhyUlNFUXFqQ3lsU202d09rTDhKSkFsVlk5RmNhY3gxeWcrWGh4MFJUSDBuVndBT3daa25uU0ZFNmZJY2kKMHUwdmJoSFRuK0EwQlNGZG9oR3laT0MzcVBsbm1ucVNZQVVtd0xFS1ZpcUkrb0hDRG9NSHVTZTcrcHdLUldDdApqd2t0WDBxdGVUbTZBSzk5ZEZ2endHYWxlakg5aWtvN1BYQmdWOWI1UWJGeDFVMEhEd2dCdEpOSGNJVU5XT2dtCm1aOXA3YXROdlAwOWx5U3RYT05nWkZCaWdjTDJ2ZUVxVmMxQkRuVHZFQkFoQnowU3hSOFBKMU14dmFPeERUVWQKKzJycEFvSUJBUUMydi9jekN2QkJsdmMxbHE2YVlzckFBNEdnK3ZId2tnSzFiaW1URzQyQWFLc3N3VWg5VHJNWApUOHBFNkFqVFdqUXoxOE4xejdsdXd2dWtDL2FQYVZoOWFHZlZRazIzSlA1S0VJTTZ2aHRUMkFSR1VFbWM5VDhwClhITmVSTTAzMll1SXZpMWxaRzdqMjRPQTl0czdtRnRrMEpWdTdIM1loakFXbnNCZDJEcjVNWFVVdmEyeUg4YUMKQ0JZNWNVQ1pSZlRvdkJ4OXduZVhwNVAxUzdWRXArbGVUTDB0NlZoV1lJZ1NwZTRvN1Z5ajd5Z3RvM2FPdE5QYwo0SjlKa25OYSszWHZnOTVVUjg0VEVBSzk4a3hGck5aQ3JBekZwRCt5UFJhZ0tlUnR1eE1iRHcrZmYxZnRYUHRBCi9iTWs5NVJIc3JLMm9uRUV0NG9qMmIwY2N5dnJUb3l4QW9JQkFEamZ3WjIxZWRQL1ZCMFlIMHo0bGM5b3pUT0YKbXg5M21XTDZyNjF0NmpVT09zZTRuNE4wZERtbWJRY0h5V21FWTkvMVdDbzF6L3RBMC91OS9tQzZNYkVoQjEraApGOUFCQWRZN1dpcnVzYkJZakFldSt2NWlOMTVXYUwrVURQb0I3Wjc5S00rZVVVOWc4TUI3a3VCYmJiMm00SzUrCjlpWDdkT3hYRkRFeHQxMzh4eFAvK1p2UG1UNDBOajIrUllndHNsR25zbXNPeVk0dm0rYk82MnZMMDd3UzlObysKR0lZSjhyMVNiVUZrWnpnaWU1WkhwM28yd3J2Vy9GajlWWlBxbGhGQ2V4TUdYMTlybm5PZW4zcW01MlFGS0MxZgorbjZHZEVzdGdiNXVKeUtseGZqeDQwNDJBZGFORXJKUjZLNmdMZXpVK2Y0aTNCQzNrUzZpYmVhOGQ1cz0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0K"
  echo "JWT_VERIFYING_KEY=LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFweURoL0FKWUV1cW4yVEZVeGprNwo5eno2V1VGcmJ3Rk5DaFdyWWUvY3ROK3ZpdnJVdU9qS3phcUdndXBPS0pyVmVITzAxMmQzVmtEajMzWnVDNE53CmxxZjYvOUY4QnFCd3BoWHVsNkhOelB6YmdBL29tR0E3UjhpdmlnaXdULytjaWx4QnhXTThYV0VGZk1OZ0J0aFUKbGtDeFB5MnRkRjNJNTdTbVBtUzdhNjNsZ3RWTnFJdm8xV1VWUjN5Wk96UDg4ZTVjQWxNdlhoaS9OYytkWVNyRgpZdVpON1FwbTJCMmVIQzVmQlI4TXFRQ0lWL2JvN2hWbHd3ZHp2WXlaR2Q3enh3M3BUREZheWJKNzFWaHY2TmhWCmpYdkIrckVDTW9KMWFxRExjdkFwcE1yT29wUkNGNnFHSlRkNGhtaGVQQ1BzeS9vdXROcWE5U0crdXFKVUVHb20KSjNyaGJadzdJdlo3T0VSQXN2eE9rbCs4MVNjcTd6UitvSkQ3RHNMVy84UG9FeWwydzhvV3JaQ1ZlNGM0U1QvZwpKOGxlVDlBbkNBcnN1QVpDR2JJZ3B2MnRDKzVycDBlNGRHckZ2VGg1WlpWbHpvam85bUl2Y1NkeVlEYWJjR0xlCjEzNmgwU1VjNDNYbDJrTXlaRDUrN2ZoelNMMkNWOFAzbzZ4TStvVzU2UndCMTlLUE9xVndSK3R5UFNUTUwxeloKTGw5bmkvbW1ndk1uTTQrTlpkMFliaXZ3Zy9GaHpGRGtPZ3BUS2Y1Y29TZnVJSk9ia2J5M01nYzMzc1ZCbUlnZwpXNnFjR2tzNFlEVC9SSEY1ZUZFNm52YVZTMy9pek5OZjR4VC9lNDl0dHB4b0xJNk1zQW5vZmlDRjBLR3hvUWI1CkU0YnlndXRieS94NUh3NmJNNm9PeDZzQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo="

  # Redis config
  echo "REDIS_HOST=localhost"
  echo "REDIS_PORT=6379"
  echo "REDIS_USERNAME=user"
  echo "REDIS_PASSWORD=pass"
  echo "REDIS_CACHE_TTL=86400"
  echo "CACHE_ENABLED=False"
  echo "PROJECT_NAME=auth"
} > $env_path

echo "Local $env_path file created."
