# PGP/GPG

PGP: Pretty Good Privacy

GPG: GNU Privacy Guard

### PGP

- from 1991
- cryptographically sign/verify, encrypt/decrypt files, emails, etc.

- OpenPGP standard, RFC 4880

- key "verification" via fingerprints, *Web of trust*

- public/private keys

### GPG

Free/open replacement for PGP, implements RFC 4880, from 1997.

## Basic usage

```shell
$ gpg --list-keys
... list of public keys you know about
$ gpg --list-secret-keys
# your private keys
sec   dsa1024 2004-09-28 [SC]
      3CC6CD7FFD08EEEC39BD9962FF611208CD191EF6
uid           [ultimate] Horak Gyuri <dyuri@horak.hu>
ssb   elg1024 2004-09-28 [E]

sec   rsa4096 2017-06-18 [SC] [expires: 2033-06-14]
      067E886C5034E8C86B15CD274993F07B3EAE8D38
uid           [ unknown] Gyuri Hork <dyuri@horak.hu>
uid           [ unknown] Gyuri Hork <gyuri@horak.hu>
ssb   rsa4096 2017-06-18 [E] [expires: 2033-06-14]
```

Encrypt file

```shell
$ echo hello > secret.txt
$ gpg --armor --encrypt titkos.txt
$ cat titkos.txt.asc
-----BEGIN PGP MESSAGE-----

hQEOA63fG0ACEu5oEAP/cMTJbhUX3cmUpF3rEyJsmS/AMOOTkGUxIYOgE4vkg1WT
fcaOcKdf46zdpcEjFjHMiC59XK5EyoDeqGP48ZgH6tGuk781oi0F2B0oQIPkHvxQ
3fROjO0Qmwr67mX9u4vghwt9joeblBX/oHCUgR91nWkg1/4O4BAQ7H97JjN//wAD
/0hKEk+TN+KQd/JEHcJBxI6cIygTu9y4KKVxQN5iMCHn/IqeJv9J/SQ5SuDcO4z6
r+sj8wQYg5fUhsljgVUpG5mD7ob3otxZOlLJzfSTjheOiOYb3xNazuJsc9fWlw7Y
Rol7rixwLQiOAQMJCIK3R02A3Dq16SU4/wXUWhqdYLAw0ksB/rSdqsF044dnzP2k
UK4/XOiSQvsUs/Qe9yx0hF0nIVbla9jIB4F7tW6giTF+Li8HtDDg+wYXKpaxw7+j
lqpBWr1GhenjD5ccJc0=
=NfGw
-----END PGP MESSAGE-----

$ gpg --armor --decrypt titkos.txt.asc
[password]
hello
```

Sign something

```shell
# detached signature
$ gpg --armor --detach-sign titkos.txt
$ cat titkos.txt.asc
-----BEGIN PGP SIGNATURE-----

iQIzBAABCAAdFiEEBn6IbFA06MhrFc0nSZPwez6ujTgFAmHyfFEACgkQSZPwez6u
jTgBcA//WnTLaR5En3dj8HVTUHH3SyFoK6WxxzX7GSCURcVM8vvvC9ofud1jGczK
jECrylm5CyKCh5XTRdy6hUq+2ZdUVIN/zJT3qZMK9JIZPnBOXBrH1lBs7+6ix/Ub
dyqG2hbkPSULMuU3b0SkVm9fLYxD4o3Blr89+2QJsmOIL2QadxCFS17l1oJC0/cF
hJbfRlohYakhY9qtSpgzYaHun0W9UzAhKLhCTiJ0otlX0ufv5fQ0vc7mv/if6PKS
LGMkFnIDiKaPhiNrPcgP80XuRgOvGgCGlyykYwKz3vfxA0immT42kf04KLrrDmIs
MYSrRJT7z+mywexFVdM7msy70VCWRN8dx6dx3SWYK323yEpBy/1Wh6efUxvXTBh6
wyE0zn9bsjRGpKBxvEQKto+KCijVPelsVIcxA6T349pvFDjV/FuzzCJcSvWSprJ2
vYJMhP9nhjCd1I41WGgDYrF5YMOkbxe+HppzQY7TJ0mqJUMAA7AQnAZ+zWnlJAqT
XAIUi/mOJlGyHr6OpypYWQeJ86UQWX3OB3x9et8CaBGuk+c549jwz0HGhqe1WyOr
isMgDiThh1tHxKkGMgpfOl5Fv3wPpGHaxv9wYL2Fvg87knQtVOGhaXy7alhndPXY
wd3sZRyFg+v/UvqkFmd/Pr4jY7niOKC5zNb+AS2Gv6gY4woqEmI=
=F1qO
-----END PGP SIGNATURE-----
$ gpg --verify titkos.txt.asc
gpg: assuming signed data in 'titkos.txt'
gpg: Signature made Thu 27 Jan 2022 12:04:49 PM CET
gpg:                using RSA key 067E886C5034E8C86B15CD274993F07B3EAE8D38
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: classic
gpg: depth: 0  valid:   5  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 5u
gpg: depth: 1  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 1f, 0u
gpg: next trustdb check due at 2033-06-14
gpg: Good signature from "Gyuri Hork <dyuri@horak.hu>" [ultimate]
gpg:                 aka "Gyuri Hork <gyuri@horak.hu>" [ultimate]
```

## Use cases

- email (sign + encrypt)
- file/disk encryption
- password manager
- signing documents, git changesets (*)