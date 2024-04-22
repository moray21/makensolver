# makensolver
入力した数字で目標の数字を作ることができる組み合わせを探索するプログラム


## コマンドでの使用方法
### コマンドとオプション
```
$ makeN $available_numbers -t $target

available_numbers: list[int]
    使用する数字のリスト
    (例) [1, 2, 3]の3つで目標の数字をつくるということ
target: int
    作成する数字
--require_one_result:
    オプション.結果が1つだけでいい場合はオプションを使用する.
```

### Examples
```
$ makeN 1 3 3 4 -t 23
    available_numbers:  [1, 3, 3, 4]
    target:  23
    result:
        No.1: (3 + 3) * 4 - 1
        No.2: (3 + 3) * 4 - 1
        No.3: 4 * (3 + 3) - 1
        No.4: 4 * (3 + 3) - 1

$ makeN 1 3 3 4 -t 23 --require_one_result
    available_numbers:  [1, 3, 3, 4]
    target:  23
    result:
        No.1: (3 + 3) * 4 - 1
```
