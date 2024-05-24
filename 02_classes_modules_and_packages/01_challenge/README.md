# チャレンジ1
個人の本のコレクションを管理するためのPythonクラス `Library` を作成してください。

このクラスでは、本の追加、本の削除、現在の本のコレクションの取得ができるようにします。

- 本を追加、削除、表示するためのメソッドを備えた `Library` クラスを実装します。
- プライベートの属性を使用して本の情報を格納します。
- 削除した本が適切に処理されるようにします。

## 要件
- **クラス名**: `Library`
- **インターフェイス**:
    - `add_book(title, author)`: 新しい本を追加します。
    - `remove_book(title)`: タイトルで指定した本を削除します。
    - `retrieve_books()`: ライブラリ内の本を表す辞書のリストを返します。

## 使用例

```python
my_library = Library()
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
for book in my_library.retrieve_books():
    print(book)
my_library.remove_book("1984")
for book in my_library.retrieve_books():
    print(book)
```
