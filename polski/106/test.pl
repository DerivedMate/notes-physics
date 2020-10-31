#!/usr/bin/perl
use strict;
use warnings;
use List::Util;

my @names = ("john", "bob", "cathrine");

my $last = $names[0];
foreach my $name (@names[1..@names]) {
  $last .= $name;

  print "$last\n";
}

DUMP $last;

