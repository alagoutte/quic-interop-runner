# add your QUIC implementation here
IMPLEMENTATIONS = { # name => docker image
  "quicgo": "martenseemann/quic-go-interop:latest",
  "quicly": "janaiyengar/quicly:interop",
  "ngtcp2": "ngtcp2/ngtcp2-interop:latest",
  "quant":  "ntap/quant:interop",
  "mvfst":  "lnicco/mvfst-qns:latest",
  "quiche":  "cloudflare/quiche-qns:latest",
  "kwik":   "peterdoornbosch/kwik_n_flupke-interop",
}

IMPLEMENTATION_ROLES = {  # name => role, 0 == 'client', 1 == 'server', 2 == both, default is 'both'
  "kwik": 0,
}