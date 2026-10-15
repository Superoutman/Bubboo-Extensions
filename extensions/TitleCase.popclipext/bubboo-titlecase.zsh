set -eu
case "$POPCLIP_TEXT" in
  *$'\n'*|*$'\r'*) exit 2 ;;
esac
(( ${#POPCLIP_TEXT} <= 10000 )) || exit 2
export LC_ALL=en_US.UTF-8
printf '%s' "$POPCLIP_TEXT" | /usr/bin/perl ./titlecase.pl
