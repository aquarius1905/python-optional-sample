# Python Optional型 サンプルコード

PythonのOptional型とUnion型の使い方を学ぶためのサンプルコードです。

## 📝 関連記事

- [【Python】Optional[T] と Union[T, None] について解説](あなたのZenn記事URL)

## 🚀 使い方

### 1. リポジトリをクローン
```bash
git clone https://github.com/your-username/python-optional-sample.git
cd python-optional-sample
```

### 2. サンプルコードを実行

#### ✅ まずは実行してみる（mypyなしでOK）
```bash
python sample_ok.py
python sample_all.py
```

> **Note:** Pythonは実行時に型チェックをしないため、mypyをインストールしなくてもコードは動作します。

#### 🔍 型チェックを体験する（mypyが必要）

型ヒントが正しいかチェックするには、mypyをインストールします。
```bash
# mypyをインストール
pip install -r requirements.txt

# 型チェック実行
mypy sample_ok.py    # ✅ エラーなし
mypy sample_ng.py    # コメントアウトされているのでエラーなし
mypy sample_all.py   # ✅ エラーなし
```

#### ❌ 型エラーを確認してみる

`sample_ng.py` のコメントアウトを外してから：
```bash
mypy sample_ng.py  # ❌ 型エラーが表示される
```

これにより、型ヒントに違反するコードがどのように検出されるか体験できます。

## 📂 ファイル構成
```
.
├── README.md           # このファイル
├── requirements.txt    # mypy（型チェック用、オプション）
├── sample_ok.py        # 型チェックOKの例
├── sample_ng.py        # 型チェックNGの例
└── sample_all.py       # 全パターンまとめ
```

## 🔍 学べること

- `Optional[T]` と `Union[T, None]` の違い（実は同じ）
- `Optional` は「省略可能」ではなく「Noneを許可」の意味
- 引数を省略可能にするにはデフォルト値が必要
- Python 3.10以降の `T | None` 記法
- mypyによる型チェックの実例

## 💡 試してみよう

1. まず `python sample_ok.py` で実行してみる
2. `pip install mypy` してから `mypy sample_ok.py` で型チェック
3. `sample_ng.py` のコメントアウトを外して型エラーを確認
4. `sample_all.py` を自分なりに改造してみる

## ❓ mypyは必要？

| やりたいこと | mypyの必要性 |
|------------|-------------|
| コードを実行する | ❌ 不要 |
| 型エラーを検出する | ✅ 必要 |

Pythonは動的型付け言語なので、型ヒントが間違っていても実行はできます。  
型チェックを体験したい場合のみ、mypyをインストールしてください。

## 📋 動作環境

- Python 3.10以降推奨（`str | None` 記法を使う場合）
- Python 3.7以降でも動作（一部記法は使えません）
- mypy 1.0以降（型チェックをする場合のみ）