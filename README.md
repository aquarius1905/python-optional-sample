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

### 2. mypyをインストール
```bash
pip install -r requirements.txt
```

### 3. サンプルコードを実行

#### ✅ 型チェックがOKになる例
```bash
python sample_ok.py
mypy sample_ok.py  # エラーなし
```

#### ❌ 型チェックがNGになる例
```bash
python sample_ng.py  # コメントアウトされているので実行は成功

# sample_ng.py のコメントアウトを外してから実行
mypy sample_ng.py  # エラーが表示される
```

#### 📚 全パターンを確認
```bash
python sample_all.py
mypy sample_all.py  # コメントアウトされている行以外はエラーなし
```

## 📂 ファイル構成
```
.
├── README.md           # このファイル
├── requirements.txt    # 必要なパッケージ
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

1. `sample_ng.py` のコメントアウトを外して型エラーを確認
2. `sample_all.py` を自分なりに改造してみる
3. 自分のコードで型ヒントを追加してmypyで確認

## 📋 動作環境

- Python 3.10以降推奨（`str | None` 記法を使う場合）
- Python 3.7以降でも動作（一部記法は使えません）

## 🤝 コントリビューション

バグ報告や改善提案は Issues からお願いします。

## 📄 ライセンス

MIT License