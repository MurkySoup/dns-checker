#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Comprehensive DNS Checker, Ver 0.3-Alpha (Do Not Distribute)
By Rick Pelletier (galiagante@gmail.com), 10 July 2023
Last Update: 10 July 2023

Ref: https://gist.github.com/akshaybabloo/2a1df455e7643926739e934e910cbf2e
"""


import sys
import json
import argparse
import dns.resolver


def get_records(domain):
  record_data = {'records':list()}
  line_items = list()

  ids = [ 'A', 'A6', 'AAAA', 'AFSDB', 'ANY', 'APL', 'AXFR', 'CAA', 'CDNSKEY', 'CDS', 'CERT', 'CNAME',
          'CSYNC', 'DHCID', 'DLV', 'DNAME', 'DNSKEY', 'DS', 'EUI48', 'EUI64', 'GPOS', 'HINFO', 'HIP',
          'IPSECKEY', 'ISDN', 'IXFR', 'KEY', 'KX', 'LOC', 'MAILA', 'MAILB', 'MB', 'MD',  'MF', 'MG',
          'MINFO', 'MR', 'MX', 'NAPTR', 'NONE', 'NS', 'NSAP', 'NSAP-PTR', 'NSEC', 'NSEC3', 'NSEC3PARAM',
          'NULL', 'NXT', 'OPT', 'PTR', 'PX', 'RP', 'RRSIG', 'RT', 'SIG', 'SOA', 'SPF', 'SRV', 'SSHFP',
          'TA', 'TKEY', 'TLSA', 'TSIG', 'TXT', 'UNSPEC', 'URI', 'WKS', 'X25' ]

  record_data['records'].append({'DOMAIN': domain})

  for a in ids:
    try:
      answers = dns.resolver.resolve(domain, a)

      for rdata in answers:
        line_items.append(rdata.to_text())

      line_items.sort()
      record_data['records'].append({a: list(line_items)})
      del line_items[:]

    except Exception as e:
      pass

  return record_data


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--domain", type=str, required=True)
  args = parser.parse_args()

  records = get_records(args.domain)

  print(json.dumps(records, sort_keys=True, indent=2))

  sys.exit(0)
else:
  sys.exit(1)

# end of script
