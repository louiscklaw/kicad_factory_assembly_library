#!/bin/bash

set -eu

die() {
  echo "Dying!!"
  exit "$1"
}

trap 'die $?' EXIT

./scripts/test_kicad.sh
# echo yeah
# echo $unbound
# echo boo