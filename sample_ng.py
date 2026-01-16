# sample_ng.py
"""
型チェックがNGになる例
コメントアウトを外すとmypyでエラーが出るパターンを集めたファイルです。

使い方:
1. 各行のコメントアウト(#)を外す
2. mypy sample_ng.py を実行
3. エラーメッセージを確認
"""
from typing import Optional, Union


def func_union(sample_str: Union[str, None]):
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_optional(sample_str: Optional[str]):
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_with_default(sample_str: Optional[str] = None):
    if sample_str is None:
        print("引数が省略されたか、Noneが渡されました")
    else:
        print(f"文字列: {sample_str}")


if __name__ == "__main__":
    # ========================================
    # Union[str, None] の型チェックNG例
    # ========================================

    # ❌ int型を渡す（エラー）
    # func_union(123)
    # エラー: Argument 1 to "func_union" has incompatible type "int"; expected "str | None"

    # ❌ list型を渡す（エラー）
    # func_union([])
    # エラー: Argument 1 to "func_union" has incompatible type "List[<nothing>]"; expected "str | None"

    # ❌ 引数を省略（エラー）
    # func_union()
    # エラー: Missing positional argument "sample_str" in call to "func_union"

    # ========================================
    # Optional[str] の型チェックNG例
    # ========================================

    # ❌ int型を渡す（エラー）
    # func_optional(456)
    # エラー: Argument 1 to "func_optional" has incompatible type "int"; expected "str | None"

    # ❌ 引数を省略（エラー） ← Optional は「省略可能」ではない！
    # func_optional()
    # エラー: Missing positional argument "sample_str" in call to "func_optional"

    # ========================================
    # デフォルト値ありの型チェックNG例
    # ========================================

    # ❌ int型を渡す（エラー）
    # func_with_default(789)
    # エラー: Argument 1 to "func_with_default" has incompatible type "int"; expected "str | None"

    # ✅ 引数省略はOK（デフォルト値があるため）
    func_with_default()

    print("このファイルはコメントアウトされた状態では正常に実行されます")
    print("コメントアウトを外してmypyを実行すると、型エラーが検出されます")
