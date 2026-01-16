"""
型チェックがOKになる例
mypyでエラーが出ないパターンを集めたファイルです。
"""

from typing import Optional, Union


def func_union(sample_str: Union[str, None]):
    """Union[str, None]を使った関数"""
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_optional(sample_str: Optional[str]):
    """Optional[str]を使った関数"""
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_with_default(sample_str: Optional[str] = None):
    """デフォルト値ありの関数（引数省略可能）"""
    if sample_str is None:
        print("引数が省略されたか、Noneが渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_modern(sample_str: str | None):
    """Python 3.10以降の記法"""
    if sample_str is None:
        print("None が渡されました")
    else:
        print(f"文字列: {sample_str}")


def func_modern_with_default(sample_str: str | None = None):
    """Python 3.10以降の記法 + デフォルト値"""
    if sample_str is None:
        print("引数が省略されたか、Noneが渡されました")
    else:
        print(f"文字列: {sample_str}")


if __name__ == "__main__":
    print("=== Union[str, None] ===")
    func_union("hello")
    func_union(None)

    print("\n=== Optional[str] ===")
    func_optional("world")
    func_optional(None)

    print("\n=== Optional[str] with default ===")
    func_with_default("test")
    func_with_default(None)
    func_with_default()  # 引数省略可能

    print("\n=== str | None (Python 3.10+) ===")
    func_modern("python")
    func_modern(None)

    print("\n=== str | None with default ===")
    func_modern_with_default("modern")
    func_modern_with_default(None)
    func_modern_with_default()  # 引数省略可能
