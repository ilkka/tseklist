#!/bin/sh
GIT=$(which git)
[ -x $GIT ] || (echo "Git binary not found in path" >&2; exit 1)

$GIT clone http://github.com/ilkka/chef-cookbooks.git chef-cookbooks
