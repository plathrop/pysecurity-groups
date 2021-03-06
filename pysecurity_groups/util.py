### -*- coding: utf-8 -*-
###
### © 2012 Krux Digital, Inc.
### Author: Paul Lathrop <paul@krux.com>
###

"""Utility functions for pysecurity-groups."""

from IPy import IP


def rule_dict(sources, target, protocol, spec):
    """
    Return a dictionary representing a rule.

    * SOURCES is the list of sources for this rule. These can be security
      group names or CIDR addresses.
    * TARGET is the name of the security group this rule should be applied to.
    * PROTOCOL is 'tcp', 'icmp', or 'udp'
    * SPEC is the list of ports (tcp/udp) or types (icmp) this rule
      allows.
    """
    return {'source': sources,
            'target': target,
            'protocol': protocol,
            'port/type': spec}


def expand_sources(rule):
    """
    Given a RULE (as a dict) return a list of rules, one for each source.
    """
    return [rule_dict(as_cidr(source),
                      rule['target'],
                      rule['protocol'],
                      rule['port/type']) for source in rule['source']]


def as_cidr(source):
    """
    If SOURCE looks like an IP address, add a CIDR suffix to it. Otherwise,
    return it unchanged.
    """
    try:
        src_ip = IP(source)
        if '/' in source:
            return source
        else:
            return src_ip.strNormal() + '/' + str(src_ip.prefixlen())
    except ValueError:
        return source


def regions(config):
    """
    Given CONFIG, return a list of regions specified in the CONFIG.
    """
    return [region.strip() for region in
            config.get('CONFIG', 'regions').split(',')]
