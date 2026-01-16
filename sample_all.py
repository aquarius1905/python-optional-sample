# sample_all.py
"""
全パターンをまとめたファイル
OKパターンとNGパターンを一度に確認できます。
"""
from typing import Optional, Union


# ========================================
# 1. Union[str, None] のパターン
# ========================================
def func1(sample_str: Union[str, None]):
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


print("=== 1. Union[str, None] ===")
# ✅ 型チェックOK
func1("hello")
func1(None)

# ❌ 型チェックNG（コメントアウトを外すとmypyでエラー）
# func1(123)        # error: Argument 1 has incompatible type "int"
# func1([])         # error: Argument 1 has incompatible type "List[<nothing>]"
# func1()           # error: Missing positional argument


# ========================================
# 2. Optional[str] のパターン
# ========================================
def func2(sample_str: Optional[str]):
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


print("\n=== 2. Optional[str] ===")
# ✅ 型チェックOK
func2("world")
func2(None)

# ❌ 型チェックNG（コメントアウトを外すとmypyでエラー）
# func2(456)        # error: Argument 1 has incompatible type "int"
# func2()           # error: Missing positional argument ← 省略不可！


# ========================================
# 3. デフォルト値を指定したパターン（省略可能）
# ========================================
def func3(sample_str: Optional[str] = None):
    if sample_str is None:
        print("引数が省略されたか、Noneが渡されました")
    else:
        print(f"文字列: {sample_str}")


print("\n=== 3. Optional[str] with default ===")
# ✅ 型チェックOK
func3("test")
func3(None)
func3()  # 引数省略が可能！

# ❌ 型チェックNG（コメントアウトを外すとmypyでエラー）
# func3(789)        # error: Argument 1 has incompatible type "int"


# ========================================
# 4. Python 3.10以降の記法
# ========================================
def func4(sample_str: str | None):
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


print("\n=== 4. str | None (Python 3.10+) ===")
# ✅ 型チェックOK
func4("python")
func4(None)

# ❌ 型チェックNG（コメントアウトを外すとmypyでエラー）
# func4(100)        # error: Argument 1 has incompatible type "int"
# func4()           # error: Missing positional argument


# ========================================
# 5. Python 3.10以降 + デフォルト値
# ========================================
def func5(sample_str: str | None = None):
    if sample_str is None:
        print("引数が省略されたか、Noneが渡されました")
    else:
        print(f"文字列: {sample_str}")


print("\n=== 5. str | None with default ===")
# ✅ 型チェックOK
func5("modern")
func5(None)
func5()  # 引数省略が可能！

# ❌ 型チェックNG（コメントアウトを外すとmypyでエラー）
# func5(200)        # error: Argument 1 has incompatible type "int"
