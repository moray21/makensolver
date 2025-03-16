# makensolver
入力した数字で目標の数字を作ることができる組み合わせを探索するプログラム

## インストール
```console
$ pip install git+https://github.com/moray21/makensolver
```

## コマンドでの使用方法
### コマンドとオプション
```console
$ makeN $available_numbers -t $target

available_numbers: list[int]
    使用する数字のリスト
    (例) [1, 2, 3]の3つで目標の数字をつくるということ
target: int
    作成する数字
--timeout: float
    オプション(default: 10秒)
    タイムアウト時間(単位: 秒)
    タイムアウトするまでに探索された結果を返す
--require_one_result:
    オプション
    結果が1つだけでいい場合はオプションを使用する.
--special
    オプション
    四則演算以外も許可する
```

### Examples
```console
$ makeN 1 3 3 4 -t 10

available_numbers:  [1, 1, 3, 4]
target:  10
result:
    No.1: (1 + 1) * 3 + 4
    No.2: 1 + 3 * (4 - 1)
    No.3: 1 - (1 - 4) * 3
```

```
$ makeN 1 3 3 4 -t 10 --require_one_result

available_numbers:  [1, 1, 3, 4]
target:  10
result:
    No.1: (1 + 1) * 3 + 4
```

```console
$ makeN 1 1 3 4 -t 23 --special

available_numbers:  [1, 1, 3, 4]
target:  23
WARNING: timeout. solve have not completed yet.
result: 
    No.1: 1 + 1 - 3 + 4 !
    No.2: 1 + 1 - (3 - 4 !)
    No.3: (1 + 3) ! - 1 ^ 4
```

## 開発
### インストール
```console
$ pip install -e .[dev]
```

### format
```console
$ pysen run format
```

### lint
```console
$ pysen run lint
```

### test
```console
$ coverage run -m pytest  && coverage combine && coverage report -m
```
