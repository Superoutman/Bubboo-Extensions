use strict;
use warnings;
use MIME::Base64 qw(encode_base64 decode_base64);
use Encode qw(decode encode FB_CROAK);
binmode STDOUT, ':raw';
my $text = $ENV{POPCLIP_TEXT} // '';
my $mode = shift // '';
if ($mode eq 'standard' || $mode eq 'url') {
    # Validate input as UTF-8 without changing its bytes.
    my $copy = $text;
    decode('UTF-8', $copy, FB_CROAK);
    my $out = encode_base64($text, '');
    if ($mode eq 'url') { $out =~ tr!+/!-_!; $out =~ s/=+$//; }
    print $out;
} elsif ($mode eq 'decode') {
    $text =~ s/[\r\n\t ]//g;
    die "Invalid Base64\n" unless $text =~ /\A[A-Za-z0-9+\/_-]*={0,2}\z/;
    die "Mixed Base64 variants\n" if $text =~ /[+\/]/ && $text =~ /[-_]/;
    $text =~ tr!-_!+/!;
    my $bare = $text; $bare =~ s/=+$//;
    die "Invalid Base64 length\n" if length($bare) % 4 == 1;
    my $padded = $bare . '=' x ((4 - length($bare) % 4) % 4);
    die "Invalid padding\n" if $text =~ /=/ && $text ne $padded;
    my $bytes = decode_base64($padded);
    die "Non-canonical Base64\n" if encode_base64($bytes, '') ne $padded;
    my $copy = $bytes;
    my $decoded = decode('UTF-8', $copy, FB_CROAK);
    die "Unsupported control character\n" if $decoded =~ /[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/;
    print $bytes;
} else { die "Invalid mode\n"; }
