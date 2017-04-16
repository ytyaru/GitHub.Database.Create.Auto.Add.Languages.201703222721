# このソフトウェアについて

GitHubアップローダで使うマスターDBを作成するツール。（言語DB追加版）

[前回](https://github.com/ytyaru/GitHub.Database.Create.Auto.Add.GnuLicense.201703211232)の追加版。

# 前回まで

* https://github.com/ytyaru/GitHub.Licenses.Database.Create.Auto.201703201854
* https://github.com/ytyaru/GitHub.Database.Create.Auto.Add.GnuLicense.201703211232
* https://github.com/ytyaru/Python.dataset.SQLite3.Tsv2Insert.201703211257

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.4](https://www.python.org/downloads/release/python-343/)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 実行

```sh
python3 Main.sh
```

# 結果

* `./res/db`配下にDBファイルが作成される

出力パスを変更したいなら`./src/config.ini`の`Path.DB`値を変更すること。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)

